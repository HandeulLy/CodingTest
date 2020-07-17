# 입력 : 문자열 s(길이 100,000이하), 문자는 '('과 ')'으로만 이루어짐
# 목표 : 괄호로 구성된 문자열이 올바르게 짝 지어진 것인지 확인
# 출력 : 올바른 짝이면 True, 아니면 False를 반환​

# 짝이 맞지 않는 경우 : 왼쪽 괄호만 있을 때(조건1), 오른쪽 괄호만 있을 때(조건2)​

# Stack 구조를 활용하면 될 듯
# 왼쪽 괄호를 만났을 때 push, 오른쪽 괄호를 만났을 때 pop
# 오른쪽 괄호를 만나서 pop()하면 왼쪽 괄호가 나와야 함
# 스택 구조에 아무것도 없어서 pop()을 할 수 없다면 짝이 맞지 않으면 조건2
# 문자열 끝까지 push/pop 작업을 수행했는데 스택 구조에 원소가 있다면 조건1

def solution(s):
    stack = []
    for i in s :
        if i == '(' : stack.append(i)
        else :
            if len(stack) == 0 : return False
            if stack.pop() != '(' : return False # 다른 문자가 입력된 경우를 위해서
    return True if len(stack) == 0 else False