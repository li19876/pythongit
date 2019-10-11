import pyautogui as g
from PIL import Image
import time
time.sleep(5)
im = g.screenshot(region=(666,330,288,145))
aa=g.locateOnScreen("dian.jpg",region=(666,330,288,145),grayscale=True)
print(aa)

Image._show(im)