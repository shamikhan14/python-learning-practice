from typing import TypedDict
from langgraph.graph import StateGraph, START, END

TASKS = []

class AgentState(TypedDict):
    user_query: str
    route: str
    result: str

def router_node(state: AgentState):
    query = state["user_query"].lower()

    if "calculate" in query or "+" in query or "gst" in query:
        return {"route": "calculator"}

    elif "add task" in query or "show tasks" in query or "list tasks" in query or "what tasks" in query:
        return {"route": "task"}

    else:
        return {"route": "general"}

def route_decision(state: AgentState):
    if state["route"] == "calculator":
        return "calculator_node"
    elif state["route"] == "task":
        return "task_node"
    else:
        return "general_node"


def calculator_node(state: AgentState):
    query = state["user_query"]

    if "5000" in query and "18" in query:
        answer = "5000 + 18% GST = 5900"
    else:
        answer = "Calculator tool selected. Calculation logic will be improved later."

    return {"result": answer}


def task_node(state: AgentState):
    query = state["user_query"]
    query_lower = query.lower()

    if "add task" in query_lower:
        task = query.replace("Add task", "").replace("add task", "").strip()

        if task == "":
            return {"result": "Please tell me what task to add."}

        TASKS.append(task)
        return {"result": f"Task added successfully: {task}"}

    elif "show tasks" in query_lower or "list tasks" in query_lower or "what tasks" in query_lower:
        if len(TASKS) == 0:
            return {"result": "No tasks added yet."}

        task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(TASKS)])
        return {"result": f"Your tasks:\n{task_list}"}

    else:
        return {"result": "Task tool selected, but I need a clear task command."}


def general_node(state: AgentState):
    return {"result": "This is a general question. Later we will connect this to an LLM."}


graph_builder = StateGraph(AgentState)

graph_builder.add_node("router_node", router_node)
graph_builder.add_node("calculator_node", calculator_node)
graph_builder.add_node("task_node", task_node)
graph_builder.add_node("general_node", general_node)

graph_builder.add_edge(START, "router_node")

graph_builder.add_conditional_edges(
    "router_node",
    route_decision,
    {
        "calculator_node": "calculator_node",
        "task_node": "task_node",
        "general_node": "general_node",
    },
)

graph_builder.add_edge("calculator_node", END)
graph_builder.add_edge("task_node", END)
graph_builder.add_edge("general_node", END)


app = graph_builder.compile()

while True:
    user_input = input("Ask your agent: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Agent: Goodbye!")
        break

    response = app.invoke({
        "user_query": user_input,
        "route": "",
        "result": ""
    })

    print("Agent:", response["result"])