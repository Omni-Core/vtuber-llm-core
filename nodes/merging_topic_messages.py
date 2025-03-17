from vtube_state.vtuber_graph import GraphState


def merging_topic_messages(state: GraphState) -> GraphState:
    """
    topic_messages를 합치고, 일정 개수 이상이 되면 summarize한다.
    """
    new_topics = [("user", state["topic"]), ("assistant", state["vtuber_output"])]
    return GraphState(topic_memory=new_topics)
