from vtube_state.vtuber_graph import GraphState
from typing import Literal


def check_userInput(
    state: GraphState,
) -> Literal["get_userInput", "soliloquy_prompt_handler"]:
    """ 
    INITIAL_STATE에서 분기
    user input(chat)에 따라 GET_USER_INPUT, GENERATE_CONVERSATION_TOPIC으로 분기한다.
    """
    # user_input을 받거나, 없다면 다른 노드로 분기(대화 주도하기)
    user_content = state.get("user_input", "")

    if len(user_content) > 0:
        return "get_userInput"
    else:
        return "soliloquy_prompt_handler"