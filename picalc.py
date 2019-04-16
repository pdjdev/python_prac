#30813 박동준


title='''┌───┐ ┌──┐
│┌─┐│ └┐┌┘
│└─┘│  ││
│┌──┘  ││
││     ││
││    ┌┘└┐ 
└┘    └──┘'''

import math
print(title,'=',math.pi)

#print('계산 시작... (2의 10억승) ', end='')
#getnum = 2**1000000000
#print('...완료')

#확인문제1

r = input('반지름 입력(float):')

print('지름: \t', float(r) * 2)
print('둘레: \t', (math.pi * 2 * float(r)))
print('넓이: \t', (math.pi * float(r) ** 2))
      

#확인문제2

x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2"'))

print("두 점 (",x1,",",y1,") (",x2,",",y2,") 사이 거리:",
      math.sqrt((x1-x2)**2 + (y1-y2)**2))


#확인문제3

degree = int(input('각도 입력:'))
rad=math.radians(degree)

print("입력받은 각도 (",degree,")를 라디안값으로 변환:", rad)
print("sin" + str(degree) + "˚ =", math.sin(rad))
print("cos" + str(degree) + "˚ =", math.cos(rad))
print("tan" + str(degree) + "˚ =", math.tan(rad))


