import re
""" 
txt 파일 정규화 하는 함수 
숫자 뒤 한칸 띄우고, 목차마다 두칸 줄바꿈 한다.
추후 함수로 쓸 일이 있다면 함수로 바꾸겠다.

예시 동작)
타자(三), (七), (八)의 득점은 각 투수의 자책점이지만 팀의 자책점은 아니 다. 즉, 반자책점이다.
97통계관련 기록규칙
통계 (Statistics)

타자(三), (七), (八)의 득점은 각 투수의 자책점이지만 팀의 자책점은 아니 다. 즉, 반자책점이다.

97 통계관련 기록규칙
통계 (Statistics)

"""
with open("data/baseballBucket/baseballrule.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern_newline_before = r'\n*(?=[5-9]\d|10[0-5])'
text = re.sub(pattern_newline_before, '\n', text)

# 2) '숫자' 뒤에 공백이 없다면 공백을 추가한다.
#    - 캡처 그룹 '([5-9]\d|10[0-5])' = 58~105 범위 숫자
#    - '(?! )' = 그 뒤가 공백이 아닌 경우(negative lookahead)
pattern_space_after_number = r'([5-9]\d|10[0-5])(?! )'
text = re.sub(pattern_space_after_number, r'\1 ', text)

print(text)

with open("data/baseballBucket/baseballrule.txt", "w", encoding="utf-8") as f:
    f.write(text)
