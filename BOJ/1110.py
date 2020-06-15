number = int(input())
number_10 = number // 10
number_01 = number % 10

number_new = -1
count = 0

while number_new != number :
    count += 1
    number_new = number_01*10 + (number_10 + number_01)%10
    number_10 = number_new // 10
    number_01 = number_new % 10
    
print(count)