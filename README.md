# Intelligent Research Agent 🤖

This is a smart command-line assistant that answers your questions by using its own knowledge, checking the current date, and searching the internet in real-time.

---

## ▶️ How It Works: A Simple Analogy

Think of the agent as a **personal research assistant**.

* 🧠 **The Brain (Google Gemini LLM):** This is the core intelligence. It understands your questions and makes decisions.

* 🧰 **The Toolbox:** The assistant has two special tools to find information:
    * `get_current_date`: A calendar to instantly check today's date.
    * `web_search`: A high-speed internet connection (Tavily Search) to find the latest information.

* 📜 **The Instructions (System Prompt):** The assistant has a clear set of rules. For example: "If someone asks for today's date, use the calendar. If they ask for the latest news, use the internet. Don't use the calendar for general news questions."

When you ask a question, the **Brain** follows its **Instructions** and decides which **Tool** (if any) is needed to give you the best possible answer.

---

## 🚀 Setup and Run

Follow these steps to get the agent running on your machine.

### 1. Get the Code
First, clone this repository to your computer and navigate into the project folder.
```bash
git clone <your_repository_url>
cd <your_repository_name>
```

### 2. Install All Libraries
This single command will install everything you need (LangChain, Google's libraries, Tavily, and Rich for the interactive display).
```bash
pip install langchain langchain-google-genai tavily-python python-dotenv rich
```
> **Optional:** For good practice, you can save these dependencies to a file by running:
> `pip freeze > requirements.txt`

### 3. Add Your API Keys
You need to provide the agent with your secret API keys.

1.  Create a new file in the project folder named `.env`.
2.  Open the file and add your keys in the following format:
    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
    TAVILY_API_KEY="YOUR_TAVILY_API_KEY_HERE"
    ```

### 4. Run the Agent!
Execute the main Python script from your terminal.
```bash
python your_script_name.py
```

The interactive agent will start. Just type your question and press Enter. To exit, type `q`.
