import os,sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import random
import numpy as np
from os import environ
from matplotlib import pyplot as plt

path = "/Users/qingyun/Desktop/CV/assignment5/rotatePositive/"
tuna = []
tuna = os.listdir(path)
print tuna[0]
print len(tuna)
for x in range(102):
	try:
		image = cv2.imread('{}'.format(tuna[x]))
		(h,w) = image.shape[:2]
		center = (w / 2, h / 2)
		angle = 0
		for y in range(9):
			angle += 36
			M = cv2.getRotationMatrix2D(center, angle, 1.0)
			rotated = cv2.warpAffine(image, M, (w, h))
			cv2.imwrite('{}.{}.jpg'.format(x, angle), rotated)
	except:
		print "pass"
		