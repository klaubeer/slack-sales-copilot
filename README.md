[English version here](README-EN.md)

<div align="center">

# 🤖 Slack Sales Copilot

**Bot de IA para Slack que auxilia equipes de vendas B2B SaaS com análise inteligente de oportunidades e sugestão de próximos passos.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![Slack](https://img.shields.io/badge/Slack-Bolt-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://slack.dev/bolt-python/)
[![Socket Mode](https://img.shields.io/badge/Socket%20Mode-enabled-00C7B7?style=for-the-badge&logo=socketdotio&logoColor=white)](https://api.slack.com/apis/connections/socket)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📋 Visão Geral

O **Slack Sales Copilot** é um assistente de IA integrado ao Slack que age como um coach de vendas em tempo real. Ele analisa conversas, transcrições de calls e contexto de oportunidades para entregar insights estratégicos diretamente para o time comercial — sem sair do Slack.

### Como funciona

```
Mensagem no Slack → Classificação de Intenção → Módulo de IA → Resposta no Slack
```

O bot classifica automaticamente a intenção do usuário e aciona o módulo correto:

| Intenção detectada | Módulo acionado |
|---|---|
| Sugestão de resposta | `generate_reply.py` |
| Análise de mensagem | `analyze_message.py` |
| Battlecard competitivo | `battlecards.py` |
| Análise de call | `analyze_call.py` |

---

## 🎥 Demonstração

[![Assista ao vídeo de demonstração](https://img.youtube.com/vi/xrpBH9gVwJQ/maxresdefault.jpg)](https://youtu.be/xrpBH9gVwJQ)

---

## ✨ Funcionalidades

- **💬 Sugestão de Respostas** — Gera respostas estratégicas para mensagens de prospects, identificando objeções e sugerindo táticas de avanço.
- **🔍 Análise de Mensagens** — Avalia risco do negócio, intenções do cliente, sinais de compra e ações recomendadas.
- **⚔️ Battlecards Competitivos** — Cria análises de concorrentes com pontos fortes, fracos e estratégia de posicionamento.
- **📞 Análise de Calls** — Processa transcrições de reuniões e extrai estágio do negócio, stakeholders, riscos e probabilidade de fechamento.

---

## 🏗️ Estrutura do Projeto

```
slack-sales-copilot/
├── backend/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── slack_agent.py       # Inicialização do Slack Bolt (Socket Mode)
│   ├── handlers.py          # Roteador de intenções e handler principal
│   └── sales_ai/
│       ├── generate_reply.py   # Geração de respostas para prospects
│       ├── analyze_message.py  # Análise de mensagens e sinais de risco
│       ├── battlecards.py      # Geração de battlecards competitivos
│       └── analyze_call.py     # Análise de transcrições de calls
├── .env.example             # Variáveis de ambiente necessárias
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Como rodar localmente

### Pré-requisitos

- Python 3.10+
- Conta no [Slack API](https://api.slack.com/apps) com app configurado em Socket Mode
- Chave de API da [OpenAI](https://platform.openai.com/)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/slack-sales-copilot.git
cd slack-sales-copilot
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:

```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
OPENAI_API_KEY=sk-...
```

### 5. Inicie o bot

```bash
python backend/main.py
```

---

## 🔧 Configuração do Slack App

1. Acesse [api.slack.com/apps](https://api.slack.com/apps) e crie um novo app
2. Em **Socket Mode**, ative e gere um `App-Level Token` com escopo `connections:write`
3. Em **OAuth & Permissions**, adicione os escopos:
   - `app_mentions:read`
   - `chat:write`
   - `im:history`
   - `im:read`
   - `im:write`
4. Em **Event Subscriptions**, ative e assine os eventos:
   - `message.im`
   - `app_mention`
5. Instale o app no workspace e copie o `Bot User OAuth Token`

---

## 📦 Dependências

| Pacote | Versão | Uso |
|---|---|---|
| `slack-bolt` | latest | Framework do Slack Bot |
| `openai` | latest | Cliente da API OpenAI |
| `python-dotenv` | latest | Gerenciamento de variáveis de ambiente |

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

1. Faça um fork do projeto
2. Crie sua branch: `git checkout -b feature/minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: minha feature'`
4. Push para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

## Autor

**Klauber Fischer**
