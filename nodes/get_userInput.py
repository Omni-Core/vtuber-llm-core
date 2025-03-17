from vtube_state.vtuber_graph import GraphState

def get_userInput(state: GraphState) -> GraphState:
    """ 
    user_id, user_content(chat)의 입력을 받는다. 

    """
    user_id, user_content = state["user_id"], state["user_input"]
    return GraphState(user_id=user_id, user_content=user_content)