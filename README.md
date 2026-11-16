🤖 AI Study Assistant

📌 Project Overview

The AI Study Assistant is an AI-powered chatbot designed to help students understand academic topics easily. It accepts questions from students and generates simple, clear, and understandable explanations using Google Gemini AI.

The main goal of this project is to make learning easier, faster, and more interactive.

🎯 Objectives

- Help students understand difficult concepts.
- Provide simple explanations for academic questions.
- Give quick answers using Artificial Intelligence.
- Make learning more interactive and accessible.

🛠️ Technologies Used

- Python – Programming language
- Streamlit – Web application interface
- LangChain – AI application framework
- Google Gemini 2.5 Flash – AI language model
- python-dotenv – Environment variable management

📂 Project Structure

AI-Study-Assistant/
│
├── app.py
├── web_app.py
├── .env
├── requirements.txt
├── README.md
└── venv/

⚙️ Installation and Setup

Step 1: Clone or download the project

Download the project to your computer.

Step 2: Create a virtual environment

python -m venv venv

Step 3: Activate the virtual environment

For Windows Command Prompt:

venv\Scripts\activate.bat

Step 4: Install the required libraries

pip install streamlit langchain langchain-google-genai python-dotenv

Step 5: Configure the Google API Key

Create a ".env" file in the project folder and add:

GOOGLE_API_KEY=your_google_api_key

Replace "your_google_api_key" with your actual Google Gemini API key.

Step 6: Run the application

To launch the web application:

streamlit run web_app.py

If your Streamlit interface is in "app.py", use:

streamlit run app.py

Open the local URL displayed in the terminal, usually:

http://localhost:8501

💡 How It Works

1. The student opens the AI Study Assistant.
2. The student enters an academic question.
3. The application sends the question to Google Gemini through LangChain.
4. The AI processes the question.
5. The application displays a simple and understandable answer.

🔐 Security

- API keys are stored in the ".env" file.
- Sensitive credentials should not be uploaded to GitHub.
- The ".env" file should be included in ".gitignore".

🚀 Future Enhancements

- Add subject-wise learning.
- Include quiz generation.
- Add multiple-choice questions.
- Provide personalized learning assistance.
- Add chat history.
- Support PDF document-based question answering.

👩‍🎓 Conclusion

The AI Study Assistant demonstrates how Artificial Intelligence can support students in their learning process. By integrating Python, LangChain, Streamlit, and Google Gemini, this project provides an interactive platform for asking academic questions and receiving easy-to-understand explanations.