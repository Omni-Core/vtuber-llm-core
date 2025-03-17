from vtube_state.vtuber_graph import GraphState

def initial_state(state: GraphState) -> GraphState:
    """ 
    아래 GraphState들을 초기화 하는 함수.
    GraphState를 초기화 하면 check_userInput에 따라 GET_USER_INPUT, GENERATE_CONVERSATION_TOPIC으로 분기한다.

    present_contents : 현재 진행중인 콘텐츠 e.g. 야구 관람, 시청자와 인사
    significant      : 현재 발생한 특이사항 e.g. 시청자가 들어왔습니다.
    summary          : 시청자와 대화 요약

    """

    present_contents = state.get("present_contents", "")
    significant = state.get("significant", "")
    # situation_so_far = ""

    # summary 키 없는 문제 때문에 넣음, 추후 Init 노드 고려중
    summary = state.get("summary", "")

    # custom_chat_history = []
    # for msg in state["messages"]:
    #     custom_chat_history.append(msg.content)

    # context_content = {
    #     "present_contents": state["present_contents"],
    #     "summary": summary,
    #     "conversation_record" : custom_chat_history,
    # }

    # if summary:
    #     summary_message = (
    #         f"This is summary of the conversation to date: {summary}\n\n"
    #         "Extend the summary by taking into account the new messages above in Korean:"
    #     )
    # else:
    #     # 요약 메시지 생성
    #     summary_message = "Create a summary of the conversation above in Korean:"

    # context_summarize = understanding_context_flow.format(**context_content) + str(HumanMessage(content=summary_message))

    # context_output = llm.invoke(context_summarize).content
    return GraphState(
        present_contents=present_contents, summary=summary, significant=significant
    )
    # return GraphState(present_contents= present_contents, summary= summary, significant=significant, situation_so_far=context_output)
