from langgraph.types import interrupt

from src.graph.state import State


def human_review(state: State) -> dict:
    # A recomendação é a resposta final do analyze (última mensagem).
    recomendacao = str(state["messages"][-1].content)

    # Pausa o grafo. Na retomada, o valor de Command(resume=...) volta aqui.
    # Este nó roda de novo desde o início ao retomar, então nada antes do
    # interrupt pode ter efeito colateral.
    decisao = interrupt(
        {"recomendacao": recomendacao, "pergunta": "Aprovar a recomendação?"}
    )

    return {
        "recomendacao": recomendacao,
        "aprovado": bool(decisao["aprovado"]),
        "nota_operador": decisao.get("nota", ""),
    }
