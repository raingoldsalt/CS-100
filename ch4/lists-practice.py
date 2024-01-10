# 1

myString = 'abc'
#myString[0] = 'd'
print(myString)
       
myList = ['a', 'b', 'c']
myList[0] = 'd'
print(myList)

# It says "TypeError: 'str' object does not support item assignment"
# Because we cannot change individual characters in a string using this method, it gets the error.

# 2

s = "I like apples"
k1 = s.split() # 'I', 'like', 'apples'
print(k1)
k2 = s.split('a') # 'I like ', 'pples'
print(k2)
k3 = s.split('e') # 'I lik', ' appl', 's'
print(k3)

# 3

st = 'mississippi'
st1 = st.split('i')
print(st1)

# 4

def numWords(sentence):
    s1 = sentence.split()
    print(s1)
    return len(s1)
    
print(numWords("the quick brown fox"))

# 5

def makeString(myList):
    text = ""
    for i in range(len(myList)):
        text = text+myList[i]+" "
    return text

print(makeString(["the", "quick", "brown", "fox"]))
