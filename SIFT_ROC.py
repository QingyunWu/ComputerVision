import os,sys
# sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2

from os.path import join, dirname

from matplotlib import pyplot as plt

tuna = []
path = "/Users/qingyun/Desktop/CV/assignment6/positive/"
tuna = os.listdir(path)

negative = []
path2 = "/Users/qingyun/Desktop/CV/assignment6/negative/"
negative = os.listdir(path2)

positive_scores = []
negative_scores = []
for x in range(1, 21):
	for y in range(1,21):

		img1link = path2 + '{}'.format(negative[y])
		img2link = path + '{}'.format(tuna[x])
		img1 = cv2.imread(img1link,0)
		img2 = cv2.imread(img2link,0)
		sift = cv2.xfeatures2d.SIFT_create()

		kp2, des2 = sift.detectAndCompute(img2,None)
		kp1, des1 = sift.detectAndCompute(img1,None)

		# BFMatcher with default params
		bf = cv2.BFMatcher()
		matches = bf.knnMatch(des1, des2, k=2)

		# Apply ratio test
		good = []
		for m,n in matches:
			if m.distance < 0.80*n.distance:
				good.append([m])

		# cv2.drawMatchesKnn expects list of lists as matches
		# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

		# plt.imshow(img3), plt.show()
		negative_scores.append(len(good) / float(len(matches)))
	
	for y in range(1,21):

		img1link = path + '{}'.format(tuna[y])
		img2link = path + '{}'.format(tuna[x])
		img1 = cv2.imread(img1link,0)
		img2 = cv2.imread(img2link,0)
		sift = cv2.xfeatures2d.SIFT_create()

		kp1, des1 = sift.detectAndCompute(img1,None)
		kp2, des2 = sift.detectAndCompute(img2,None)

		# BFMatcher with default params
		bf = cv2.BFMatcher()
		matches = bf.knnMatch(des1, des2, k=2)

		# Apply ratio test
		good = []
		for m,n in matches:
			if m.distance < 0.80*n.distance:
				good.append([m])

		# cv2.drawMatchesKnn expects list of lists as matches
		# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

		# plt.imshow(img3), plt.show()
		positive_scores.append(len(good) / float(len(matches)))

	
tpr_list = []
fpr_list = []
curt_threshold = 0

for iteration in range(0,1000):
	countTP = 0
	countFP = 0
	for positive_score in positive_scores:
		if positive_score >= curt_threshold:
			countTP += 1
	for negative_score in negative_scores:
		if negative_score >= curt_threshold:
			countFP += 1
	tpr_list.append(countTP/400.0)
	fpr_list.append(countFP/400.0)
	curt_threshold += 0.001

a = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
b = a
fig = plt.figure()
fig.suptitle('ROC of tuna from SIFT', fontsize = 14, fontweight='bold')
plt.plot(a, b, linestyle="--")
plt.plot(fpr_list,tpr_list,'-or')
plt.show()

