"""
Alex Vickers
apv5032 @ psu . edu
IST 441: Information Retrieval and Search Engines
Exercise 1, Problem 2:
   Using Google, Bing, blekko, DuckDuckGo, and Ask, query "jaguar" and "jaguar cat" and plot precision for the first 20 documents returned for each engine. Also plot average precision for each query.
"""

import matplotlib.pyplot as plt

# When querying 'jaguar', # of documents that were relevent to the cat are stored.  An array index = # of documents, it's key = number of relevent docs
googleJag   = [0,1,1,1,1,1,2,2,3,3,3,4,4,5,6,7,8,9,9,9]
bingJag     = [0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,4,4,4,5]
blekkoJag   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
duckJag     = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2]
askJag      = [1,2,2,2,3,4,4,4,5,5,5,6,7,7,8,9,9,10,10,11]

# When querying 'jaguar cat', # of documents that were relevent to the cat are stored.  An array index = # of documents, it's key = number of relevent docs
googleCat   = [1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15,16,17,18,19]
bingCat     = [1,2,3,4,5,6,7,8,9,10,10,11,11,12,13,14,15,16,17,18]
blekkoCat   = [1,2,3,4,5,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18]
duckCat     = [1,2,3,4,5,6,7,8,9,9,10,11,12,13,14,15,15,16,17,17]
askCat      = [1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,14,15,16,17,18]

# precision = |returned relevant documents| / |total returned documents|
def precision(numberOfDocuments, searchEngine):
   return float(float(searchEngine) / float(numberOfDocuments))

# structures to hold precision of each query for each engine
googlePrecisionJag = []
googlePrecisionCat = []
bingPrecisionJag = []
bingPrecisionCat = []
blekkoPrecisionJag = []
blekkoPrecisionCat = []
duckPrecisionJag = []
duckPrecisionCat = []
askPrecisionJag = []
askPrecisionCat = []
googleAverage = []
bingAverage = []
blekkoAverage = []
duckAverage = []
askAverage = []
x = []

for n in range(1,21):
   googlePrecisionJag.append(precision(n,googleJag[n-1]))
   googlePrecisionCat.append(precision(n,googleCat[n-1]))
   bingPrecisionJag.append(precision(n,bingJag[n-1]))
   bingPrecisionCat.append(precision(n,bingCat[n-1]))
   blekkoPrecisionJag.append(precision(n,blekkoJag[n-1]))
   blekkoPrecisionCat.append(precision(n,blekkoCat[n-1]))
   duckPrecisionJag.append(precision(n,duckJag[n-1]))
   duckPrecisionCat.append(precision(n,duckCat[n-1]))
   askPrecisionJag.append(precision(n,askJag[n-1]))
   askPrecisionCat.append(precision(n,askCat[n-1]))
   googleAverage.append(float((float(googlePrecisionJag[n-1]) + float(googlePrecisionCat[n-1])) / 2))
   bingAverage.append(float((float(bingPrecisionJag[n-1]) + float(bingPrecisionCat[n-1])) / 2))
   blekkoAverage.append(float((float(blekkoPrecisionJag[n-1]) + float(blekkoPrecisionCat[n-1])) / 2))
   duckAverage.append(float((float(duckPrecisionJag[n-1]) + float(duckPrecisionCat[n-1])) / 2))
   askAverage.append(float((float(askPrecisionJag[n-1]) + float(askPrecisionCat[n-1])) / 2))
   x.append(n)

plt.title('Precision for Ask')
plt.xlabel('Number of Documents')
plt.ylabel('Precision')
plt.plot(x,askPrecisionJag, '-o', color='r', label='Jaguar Query')
plt.plot(x,askPrecisionCat, '-o', color='b', label='Jaguar Cat Query')
plt.plot(x,askAverage, '-o', color='k', label='Average Precision')
plt.legend(loc=3)
plt.show()
