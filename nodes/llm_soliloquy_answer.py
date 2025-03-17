from vtube_state.vtuber_graph import GraphState

def llm_soliloquy_answer(state: GraphState) -> GraphState:

    vtuber_output = llm.invoke(state["soliloquy_prompt"]).content
    # debug_io.append(["solo", vtuber_output])

    return GraphState(vtuber_output=vtuber_output)