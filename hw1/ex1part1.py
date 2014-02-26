"""
Alex Vickers
apv5032 @ psu . edu
IST 441: Information Retrieval and Search Engines
Exercise 1, Problem 1
"""

import matplotlib.pyplot as plt

# total relevant documents from the 1000 documents for the given query
relevant = ["d1", "d5", "d6", "d10", "d88", "d150", "d200", "d210", "d250", "d300", "d399", "d400", "d405", "d450", "d472", "d500", "d501", "d530", "d545", "d590", "d600", "d700", "d800", "d888", "d900"]
# approach 1's top 10 returned documents for given query
approach1 = ["d3", "d5", "d150", "d250", "d11", "d33", "d50", "d60", "d500", "d720"]
# approach 2's top 10 returned documents for given query
approach2 = ["d250", "d400", "d150", "d210", "d999", "d1", "d530", "d800", "d200", "d300"]

# precision = |returned relevant documents| / |total returned documents|
def precision(approachList, relevantList):
   returnedRelevant = set(approachList).intersection(set(relevantList))
   returnedReleventLength = float(len(returnedRelevant))
   appLength = float(len(set(approachList)))
   return float(returnedReleventLength / appLength)

# recall = |returned relevant documents| / |total relevant documents|
def recall(approachList, relevantList):
   returnedRelevant = set(approachList).intersection(set(relevantList))
   returnedReleventLength = float(len(returnedRelevant))
   relevantLength = float(len(set(relevantList)))
   return float(returnedReleventLength / relevantLength)

# various data structures
precision1 = []
precision2 = []
recall1 = []
recall2 = []
precisionOverRecall1 = []
precisionOverRecall2 = []
x = []

# fill our precision and recall points
for n in range(1, 11):
   precision1.append(precision(approach1[:n], relevant))
   precision2.append(precision(approach2[:n], relevant))
   recall1.append(recall(approach1[:n], relevant))
   recall2.append(recall(approach2[:n], relevant))
   x.append(n)

# plot the data
plt.xlabel('Number of Documents')
#plt.title('Precision/Recall')
#plt.xlabel('Recall')
#plt.ylabel('Precision')
plt.plot(x, precision1, '-o', color='r', label='Approach1 Precision')
plt.plot(x, precision2, '-o', color='k',label='Approach2 Precision')
plt.plot(x, recall1, '-o', color='g', label='Approach1 Recall')
plt.plot(x, recall2, '-o', color='b',label='Approach2 Recall')
#plt.plot(recall1, precision1, '-o', color='m', label='Approach1')
#plt.plot(recall2, precision2, '-o', color='y', label='Approach2')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), ncol = 2,loc=3, mode="expand",borderaxespad=0.)
#plt.legend(loc=8)
plt.show()
