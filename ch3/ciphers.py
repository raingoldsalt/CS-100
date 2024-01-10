def transpositionDecrypt():
    message = "o r ue wsmyuaespraeoe"
    cipherText = message
    #print(len(cipherText))
    halfLength = len(cipherText) // 2
    #print(halfLength)
    evenChars = cipherText[halfLength:]
    #print(evenChars)
    oddChars = cipherText[:halfLength]
    #print(oddChars)
    plainText = ""
    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]
        #print(i)
        #print(plainText)
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]
    print(plainText)
transpositionDecrypt() # It says 'you are super awesome.' Thanks, you too!

def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

# add code here to implement the substitutionDecrypt function

def substitutionDecrypt(eText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryptText = ""
    for ch in eText:
        idx = alphabet.find(ch)
        decryptText = decryptText + key[idx]
    return decryptText

key = 'zyxwvutsrqponmlkjihgfedcba '
plainText = 'the quick brown fox'

encryptMsg = substitutionEncrypt(plainText,key)
print( "Encrypted message: " + encryptMsg)

# add code here to call the function to decrypt and test

#key = 'stuvwxyzabcdefghijklmnopqr'
#encryptMsg = 'xsflsklau bgt qgm sjw xstmdgmk'

decryptMsg = substitutionDecrypt(encryptMsg,key)
print( "Decrypted message: " + decryptMsg)


