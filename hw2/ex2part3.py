"""
Alex Vickers
apv5032 @ psu . edu
IST 441: Information Retrieval and Search Engines
Exercise 2, Problem 3, Part 2:
   Calculate Lucene Scores between Documents and Queries
   D1: You say goodbye, I say hello
   D2: You say stop, I say go
   D3: Hello, hello, you say goodbye
   D4: I say yes, you say no

   Q1: say goodbye
   Q2: you hello

   Lucene Score defined as follows:
   luceneScore(Q,D) = coord(Q,D) * queryNorm(Q) *
               sumOf tinQ ( tf(tinD) * idf(t)^2 * t.getBoost() * norm(D) )
   where (get ready lol..)

   coord(Q,D) = # of matching terms / # of total terms in Q

   queryNorm(Q) = 1/((sumOf tinQ ( idf(t)^2 ))^1/2
   ( In this exercise, t.getBoost() = 1, q.getBoost() = 1 )

   tf(t in D) = raw-term-frequency^1/2

   idf(t) = ln (N/(nj+1)) + 1
   (N: number of documents, nj: document frequency of term t )

   norm(D) = 1/(number of terms in doc)^1/2

   """
import math

numberOfDocumentTerms = [6,6,5,6]
numberOfQueryTerms = 2

d1RawFrequency = [1,1,2,1]
d2RawFrequency = [0,0,2,1]
d3RawFrequency = [1,2,2,1]
d4RawFrequency = [0,0,2,1]

d1idf = [1.29, 1.29, 1.55, 0.78]
d2idf = [0, 0, 1.55, 0.78]
d3idf = [1.29, 2.58, 0.78, 0.78]
d4idf = [0, 0, 1.55, 0.78]

q1RawFrequency = [1,0,1,0]
q2RawFrequency = [0,1,0,1]

q1idf = [1.29, 0, 0.78, 0]
q2idf = [0, 1.29, 0, 0.78]

def norm(numTerms):
   return float(1 / float(math.sqrt(numTerms)))

# python division sucks so floats all around yo
def coord(matchingTerms, queryTerms):
   return (float(matchingTerms) / float(queryTerms))

def queryNorm(idfQ):
   total = 0
   for n in range(len(idfQ)):
      total += float(math.pow(idfQ[n], 2))
   return float(1 / math.sqrt(total))

def termFreq(termsInDoc):
   return float(math.sqrt(termsInDoc))

# To allow for only terms matching in documents and queries to count, I multiply the queryRawFreq by the documentRawFreq (so terms that don't appear in both become 0 in the sum).
def luceneScore(queryRawFreq, documentRawFreq, documentIDF, coord, queryNorm, norm):
   sum = 0
   for n in range(len(documentRawFreq)):
      sum += float(float(queryRawFreq[n]) * float(termFreq(documentRawFreq[n])) * float(math.pow(documentIDF[n], 2)) * float(norm))
   return float(coord * queryNorm * sum)




Q1D1 = luceneScore(q1RawFrequency, d1RawFrequency, d1idf, coord(2, numberOfQueryTerms), queryNorm(q1idf), norm(numberOfDocumentTerms[0]))

Q1D2 = luceneScore(q1RawFrequency, d2RawFrequency, d2idf, coord(1, numberOfQueryTerms), queryNorm(q1idf), norm(numberOfDocumentTerms[1]))

Q1D3 = luceneScore(q1RawFrequency, d3RawFrequency, d3idf, coord(2, numberOfQueryTerms), queryNorm(q1idf), norm(numberOfDocumentTerms[2]))

Q1D4 = luceneScore(q1RawFrequency, d4RawFrequency, d4idf, coord(1, numberOfQueryTerms), queryNorm(q1idf), norm(numberOfDocumentTerms[3]))

Q2D1 = luceneScore(q2RawFrequency, d1RawFrequency, d1idf, coord(2, numberOfQueryTerms), queryNorm(q2idf), norm(numberOfDocumentTerms[0]))

Q2D2 = luceneScore(q2RawFrequency, d2RawFrequency, d2idf, coord(1, numberOfQueryTerms), queryNorm(q2idf), norm(numberOfDocumentTerms[1]))

Q2D3 = luceneScore(q2RawFrequency, d3RawFrequency, d3idf, coord(2, numberOfQueryTerms), queryNorm(q2idf), norm(numberOfDocumentTerms[2]))

Q2D4 = luceneScore(q2RawFrequency, d4RawFrequency, d4idf, coord(1, numberOfQueryTerms), queryNorm(q2idf), norm(numberOfDocumentTerms[3]))

print "Query 1 & Document 1 Lucene Score: %f" % Q1D1
print "Query 1 & Document 2 Lucene Score: %f" % Q1D2
print "Query 1 & Document 3 Lucene Score: %f" % Q1D3
print "Query 1 & Document 4 Lucene Score: %f" % Q1D4
print ""
print "Query 2 & Document 1 Lucene Score: %f" % Q2D1
print "Query 2 & Document 2 Lucene Score: %f" % Q2D2
print "Query 2 & Document 3 Lucene Score: %f" % Q2D3
print "Query 2 & Document 4 Lucene Score: %f" % Q2D4

