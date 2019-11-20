from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt
import time


def threshold(imageArray):
	balanceAR = []
	newAR = imageArray


x = Image.open('images/numbers/y0.4.png')
xar = np.asarray(x)
print(xar)

plt.imshow(xar)
plt.show()


i = Image.open('images/dotndot.png')
iar = np.asarray(i)
print(iar)


plt.imshow(iar)
plt.show()


# with open("texts.npy", mode="wb") as f:
# 	np.save(f, iar)  
