# What is a string?
# A string text data type
# '' , " "
# what length of a string 1 or many pages

l ='jbjfbjfejbfebfuslkjzifbebir'
print(l)
print(len(l))

vowels = 'aeiouy'
consosnants = 'bcdfghjklmnpqrstvwxz'
print("the length of vowels: " ,len(vowels))
print("the length of consosants: ", len(consosnants))
print(l.upper())
print(dir(l)) # dir() function shows all the methods that can be used with a string

challenge = '30 days Of python'
print(challenge.upper())
print(challenge.title())
print(challenge.swapcase())
print(challenge.find('0'))
print(challenge.find('y'))
print(challenge.find('f'))


language = 'Python'
print(language.upper())
print(language.title())
print(language[0])
print(language[0:2])
print(language[2:])
print(language[-1])
print(language[-2])
print(language[-2:])
print(language[::-1])
print(language.lower())
print(language.islower())