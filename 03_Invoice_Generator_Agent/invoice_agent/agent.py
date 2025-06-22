from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, RoundRect
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import json
import os
import random

# Google Brand Colors
GOOGLE_BLUE = colors.Color(0.259, 0.522, 0.957)  # #4285F4
GOOGLE_RED = colors.Color(0.918, 0.263, 0.208)   # #EA4335
GOOGLE_YELLOW = colors.Color(0.980, 0.737, 0.016) # #FBBC04
GOOGLE_GREEN = colors.Color(0.208, 0.682, 0.325)  # #34A853
GOOGLE_GREY = colors.Color(0.376, 0.376, 0.376)   # #606060


APP_NAME = "invoice_app"
USER_ID = "1234"
SESSION_ID = "session1234"

def generate_invoice_pdf(invoice_data: str):
    """
    Generates an invoice PDF from the provided invoice data.

    Args:
        invoice_data (str): JSON string containing invoice information

    Returns:
        str: Path to the generated PDF file
    """
    try:
        # Parse the invoice data
        data = json.loads(invoice_data)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"invoice_{timestamp}.pdf"
        filepath = os.path.join(os.getcwd(), filename)
        
        # Create PDF document with rounded corners
        doc = SimpleDocTemplate(filepath, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Add gradient header background with rounded corners
        header_drawing = Drawing(letter[0], 80)
        header_rect = RoundRect(0, 0, letter[0], 80, 15, 15)  # 15pt radius for rounded corners
        header_rect.fillColor = GOOGLE_BLUE
        header_rect.strokeColor = None
        header_drawing.add(header_rect)
        story.append(header_drawing)
        story.append(Spacer(1, -60))  # Overlap for text on background
        
        # Company Header with softer fonts
        company_style = ParagraphStyle(
            'CompanyHeader',
            parent=styles['Normal'],
            fontSize=22,
            textColor=colors.white,
            spaceAfter=10,
            alignment=1,  # Center alignment
            fontName='Times-Roman'  # Softer serif font
        )
        story.append(Paragraph("Easy AI labs", company_style))
        
        # Title with softer styling
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=28,
            textColor=colors.white,
            spaceAfter=30,
            alignment=1,  # Center alignment
            fontName='Times-Bold'  # Softer serif bold
        )
        story.append(Paragraph("INVOICE", title_style))
        
        # Generate random 16-digit invoice number if not provided
        if 'invoice_number' not in data or not data['invoice_number']:
            data['invoice_number'] = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        
        # Use today's date
        data['date'] = datetime.now().strftime("%Y-%m-%d")
        
        # Invoice details (no due date)
        invoice_info = [
            ["Invoice Number:", data.get('invoice_number')],
            ["Date:", data.get('date')]
        ]
        
        invoice_table = Table(invoice_info, colWidths=[2*inch, 3*inch])
        invoice_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),  # Softer font
            ('FONTSIZE', (0, 0), (-1, -1), 13),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TEXTCOLOR', (0, 0), (-1, -1), GOOGLE_GREY),
            ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.97, 0.97, 0.97)),  # Very light grey
            ('GRID', (0, 0), (-1, -1), 1, colors.Color(0.9, 0.9, 0.9)),  # Light border
            ('ROUNDEDCORNERS', (0, 0), (-1, -1), 8),  # Rounded corners
        ]))
        story.append(invoice_table)
        story.append(Spacer(1, 20))
        
        # Billing information with softer styling
        bill_to_style = ParagraphStyle(
            'BillToHeader',
            parent=styles['Heading2'],
            textColor=GOOGLE_BLUE,
            fontSize=16,
            fontName='Times-Bold'  # Softer serif font
        )
        story.append(Paragraph("BILL TO:", bill_to_style))
        bill_to = data.get('bill_to', {})
        billing_info = f"""
        {bill_to.get('name', 'Customer Name')}<br/>
        {bill_to.get('address', 'Customer Address')}<br/>
        {bill_to.get('city', 'City')}, {bill_to.get('state', 'State')} {bill_to.get('zip', 'ZIP')}
        """
        # Only add email if it exists
        if bill_to.get('email'):
            billing_info += f"<br/>{bill_to.get('email')}"
        story.append(Paragraph(billing_info, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Items table with softer styling
        items_style = ParagraphStyle(
            'ItemsHeader',
            parent=styles['Heading2'],
            textColor=GOOGLE_BLUE,
            fontSize=16,
            fontName='Times-Bold'  # Softer serif font
        )
        story.append(Paragraph("ITEMS:", items_style))
        
        items = data.get('items', [])
        if not items:
            items = [{"description": "Sample Item", "quantity": 1, "rate": 100.00, "amount": 100.00}]
        
        # Prepare table data
        table_data = [["Description", "Quantity", "Rate", "Amount"]]
        total = 0
        
        for item in items:
            quantity = item.get('quantity', 1)
            rate = item.get('rate', 0)
            amount = quantity * rate
            total += amount
            
            table_data.append([
                item.get('description', ''),
                str(quantity),
                f"${rate:.2f}",
                f"${amount:.2f}"
            ])
        
        # Add total row
        table_data.append(["", "", "TOTAL:", f"${total:.2f}"])
        
        # Create and style the table with soft rounded edges
        items_table = Table(table_data, colWidths=[3*inch, 1*inch, 1*inch, 1*inch])
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), GOOGLE_BLUE),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),  # Softer serif bold
            ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),  # Softer serif regular
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            ('BACKGROUND', (0, 1), (-1, -2), colors.Color(0.98, 0.98, 0.98)),  # Very light grey
            ('BACKGROUND', (0, -1), (-1, -1), GOOGLE_GREEN),
            ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
            ('FONTNAME', (0, -1), (-1, -1), 'Times-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.Color(0.9, 0.9, 0.9)),  # Very light border
            ('ROUNDEDCORNERS', (0, 0), (-1, -1), 10),  # Rounded corners
        ]))
        
        story.append(items_table)
        story.append(Spacer(1, 20))
        
        # Notes with softer styling
        if data.get('notes'):
            notes_style = ParagraphStyle(
                'NotesHeader',
                parent=styles['Heading2'],
                textColor=GOOGLE_BLUE,
                fontSize=16,
                fontName='Times-Bold'  # Softer serif font
            )
            story.append(Paragraph("NOTES:", notes_style))
            notes_content_style = ParagraphStyle(
                'NotesContent',
                parent=styles['Normal'],
                fontName='Times-Roman'  # Softer serif font
            )
            story.append(Paragraph(data['notes'], notes_content_style))
            story.append(Spacer(1, 20))
        
        # Footer with soft rounded background
        footer_drawing = Drawing(letter[0], 60)
        footer_rect = RoundRect(0, 0, letter[0], 60, 15, 15)  # Rounded corners
        footer_rect.fillColor = GOOGLE_GREY
        footer_rect.strokeColor = None
        footer_drawing.add(footer_rect)
        story.append(footer_drawing)
        story.append(Spacer(1, -45))  # Overlap for text on background
        
        # Footer with soft fonts
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=11,
            textColor=colors.white,
            alignment=1,  # Center alignment
            spaceAfter=20,
            fontName='Times-Roman'  # Softer serif font
        )
        
        footer_text = '''
        Connect with us:<br/>
        <font color="#4285F4">GitHub:</font> <a href="https://github.com/Yash-Kavaiya" color="white">https://github.com/Yash-Kavaiya</a><br/>
        <font color="#4285F4">LinkedIn:</font> <a href="https://www.linkedin.com/in/yashkavaiya/" color="white">https://www.linkedin.com/in/yashkavaiya/</a>
        '''
        story.append(Paragraph(footer_text, footer_style))
        
        # Build PDF
        doc.build(story)
        
        return f"Invoice PDF generated successfully: {filepath}"
        
    except Exception as e:
        return f"Error generating invoice PDF: {str(e)}"


invoice_generator_agent = Agent(
    model='gemini-2.0-flash',
    name='invoice_generator_agent',
    instruction='''You are an invoice generator agent. When a user requests to create an invoice, collect the following information:
    
    1. Billing information (customer name, address)
    2. Items/services (description, quantity, rate)
    3. Any additional notes
    
    Email is optional and should not be requested unless specifically provided by the user.
    
    Invoice details like invoice number and date are automatically generated:
    - Invoice number: Random 16-digit number (automatically generated)
    - Date: Today's date (automatically set)
    - No due date is included
    
    Once you have the billing and items information, format it as a JSON string and use the generate_invoice_pdf function to create a PDF invoice.
    
    Example JSON format:
    {
        "bill_to": {
            "name": "John Doe",
            "address": "123 Main St",
            "city": "Anytown",
            "state": "ST",
            "zip": "12345"
        },
        "items": [
            {
                "description": "Web Development Services",
                "quantity": 10,
                "rate": 75.00
            }
        ],
        "notes": "Payment terms or additional notes"
    }
    
    If the user doesn't provide all information, ask for the missing details or use reasonable defaults. Do not ask for invoice number, date, due date, or email as these are handled automatically or optional.''',
    description='This agent specializes in generating professional invoices in PDF format. It collects invoice details, billing information, and line items to create formatted PDF invoices saved locally.',
    tools=[generate_invoice_pdf],
)


# Session and Runner
session_service = InMemorySessionService()
session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
runner = Runner(agent=invoice_generator_agent, app_name=APP_NAME, session_service=session_service)


# Agent Interaction
def call_agent(query):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

call_agent("Create an invoice for ABC Company with the following details: Customer: John Smith, Address: 456 Oak Street, City: Springfield, Email: john.smith@email.com. Invoice for Web Development Services, 20 hours at $85/hour. Invoice number INV-2025-001, due in 30 days.")
root_agent = invoice_generator_agent