# 📖 Name Story Agent

![name_story_agent](/Images/01_name_story_agent.png)

## 🌟 Overview

The **Name Story Agent** is an interactive AI agent that creates personalized stories based on the meaning and origin of user names. This agent demonstrates the power of conversational AI by combining name etymology research with creative storytelling to deliver a unique, engaging experience for each user.

## ✨ Features

- **Interactive Greeting**: Warmly welcomes users and asks for their name
- **Name Research**: Provides information about name meanings, origins, and cultural significance
- **Creative Storytelling**: Generates 2-3 paragraph personalized stories using the user's name as the protagonist
- **Cultural Awareness**: Handles names from various cultural backgrounds
- **Fallback Creativity**: Creates beautiful stories even for uncommon names based on their sound and feel
- **Positive Experience**: Always maintains an encouraging and uplifting tone

## 🎯 How It Works

1. **Greeting Phase**: The agent introduces itself and asks for the user's name
2. **Research Phase**: Looks up or provides information about the name's meaning and origin
3. **Story Creation**: Crafts a personalized narrative incorporating the name's significance
4. **Delivery**: Presents the story in an engaging, warm manner

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google ADK (Agent Development Kit)
- Access to Gemini 2.0 Flash model

### Installation

1. Navigate to the first agent directory:
   ```bash
   cd 01_first_agent/multi_tool_agent
   ```

2. Ensure you have the required dependencies installed:
   ```bash
   pip install -r ../../requirements.txt
   ```

### Running the Agent

1. Run the agent:
   ```python
   python agent.py
   ```

2. Follow the prompts:
   - The agent will greet you and ask for your name
   - Enter your name when prompted
   - Enjoy your personalized story!

## 💡 Example Interaction

```
Agent: Greetings! I'm the Name Story Agent, and I'm thrilled to meet you! What a pleasure it is to connect.

User: Hello

Agent: First things first, could you share your name with me? Once I know your name, I'll weave a special story just for you, inspired by the meaning and origin of your name. I'm excited to see what we'll create together! 😊

User: Yash

Agent: Hello Yash, it's a pleasure to meet you!

Yash is a wonderful name with rich significance. Originating from Sanskrit, Yash (यश) generally means "success," "glory," "fame," or "splendor." It carries a sense of achievement and honor.

Now, let's weave a story that celebrates the essence of your name:

In the vibrant city of luminaries, lived a young man named Yash. From his early days, Yash was known for his unwavering dedication and radiant spirit...
```

## 🛠️ Technical Details

### Agent Configuration

- **Name**: `name_story_agent`
- **Model**: `gemini-2.0-flash`
- **Type**: Conversational AI Agent
- **Framework**: Google ADK

### Key Components

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="name_story_agent",
    model="gemini-2.0-flash",
    description="An interactive agent that asks for the user's name and creates a personalized story based on the meaning and origin of their name.",
    instruction="Detailed instructions for greeting, researching names, and creating stories..."
)
```

## 🎨 Customization

You can customize the agent by modifying:

- **Greeting Style**: Adjust the initial greeting in the instructions
- **Story Length**: Modify the paragraph count requirement
- **Story Themes**: Add specific themes or genres for stories
- **Cultural Focus**: Emphasize certain cultural backgrounds or name origins

## 📚 Learning Outcomes

This agent demonstrates:

- **Conversational Flow Design**: How to structure multi-turn conversations
- **Personalization**: Creating unique experiences for each user
- **Cultural Sensitivity**: Handling diverse name backgrounds respectfully
- **Creative AI Applications**: Using AI for storytelling and entertainment
- **User Engagement**: Maintaining interest through interactive experiences

## 🔮 Future Enhancements

Potential improvements could include:

- Integration with name databases or APIs for more accurate meanings
- Multiple story themes or genres to choose from
- Support for multiple languages
- Voice narration capabilities
- Story export functionality
- Family name history exploration

## 🤝 Contributing

Feel free to contribute improvements or suggestions! This is part of the ADK course learning materials.

## 📄 License

This project is part of the Agent Development Kit course materials.

---

*Happy storytelling! 📖✨*