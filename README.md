# FridayProject9
# AI Completion App (ChatGPT GUI)

This is a Python-based desktop application that allows you to type a prompt into a simple GUI and generate an AI response using OpenAI's GPT-3.5 Turbo model.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-completion-app.git
cd ai-completion-app
```

### 2. Create a `.env` File
Create a file named `.env` in the root of your project folder and add your OpenAI API key:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
You can get your API key at: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

### 3. Run the App
```bash
python gui_app.py
```
> Python 3.6+ is required. No external libraries are needed.

## Usage

1. Launch the app.
2. Enter a prompt into the text box (e.g., "What is supply chain management?").
3. Click the **Generate Response** button.
4. The AI-generated response will appear in the output area.

