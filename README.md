Live News RAG Bot
Dynamic Retrieval-Augmented Generation for Real-Time News
Overview

Live News RAG Bot is a real-time AI system that answers user questions using only the latest news data.
It automatically refreshes its knowledge every 60 seconds without restarting and proves “Live AI” behavior.
Built for DataQuest 2026 – IIT Kharagpur Hackathon.

What This Project Does -

Fetches live news from NewsAPI
Updates data automatically within every 60 seconds
Answers only from the latest data
Says “Not found in current news” if answer is not present
Logs every update with timestamp for proof
Demonstrates Dynamic RAG + Live AI concept

Key Features

Live data ingestion
Background auto-refresh
Retrieval-Augmented Generation (RAG)
Update logging for demo proof
Simple CLI interface
Hackathon-ready structure

Tech Stack

Python
NewsAPI
Gemini API
Requests
python-dotenv

Project Structure
live-news-project/
│
├── main.py        # Main live loop
├── news.py        # Fetches live news
├── rag.py         # RAG logic using LLM
├── logger.py      # Logs updates
├── update_log.txt # Auto-generated log
├── demo/          # Screenshots / demo proof
├── .env           # API keys (not pushed to GitHub)
└── README.md

How It Works

News is fetched from NewsAPI
System refreshes data every 60 seconds automatically
User can ask unlimited questions anytime
AI answers only from current news
Every refresh is logged with timestamp

Setup Instructions
1. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2. Install Dependencies
pip install requests python-dotenv google-genai

3. Create .env File
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key

4. Run Project
python main.py

Demo Proof Method

Start program
Ask a question
Wait 60–120 seconds
System refreshes automatically
Ask same question again
Answer changes if news changed
Open update_log.txt to show timestamps
This proves real-time behavior.

Example Questions

What happened in sports today?

What is the latest world news?

What news is related to conflict?

Who is the president of India?
→ Should return “Not found in current news”

Hackathon Alignment

This project satisfies DataQuest 2026 requirements:
Dynamic data source
Live updates
RAG pipeline
Real-time behavior proof
Production-style structure

Author

Arijit Sen
DataQuest 2026 Participant
ECE Student