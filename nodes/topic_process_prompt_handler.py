from vtube_state.vtuber_graph import GraphState
from personas.manager import PersonaManager


def topic_process_prompt_handler(state: GraphState) -> GraphState:
    """
    주어진 topic을 이용해서 스몰토크를 생성하는 노드
    topic을 바탕으로 혼잣말을 함
    """

    # Persona 정보 불러오기
    persona_manager = PersonaManager()
    persona_name = persona_manager.persona_name
    llm = persona_manager.llm

    persona_content = {"name": persona_name}

    topic = state["topic"]
    present_contents = state["present_contents"]
    user_content = {"topic": topic, "present_contents": present_contents}

    # 캐싱된 템플릿 불러옴
    topic_generation_template = persona_manager.topic_generation_template
    storytelling_template = persona_manager.storytelling_template

    combined_system_content = topic_generation_template.format(**persona_content)
    user_prompt_content = storytelling_template.format(**user_content)

    prompt = [
        {"role": "system", "content": combined_system_content},
        {"role": "user", "content": user_prompt_content},
    ]

    answer = llm.invoke(prompt).content
    # print(answer)

    return GraphState(vtuber_output=answer)
