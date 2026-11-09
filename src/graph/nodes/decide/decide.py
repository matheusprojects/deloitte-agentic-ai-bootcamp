import json


from src.graph.prompts.prompts import PROMPT_MELHORADO
from src.graph.state import State
from src.utils.llm_adapter import get_llm


def decide(state: State) -> dict:
    frota = state.get("frota", {})
    chain = PROMPT_MELHORADO | get_llm()
    resposta = chain.invoke({"frota": json.dumps(frota, ensure_ascii=False)})

    # Gera recomendação operacional com base na decisão de chegada
    navios = frota.get("navios", [])
    recomendacao = "Monitorar e preparar berço de atracação para o primeiro navio previsto a chegar."

    return {
        "resposta_llm": resposta.content,
        "recomendacao": recomendacao,
    }
