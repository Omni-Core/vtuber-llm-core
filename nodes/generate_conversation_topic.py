from vtube_state.vtuber_graph import GraphState
from personas.manager import PersonaManager


def generate_conversation_topic(state: GraphState) -> GraphState:
    """
    방송을 이끌어나가는 주제를 정하는 노드.
    '현재 진행 방식'과 '이전 대화 주제'를 바탕으로,
    자연스럽게 이어갈 수 있는 다음 대화 주제를 하나 생성한다.

    이번에는 "{name}은 ~했다." 형식의 스몰토크/썰을 생성하도록 한다.
    """
    present_contents = state["present_contents"]
    previous_topic = state.get("topic", "방송시작")
    
    # Persona 정보 불러오기
    persona_manager  = PersonaManager()
    persona_name = persona_manager.persona_name
    llm = persona_manager.llm


    prompt = f""" 
    현재 진행 방식: {present_contents}
    이전 대화 주제: {previous_topic}
    
    # 다음 조건을 만족하며, '{persona_name}'에 대한 짧은 스몰토크 문장을 하나 생성하세요:
    1) 문장은 단 한 줄(하나의 문장)만 작성합니다.
    2) 주제는 질문 형태가 아니라, **평서형** 문장으로 작성합니다.
    3) **'{persona_name}은 ~~~했습니다.'** 처럼, '{persona_name}'이 주어가 되어
       최근에 했거나 하고 있는 일, 스몰토크 느낌의 짧은 썰 등을 표현하세요.
    4) 문장 길이는 너무 길지 않게 해주세요.
    5) 가능한 한 구체적으로, 흥미로운 방송 주제가 되도록 해주세요.

    # 예시(가능한 형태):
    - "{persona_name}은 주말 동안 오사카 여행을 다녀왔습니다."
    - "{persona_name}은 어제 새로운 게임을 플레이했습니다."
    - "{persona_name}은 오늘 아침에 기상하자마자 달리기를 했습니다."

    # 다음 대화 주제(한 문장):
    """

    new_topic = llm.invoke(prompt).content.strip()
    # debug_topics.append([previous_topic, new_topic])

    return GraphState(topic=new_topic)
