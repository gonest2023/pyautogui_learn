import pyautogui as pag
from pywinauto import Application,Desktop
import time
app = Application(backend='uia')
des = Desktop(backend='uia')

from pyperclip import copy,paste


def start():
    try:
        app.connect(title_re='.*Microsoft​ Edge',timeout=10)
    except:
        app.start('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        app.connect(title_re='.*Microsoft​ Edge', timeout=10)

    print(app.windows())

    return app['Dialog']

def goto(edge,url):

    # edge.dump_tree()
    edge['Edit'].set_text(url)

    pag.press('enter')
    time.sleep(2)

def find_text(text):
    pag.hotkey('ctrl','f')
    time.sleep(0.5)
    copy(text)
    time.sleep(0.5)
    pag.hotkey('ctrl', 'v')
    # paste()
    time.sleep(1)

def find_pic(pic):
    c = pag.locateCenterOnScreen(pic,confidence=0.9)
    print(c)
    if c:
        pag.moveTo(c.x,c.y)
        pag.click()

    time.sleep(1)




if __name__ == '__main__':
    edge = start()
    url = 'https://www.yoozhibo.com/zuqiu/shijiebei/video-p1.html'
    goto(edge,url)

    home='波兰'
    # visit = '波兰'
    visit = '阿根廷'
    title = f'{home}vs{visit} 全场录像及集锦'
    find_text(title)
    pic = 'pic/full.png'
    find_pic(pic)
    time.sleep(1)
    c5= '咪咕'
    find_text(c5)
    ys = 'pic/ys.png'
    find_pic(ys)
    time.sleep(4)
    fs = 'pic/fullscreen.png'
    find_pic(fs)