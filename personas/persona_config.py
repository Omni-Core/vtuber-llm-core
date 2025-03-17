from langchain_core.prompts import load_prompt

def get_persona(persona_name="박점례"):
    """ 
    persona config 반환 함수

    """
    if persona_name == "박점례":
        custom_chat_history = []

    return persona_name


def get_persona_template(persona_name="박점례"):
    """ 
    persona 템플릿 반환 함수
    """
    if persona_name == "박점례":
        persona_raw = "personas/parkJeomRye/prompts/persona.yaml"
        chat_raw = "personas/parkJeomRye/prompts/chat.yaml"
        previous_chat_raw = "personas/parkJeomRye/prompts/previous_chat.yaml"
    
    persona = load_prompt(persona_raw, encoding="utf-8")
    chat = load_prompt(chat_raw, encoding="utf-8")
    previous_chat = load_prompt(previous_chat_raw, encoding="utf-8")

    return persona, chat, previous_chat
