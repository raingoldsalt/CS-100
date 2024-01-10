cents = {'Nickel': 5, 'Dime': 10, 'Quarter': 25, 'Dollar': 100}

for keys in cents:
    print(keys, cents[keys])
print(cents.keys())

personnel = {'Joe': 2000, 'Ana': 2500, 'Bob': 1800, 'Chris': 2100, 'Diana': 1900}
print(personnel)
salary = int(input("How many?: "))
for who in personnel:
    personnel[who] = personnel[who]+salary
    print(who,": ",personnel[who])

def toPirate(sentence):
    English = {'hello': 'avast',
               'excuse me': 'arr',
               'sir':'matey',
               'boy':'matey',
               'man':'matey',
               'madam': 'proud beauty',
               'officer': 'foul blaggart',
               'the': "th'",
               'my': 'me',
               'your': 'yer',
               'is':'be',
               'are':'be',
               'restaurant':'galley',
               'ocean':"Davey Jones' Locker",
               }
    words = sentence.split()
    changed = ""
    print(words)
    for word in words:
        if(word in English):
            changed = changed+English[word]+" "
        else:
            changed = changed+word+" "
    return changed

sentence = "hello there madam how are you"
print(toPirate(sentence))