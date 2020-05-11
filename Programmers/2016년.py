def solution(a, b):    
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(month[0:a-1]) + b
    
    answer = day[days%7-1] 
    return answer