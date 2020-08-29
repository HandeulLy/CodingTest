def oper_one(expre) :
    return abs(eval(expre))

def oper_two(expre, oper) :
    s_e_1 = expre.split(oper[0])
    for i, s in enumerate(s_e_1) :
        s_e_1[i] = str(oper_one(s))
    s_e_1_r = oper_one(oper[0].join(s_e_1))

    s_e_2 = expre.split(oper[1])
    for i, s in enumerate(s_e_2) :
        s_e_2[i] = str(oper_one(s))
    s_e_2_r = oper_one(oper[1].join(s_e_2))
    return max(s_e_1_r, s_e_2_r)
    
def solution(expression):
    answer, operator = 0, []
    if '*' in expression : operator.append('*')
    if '+' in expression : operator.append('+')
    if '-' in expression : operator.append('-')

    if len(operator) == 1 :
        return oper_one(expression)
    elif len(operator) == 2 : 
        return oper_two(expression, operator)
    else :
        s_e_1 = expression.split(operator[0])
        for i, s in enumerate(s_e_1) :
            s_e_1[i] = str(oper_two(s, operator[1:]))
        s_e_1_r = oper_one(operator[0].join(s_e_1))

        s_e_2 = expression.split(operator[1])
        for i, s in enumerate(s_e_2) :
            s_e_2[i] = str(oper_two(s, [operator[0], operator[2]]))
        s_e_2_r = oper_one(operator[1].join(s_e_2))
        
        s_e_3 = expression.split(operator[2])
        for i, s in enumerate(s_e_3) :
            s_e_3[i] = str(oper_two(s, operator[:2]))
        s_e_3_r = oper_one(operator[2].join(s_e_3))
        
        return max(s_e_1_r, s_e_2_r, s_e_3_r)


i_e = "100-200*300-500+20"
print(solution(i_e)) # 60420

# i_e = "50*6-3*2"
# print(solution(i_e)) # 300

# i_e = "0+1+0+0"
# print(solution(i_e)) # 300

i_e = "999*999*999*999*999-999+0"
print(solution(i_e)) # 300


'''
참가자들은 자신에게 주어진 숫자와 연산문자를 이용해 가장 큰 수를 만들어 제출한다
연산자의 우선 순위는 본인이 재정의 할 수 있고, 2개 이상의 연산자가 동일한 우선순위를 가질 수는 없다
계산 결과가 음수면 절대값으로 변환하여 처리한다
제출 숫자가 가장 큰 참가자가 우승자가 되고, 그 숫자 값이 우승 상금이다
'''