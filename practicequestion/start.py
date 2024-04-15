# def lengthword(name:str) ->int :
#     arr=name.split(' ')
#     last_word=tuple(arr[-1])
#     print(type(last_word))
#     print(last_word)
#     size=len(last_word)
#     if(size):
#         return size

# print(lengthword("hello kunal kumar mishra"))    


#remove duplicates from the sorted array
def removeduplicates(arr:list):
    n=len(arr)-1
    last_occur=0
    pivot=0
    temp=[0]*n
    print(temp)
    for last_occur in range(0,n-1):
        if(arr[last_occur]!=arr[last_occur+1]):
            temp[pivot]=arr[last_occur]
            pivot=pivot+1

    temp[pivot]=arr[n-1]

    return temp    

print(removeduplicates([1,1,2,2,2,3,4,4,4,5,5]))        


def log1remove(arr:list):
    n=len(arr)-1
    last_occur=0
    pivot=0
    for last_occur in range(0,n-1):
        if(arr[last_occur]!=arr[last_occur+1]):
            arr[pivot]=arr[last_occur]
            pivot=pivot+1
    arr[pivot]=arr[n-1]

    return arr[0:pivot+1]      

print(log1remove([1,1,2,2,2,3,4,4,4,5,5]))        
