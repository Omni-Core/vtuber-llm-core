from vtube_state.vtuber_graph import GraphState
from typing import Literal
from langgraph.graph import END

# 대화 종료 또는 요약 결정 로직
def should_continue(state: GraphState) -> Literal["summarize_conversation", END]:
    # 메시지 목록 확인
    messages = state["messages"]

    # 메시지 수가 6개 초과라면 요약 노드로 이동
    if len(messages) > 6:
        return "summarize_conversation"
    return END