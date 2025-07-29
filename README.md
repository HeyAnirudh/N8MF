# 🧠 N8MF – Mutual Fund AI Assistant using n8n + Gemini + Google Drive + Flask

**N8MF** is a fully automated Mutual Fund portfolio analyzer that combines the power of:
- 🔁 **n8n** for automation and chat interface
- 🧠 **Gemini AI** for intelligent insights
- 📂 **Google Drive** for uploading your mutual fund statements
- 📊 **Google Sheets** for structured data analysis
- 🔧 **Flask API hosted on Render** for backend data cleaning

## 🚀 What It Does

1. You upload your mutual fund (Tested on Groww) statement to **Google Drive**.
2. An **n8n workflow** is triggered automatically.
3. The file is sent to a **Flask API hosted on Render** to parse and clean it.
4. Cleaned data is saved to a **Google Sheet**.
5. You can **chat with an AI (Gemini)** via n8n to get portfolio insights like:
   - Fund performance
   - SIP summary
   - Asset allocation
   - Portfolio health checks

All you do is: **Drop your file + Ask your questions!**

---

## 🛠️ Tech Stack

| Component | Tech |
|----------|------|
| Backend | Python Flask (Hosted on Render) |
| Orchestration | n8n |
| File Storage | Google Drive |
| Spreadsheet | Google Sheets |
| AI Assistant | Gemini AI |
| Deployment | Render |
| Input Format |  Mutual Fund Statements (Excel) |


## ⚙️ Setup

### 1. 🔧 Deploy Backend on Render

1. Sign into [Render](https://render.com).
2. Deploy a new **Web Service** with the `/clean-mf` directory.
3. Use:
   - `requirements.txt`
   - `runtime.txt`
   - `.render` for automatic build
4. Note down the public URL of your Flask API.

### 2. 🔁 Configure n8n

1. Self-host n8n or use [n8n.cloud](https://n8n.io).
2. Import `TradeAnalysis.json` via **Import Workflow**.
3. Update:
   - Google Drive trigger (folder ID)
   - HTTP request node (your Flask Render URL)
   - Google Sheets destination ID
   - Gemini API Key (if using Gemini via HTTP)

### 3. 🧪 Try it out

1. Upload a **Groww Mutual Fund** Excel file to the configured Drive folder.
2. n8n will:
   - Trigger flow
   - Send data to Flask
   - Save cleaned results to Google Sheets
   - Wait for your chat input
3. Type:  
   - “How is my portfolio doing?”
   - “What’s my SIP summary?”
   - “Suggest rebalance strategy.”

---
## 🔮 Possible Applications

- Portfolio review bot
- SIP tracking and advice
- Expense ratio optimization
- MF performance summaries via chat
- WhatsApp/Slack MF assistant (future)

---

## 🛠️ Dependencies

- Python 3.10+
- Flask
- n8n
- Google Sheets API
- Google Drive API
- Gemini API 

---

## 🤖 Built With

- Flask backend (in `/clean-mf`)
- Render deployment (`.render`, `requirements.txt`, `runtime.txt`)
- n8n Workflow (`TradeAnalysis.json`)
- Google Drive + Sheets
- Gemini AI

---

## 👨‍💻 Author

Made by [Anirudh Soni](https://www.linkedin.com/in/heyanirudh) — blending no-code workflows with powerful AI tooling.

---

## 📝 License

MIT License – feel free to use, remix, and share.

---

