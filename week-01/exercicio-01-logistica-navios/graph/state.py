from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages

class State(TypedDict, total=False):
    pergunta: str
    intent: str
    frota: dict
    dados: str
    resposta_llm: str
    resultado: str
    messages: Annotated[list, add_messages]
    recomendacao: str
    aprovado: bool
    nota_operador: str