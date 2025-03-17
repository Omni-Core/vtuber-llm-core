from typing import TypedDict, Annotated, List
from langchain_core.documents import Document
from langgraph.graph.message import add_messages
import operator


# State 정의
class GraphState(TypedDict):
    user_id: Annotated[str, "user id"]
    user_input: Annotated[str, "user input"]
    retrieved_fewshot: Annotated[List[Document], operator.add]
    vtuber_output: Annotated[str, "Vtuber answer"]
    # 시청자들과 대화할 때 사용하는 프롬프트
    prompt: Annotated[list, "final prompt"]
    # 혼잣말, 대화 이끌어나갈때 사용하는 프롬프트
    soliloquy_prompt: Annotated[list, "soliloquy prompt string"]

    # 현재 진행중인 컨텐츠
    present_contents: Annotated[str, "present contents of vtuber"]

    # 현재까지의 상황(context 중심적으로 보는 상황)
    situation_so_far: Annotated[str, "summary of context"]

    # 특이 사항(갑작스럽게 발생한, 또는 주목할만한 상황)
    significant: Annotated[str, "significant moment if exist"]

    # 현재 사용되는 스몰토크(혼잣말) 주제
    topic: Annotated[str, "present topic of this broadcast"]

    # 단기 기억 구성 요소들
    # 유저-버튜버 간 주고받는 대화, 또는 버튜버 혼잣말(soliloquy)
    messages: Annotated[list, add_messages]
    # 단기 기억(유저-버튜버간 대화 뿐만 아니라 혼잣말까지 모조리 요약)
    # 별 중요하지 않은 내용들도 단기 기억에서 요약이 될 텐데 이걸 어떻게 처리할 지 고민
    summary: str

    # 혼잣말(썰: topic-> generate) 저장 메시지(단기 기억에 사용됨) : 했던 말 등등
    topic_memory: Annotated[list, add_messages]
    topic_summary: str

    # 기억하는 유저들 : 유저마다 다른 반응
    remembered_users: Annotated[set[str], "Set of remembered user IDs"]