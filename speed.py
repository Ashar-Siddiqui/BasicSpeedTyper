import time
string = "Python is a great language to learn and use"
word_count = len(string.split())
while str(input('Enter "yes" when you are ready')):
    t0 = time.time()
    inputText = str(input('Enter the phrase:"%s" as fast as possible' % string))
    t1 = time.time()
    acc = len(set(inputText.split()) & set(string.split()))
    acc = acc/word_count
    timeTaken = t1 - t0
    wordPM = (word_count/timeTaken)
    print(wordPM, acc, timeTaken)