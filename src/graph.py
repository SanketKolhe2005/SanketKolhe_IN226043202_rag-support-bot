from langgraph.graph import StateGraph

def process(state):
    query = state["query"]
    retriever = state["retriever"]

    docs = retriever.invoke(query)

    if not docs:
        return {"response": "No answer found", "escalate": True}

    answer = state["qa"](query, docs)

    escalate = False
    if len(answer) < 20 or "not sure" in answer.lower():
        escalate = True

    return {"response": answer, "escalate": escalate}


def hitl(state):
    return {"response": "Escalated to human support"}


def build_graph():
    builder = StateGraph(dict)

    builder.add_node("process", process)
    builder.add_node("hitl", hitl)

    builder.set_entry_point("process")

    builder.add_conditional_edges(
        "process",
        lambda x: "hitl" if x["escalate"] else "__end__"
    )

    return builder.compile()