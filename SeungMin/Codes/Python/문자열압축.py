def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(my_solution(s[i]))
    return answer

def my_solution(s):
    # 문자열 총 길이
    idx = len(s)

    # 최소 문자열 길이 | Default : 기존 문자열 길이
    min_len = len(s)

    # 만들어지는 문자열 확인용
    final_letter = s

    # 1개부터 짤라본다. 절반 초과의 길이는 자를 필요가 없다.
    # i : 자를 문자열 길이
    for i in range(1, idx//2+1):
        # 초기값 설정
        letters = s[0:i]  # 가장 처음 문자열, 이후에 값들을 추가해 갈 변수
        current_letter = s[0:i]  # 현재 선택된 문자열, 이후의 문자열과 비교 용도
        current_idx = i  # 현재 index 저장 변수

        # current_idx 를 자르는 길이만큼 늘려주면서 문자열 총 길이보다 크거나 같아 지면 종료
        while current_idx < idx:
            next_letter = s[current_idx:current_idx+i]  # 다음 i 길이의 문자열

            # 다음 문자열과 현재 문자열이 같음
            if next_letter == current_letter:
                # 마지막 character 가 a~z 사이인 경우 "2" 만 추가
                if 97 <= ord(letters[-1]) <= 122:
                    letters += "2"

                # 마지막 character 가 숫자인 경우
                else:
                    # 현재까지 반복된 갯수를 센다.
                    num_idx = len(letters)-1
                    while 48 <= ord(letters[num_idx]) <= 57:
                        num_idx -= 1
                    num_idx += 1
                    num = int(letters[num_idx:]) + 1  # 현재까지 반복된 갯수에 1을 추가
                    letters = letters[:num_idx] + str(num)  # 반복된 갯수를 문자열 마지막에 추가
            # 다음 문자열과 현재 문자열이 다른 경우
            # 다음 문자열을 최종 문자열에 추가한 후, 현재 문자열 갱신
            else:
                letters += next_letter
                current_letter = next_letter

            # 다음 자를 문자열로 넘어간다.
            current_idx += i

        # 압축된 문자열의 길이가 현재까지의 최소 압축 문자열 길이보다 작으면 갱신
        if len(letters) < min_len:
            min_len = len(letters)
            final_letter = letters

    return min_len

# s = [
#     "aabbaccc",
#     "ababcdcdababcdcd",
#     "abcabcdede",
#     "abcabcabcabcdededededede",
#     "xababcdcdababcdcd"
# ]
s = "aabbaccc"
print(my_solution(s))