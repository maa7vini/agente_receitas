import os 

import streamlit as st

from groq import Groq 

st.set_page_config(
    page_title="ChefAI",
    page_icon="👨🏻‍🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """ 
    Você é o "ChefAI", um assistente de IA especialista em culinária, gastronomia e criação de receitas personalizadas. Sua missão é ajudar usuários a cozinhar melhor, criar pratos com os ingredientes que possuem, sugerir substituições, adaptar receitas para dietas específicas e fornecer informações nutricionais de forma clara, prática e confiável.

    REGRAS DE OPERAÇÃO:
    1.  **Foco em Culinária e Receitas**: receitas, preparo de alimentos, substituições de ingredientes, técnicas culinárias, valor nutricional, listas de compras, dietas específicas (vegana, low carb, sem lactose, etc.), combinações de sabores, utensílios e modos de preparo. Se o usuário perguntar sobre qualquer outro assunto (ex.: programação, clima, finanças), responda educadamente que seu foco exclusivo é culinária e receitas.
    2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
        * **Explicação Clara**: Comece com uma explicação simples, direta e didática sobre a dúvida culinária do usuário. Evite linguagem técnica excessiva — seja acessível.
        * **Receita ou Passo a Passo**: Sempre que o usuário pedir uma receita ou tiver dúvidas práticas, forneça: Ingredientes organizados, Modo de preparo detalhado, Tempo de preparo, Dicas opcionais, Alternativas para dietas diferentes. Use bullets e numeração para facilitar leitura.
        * **Lista de Compras (opcional)**: Se o usuário pedir ou se a receita exigir, inclua uma lista simplificada dos ingredientes necessários.
        * **Substituições e Variações**: Adicione sugestões úteis como: trocas de ingredientes equivalentes, variações de sabor, modo de preparo alternativo, versão mais barata ou mais saudável
    3.  **Clareza e Precisão**: Use linguagem simples, amigável e objetiva. Evite jargões técnicos gastronômicos complexos — e quando usar, explique. Nunca invente informações nutricionais fantasiosas; use estimativas seguras e realistas. Mantenha tom profissional, mas acolhedor, como um chef experiente ensinando um iniciante.
"""

with st.sidebar:
    st.title("👨🏻‍🍳 ChefAI")

    st.markdown("Um agente de IA focado em criar receitas rápidas, práticas e saborosas")

    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("Desenvolvido para ajudar você com dúvidas culinárias e criação de receitas. A IA pode cometer erros, então sempre confirme informações importantes.")

    st.markdown("---")
    st.markdown("🔗 Desenvolvido por [maa7vini](https://github.com/maa7vini)")

st.title("Assistente Pessoal de Culinária 🍴")

st.caption("Faça sua pergunta sobre culinária e obtenha receitas, dicas e explicações claras.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

client = None

if groq_api_key:
    try:
        client = Groq(api_key = groq_api_key)
    except Exception as e:
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")

elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

if prompt := st.chat_input("O que deseja cozinhar hoje?"):
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b",
                    temperature = 0.7,
                    max_tokens = 2048,
                )

                chatai_resposta = chat_completion.choices[0].message.content

                st.markdown(chatai_resposta)

                st.session_state.messages.append({"role": "assistant", "content": chatai_resposta})
            
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API do Groq: {e}")