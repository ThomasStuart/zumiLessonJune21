# make a class called VowelCount that has the properties words and top.  
# where top represents the word with the highest vowel count 
        
from math import inf 

class VowelCount:
    
    def __init__(self, words):
        self.w = words
        self.t = None  # calculate it ...
        
    def getWords(self):
        return self.w 
    
    def getTop(self):
        # calc that top value top = {maxWord, maxCount}
        # hint use: mapWordsToCount and self.w
        # call mapWordsToCount on self.w 
        answer = self.mapWordsToCount(self.w) # one line of code goes after the RHS of equal sign 
        return answer 
        

    def setNumberVowels(self, word ): 
        counter = 0
        #vowels  = #list containin the vowels

        #hint: use a for-loop , go char by char to check if particualr char in word is vowel
        for i in range(0, len(word) ):
            char = word[i]

            # if what ? char is a vowel -> 
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                counter += 1 

        return counter 



                # words1 = "hello", world 
                # words2 = "it", "dictionary", "food"
    def mapWordsToCount(self, words):
        # creates an list called pairs 
        pairs = []

        # calcs the number of vowels per word
        for i in range(0, len(words)): 
            countV = self.setNumberVowels(words[i])
            pairs.append( (words[i], countV) )


        # selects the word with highest vowel count
        maxWord        = ""
        maxVowelCount  = -inf
        for i in range(0, len(pairs) ):
            currWord       = pairs[i][0]
            currVowelCount = pairs[i][1]

            # check if new max
            if currVowelCount > maxVowelCount:
                maxWord       = currWord
                maxVowelCount = currVowelCount 


        return maxWord, maxVowelCount 

    
words1 = ["hello", "world"]
obj1   =  VowelCount( words1 )
print( obj1.getTop() )  # hello, 2

words2 = ["it", "dictionary", "food"]  
    
obj2   =  VowelCount( words2 )
print( obj2.getTop() )  # dictioanry, 4
