from vtube_state.vtuber_graph import GraphState
from langchain_core.messages import RemoveMessage, HumanMessage
from llm_core.llm_factory import create_llm

# 대화 내용 요약 및 메시지 정리 로직
# 고려해볼 점 : 메시지 요약시 대화의 연속성을 위해 마지막 메시지는 요약하지 말고, 나머지 메시지만 요약
def summarize_conversation(state: GraphState):
    # 이전 요약 정보 확인
    summary = state.get("summary", "")

    llm = create_llm()

    # 이전 요약 정보가 있다면 요약 메시지 생성
    if summary:
        summary_message = (
            f"This is summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into account the new messages above in Korean:"
        )
    else:
        # 요약 메시지 생성
        summary_message = "Create a summary of the conversation above in Korean:"

    # 요약 메시지와 이전 메시지 결합
    messages = state["messages"] + [HumanMessage(content=summary_message)]
    # 모델 호출
    response = llm.invoke(messages)
    # 오래된 메시지 삭제
    delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:]]
    # 요약 정보 반환
    return {"summary": response.content, "messages": delete_messages}