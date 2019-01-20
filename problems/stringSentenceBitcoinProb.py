
"""

3
it go will away
go do art
what to will east
3
it will
go east will
will

"""
# getting input 
numSentence = int(input())

sentenceList = []
for i in range(numSentence):
	sentenceList.append(input())


numQueries = int(input())

queriesList = []
for i in range(numQueries):
	queriesList.append(input())


#checking for query sentence in input sentence
def getQueryIndices(sentenceList,queriesList):
	outputList = []
	for query in queriesList:
		queryTokens = query.split(" ")
		sentIndex = 0
		querySentIndexList = []
		for sentence in sentenceList:
			sentenceTokens = sentence.split(" ")
			allTokenCount = len(queryTokens)

			for token in queryTokens:
				if token in sentenceTokens: allTokenCount -= 1

			if allTokenCount == 0: 
				querySentIndexList.append(sentIndex)
			
			sentIndex += 1

			if sentIndex == (len(sentenceList)-1) and len(querySentIndexList) == 0:
				querySentIndexList.append(-1)

		outputList.append(querySentIndexList)

	return outputList

print(getQueryIndices(sentenceList,queriesList))

"""
output 

We perform the following q = 3 queries on sentences = ["it go will away", "go do art", "what to will east"]:

    Find the indices of sentences containing both the words "it" and "will". These words only appear in sentences0, so the array [0] is stored in index 0 of the answer array.

    Find the indices of sentences containing the words "go", "east", and "will". These words do not appear in any sentence, so the array [-1] is stored in index 1 of the answer array.
    
    Find the indices of sentences containing the word "will". This word appears in sentences0 and sentences2, so the array [0, 2] is stored in index 2 of the answer array.

We then print [[0], [-1], [0, 2]] as our answer.
"""
