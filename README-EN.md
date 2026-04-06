<div align="center">

# 🤖 Slack Sales Copilot

**AI-powered Slack bot that assists B2B SaaS sales teams with intelligent opportunity analysis and next-step suggestions.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![Slack](https://img.shields.io/badge/Slack-Bolt-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://slack.dev/bolt-python/)
[![Socket Mode](https://img.shields.io/badge/Socket%20Mode-enabled-00C7B7?style=for-the-badge&logo=socketdotio&logoColor=white)](https://api.slack.com/apis/connections/socket)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📋 Overview

**Slack Sales Copilot** is an AI assistant integrated with Slack that acts as a real-time sales coach. It analyzes conversations, call transcripts, and opportunity context to deliver strategic insights directly to the sales team — without leaving Slack.

### How it works

```
Slack Message → Intent Classification → AI Module → Slack Response
```

The bot automatically classifies user intent and triggers the correct module:

| Detected intent | Module triggered |
|---|---|
| Reply suggestion | `generate_reply.py` |
| Message analysis | `analyze_message.py` |
| Competitive battlecard | `battlecards.py` |
| Call analysis | `analyze_call.py` |

---

## 🎥 Demo

[![Watch the demo video](https://img.youtube.com/vi/xrpBH9gVwJQ/maxresdefault.jpg)](https://youtu.be/xrpBH9gVwJQ)

---

## ✨ Features

- **💬 Reply Suggestions** — Generates strategic responses to prospect messages, identifying objections and suggesting advancement tactics.
- **🔍 Message Analysis** — Evaluates deal risk, customer intent, buying signals, and recommended actions.
- **⚔️ Competitive Battlecards** — Creates competitor analyses with strengths, weaknesses, and positioning strategy.
- **📞 Call Analysis** — Processes meeting transcripts and extracts deal stage, stakeholders, risks, and closing probability.

---

## 🏗️ Project Structure

```
slack-sales-copilot/
├── backend/
│   ├── main.py              # Application entry point
│   ├── slack_agent.py       # Slack Bolt initialization (Socket Mode)
│   ├── handlers.py          # Intent router and main handler
│   └── sales_ai/
│       ├── generate_reply.py   # Reply generation for prospects
│       ├── analyze_message.py  # Message analysis and risk signals
│       ├── battlecards.py      # Competitive battlecard generation
│       └── analyze_call.py     # Call transcript analysis
├── .env.example             # Required environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Running Locally

### Prerequisites

- Python 3.10+
- [Slack API](https://api.slack.com/apps) account with app configured in Socket Mode
- [OpenAI](https://platform.openai.com/) API key

### 1. Clone the repository

```bash
git clone https://github.com/seu-usuario/slack-sales-copilot.git
cd slack-sales-copilot
```

### 2. Create and activate the virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit the `.env` file with your credentials:

```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
OPENAI_API_KEY=sk-...
```

### 5. Start the bot

```bash
python backend/main.py
```

---

## 🔧 Slack App Configuration

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Under **Socket Mode**, enable it and generate an `App-Level Token` with the `connections:write` scope
3. Under **OAuth & Permissions**, add the following scopes:
   - `app_mentions:read`
   - `chat:write`
   - `im:history`
   - `im:read`
   - `im:write`
4. Under **Event Subscriptions**, enable and subscribe to events:
   - `message.im`
   - `app_mention`
5. Install the app in your workspace and copy the `Bot User OAuth Token`

---

## 📦 Dependencies

| Package | Version | Usage |
|---|---|---|
| `slack-bolt` | latest | Slack Bot Framework |
| `openai` | latest | OpenAI API client |
| `python-dotenv` | latest | Environment variable management |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

1. Fork the project
2. Create your branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## Author

**Klauber Fischer**
