from src.graph.prompts.analyze_prompt import ANALYZE_PROMPT
from src.graph.state import State
from src.graph.tools import TOOLS
from src.utils.llm_adapter import get_llm


def analyze(state: State) -> dict:
    llm = get_llm().bind_tools(TOOLS)

    if state.get("messages"):
        # Volta do ciclo tools -> analyze: o histórico já tem as mensagens do prompt
        # e os resultados das ferramentas. Reenviar só o prompt faria o modelo perder isso.
        historico = []
        mensagens = state["messages"]
    else:
        pergunta = f"{state.get('pergunta', '')}\n\nFrota:\n{state.get('dados', '')}"
        historico = ANALYZE_PROMPT.format_messages(pergunta=pergunta)
        mensagens = historico

    resposta = llm.invoke(mensagens)
    return {"messages": historico + [resposta]}
