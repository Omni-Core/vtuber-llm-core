from vtube_state.vtuber_graph import GraphState
from personas.manager import PersonaManager
from langchain_core.messages import RemoveMessage


# topic memory 요약
def summarize_topic_memory(state: GraphState):
    # 이전 요약 정보 확인
    topic_summary = state.get("topic_summary", "")
    raw_topic_memory = state["topic_memory"]

    topic_memory = ""

    i = 0
    for mem in raw_topic_memory:
        if i % 2 == 0:
            topic_memory += f"topic:{mem.content}\n"
        else:
            topic_memory += f"content:{mem.content}\n"
        i += 1

    print(topic_memory)

    # Persona 정보 불러오기
    persona_manager = PersonaManager()
    persona_name = persona_manager.persona_name
    llm = persona_manager.llm

    system_summary_additional_prompt = f""" 
    이때까지 요약한 내용인 {topic_summary}에 아래 메시지 목록을 추가해 요약하세요.

    """

    system_prompt = f"""
    다음은 '{persona_name}'이 개인적으로 활동한 최근 이야기들입니다. 
    주어진 메시지들은 장난스러운 말투와 유머가 섞여 있지만, 당신은 이러한 표현을 모두 배제하고, **내용 중심으로만 간결하게 요약**해야 합니다.

    ### 요약 규칙:
    1. **중요 사건이나 활동 중심으로 요약**해 주세요.
    2. 캐릭터의 유머, 장난스러운 말투, 감정 표현은 제외하고 **객관적인 사건만 요약**해 주세요.
    3. 중복되는 정보는 하나로 통합하여 작성해 주세요.
    4. 필요 없는 부연 설명은 생략하고, 핵심 정보만 간결하게 작성해 주세요.
    5. 요약은 **1~2개의 문장**으로 작성해 주세요.
    6. "{persona_name}"가 주어가 되도록 자연스럽게 작성해 주세요.

    ### 메시지 목록:
    {topic_memory}

    ### 내용 중심의 요약:

    """

    topic_content = {
        "persona_name": persona_name,
        "topic_memory": state["topic_memory"],
    }

    topic_summary_content = {"topic_summary": topic_summary}
    print(topic_content)

    context_summarize = system_prompt.format(**topic_content)
    print(context_summarize)

    topic_summarize = system_summary_additional_prompt.format(**topic_summary_content)

    # 이전 요약 정보가 있다면 요약 메시지 생성
    if topic_summary:
        summary_message = topic_summarize + context_summarize
    else:
        # 요약 메시지 생성
        summary_message = context_summarize

    # 요약 메시지와 이전 메시지 결합
    # topic_memory = state["topic_memory"] + [HumanMessage(content=summary_message)]
    # 모델 호출
    response = llm.invoke(summary_message)
    # 오래된 메시지 삭제
    delete_messages = [RemoveMessage(id=m.id) for m in state["topic_memory"][:]]
    # 요약 정보 반환
    return {"topic_summary": response.content, "topic_memory": delete_messages}
