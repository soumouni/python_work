#try it yourself page 202
#10-10 Common words
print('I can tell you how many times a specific word appears in a text')
word=input('whish word do you want to count: ')
word=word.lower()
try:
    with open('little_women.txt', encoding='utf-8') as f:
        content=f.read()
except FileNotFoundError:
    print('the file was not found')
else:
    n= content.lower().count(word)   
    print(n)
