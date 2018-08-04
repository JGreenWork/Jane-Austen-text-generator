import random

class Markov(dict):
    def __init__(self, myList, n=0):
        super(Markov, self).__init__()
        listLength = len(myList)
        self.length = 0
        self.order = n

        if self.order <= 1:
            for word in range(0, listLength-1):
                if myList[word] in self:
                    if myList[word+1] in self[myList[word]]:
                        self[myList[word]][myList[word+1]] +=1
                    else:
                        self[myList[word]][myList[word+1]] = 1
                else:
                    self[myList[word]] = {myList[word+1] : 1}
                    self.length +=1

        elif self.order == 2:
            for word in range(0, listLength-2):
                if (myList[word], myList[word+1]) in self:
                    if myList[word+2] in self[(myList[word], myList[word+1])]:
                        self[(myList[word], myList[word+1])][myList[word+2]] +=1
                    else:
                        self[(myList[word], myList[word+1])][myList[word+2]] = 1
                else:
                    self[(myList[word], myList[word+1])] = {myList[word+2] : 1}
                    self.length +=1

        elif self.order == 3:
            for word in range(0, listLength-3): #Third order
                if (myList[word], myList[word+1], myList[word+2]) in self:
                    if myList[word+3] in self[(myList[word], myList[word+1], myList[word+2])]:
                        self[(myList[word], myList[word+1], myList[word+2])][myList[word+3]] +=1
                    else:
                        self[(myList[word], myList[word+1], myList[word+2])][myList[word+3]] = 1
                else:
                    self[(myList[word], myList[word+1], myList[word+2])] = {myList[word+3] : 1}
                    self.length +=1
        elif self.order == 4:
            for word in range(0, listLength-4): #Fourth order
                if (myList[word], myList[word+1], myList[word+2], myList[word+3]) in self:
                    if myList[word+4] in self[(myList[word], myList[word+1], myList[word+2], myList[word+3])]:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3])][myList[word+4]] +=1
                    else:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3])][myList[word+4]] = 1
                else:
                    self[(myList[word], myList[word+1], myList[word+2], myList[word+3])] = {myList[word+4] : 1}
                    self.length +=1
        elif self.order == 5:
            for word in range(0, listLength-5): #Fifth order
                if (myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4]) in self:
                    if myList[word+5] in self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4])]:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4])][myList[word+5]] +=1
                    else:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4])][myList[word+5]] = 1
                else:
                    self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4])] = {myList[word+5] : 1}
                    self.length +=1
        elif self.order == 6:
            for word in range(0, listLength-6): #Sixth order
                if (myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5]) in self:
                    if myList[word+6] in self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5])]:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5])][myList[word+6]] +=1
                    else:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5])][myList[word+6]] = 1
                else:
                    self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5])] = {myList[word+6] : 1}
                    self.length +=1
        elif self.order == 7:
            for word in range(0, listLength-7): #Seventh order
                if (myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5], myList[word+6]) in self:
                    if myList[word+7] in self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5], myList[word+6])]:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5], myList[word+6])][myList[word+7]] +=1
                    else:
                        self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5], myList[word+6])][myList[word+7]] = 1
                else:
                    self[(myList[word], myList[word+1], myList[word+2], myList[word+3], myList[word+4], myList[word+5], myList[word+6])] = {myList[word+7] : 1}
                    self.length +=1

    def randomWord(self):
        index = random.randint(0, self.length-1)
        count = 0
        for words in self:
            if count == index:
                return words
            count += 1
        return "Failure"

    def weightedWord(self, dict):
        count = 0
        totalWords = sum(dict.values())
        index = random.randint(0, totalWords-1)
        for words in dict:
            if count == index:
                return words
            count += dict[words]
            if count > index:
                return words
        return "Failure"

    def printMarkov(self, str):
        print "\n\n"
        tempStr = " ".join(str)
        newStr = ' '
        skipCount = 0
        #print "Original:  ", tempStr
        #print "\n"
        strlen = len(tempStr)
        for i in range(0, strlen):
            if skipCount == 0:
                if i<= strlen-4:
                    if tempStr[i]=='-' and tempStr[i+1] == ' ' and tempStr[i+2] == '\'' and tempStr[i+3] == '\'':
                        newStr+= '- \"'
                    if tempStr[i] == '\'' and tempStr[i+1] == '\'':
                        if tempStr[i+2] == ' ' and tempStr[i+3] == '`' and tempStr[i+4] == '`':
                            newStr+= "\"\n\n\""
                            skipCount += 6
                        else:
                            newStr+='\"'
                            skipCount +=2
                if i<= strlen-3:
                    if tempStr[i+1] == 'n' and tempStr[i+2] == '\'' and tempStr[i+3] == 't':
                        skipCount+=1
                if i<= strlen-2:
                    if tempStr[i] == ' ':
                        if tempStr[i+1] == '\'' or tempStr[i+1] == '?' or tempStr[i+1] == '!' or tempStr[i+1] == '.' or tempStr[i+1] == ',' or tempStr[i+1] == ';' or tempStr[i+1] == ':':
                            skipCount+=1
                    if tempStr[i] == '`' and tempStr[i+1] == '`':
                        newStr+='\"'
                        skipCount+=3
            if skipCount > 0:
                skipCount-=1
                continue
            newStr+=tempStr[i]
        print newStr
    def makeChain(self, length, char='r'):
        pride = (('It', 'PRP'), ('is', 'VBZ'), ('a', 'DT'), ('truth', 'NN'), ('universally', 'RB'), ('acknowledged', 'VBD'), (',', ','), ('that', 'IN'), ('a', 'DT'), ('single', 'JJ'))
        persuasion = (('Sir', 'NNP'), ('Walter', 'NNP'), ('Elliot', 'NNP'), (',', ','), ('of', 'IN'), ('Kellynch', 'NNP'), ('Hall', 'NNP'), (',', ','), ('in', 'IN'), ('Somersetshire', 'NNP'))
        emma = (('Emma', 'NNP'), ('Woodhouse', 'NNP'), (',', ','), ('handsome', 'NN'), (',', ','), ('clever', 'NN'), (',', ','), ('and', 'CC'), ('rich', 'JJ'), (',', ','))
        mansfield = (('About', 'IN'), ('thirty', 'NN'), ('years', 'NNS'), ('ago', 'RB'))
        sense = (('The', 'DT'), ('family', 'NN'), ('of', 'IN'), ('Dashwood', 'NNP'))
        northanger = (('No', 'NNP'), ('one', 'NN'), ('who', 'WP'), ('had', 'VBD'))
        test = (('of', 'IN'), ('uniting', 'VBG'), ('them', 'PRP'), ('.', '.'))
        if char == 'p':
            startWord = pride
        elif char == 'ps':
            startWord = persuasion
        elif char == 'e':
            startWord = emma
        elif char == 'm':
            startWord = mansfield
        elif char == 's':
            startWord = sense
        elif char == 'n':
            startWord = northanger
        elif char == 't':
            startWord = test

        chain = []
        if self.order == 0:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = startWord[0]
            chain.append(nextWord[0])
            for i in range (0,(length-len(chain))):
                if self.get(nextWord) == None:
                    break
                nextWord = self.randomWord()
                chain.append(nextWord[0])
        elif self.order == 1:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = startWord[0]
            chain.append(nextWord[0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                nextWord = self.weightedWord(self[nextWord])
                chain.append(nextWord[0])
        elif self.order == 2:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = (startWord[0], startWord[1])
            chain.append(nextWord[0][0])
            chain.append(nextWord[1][0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                temp = self.weightedWord(self[nextWord])
                newWord = (nextWord[1], temp)
                nextWord = newWord
                chain.append(nextWord[1][0])
        elif self.order == 3:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = (startWord[0], startWord[1], startWord[2])
            chain.append(nextWord[0][0])
            chain.append(nextWord[1][0])
            chain.append(nextWord[2][0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                temp = self.weightedWord(self[nextWord])
                newWord = (nextWord[1], nextWord[2], temp)
                nextWord = newWord
                chain.append(nextWord[2][0])
        elif self.order == 4:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = (startWord[0], startWord[1], startWord[2], startWord[3])
            chain.append(nextWord[0][0])
            chain.append(nextWord[1][0])
            chain.append(nextWord[2][0])
            chain.append(nextWord[3][0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                temp = self.weightedWord(self[nextWord])
                newWord = (nextWord[1], nextWord[2], nextWord[3], temp)
                nextWord = newWord
                chain.append(nextWord[3][0])
        elif self.order == 5:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = (startWord[0], startWord[1], startWord[2], startWord[3], startWord[4])
            chain.append(nextWord[0][0])
            chain.append(nextWord[1][0])
            chain.append(nextWord[2][0])
            chain.append(nextWord[3][0])
            chain.append(nextWord[4][0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                temp = self.weightedWord(self[nextWord])
                newWord = (nextWord[1], nextWord[2], nextWord[3], nextWord[4], temp)
                nextWord = newWord
                chain.append(nextWord[4][0])
        elif self.order == 6:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = (startWord[0], startWord[1], startWord[2], startWord[3], startWord[4], startWord[5])
            chain.append(nextWord[0][0])
            chain.append(nextWord[1][0])
            chain.append(nextWord[2][0])
            chain.append(nextWord[3][0])
            chain.append(nextWord[4][0])
            chain.append(nextWord[5][0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                temp = self.weightedWord(self[nextWord])
                newWord = (nextWord[1], nextWord[2], nextWord[3], nextWord[4], nextWord[5], temp)
                nextWord = newWord
                chain.append(nextWord[5][0])
        elif self.order == 7:
            if char == 'r':
                nextWord = self.randomWord()
            else:
                nextWord = (startWord[0], startWord[1], startWord[2], startWord[3], startWord[4], startWord[5], startWord[6])
            chain.append(nextWord[0][0])
            chain.append(nextWord[1][0])
            chain.append(nextWord[2][0])
            chain.append(nextWord[3][0])
            chain.append(nextWord[4][0])
            chain.append(nextWord[5][0])
            chain.append(nextWord[6][0])
            for i in range (0, (length-len(chain))):
                if self.get(nextWord) == None:
                    break
                temp = self.weightedWord(self[nextWord])
                newWord = (nextWord[1], nextWord[2], nextWord[3], nextWord[4], nextWord[5], nextWord[6], temp)
                nextWord = newWord
                chain.append(nextWord[6][0])
        return chain

    def testAccuracy(self, testString, char):
        length = len(testString)
        compLength = length
        count = 0.0
        totalCount = 0.0
        testSize = 1000
        completeSuccess = 0
        word = " "
        for i in range(0,testSize):
            chain = self.makeChain(length, char)
            for word1, word2 in zip(testString, chain):
                if word1==word2:
                    count+=1
                else:
                    break
            if count/length == 1:
                completeSuccess +=1
            if self.order > 1:
                count -=self.order
                compLength -= self.order
            else:
                count -= 1
                compLength -= 1
            totalCount += count/compLength
            count = 0.0
            compLength = length
        if self.order == 0:
            word = "Random"
        elif self.order == 1:
            word = "First"
        elif self.order == 2:
            word = "Second"
        elif self.order == 3:
            word = "Third"
        elif self.order == 4:
            word = "Fourth"
        elif self.order == 5:
            word = "Fifth"
        elif self.order == 6:
            word = "Sixth"
        elif self.order == 7:
            word = "Seventh"

        print word, "Order Accuracy: ", totalCount/testSize*100,"%"
        print "Number of successes: ", completeSuccess, "\n"

    def printMarkovDict(self):
        for words in self:
            print words, self[words], "\n"
