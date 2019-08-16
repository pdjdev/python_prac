#30813 박동준
import turtle, time, wget, os

t = turtle.Pen()
a = turtle.Pen()
txt = turtle.Pen()
t.speed(0)
a.speed(0)
t.ht()
a.ht()
txt.ht()

def wait():
    time.sleep(3)
    penreset()
    time.sleep(0.1)

def penreset():
    t.clear()
    a.clear()
    t.color('black')
    a.color('black')
    t.penup()
    a.penup()
    t.home()
    a.home()
    t.pendown()
    a.pendown()

def writetxt(s):
    txt.clear()
    txt.penup()
    txt.goto(0,300)
    txt.pendown()
    txt.write(s, align='center', font=('돋움', 15))
    txt.pendown()
    
os.system('copy "sa-digital-number.ttf" "%WINDIR%\Fonts" && pause')
open('run.vbs', 'w').write('''Set objShell = CreateObject("Shell.Application")
Set objFolder = objShell.Namespace("C:\Windows\Font")
Set objFolderItem = objFolder.ParseName("sa-digital-number.ttf")
objFolderItem.InvokeVerb("Install")''')
os.system('run.vbs')

writetxt('이름 쓰기')

name = turtle.textinput('입력', '이름?')
t.penup()
t.goto(-50,20)
t.pendown()
for x in range(2):
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
t.penup()
t.home()
t.goto(0,-12)
t.write(name, align='center', font=('궁서', 20, 'bold'))
wait()

writetxt('회전 정사각형')
for i in range(100):
    for x in range(4):
        t.forward(100)
        t.left(90)
    t.left(3)
wait()

writetxt('정육각형')
for i in range(6):
    for x in range(2):
        t.forward(100)
        t.left(120)
    t.forward(100)
    t.left(60)
wait()

writetxt('시계')
wget('https://github.com/pdjdev/python_prac/raw/master/sa-digital-number.ttf')
os.system('sa-digital-number.ttf')
while True:
    tm = time.gmtime()
    s = time.asctime(tm)
    
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.write(s, align='center', font=('Arial', 30))
    t.pendown()
    time.sleep(1)
wait()
