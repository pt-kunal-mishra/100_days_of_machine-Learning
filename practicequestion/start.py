def lengthword(name:str) ->int :
    arr=name.split(' ')
    last_word=tuple(arr[-1])
    print(type(last_word))
    print(last_word)
    size=len(last_word)
    if(size):
        return size

print(lengthword("hello kunal kumar mishra"))    
