#30812 박동준
import time
 
def titleprint(title):
 
    padding = int((30 - len(title)) / 2)
 
    print('┌──────────────────────────────┐')
    print('│' + ' '*(padding)+title+' '*padding+'│')
    print('└──────────────────────────────┘')
 
 
def binary(num):
    binStr = ''
    while (num != 0):
        remain = num % 2
        num = num // 2
        binStr = str(remain) + binStr
    return binStr
 
 
#==========2,3-총합 구하기==========
 
titleprint('Number Sum')
print("※'E'를 입력하면 입력이 종료됩니다")
end = False
inp = ''
log = ''
snum = 0
 
while(not end):
 
    inp = input(log + '? > ')
 
    if inp.isdigit():
        snum += int(inp)
        log += inp + '+'
    else:
        if inp == 'e' or inp == 'E':
            end = True
        else:
            print('올바른 형식을 입력해 주십시오.')
 
print('식:', log[:len(log)-1])
print('총합:', snum)
 
print('\n')
 
 
 
#==========4-이진법 변환기==========
 
titleprint('Binary Converter')
 
print('결과:', binary(int(input('입력: '))))
 
print('\n')
 
 
 
#==========5-합계 구하기(for)==========
 
i = 1
s = 0
 
while i <= 5:
    print(i, end = '+')
    s += i
    i += 1
 
print(' 합계는', s)
 
print('\n')
 
 
#==========기본1-입력받고 총합 구하기==========
 
loop = int(input('몇 개의 수를 합하시겠습니까?'))
count = 0
snum = 0
 
while (count < loop):
    inp = input(str(count+1)+'번째:')
 
    if inp.isdigit():
        count += 1
        snum += int(inp)
 
print('총합:', snum)
 
print('\n')
 
 
#==========기본2-카운트다운==========
 
count = int(input('카운트 다운 숫자 입력: '))
 
while (count > 0):
    print('Time remaining:', count)
    count -= 1
    time.sleep(1)
 
print('LIFTOFF')
 
print('\n')
