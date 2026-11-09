from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from src.graph.nodes.analyze.analyze import analyze
from src.graph.nodes.answer_rules.answer_rules import answer_rules
from src.graph.nodes.classify.classify import classify
from src.graph.nodes.format_output.format_output import format_output
from src.graph.nodes.human_review.human_review import human_review
from src.graph.nodes.prepare.prepare import prepare
from src.graph.nodes.receive.receive import receive
from src.graph.nodes.refuse.refuse import refuse
from src.graph.routing import route_by_intent
from src.graph.state import State
from src.graph.tools import TOOLS


def build_graph():
    graph = StateGraph(State)

    # 1. Registro dos nós
    graph.add_node("receive", receive)
    graph.add_node("classify", classify)
    graph.add_node("prepare", prepare)
    graph.add_node("analyze", analyze)
    graph.add_node("tools", ToolNode(TOOLS))
    graph.add_node("answer_rules", answer_rules)
    graph.add_node("refuse", refuse)
    graph.add_node("human_review", human_review)
    graph.add_node("format_output", format_output)

    # 2. Fluxo inicial: carregar dados da frota e classificar pergunta
    graph.add_edge(START, "receive")
    graph.add_edge("receive", "classify")

    # 3. Roteamento condicional por intenção
    graph.add_conditional_edges(
        "classify",
        route_by_intent,
        {
            "primeiro_a_chegar": "prepare",
            "chegada": "prepare",
            "regras": "answer_rules",
            "outros": "refuse",
        },
    )

    # 4. Ciclo de ferramentas: analyze pede tools até não haver mais tool_calls
    graph.add_edge("prepare", "analyze")
    graph.add_conditional_edges(
        "analyze",
        tools_condition,
        {"tools": "tools", END: "human_review"},
    )
    graph.add_edge("tools", "analyze")

    # 5. Aprovação humana, convergência e fim do grafo
    graph.add_edge("human_review", "format_output")
    graph.add_edge("answer_rules", "format_output")
    graph.add_edge("refuse", "format_output")
    graph.add_edge("format_output", END)

    return graph.compile(checkpointer=MemorySaver())
