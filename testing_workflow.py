from vtube_state.vtuber_graph import GraphState
from langgraph.graph import END, StateGraph
from nodes.initial_state import initial_state
from nodes.generate_conversation_topic import generate_conversation_topic
from nodes.topic_process_prompt_handler import topic_process_prompt_handler
from nodes.merging_topic_messages import merging_topic_messages
from nodes.summarize_topic_memory import summarize_topic_memory
from nodes.merging_topic_messages import merging_topic_messages
from conditions.should_merge_topic_memory import should_merge_topic_memory
from langgraph.checkpoint.memory import MemorySaver

# from langchain_teddynote.graphs import visualize_graph


workflow = StateGraph(GraphState)

workflow.add_node("initial_state", initial_state)
workflow.add_node("generate_conversation_topic", generate_conversation_topic)
workflow.add_node("topic_process_prompt_handler", topic_process_prompt_handler)
workflow.add_node("merging_topic_messages", merging_topic_messages)
workflow.add_node("summarize_topic_memory", summarize_topic_memory)

workflow.add_edge("initial_state", "generate_conversation_topic")
workflow.add_edge("generate_conversation_topic", "topic_process_prompt_handler")
workflow.add_edge("topic_process_prompt_handler", "merging_topic_messages")

# 조건부 엣지 추가
workflow.add_conditional_edges(
    "merging_topic_messages",
    should_merge_topic_memory,
)

workflow.add_edge("summarize_topic_memory", END)

# 시작점 설정
workflow.set_entry_point("initial_state")

# 메모리 설정
memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

# visualize_graph(app)
