#타자연습
#pip install hgtk six requests
import turtle, random, time, hgtk, requests

dbtxt = requests.get('https://raw.githubusercontent.com/pdjdev/tazadb/master/db.txt').text.split('\n')

history = []
t = 1
l = 1

def getkolen(txt):
    return len(hgtk.text.decompose(txt).replace('ᴥ', ''))

while True:
    pick = random.choice(dbtxt).strip()
    if not p
    ick in history:
        print('\n'*40)
        
        print('소요 시간:', t)
        print('길이:', l)
        print('타/분:', 60/(t/l))
        
        history.append(pick)
        time.sleep(0.5)
        print('>' + pick)

        t = time.time()
        enter = ''
        
        while not enter == pick:
            enter = input(':')

        t = time.time() - t
        l = getkolen(enter)
        
        print()

    else:
        if len(history) == len(dbtxt) - 1: break
