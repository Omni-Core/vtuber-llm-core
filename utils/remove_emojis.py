import re


# 나중에 나온 답변에서 이모티콘을 제거
def remove_emojis(text):
    # 이모티콘을 포함하는 정규식 패턴
    emoji_pattern = re.compile(
        "[\U0001f600-\U0001f64f"  # 감정 이모티콘
        "\U0001f300-\U0001f5ff"  # 물리적 이모티콘
        "\U0001f680-\U0001f6ff"  # 교통 이모티콘
        "\U0001f700-\U0001f77f"  # 기호, 사물 이모티콘
        "\U0001f780-\U0001f7ff"  # 추가 기호 이모티콘
        "\U0001f800-\U0001f8ff"  # 상징 이모티콘
        "\U0001f900-\U0001f9ff"  # 사람 이모티콘
        "\U0001fa00-\U0001fa6f"  # 물건 이모티콘
        "\U0001fa70-\U0001faff"  # 사람의 동작 이모티콘
        "\U00002702-\U000027b0"  # 기타 기호
        "]+",
        flags=re.UNICODE,
    )
    return re.sub(emoji_pattern, "", text)
