# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        lines = f.read()
        return lines 

''' print(read_file_content("story.txt")) '''

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    words = text.strip()
    output = words.split()
    count = dict()
    for i in output:
        if i in count:
            count[i]+=1
        else:
            count[i]=1 
    return count

print(count_words()) 