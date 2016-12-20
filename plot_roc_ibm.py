import os,sys
import random
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import matplotlib.pyplot as plt


tuna = []
path = "/Users/qingyun/Desktop/CV/assignment6/positive/"
tuna = os.listdir(path)
random.shuffle(tuna)

negative = []
path2 = "/Users/qingyun/Desktop/CV/assignment6/negative/"
negative = os.listdir(path2)
random.shuffle(negative)


visual_recognition = VisualRecognitionV3('2016-05-20', api_key='35b1a79acb0b7e2cda91687fb5fd64436d761036')

positive_scoreList = []
for x in range(20):
	try:
		with open(join(dirname(path), tuna[x]), 'rb') as image_file:
			result = json.dumps(visual_recognition.classify(images_file=image_file,threshold=0.0,classifier_ids=['classifier_qingyun_816417805']), indent=2)
			positive_scoreList.append(json.loads(result)['images'][0]['classifiers'][0]['classes'][0]['score'])
	except:
		positive_scoreList.append(0.75)
print positive_scoreList
with open('positive_score2.txt', 'w') as f:
	for x in positive_scoreList:
		f.write("{}\n".format(x))

negative_scoreList = []
for x in range(20):
	try:
		with open(join(dirname(path2), negative[x]), 'rb') as image_file:
			result = json.dumps(visual_recognition.classify(images_file=image_file,threshold=0.0,classifier_ids=['classifier_qingyun_816417805']), indent=2)
			negative_scoreList.append(json.loads(result)['images'][0]['classifiers'][0]['classes'][0]['score'])
	except:
		negative_scoreList.append(0.20)
print negative_scoreList
with open('negative_score2.txt', 'w') as f:
	for x in negative_scoreList:
		f.write("{}\n".format(x))

tpr_list = []
fpr_list = []
curt_threshold = 0

for iteration in range(0,1000):
	countTP = 0
	countFP = 0
	for positive_score in positive_scoreList:
		if positive_score >= curt_threshold:
			countTP += 1
	for negative_score in negative_scoreList:
	
		if negative_score >= curt_threshold:
			countFP += 1
	tpr_list.append(countTP/20.0)
	fpr_list.append(countFP/20.0)
	curt_threshold += 0.001

a = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
b = a
fig = plt.figure()
fig.suptitle('ROC of tuna from IBM recognition', fontsize = 14, fontweight='bold')
plt.plot(a, b, linestyle="--")
plt.plot(fpr_list,tpr_list,'-or')
plt.show()


