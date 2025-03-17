from vtube_state.vtuber_graph import GraphState
from typing import Literal
from langgraph.graph import END

# 대화 종료 또는 요약 결정 로직
def should_merge_topic_memory(
    state: GraphState,
) -> Literal["summarize_topic_memory", END]:
    # 메시지 목록 확인
    topic_memory = state["topic_memory"]

    # 메시지 수가 6개 초과라면 요약 노드로 이동
    if len(topic_memory) > 6:
        return "summarize_topic_memory"
    return END
