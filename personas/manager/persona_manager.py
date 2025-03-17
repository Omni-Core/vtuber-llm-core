from functools import cached_property
from llm_core.llm_factory import create_llm
from langchain_core.prompts import load_prompt


class PersonaManager:
    _instance = None

    def __new__(cls, persona_name="박점례"):
        if cls._instance is None or cls._instance.persona_name != persona_name:
            cls._instance = super().__new__(cls)
            cls._instance._initialize(persona_name)
        return cls._instance

    def _initialize(self, persona_name):
        self.persona_name = persona_name
        self.llm = create_llm()

    @cached_property
    def persona_template(self):
        """
        persona 템플릿을 캐싱하여 반환
        """
        if self.persona_name == "박점례":
            persona_raw = "personas/parkJeomRye/prompts/persona.yaml"
            chat_raw = "personas/parkJeomRye/prompts/chat.yaml"
            previous_chat_raw = "personas/parkJeomRye/prompts/previous_chat.yaml"

            persona = load_prompt(persona_raw, encoding="utf-8")
            chat = load_prompt(chat_raw, encoding="utf-8")
            previous_chat = load_prompt(previous_chat_raw, encoding="utf-8")

        else:
            raise ValueError(f"Unsupported persona: {self.persona_name}")

        return persona, chat, previous_chat

    @cached_property
    def topic_generation_template(self):
        """
        topic_generation 템플릿을 캐싱하여 반환
        """
        topic_generation = "personas/parkJeomRye/prompts/topic_generation.yaml"
        return load_prompt(topic_generation, encoding="utf-8")

    @cached_property
    def storytelling_template(self):
        """
        storytelling_template 템플릿을 캐싱하여 반환
        """
        storytelling = "personas/parkJeomRye/prompts/storytelling_template.yaml"
        return load_prompt(storytelling, encoding="utf-8")

    def reset(self):
        print(f"Persona Manager 캐시 초기화 {self.persona_name}")

        if "persona_template" in self.__dict__:
            del self.__dict__["persona_template"]
