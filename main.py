def count_words(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
#open the file in read mode
file = open('C:/Users/Omotosho Rhoda/Desktop/story.txt', 'r')

#read content of file to string
data = file.read()
#print it
print(count_words(data))