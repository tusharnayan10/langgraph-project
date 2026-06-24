from typing import TypedDict

class PortfolioState(TypedDict):
    amount_usd: float
    total_usd: float
    total_inr: float
    

my_obj: PortfolioState = {
    "amount_usd": 1000.0,
    "total_usd": 1000.0,
    "total_inr": 1000.0,
} 


def calc_total(state: PortfolioState) -> PortfolioState:
    state["total_usd"] =  state["amount_usd"] * 1.80
    return state

def conver_to_inr(state: PortfolioState) -> PortfolioState:
    state["total_inr"] = state["total_usd"] * 95.0
    return state


from langgraph.graph import StateGraph

builder = StateGraph(PortfolioState)

builder.add_node("calc_total_node", calc_total)
builder.add_node("convert_to_inr_node", conver_to_inr)

builder.add_edge(START, "calc_total_node")
builder.add_edge("calc_total_node", "convert_to_inr_node")
builder.add_edge("convert_to_inr_node", END)

graph = builder.compile()


# graph.invoke({amount_usd: 1000.0})

