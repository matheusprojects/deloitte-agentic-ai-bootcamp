from langgraph.types import Command

from src.graph.builder import build_graph
from src.utils.langfuse_client import flush, run_config

def main() -> None:
    print("Iniciando o agente da frota..")
    graph = build_graph()

    pergunta = input("Pergunta: ").strip() or "Qual navio chega primeiro ao porto?"

    # O checkpointer exige um thread_id para identificar a conversa
    config = run_config(configurable={"thread_id": "semana-1"})
    saida = graph.invoke({"pergunta": pergunta}, config=config)

    # Se o grafo pausou em human_review, mostra a recomendação e pede a decisão
    if "__interrupt__" in saida:
        pedido = saida["__interrupt__"][0].value
        print("\nRecomendação do agente:\n" + pedido["recomendacao"])

        aprovado = input("Aprovar? (s/n): ").strip().lower() == "s"
        nota = input("Nota (opcional): ").strip()

        saida = graph.invoke(Command(resume={"aprovado": aprovado, "nota": nota}), config=config)

    print("\n" + saida["resultado"])
    flush()

main()
