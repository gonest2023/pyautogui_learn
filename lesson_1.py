import pyautogui as pag

dis = 800
t = 0.5

for i in range(3):
    pag.move(0,dis,t,pag.easeInQuad)
    dis1= -dis / 2

    pag.move(0, dis1, t,pag.easeOutQuad)
    dis = abs(dis1)
    t = t/2

