
from vtube_state.vtuber_graph import GraphState
from langgraph.graph import END, StateGraph
from nodes.initial_state import initial_state
from nodes.get_userInput import get_userInput
from nodes.prompt_handler import prompt_handler
from nodes.soliloquy_prompt_handler import soliloquy_prompt_handler
from nodes.llm_soliloquy_answer import llm_soliloquy_answer
from nodes.llm_answer import llm_answer
from nodes.result_merging import result_merging
from nodes.summarize_conversation import summarize_conversation
from conditions.should_continue import should_continue
from conditions.check_userInput import check_userInput
from nodes.generate_conversation_topic import generate_conversation_topic
from nodes.topic_process_prompt_handler import topic_process_prompt_handler
from nodes.merging_topic_messages import merging_topic_messages
from nodes.summarize_topic_memory import summarize_topic_memory
from nodes.merging_topic_messages import merging_topic_messages
from conditions.should_merge_topic_memory import should_merge_topic_memory
from langgraph.checkpoint.memory import MemorySaver
# from langchain_teddynote.graphs import visualize_graph

# 노드 식별자 정의
INITIAL_STATE = "initial_state"
GET_USER_INPUT = "get_userInput"
PROMPT_HANDLER = "prompt_handler"
SOLILOQUY_PROMPT_HANDLER = "soliloquy_prompt_handler"
LLM_ANSWER = "llm_answer"
LLM_SOLILOQUY_ANSWER = "llm_soliloquy_answer"
RESULT_MERGING = "result_merging"
SUMMARIZE_CONVERSATION = "summarize_conversation"

GENERATE_CONVERSATION_TOPIC = "generate_conversation_topic"
TOPIC_PROCESS_PROMPT_HANDLER = "topic_process_prompt_handler"
MERGING_TOPIC_MESSAGES = "merging_topic_messages"
SUMMARIZE_TOPIC_MEMORY = "summarize_topic_memory"



workflow = StateGraph(GraphState)

# 노드 추가(유저와 대화)
workflow.add_node(INITIAL_STATE, initial_state)
workflow.add_node(GET_USER_INPUT, get_userInput)
workflow.add_node(PROMPT_HANDLER, prompt_handler)
workflow.add_node(LLM_ANSWER, llm_answer)
workflow.add_node(RESULT_MERGING, result_merging)
workflow.add_node(SUMMARIZE_CONVERSATION, summarize_conversation)

## 혼잣말 노드(legacy)
# workflow.add_node(SOLILOQUY_PROMPT_HANDLER, soliloquy_prompt_handler)
# workflow.add_node(LLM_SOLILOQUY_ANSWER, llm_soliloquy_answer)


## topic 생성후 썰풀기 노드(이후 혼잣말 노드로 대체할 가능성 있다.)
workflow.add_node(GENERATE_CONVERSATION_TOPIC, generate_conversation_topic)
workflow.add_node(TOPIC_PROCESS_PROMPT_HANDLER, topic_process_prompt_handler)
workflow.add_node(MERGING_TOPIC_MESSAGES, merging_topic_messages)
workflow.add_node(SUMMARIZE_TOPIC_MEMORY, summarize_topic_memory)

# 엣지 추가 : 유저와 대화 엣지
workflow.add_edge(GET_USER_INPUT, PROMPT_HANDLER)
workflow.add_edge(PROMPT_HANDLER, LLM_ANSWER)
workflow.add_edge(LLM_ANSWER, RESULT_MERGING)

# 엣지 추가 : 썰풀기 엣지(혼잣말)
workflow.add_edge(GENERATE_CONVERSATION_TOPIC, TOPIC_PROCESS_PROMPT_HANDLER)
workflow.add_edge(TOPIC_PROCESS_PROMPT_HANDLER, MERGING_TOPIC_MESSAGES)

# 혼잣말 엣지(legacy)
# workflow.add_edge(SOLILOQUY_PROMPT_HANDLER, LLM_SOLILOQUY_ANSWER)
# workflow.add_edge(LLM_SOLILOQUY_ANSWER, RESULT_MERGING)


# 조건부 엣지 추가 : 유저와 대화
workflow.add_conditional_edges(
    RESULT_MERGING,
    should_continue,
)

# 조건부 엣지 추가 : 썰풀기 엣지(혼잣말)
workflow.add_conditional_edges(
    MERGING_TOPIC_MESSAGES,
    should_merge_topic_memory
)

workflow.add_conditional_edges(INITIAL_STATE, check_userInput)

# 요약 노드에서 종료 노드로의 엣지 추가
workflow.add_edge(SUMMARIZE_CONVERSATION, END)
workflow.add_edge(SUMMARIZE_TOPIC_MEMORY, END)
# 시작점 설정
workflow.set_entry_point(INITIAL_STATE)

# 메모리 설정
memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

# 시각화하기
# visualize_graph(app)