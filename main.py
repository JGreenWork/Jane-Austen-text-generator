import nltk, random
from markov import Markov

'''
>>>Inputting your text<<<
To open your text file, make sure you use the correct path.
If you want to use a smaller input text for faster compiling,
pride.txt is about 1/6th the size of austen.txt
'''
inputText = open("C:\\Users\\Jennifer\\Documents\\2017 Fall\\AI\\project\\austen.txt", "r")
#inputText = open("C:\\Users\\Jennifer\\Documents\\2017 Fall\\AI\\project\\pride.txt", "r")
#inputText = open("C:\\Users\\Jennifer\\Documents\\2017 Fall\\AI\\project\\snicket.txt", "r")
#inputText = open("C:\\Users\\Jennifer\\Documents\\2017 Fall\\AI\\project\\Harry_Potter.txt", "r")
#inputText = open("C:\\Users\\Jennifer\\Documents\\2017 Fall\\AI\\project\\Hunger_Games.txt", "r")
text = inputText.read()

#num = 660857
#print text[num-30:num+30]
#tokens = nltk.word_tokenize(text.decode("utf8"))

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)

'''
>>>Creating a markov chain<<<
To create a markov chain, use the form:
    NAME = Markov(tagged, NUMBER)
NUMBER is the order of your chain.  0 is the default, if you choose not to use
one.
''' '''
markov0 = Markov(tagged, 0)
markov1 = Markov(tagged, 1)
markov2 = Markov(tagged, 2)
markov3 = Markov(tagged, 3)
markov4 = Markov(tagged, 4)
markov5 = Markov(tagged, 5)
markov6 = Markov(tagged, 6)
markov7 = Markov(tagged, 7)
'''

'''
>>>Printing a dictionary<<<
If you want to print a dictionary, use the form:
    NAME.printMarkovDict()
'''
#markov0.printMarkovDict()

'''
>>>Printing new content<<<
To print out new content, use the form:
NAME.printMarkov(NAME.makeChain(#_OF_WORDS, SEED_WORDS)
If you would prefer not to use a seed word(s), use 'r' or leave that parameter
blank.  Otherwise:
Use 'p' to use the start of Pride and Prejudice
'e' for Emma
'ps' for Persuasion
'm' for Mansfield Park
's' for Sense and Sensibility
'n' for Northanger Abbey
''' '''
c = 500
for i in range(0, 25):

    print "Order 0: "
#for i in range(0, 100):
    markov0.printMarkov(markov0.makeChain(c, 'r'))
    print "\n"
    print "Order 1: "
#for i in range(0, 100):
    markov1.printMarkov(markov1.makeChain(c, 'r'))
    print "\n"
    print "Order 2: "
#for i in range(0, 100):
    markov2.printMarkov(markov2.makeChain(c, 'r'))
    print "\n"
    print "Order 3: "
#for i in range(0, 100):
    markov3.printMarkov(markov3.makeChain(c, 'r'))
    print "\n"
    print "Order 4: "
#for i in range(0, 100):
    markov4.printMarkov(markov4.makeChain(c, 'r'))
    print "\n"
    print "Order 5: "
#for i in range(0, 100):
    markov5.printMarkov(markov5.makeChain(c, 'r'))
    print "\n"
    print "Order 6: "
#for i in range(0, 100):
    markov5.printMarkov(markov5.makeChain(c, 'r'))
    print "\n"
    print "Order 7: "
#for i in range(0, 100):
    markov5.printMarkov(markov5.makeChain(c, 'r'))
    print "\n"
'''
'''
>>>Testing your model<<<
To test your model, use the form:
NAME.testAccuracy(NAME_OF_TEST_STRING, CHAR)
testString1 contains the beginning of Pride and Prejudice,
testString2 has the beginning of Emma, and
testString3 has the beginning of Persuasion

testString1 = tokens[2:78] #pride
testString2 = tokens[519385:519470] #emma
testString3 = tokens[143412:143529] #persuasion

print "Pride and Prejudice: ", testString1, "\n"
print "Emma: ", testString2, "\n"
print "Persuasion: ", testString3


markov0.testAccuracy(testString1, 'p')
markov1.testAccuracy(testString1, 'p')
markov2.testAccuracy(testString1, 'p')
markov3.testAccuracy(testString1, 'p')
markov4.testAccuracy(testString1, 'p')
markov5.testAccuracy(testString1, 'p')
markov6.testAccuracy(testString1, 'p')
markov7.testAccuracy(testString1, 'p')
'''
