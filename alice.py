#example from chapter 10 page 198
file_name='alice.txt'
with open (file_name,encoding='utf-8') as f:
    content=f.read()
    list_words=content.split()
n=len(list_words)
print(n)
