# vtuber-llm-core
V-tuber LLM core


# 📂 Project Structure: AI VTuber Core

## 📄 주요 파일 설명

- `workflow.py`: 전체 LLM 워크플로우의 구조와 흐름을 정의합니다.
- `llm_core/`: LLM 인스턴스와 관련된 디렉토리입니다.
- `vtube_state/`: 그래프에서 사용할 상태 객체를 관리하는 디렉토리입니다.
- `nodes/`: 그래프의 각 단계에서 실행될 함수(노드)를 정의합니다.
- `conditions/`: 그래프의 조건부 분기 로직을 관리합니다.
- `personas/`: 페르소나 관련 설정 및 템플릿을 관리합니다. 각각의 페르소나 별 데이터 및 프롬프트가 저장되어 있습니다.
- `utils/`: 기타 유틸리티 함수들을 관리합니다.
- `data/`: 퓨삿 데이터가 포함된 파일입니다.(legacy)


## ⚙️ 사용 방법
- test.ipynb를 참고하여 그래프를 실행합니다.
- 유저 채팅이 있다면 유저 채팅에 응답을, 없다면 혼잣말을 실행합니다.

