
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



workflow = StateGraph(GraphState)

# 노드 추가
workflow.add_node(INITIAL_STATE, initial_state)
workflow.add_node(GET_USER_INPUT, get_userInput)
workflow.add_node(PROMPT_HANDLER, prompt_handler)
workflow.add_node(SOLILOQUY_PROMPT_HANDLER, soliloquy_prompt_handler)
workflow.add_node(LLM_SOLILOQUY_ANSWER, llm_soliloquy_answer)
workflow.add_node(LLM_ANSWER, llm_answer)
workflow.add_node(RESULT_MERGING, result_merging)
workflow.add_node(SUMMARIZE_CONVERSATION, summarize_conversation)

# 엣지 추가
workflow.add_edge(GET_USER_INPUT, PROMPT_HANDLER)
workflow.add_edge(PROMPT_HANDLER, LLM_ANSWER)
workflow.add_edge(LLM_ANSWER, RESULT_MERGING)

workflow.add_edge(SOLILOQUY_PROMPT_HANDLER, LLM_SOLILOQUY_ANSWER)
workflow.add_edge(LLM_SOLILOQUY_ANSWER, RESULT_MERGING)


# 조건부 엣지 추가
workflow.add_conditional_edges(
    RESULT_MERGING,
    should_continue,
)

workflow.add_conditional_edges(INITIAL_STATE, check_userInput)

# 요약 노드에서 종료 노드로의 엣지 추가
workflow.add_edge(SUMMARIZE_CONVERSATION, END)

# 시작점 설정
workflow.set_entry_point(INITIAL_STATE)

# 메모리 설정
memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

# 시각화하기
# visualize_graph(app)