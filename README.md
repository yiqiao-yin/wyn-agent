# 🧠 WYN-Agent

Welcome to the **WYN-Agent** package! This Python package provides a simple yet powerful interface to create AI chatbots using the Mistral AI platform. It includes functionalities to handle conversation history, isolate and execute Python code from chatbot responses, and seamlessly interact with Mistral's AI agents.

Repo: [https://github.com/yiqiao-yin/wyn-agent](https://github.com/yiqiao-yin/wyn-agent)

## 📦 Installation

Before using the package, make sure you have Python installed. You can install the package via `pip`:

```bash
pip install wyn-agent
```

## 🛠️ Features

- **ChatBot Class**: Easily create a chatbot that interacts with Mistral AI services.
- **Conversation History**: Track the entire conversation history with ease.
- **Python Code Extraction**: Automatically extract and save Python code from chatbot responses.
- **Script Execution**: Execute Python scripts directly from the extracted code.
- **Interactive Agent**: Run a Mistral AI agent chatbot with simple commands.

## 🚀 Quick Start

To get started, simply initialize the `ChatBot` class with your Mistral API key and call the `run_mistral_agent()` method.

```python
from wyn_agent.mistral_agent import ChatBot

bot = ChatBot(
    api_key=YOUR_MISTRAL_API_KEY,
    agent_id=YOUR_MISTRAL_AGENT_API_ID
)

bot.run_mistral_agent()
```

This will start an interactive chatbot session where you can converse with the AI, extract Python code snippets, and even execute them on your local machine.

## 📚 Mistral AI Agent Bot Tutorial

In this section, we'll walk through using the Mistral AI Agent Bot to build a simple interactive chatbot.

### 1. **Initialization**

Start by creating a `ChatBot` instance with your API key:

```python
from wyn_agent.mistral_agent import ChatBot

bot = ChatBot(
    api_key=YOUR_MISTRAL_API_KEY,
    agent_id=YOUR_MISTRAL_AGENT_API_ID
)
```

### 2. **Running the Agent**

Call the `run_mistral_agent()` method to begin interacting with the Mistral AI agent:

```python
bot.run_mistral_agent()
```

### 3. **Interacting with the Bot**

You'll be prompted to enter your messages. The bot will respond and, if the response contains Python code enclosed in triple backticks (```), you'll have the option to save and execute the code.

### 4. **Saving and Executing Python Code**

If the bot generates Python code, you'll be asked if you want to save and execute the code. The code will be saved as a `.py` file, and you can choose to run it immediately.

### 5. **Exiting the Program**

Type `EXIT` to end the conversation.

## 📧 Contact

Developed by **Yiqiao Yin**. For any questions or feedback, feel free to reach out at [eagle0504@gmail.com](mailto:eagle0504@gmail.com).

## 🎉 Contributions

We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request.

---

Enjoy building your AI agents with Mistral! 🚀