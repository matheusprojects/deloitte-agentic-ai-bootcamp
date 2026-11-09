from typing import Literal
from pydantic import BaseModel, Field

from src.graph.prompts.classify_prompt import CLASSIFY_PROMPT
from src.graph.state import State
from src.utils.llm_adapter import get_llm


class Intencao(BaseModel):
    intent: Literal["primeiro_a_chegar", "regras", "outros"] = Field(
        description="Intenção da pergunta do usuário: 'primeiro_a_chegar', 'regras' ou 'outros'."
    )


def classify(state: State) -> dict:
    llm = get_llm()
    structured_llm = llm.with_structured_output(Intencao)
    chain = CLASSIFY_PROMPT | structured_llm

    resultado = chain.invoke({"pergunta": state.get("pergunta", "")})

    intent = resultado.intent if hasattr(resultado, "intent") else resultado["intent"]
    return {"intent": intent}
