from langchain_core.prompts import ChatPromptTemplate

CLASSIFY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um assistente de despacho marítimo encarregado de classificar a intenção da pergunta do usuário.\n"
            "Classifique a pergunta em exatamente uma das seguintes três intenções:\n"
            "- 'primeiro_a_chegar': Perguntas sobre qual navio da frota chega primeiro, quem vai chegar antes ou tempo de chegada da frota atual.\n"
            "- 'regras': Perguntas sobre regras operacionais, como funciona o cálculo de ETA, fórmulas ou diretrizes gerais do porto.\n"
            "- 'outros': Perguntas fora do escopo de operações marítimas, saudações ou assuntos irrelevantes.",
        ),
        ("human", "{pergunta}"),
    ]
)
