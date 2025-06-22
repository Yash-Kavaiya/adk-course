# Invoice Generator Agent

An AI-powered invoice generator that creates professional PDF invoices using Google's ADK (Agent Development Kit) with modern design, Google colors, and soft rounded edges.

## Features

- 🤖 **AI-Powered**: Uses Gemini 2.0 Flash model for intelligent invoice generation
- 🎨 **Modern Design**: Google Material Design colors with soft rounded edges
- 📄 **Professional PDFs**: High-quality PDF generation with Times fonts
- 🔢 **Auto-Generated Details**: Automatic 16-digit invoice numbers and timestamps
- 💼 **Easy AI labs Branding**: Company branding with GitHub and LinkedIn links
- 🚫 **No Email Required**: Streamlined process without mandatory email collection
- 📋 **Smart Data Collection**: Collects only essential customer and item information

## Design Features

### Visual Styling
- **Google Brand Colors**: Blue (#4285F4), Green (#34A853), Grey (#606060)
- **Soft Typography**: Times-Roman and Times-Bold fonts for elegance
- **Rounded Corners**: 15pt radius headers, 10pt radius tables
- **Gradient Backgrounds**: Blue header and grey footer with rounded edges
- **Light Borders**: Subtle 0.5pt borders in light grey

### Automatic Generation
- **Invoice Numbers**: Random 16-digit numbers
- **Dates**: Current timestamp (YYYY-MM-DD format)
- **File Names**: Timestamped (invoice_YYYYMMDD_HHMMSS.pdf)

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Required packages:**
   ```
   google-adk
   reportlab
   ```

3. **Set up Google ADK credentials** (follow Google ADK documentation)



## Expected Outputs

### PDF Features Verification
- ✅ **Header**: Blue rounded background with "Easy AI labs" and "INVOICE"
- ✅ **Invoice Details**: 16-digit number and current date in rounded table
- ✅ **Billing Info**: Customer details in Times-Roman font
- ✅ **Items Table**: Blue header, green total row, rounded corners
- ✅ **Footer**: Grey rounded background with GitHub/LinkedIn links
- ✅ **Typography**: Consistent Times font family throughout

### File Output Verification
- ✅ **File Location**: Current working directory
- ✅ **File Naming**: `invoice_YYYYMMDD_HHMMSS.pdf`
- ✅ **File Size**: Appropriate for content (typically 50-200KB)
- ✅ **PDF Quality**: Vector graphics, selectable text, professional layout

## Troubleshooting

### Common Issues

1. **ReportLab Import Error**
   ```bash
   pip install reportlab
   ```

2. **PDF Generation Fails**
   - Check write permissions in directory
   - Ensure sufficient disk space

3. **Font Issues**
   - Times fonts are built-in with ReportLab
   - No additional font installation required

4. **Agent Response Issues**
   - Verify Google ADK credentials
   - Check network connectivity

### Validation Checklist

- [ ] PDF file created successfully
- [ ] 16-digit invoice number generated
- [ ] Current date displayed
- [ ] Customer information formatted correctly
- [ ] Items table with proper calculations
- [ ] Total amount calculated accurately
- [ ] Company branding visible
- [ ] Rounded corners applied
- [ ] Soft fonts used throughout
- [ ] Footer links included

### Current Settings
- **Model**: Gemini 2.0 Flash
- **Company**: Easy AI labs
- **Colors**: Google Material Design palette
- **Fonts**: Times-Roman/Times-Bold
- **Invoice Format**: No due date, auto-generated numbers

### Customization Options
- Modify company name in `generate_invoice_pdf()` function
- Adjust colors by changing `GOOGLE_*` color constants
- Update footer links in footer text section
- Change fonts by modifying `fontName` parameters

## License

Copyright 2025 - Easy AI labs