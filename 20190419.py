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

 
#============================실습문제============================

titleprint('Word Reverser ')

s=''
while True:
    m = input('입력:')
    if m == '':
        break
    s = m + s
print('결과:', s)

print('\n')



#============================확인문제============================

titleprint('Check 8-3 ')

i = 10

while (i <= 100):
    if (i%3!=0):
        print(i, end=' ')
    i += 10

print('완료.')

print('\n')



#============================도전문제1============================

titleprint('Even/Odd Sum')

num = int(input('n 입력: '))
i = 0
even = 0
odd = 0

while (i<=num):
    if (i%2==0):
        even += i
    else:
        odd += i

    i += 1

print('짝수 합:', even, '\n홀수 합:', odd)

print('\n')



#============================도전문제2============================

titleprint('5 Multiplication')

i = 1

while (i<=9):
    print('5 ×', i, '=', 5*i)
    i += 1

print('\n')



#============================심화문제1============================

titleprint(' [sum_(k=1)^(n-1) 2k] calc')

n = int(input('n 입력:'))
k = 1
res = 0

while (k <= n-1):
    res += 2 * k
    k += 1

print('결과:', res)

print('\n')



#============================심화문제2============================

titleprint('9*9 Multiplication')

i = 1

while (i<=9):
    j = 1
    while (j<=9):
        print(str(i)+'×'+str(j)+'='+str(i*j), end='\t')
        j += 1
    print()
    i += 1
    
