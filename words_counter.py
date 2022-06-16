words =[word.lower() for word in input().split()]
words.sort()
lib = dict()
def key_assign(words, lib):
    unique = list(set(words))
    for i in unique:
        lib[i] = 1
def counter(words, lib): 
    i = 0
    if len(words) > 1:
        for j in words:
            if words[i] == words[i+1]:
                lib[words[i]] +=1
            i+=1
            if len(words) - 1 == i:
                break 
def printer(lib):
    for key, value in lib.items():
        print(key, value, end = '\n')

key_assign(words, lib)
counter(words, lib)
sorted_tuple = dict(sorted(lib.items(), key=lambda x: x[0]))
printer(lib)
