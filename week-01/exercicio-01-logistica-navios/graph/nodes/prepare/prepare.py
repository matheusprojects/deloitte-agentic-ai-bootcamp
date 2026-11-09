from src.graph.state import State


def prepare(state: State) -> dict:
    navios = state.get("frota", {}).get("navios", [])

    linhas = [
        f"- id: {n.get('id')}, destino: {n.get('destino')}, "
        f"distancia_nm: {n.get('distancia_nm')}, velocidade_kn: {n.get('velocidade_kn')}, "
        f"em_tempestade: {n.get('em_tempestade')}, "
        f"combustivel_t: {n.get('combustivel_t')}, reserva_t: {n.get('reserva_t')}"
        for n in navios
    ]

    return {"dados": "\n".join(linhas)}
