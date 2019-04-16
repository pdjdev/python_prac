#30813 박동준

import math

#사용자 정의 함수 영역

#덧셈
def add(n1, n2):
    ans = n1 + n2
    return ans

#뺄셈
def mns(n1, n2):
    ans = n1 - n2
    return ans

#나눗셈
def div(n1, n2):
    ans = n1 / n2
    return ans

#곱셈
def mtp(n1, n2):
    ans = n1 * n2
    return ans

#원 넓이 구하기
def cirarea(n1):
    ans = mtp(mtp(n1, n1), math.pi)
    return ans

#원 둘레 구하기
def cirlong(n1):
    ans = mtp(mtp(n1, 2), math.pi)
    return ans

#f(x) = x^2 + x + 1 함수
def f(x):
    return add(add(mtp(x, x), x), 1)

#그리드 그리기 (심화문제)
def drawGrid():
    print(("+----"*2+"+\n"+("|    "*2+"|\n")*3)*2+"+----"*2+"+")

#사용자 정의 그리드 그리기
def drawCustomGrid(x, y):
    print(("+--"*x + "+\n" + "|  "*x + "|\n")*y, end='')
    print("+--"*x + "+\n")


#========================================================================================

drawGrid()

inpOK = False
while(not inpOK):
    try:
        inp1 = int(input("처음숫자: "))
        inp2 = int(input("두번째숫자: "))
        inpOK = True
    except:
        print("오류 발생.")
        
print('\n[더해보리기]')
print(inp1, '＋', inp2, '=', add(inp1,inp2), '\n')

print('[빼보리기]')
print(inp1, '－', inp2, '=', mns(inp1,inp2), '\n')

print('[나눠보리기]')
print(inp1, '÷', inp2, '=', div(inp1,inp2), '\n')

print('[곱해보리기]')
print(inp1, '×', inp2, '=', mtp(inp1,inp2), '\n')

print('[ f(x) = x^2 + x + 1 구해보리기]')
print('f(' + str(inp1) + ') =', f(inp1))
print('f(' + str(inp2) + ') =', f(inp2))

print('[원둘레, 원넓이]')
print('반지름',inp1,'인 원의 둘레: %5.2f, 넓이: %5.2f' %(cirlong(inp1), cirarea(inp1)))
print('반지름',inp1,'인 원의 둘레: %5.2f, 넓이: %5.2f' %(cirlong(inp2), cirarea(inp2)), '\n')

print('[가로:'+str(inp1)+' 세로:'+str(inp2)+'인 표 그리기]')
drawCustomGrid(inp1, inp2)






