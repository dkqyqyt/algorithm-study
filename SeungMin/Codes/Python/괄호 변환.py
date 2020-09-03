def solution(p):
    answer = convert(p)
    return answer

# 변환 함수
def convert(p):
    # 빈 문자열일 경우 빈 문자열 반환
    if p == "":
        return ""

    # ord('(') = 40
    # ord(')') = 41
    check = [0]*128  # 괄호 갯수를 저장하고 이용하기 위한 배열, 아스키코드 전체를 담기 위해 128 크기로 만듦
    check[ord(p[0])] = 1  # 괄호 문자열의 첫 문자 확인

    # u 문자열, 가장 작은 크기의 균형잡힌 문자열을 찾는다.
    idx = 1
    while idx < len(p):
        # 균형잡힌 문자열 여부 확인
        if not check[ord('(')] and not check[ord(')')]:
            break

        if p[idx] == '(':
            if check[ord(')')]:
                check[ord(')')] -= 1
            else:
                check[ord('(')] += 1
        else:
            if check[ord('(')]:
                check[ord('(')] -= 1
            else:
                check[ord(')')] += 1
        idx += 1
    # idx 가 v 문자열의 첫 시작 지점이 된다.
    u = p[:idx]
    v = p[idx:]

    # u 가 올바른 괄호 문자열인지 여부에 따라 분기
    if proper_bracket(u):  # u 가 올바른 괄호 문자열이라면
        # v 에 대해 재귀적으로 변환 후 u 뒤에 붙인다.
        return u + convert(v)
    else: # u 가 올바른 괄호 문자열이 아니라면
        tmp = "("  # 빈 문자열에 '('을 붙인다.
        tmp += convert(v)  # v 에 대해 재귀적으로 변환 후 붙인다.
        tmp += ")"  # ')'을 붙인다.
        u = u[1:-1]  # u 의 첫 번째 문자와 마지막 문자 제거
        # 나머지 문자열은 괄호를 뒤집는다.
        for char in u:
            if char == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp

# 올바른 괄호 문자열인지 여부 반환
def proper_bracket(s):
    stack = []
    for char in s:
        if char == ')':  # 닫는 괄호인 경우
            if not stack:  # 스택이 비어있다면 올바른 괄호 문자열이 아니다.
                return False
            else: # 스택이 비어있지 않다면 '('가 들어있기 때문에 pop!
                stack.pop()
        else:  # 여는 괄호인 경우 스택에 여는 괄호 push!
            stack.append('(')
    # 반복문이 정상적으로 종료됐다면 올바른 괄호 문자열이다.
    return True

p = "()))((()"
# check ="))(("
# convert(p)
# print(proper_bracket(check))
print(solution(p))