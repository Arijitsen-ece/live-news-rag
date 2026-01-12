📰 Live News RAG Bot
Dynamic Retrieval-Augmented Generation for Real-Time News

DataQuest 2026 – IIT Kharagpur Hackathon

🚀 Overview

Live News RAG Bot is a real-time AI system that answers user questions using only the latest news data.
It refreshes its knowledge automatically every 60 seconds and proves true “Live AI” behavior.
Built specially for DataQuest 2026 – IIT Kharagpur Hackathon.

🎯 What This Project Does

Fetches live news from NewsAPI
Auto-updates data every 60 seconds
Answers only from latest data
Says “Not found in current news” if answer is not present
Logs every refresh with timestamp for proof
Demonstrates Dynamic RAG + Live AI

✨ Key Features

🔄 Live data ingestion
⏱ Background auto-refresh
🧠 Retrieval-Augmented Generation (RAG)
🧾 Update logging for demo proof
💻 Simple CLI interface
🏆 Hackathon-ready structure

🛠 Tech Stack

Python
NewsAPI
Gemini API
Requests
python-dotenv

📁 Project Structure
live-news-project/
│
├── main.py         # Main live loop
├── news.py         # Fetches live news
├── rag.py          # RAG logic using LLM
├── logger.py       # Logs updates
├── update_log.txt  # Auto-generated log
├── demo/           # Screenshots / demo proof
├── requirements.txt
├── README.md
└── .env            # API keys (NOT pushed to GitHub)

⚙️ How It Works

News is fetched from NewsAPI
Data refreshes automatically every 60 seconds
User can ask unlimited questions anytime
AI answers only from current news
Every refresh is logged with timestamp
“Live AI” behavior is clearly demonstrated

🧪 Example Remains True
Question	Result
What happened in sports today?	Answered from news
What is latest world news?	Answered from news
Who is the president of India?	❌ Not found in current news

This is correct behavior — not a general chatbot.

🔧 Setup Instructions
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create .env File
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key

4️⃣ Run Project
python main.py

🎥 Demo Proof Method

To prove “Live AI”:
Start program
Ask:

What is the latest world news?

Take screenshot → demo/demo1_start.png

Wait 60 seconds
Ask same question again
Screenshot → demo/demo2_after_refresh.png
Open update_log.txt and screenshot → demo/demo3_log.png

This proves real-time behavior.

🧠 Hackathon Alignment

This project satisfies DataQuest 2026 requirements:
✅ Dynamic data source
✅ Live updates
✅ RAG pipeline
✅ Real-time behavior proof
✅ Production-style structure

📈 Current Progress

Core RAG system: ✅
Live refresh: ✅
Logging proof: ✅
Demo evidence: ✅
GitHub + README: ✅
Project is hackathon-ready.

🔮 Future Work (Pathway Integration)

Next planned upgrade:
Integrate Pathway streaming engine
Replace timer-based refresh with event-driven streaming
Add vector indexing with Pathway
Real-time document ingestion from files/APIs

👨‍💻 Author

Arijit Sen
ECE Student
Participant – DataQuest 2026