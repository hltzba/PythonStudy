# encoding:utf-8
#! section18.py - pyautogui demo
import pyautogui
def getScreenSize():
    print(pyautogui.size())

def curseMoveTO():
    pyautogui.moveTo(100,100,duration=0.5)
    pyautogui.moveTo(200,200,duration=0.5)
    pyautogui.moveTo(0,100,duration=0.5)
    pyautogui.moveTo(100,0,duration=0.5)

def curseMoveRelation():#相对位置移动
    for i in range(1):
        pyautogui.moveRel(100,0,duration=0.25)
        pyautogui.moveRel(0,100,duration=0.25)
        pyautogui.moveRel(-100,0,duration=0.25)
        pyautogui.moveRel(0,-100,duration=0.25)

def getCursePosition():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x,y=pyautogui.position()
            posstr='X:'+str(x).rjust(4)+'Y:'+str(y).rjust(4)
            print(posstr,end='')
            print('\b'*len(posstr),end='',flush=True)
    except KeyboardInterrupt:
        print('\nDone.')


#getScreenSize()
#curseMoveTO()
#curseMoveRelation()
getCursePosition()