# 👨🏻‍🍳 ChefAI – Agente Inteligente de Receitas

O **ChefAI** é um agente de inteligência artificial especializado em culinária, capaz de gerar receitas personalizadas, sugerir combinações de ingredientes, explicar técnicas gastronômicas e ajudar no preparo de pratos de forma rápida e intuitiva.

Desenvolvido com **Python**, **Streamlit** e **Groq**, o projeto demonstra como criar um agente de IA funcional com interface limpa, responsiva e fácil de usar.

> ⚠️ **Importante:** Para executar este projeto, você precisa de uma **Groq API Key**, necessária para que o agente consiga gerar respostas.

---

## ✨ Funcionalidades

- Geração de receitas personalizadas com base em ingredientes, preferências e restrições.
- Explicações sobre técnicas culinárias e métodos de preparo.
- Sugestões de combinações de sabores e harmonizações.
- Interface interativa desenvolvida com Streamlit.
- Respostas ultrarrápidas utilizando modelos Groq.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit**
- **Groq API**
- **Dotenv (.env)**
- **Prompt Engineering**

---

## 📦 Instalação e Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo .env na raiz do projeto:

```bash
GROQ_API_KEY=sua_chave_aqui
```
Você pode obter sua chave gratuitamente no site da Groq.

Execute o projeto:

```bash
streamlit run main.py
```

## 📁 Estrutura do Projeto
```bash
/chefai
│
├── app.py               # Arquivo principal Streamlit
├── requirements.txt     # Dependências do projeto
├── .env.example         # Exemplo de configuração
└── README.md            # Documentação
```

## 🎯 Objetivo
Criar um agente de IA completo e funcional, servindo como exemplo prático para estudos de:
- **LLMs**
- **Agentes de IA**
- **Integração de APIs**
- **Streamlit**
- **Criação de interfaces para modelos de linguagem**

## 🌐 Acesse o ChefAI Online
Use a versão online aqui:
👉 [ChefAI](https://chefai-agente-ia.streamlit.app/)
