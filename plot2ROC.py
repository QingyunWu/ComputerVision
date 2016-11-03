import matplotlib.pyplot as plt


positive_scores_1 = []
positive_scores_2 = []
negative_scores_1 = []
negative_scores_2 = []

with open('positive_score1.txt', 'r') as f:
	for line in f:
		positive_scores_1.append(float(line))
with open('positive_score2.txt', 'r') as f:
	for line in f:
		positive_scores_2.append(float(line))
with open('negative_score1.txt', 'r') as f:
	for line in f:
		negative_scores_1.append(float(line))
with open('negative_score2.txt', 'r') as f:
	for line in f:
		negative_scores_2.append(float(line))

tpr_list_1 = []
tpr_list_2 = []
fpr_list_1 = []
fpr_list_2 = []

curt_threshold = 0
for iteration in range(0,1000):
	countTP = 0
	countFP = 0
	for positive_score in positive_scores_1:
		if positive_score >= curt_threshold:
			countTP += 1
	for negative_score in negative_scores_1:
	
		if negative_score >= curt_threshold:
			countFP += 1
	tpr_list_1.append(countTP/100.0)
	fpr_list_1.append(countFP/500.0)
	curt_threshold += 0.001

curt_threshold = 0
for iteration in range(0,1000):
	countTP = 0
	countFP = 0
	for positive_score in positive_scores_2:
		if positive_score >= curt_threshold:
			countTP += 1
	for negative_score in negative_scores_2:
	
		if negative_score >= curt_threshold:
			countFP += 1
	tpr_list_2.append(countTP/100.0)
	fpr_list_2.append(countFP/500.0)
	curt_threshold += 0.001

# draw two ROCs
a = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
b = a
fig = plt.figure()
fig.suptitle('ROCs of tuna before and after rotation', fontsize = 14, fontweight='bold')
plt.plot(a, b, linestyle="--")
plt.plot(fpr_list_1,tpr_list_1,'r--')
plt.plot(fpr_list_2,tpr_list_2,'g--')


plt.show()