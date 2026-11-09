from langchain_core.prompts import ChatPromptTemplate

PROMPT_UMA_LINHA = ChatPromptTemplate.from_messages(
    [("human", "Qual navio chega primeiro ao porto? Frota: {frota}")]
)

PROMPT_MELHORADO = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um despachante do porto. O ETA em horas de cada navio é "
            "distancia_nm dividido por velocidade_kn. Chega primeiro quem tem o menor ETA. "
            "Responda com o id do navio eo ETA em horas.",
        ),
        ("human", "Frota: {frota}\n\nQual navio chega primeiro ao porto?"),
    ]
)