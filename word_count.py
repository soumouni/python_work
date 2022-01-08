#function that counts words from a given document (page199)
def count_words(filename):
    """counts words in any given text document"""
    try:
        with open(filename,encoding='utf-8') as f:
            content=f.read()
    except FileNotFoundError:
        print(f'the file {filename} does not exist')
    else:
        words=content.split()
        num_words=len(words)
        print(f'the file {filename} has about {num_words} words')

filename=['alice.txt','little_women.txt','moby_dick.txt' ]
for file in filename:
    count_words(file)