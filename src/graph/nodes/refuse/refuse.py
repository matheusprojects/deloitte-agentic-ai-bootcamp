from src.graph.state import State

TEXTO_RECUSA = (
    "Solicitação recusada: Não posso responder a esta pergunta porque ela está fora do "
    "escopo de operações, regras e navegação da frota marítima do Porto Alfa."
)


def refuse(state: State) -> dict:
    return {"resposta_llm": TEXTO_RECUSA}

