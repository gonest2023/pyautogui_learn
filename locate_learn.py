import pyautogui as pag

# pag.screenshot('555.jpg',region=(100,100,1000,1000))
# im = pag.screenshot()
# print(im)
# pillow opencv
pic = 'pic/ck.png'
# pos = pag.locateOnScreen(pic,confidence=0.9,grayscale=True,region=(300,0,1000,200))
# print(pos)
# print(pos[2])
# print(pos.left)
# print(pos.width)
#

# tttt   ttt         ttttt



# pos_ = pag.center(pos)
# print(pos_)
# pag.moveTo(pos_.x,pos_.y,0.5)

# pip install opencv-python
# pos = pag.locateCenterOnScreen(pic)
# print(pos)
# tt = 'pic/tt.png'
# tt_pos = pag.locateAllOnScreen(tt)
# for i in tt_pos:
#     print(i)

# c = pag.pixel(1000,200)
# im = pag.screenshot()
# c = im.getpixel((1000,200))
# print(c)

ff = pag.pixelMatchesColor(1000,200,(53,33,43),tolerance=10)
print(ff)
