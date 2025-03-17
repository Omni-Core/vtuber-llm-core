from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


# 전역 변수로 인스턴스 관리
_llm_instances = {}

def create_llm(model_name="gemini"):
    """
    LLM 인스턴스를 싱글톤으로 관리
    """
    if model_name not in _llm_instances:
        if model_name == "gemini":
            _llm_instances[model_name] = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                temperature=0.9,
            )
        elif model_name == "chatgpt":
            _llm_instances[model_name] = ChatOpenAI(
                model_name="gpt-4o-mini",
                temperature=0,
            )
        else:
            raise ValueError(f"Unsupported model: {model_name}")

    return _llm_instances[model_name]



# class LLMManager:
#     def __init__(self):
#         self._llm_instance = None
#         self._tool_llm_instance = None

#     def get_llm(self, model_name : str = "gemini", with_tool: bool = False):
#         """
#         LLM 인스턴스를 가져옵니다.
#         - with_tool=True: Tool이 붙은 LLM을 반환
#         - with_tool=False: 기본 LLM을 반환
#         """
#         if with_tool:
#             if not self._tool_llm_instance:
#                 self._tool_llm_instance = self._create_tool_llm(model_name)
#             return self._tool_llm_instance
#         else:
#             if not self._llm_instance:
#                 self._llm_instance = self._create_llm()
#             return self._llm_instance
        
#     def _create_llm(self, model_name : str):
#         """
#         LLM을 불러오는 함수
#         """

#         if model_name == "gemini":
#             return ChatGoogleGenerativeAI(
#                 model="gemini-2.0-flash",
#                 temperature=0.9,
#                 # top_p=0.9,
#             )
        
#         elif model_name == "chatgpt":
#             return ChatOpenAI(
#                 model_name="gpt-4o-mini",
#                 temperature=0,
#             )
    
#     # 나중에 확장 기능
#     def _create_tool_llm(self):
#         """
#         Tool이 결합된 LLM 생성 (추후 확장 가능)
#         """
#         # 추후에 Tool이 결합된 LLM로 확장 가능
#         return ChatGoogleGenerativeAI(
#             model="gemini-2.0-flash",
#             temperature=0.9,
#             tools=["search", "calculator"]  # 예시로 툴 추가
#         )



