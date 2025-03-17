from vtube_state.vtuber_graph import GraphState
from personas.persona_config import get_persona

def result_merging(state: GraphState) -> GraphState:
    """ 
    유저 chat, 버튜버 답변(AI answer)의 답변을 종합한다. 
    
    should_continue를 통해 SUMMARIZE_CONVERSATION 노드로 진행하거나 대화를 저장한다. 

    """
    # State를 사용하지 않고 llm_answer 노드에서 불러오는 일반 함수로 정의해도 괜찮을 것 같다.
    # 버튜버 답변 종합, raw 데이터에 추가(혹은 가공해서 추가)
    # 외부에 저장하는 것 만으로 충분할 것 같다.
    # 날짜별, 행동(콘텐츠)별로 csv파일에 저장

    # persona 정보 불러오기
    persona_name = get_persona()

    new_messages = [
        ("user", state["user_id"] + ":" + state["user_input"]),
        ("assistant", persona_name + ":" + state["vtuber_output"]),
    ]

    return GraphState(messages=new_messages)