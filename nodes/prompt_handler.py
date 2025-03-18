from vtube_state.vtuber_graph import GraphState
from personas.persona_config import get_persona, get_persona_template

def prompt_handler(state: GraphState) -> GraphState:
    """ 
    persona에 맞게 persona_name, template들을 가져와 prompt를 조립하는 함수

    LLM_ANSWER 노드로 prompt가 넘어간다.

    """
    # 프롬프트 조립

    # persona 파라미터들 : 나중에 다른 state에서 받아오는걸로 수정
    user_id = state["user_id"]
    user_chat = state["user_input"]
    present_content = state["present_contents"]

    # persona 정보 불러오기
    persona_name = get_persona()
    persona, chat, previous_chat = get_persona_template()


    if True:
        instruction = f"현재는 {present_content}를 진행하고 있습니다. 여기서 크게 벗어나지 않는 선에서 다음 {user_id}를 언급하거나 또는, {user_chat}를 반드시 먼저 한번 출력하고 답변하세요."
    else:
        instruction = f"{user_chat}를 종합적으로 고려한 답변을 출력하세요."

    # print("==========messages==========")
    custom_chat_history = []
    for msg in state["messages"]:
        # print(msg.content)
        custom_chat_history.append(msg.content)

    # print("============================")

    # persona 정보
    # persona_content = {"name": persona_name, "searched_sentense": state["retrieved_fewshot"]}
    persona_content = {"name": persona_name}
    chat_content = {
        "name": persona_name,
        "instruction": instruction,
        "user_input": state["user_input"],
    }
    previous_content = {
        "summary": state["summary"],
        "conversation_record": custom_chat_history,
    }
    print(state["user_input"])

    # persona template에 정보 입력
    formatted_persona = persona.format(**persona_content)
    previous_info = previous_chat.format(**previous_content)

    formatted_chat = chat.format(**chat_content)

    # prompt 구성
    combined_system_content = formatted_persona + "\n\n" + previous_info
    formatted_chat = chat.format(**chat_content)

    prompt = [
        {"role": "system", "content": combined_system_content},
        {"role": "user", "content": formatted_chat},
    ]

    return GraphState(prompt=prompt)
