#30812 박동준
from datetime import datetime

def titleprint(title):
    
    padding = int((30 - len(title)) / 2)

    print('┌──────────────────────────────┐')
    print('│' + ' '*(padding+1)+title+' '*padding+'│')
    print('└──────────────────────────────┘')




#==========심화문제1==========

titleprint('Hybrid Calculator')

print('하이브리드 자동차의 배터리 정보를 입력 (단위: kWh)')
fullcap = float(input("배터리 총용량? (ex.27):"))
availcap = float(input("현재 배터리 잔량? (ex.12.2):"))

percent = availcap / fullcap

print('주행 모드:', end=' ')

if (percent > 0.3):
    print('전기')
else:
    print('휘발유')

print('\n\n')

#==========심화문제2==========

titleprint('Standard Age Calculator')

bday = input("생년원일 입력 (ex.2001-1-23):").split('-')
age = datetime.today().year - int(bday[0])
if (datetime.today().month <= int(bday[1])) and (datetime.today().day <= int(bday[2])):
        age -= 1

print('당신의 만 나이는', age, '세 입니다')
print('운전 가능 여부:', end=' ')

if (age >= 18):
    print ('가능')
else:
    print ('불가능')


print('\n\n')


#==========7호 확인문제1==========

titleprint('Club Assignment')

Korean = int(input("국어 성적:"))
English = int(input("영어 성적:"))

if Korean >= 90 and English >= 80:
    print("가입 승인됨")
else:
    if Korean >= 90:
        print("영어 성적이 부족함")
    else:
        print("국어 성적이 부족함")

print('\n\n')

#==========7호 확인문제1==========

titleprint('Pos./Neg. Discriminator')

num1 = int(input('첫번째 숫자 입력:'))
num2 = int(input('두번째 숫자 입력:'))

print('두 정수의 곱은', end=' ')

if num1 > 0:
    if num2 > 0:
        print('양수')
    elif num2 < 0:
        print('음수')
    else:
        print('0')
elif num1 < 0:
    if num2 > 0:
        print('음수')
    elif num2 < 0:
        print('양수')
    else:
        print('0')
else:
    print('0')


