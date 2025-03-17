from vtube_state.vtuber_graph import GraphState

def soliloquy_prompt_handler(state: GraphState) -> GraphState:
    persona_content = {"name": persona_name}
    combined_system_content = soliloquy_persona.format(**persona_content)

    # context_content = {"present_contents": "시청자들과 마인크래프트를 즐기고 있습니다.",
    # "situation_so_far": "시청자들과 마인크래프트를 시작하였습니다. user1은 마인크래프트 고수입니다. user2는 마인크래프트를 처음 플레이합니다. user2가 절벽에서 떨어져 죽었습니다. 최세나가 황소로부터 공격받습니다.",
    #                    "significant": "황소가 튀어나와 최세나를 계속해서 공격합니다. 황소가 거의 최세나를 죽일듯 달려듭니다. 황소는 자신의 친구들을 부릅니다.", "name": persona_name}

    # custom_chat_history = []
    # for msg in state["messages"]:
    #     custom_chat_history.append(msg.content)

    if len(state["significant"]) > 0:
        # 특이사항에 집중한(개그) 혼잣말
        context_content = {
            "present_contents": state["present_contents"],
            # "situation_so_far": state["situation_so_far"],
            "situation_so_far": state["summary"],
            # "conversation_record" : custom_chat_history,
            "significant": state["significant"],
            "name": persona_name,
        }
        context_prompt = context.format(**context_content)

    else:
        # 방송 진행용 혼잣말
        context_content = {
            "present_contents": state["present_contents"],
            # "situation_so_far": state["situation_so_far"],
            "situation_so_far": state["summary"],
            "name": persona_name,
        }
        context_prompt = ancher_context.format(**context_content)

    # context : 당신은 현재 ~을 하고 있습니다. {이전에 말한 말들} :

    prompt = [
        {"role": "system", "content": combined_system_content},
        {"role": "user", "content": context_prompt},
    ]

    return GraphState(soliloquy_prompt=prompt)