from src.graph.state import State


def format_output(state: State) -> dict:
    # Rota de chegada com revisão humana: human_review preenche "aprovado".
    if "aprovado" in state:
        nota = state.get("nota_operador", "")
        if state["aprovado"]:
            texto = f"APROVADO pelo operador.\n{state['recomendacao']}"
        else:
            texto = "REJEITADO pelo operador."
        if nota:
            texto += f"\nNota do operador: {nota}"
        return {"resultado": texto}

    # Rota de regras e recusa: já preenchem resposta_llm.
    if state.get("resposta_llm"):
        resposta = state["resposta_llm"]
    else:
        resposta = str(state["messages"][-1].content)

    return {
        "resultado": f"Pergunta: {state['pergunta']}\nResposta: {resposta}"
    }
