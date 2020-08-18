'''

문제 링크
  - https://www.acmicpc.net/problem/10039

문제 설명
  - 점수가 40점 이상인 학생들은 그 점수 그대로 처리
  - 40점 미만인 학생들은 40점으로 처리
  - 5명의 점수가 주어질 때, 평균 점수를 구하는 프로그램 작성

입력
  - 총 5줄의 입력
  - 점수는 모두 0점 이상, 100점 이하인 5의 배수
  - 따라서 평균 점수는 항상 정수로 구해짐

출력
  - 첫째 줄에 학생 5명의 평균 점수 출력

'''

# s = [int(input()) for i in range(5)]
# print(s)
# s2 = [i if i>=40 else 40 for i in s]
# print(s2)
# print(int(sum(s2)/5))

#########

# s = [int(input()) for i in range(5)]
# print(int(sum([i if i>=40 else 40 for i in s])/5))

#########

print(int(sum([i if i>=40 else 40 for i in [int(input()) for i in range(5)]])/5))