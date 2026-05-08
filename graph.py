from langgraph.graph import StateGraph
from typing import TypedDict

from utils import get_retriever, get_llm, generate_answer


class State(TypedDict):
    query: str
    docs: list
    answer: str
    escalate: bool


retriever = get_retriever()
llm = get_llm()


def retrieve_node(state):
    docs = retriever.invoke(state["query"])
    return {"docs": docs}


def generate_node(state):
    answer = generate_answer(state["query"], state["docs"], llm)

    escalate = False

    if len(state["docs"]) == 0:
        escalate = True

    if "not available" in answer.lower():
        escalate = True

    return {"answer": answer, "escalate": escalate}


def route_node(state):
    if state["escalate"]:
        return "human"
    return "end"


def human_node(state):
    print("\nEscalated to human agent.")
    response = input("Enter manual response: ")
    return {"answer": response}


def build_graph():
    graph = StateGraph(State)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)
    graph.add_node("human", human_node)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "generate")

    graph.add_conditional_edges(
        "generate",
        route_node,
        {
            "human": "human",
            "end": "__end__"
        }
    )

    graph.add_edge("human", "__end__")

    return graph.compile()