from vtube_state.vtuber_graph import GraphState
from llm_core.llm_factory import create_llm

def llm_answer(state: GraphState) -> GraphState:
    # LLM 실행
    llm = create_llm()
    vtuber_output = llm.invoke(state["prompt"]).content

    """ 
    debug_io
    """
    # debug_io.append(["a", vtuber_output])

    return GraphState(vtuber_output=vtuber_output)