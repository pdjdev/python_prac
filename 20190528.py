#30813 박동준
from datetime import datetime

#======================기본문제======================
adminId = input('관리자 ID: ')
adminPw = input('관리자 PW: ')

f = open('logfile.tmp', 'w')
f.write(adminId + '\n' + adminPw)

print('저장 완료')
f.close()


#======================확인문제======================
f = open('logfile.tmp', 'r')
readId = f.readline()
readPw = f.readline()
f.close()

if input('ID:').strip()==readId.strip() and input('PW:').strip()==readPw.strip():
    print('로그인 되었습니다')
else:
    print('값을 확인해 주십시오')


#======================도전문제======================
newfile = input('새로 백업할 파일명을 입력해 주세요:')
f = open('logfile.tmp', 'r')
f2 = open(newfile + '.tmp', 'w')
f2.write(f.read())
print('저장되었습니다 (\\' + newfile + '.tmp)')

f.close()
f2.close()


#======================심화문제1======================
print('==접속 시간 기록 모드==')
acsTime = datetime.today()

adminId = input('관리자 ID: ')
adminPw = input('관리자 PW: ')

f = open('logfile-withtime.tmp', 'w')
f.write(adminId + '\n' + adminPw)
f.write('\n[접속시간:'+acsTime.strftime('%y-%m-%d %a %H:%M:%S')+']')
f.write('\n[갱신시간:'+datetime.today().strftime('%y-%m-%d %a %H:%M:%S')+']')

print('저장 완료')
f.close()


#======================심화문제2======================

#문제 파일 쓰기
questionDb = '''1+1은?|2
5×8은?|40
영국의 수도는?|런던
가장 지루한 중학교는?|로딩중
그럼 가장 Cool한 고등학교는?|냉장고
'좋은 눈을 가진 사슴'을 다섯 글자로 뭐라고 할까?|굿아이디어
2 이상의 자연수 n에 대하여 실수 전체의 집합에서 정의된 함수 f(x) = e^(x+1) × {x^2+(n-2)x-n+3} + ax가 역함수를 갖도록 하는 실수 a의 최솟값을 g(n)이라 하자. 1 <= g(n) <= 8을 만족시키는 모든 n의 값의 합은?|52'''
open('questions.txt', 'w').write(questionDb)


#문제 파일 불러오기
with open('questions.txt', 'r') as f:
    questions = f.readlines()

#퀴즈 시작
count = 0
    
print('========= 개꿀잼 퀴즈 타임 =========')
for s in questions:
    count += 1
    tmp = s.strip().split('|')
    print('\n[' + str(len(questions)) + '개 중 ' + str(count) + '번째 문제]\n' + '질문: ' + tmp[0])
    if input('입력: ') == tmp[1]:
        print('정답!')
    else:
        print("틀렸습니다! 정답은 '" + tmp[1] + "' 였습니다...")
    
    





