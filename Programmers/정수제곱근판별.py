# Solution_1
import math

def solution(n):
    new_n = math.sqrt(n)
    if new_n == int(new_n) : return (int(new_n)+1)**2
    else : return -1


# Solution_2
def solution(n):
    if n**0.5 == int(n**0.5) : return ((n**0.5)+1)**2
    else : return -1


# Solution_3
def solution(n):
    return ((n**0.5)+1)**2 if n**0.5 == int(n**0.5) else -1