
def hash_function(key):
    return ord(key)-ord('a')


def insert(arr,key):

    hash_val=hash_function(key)

    if arr[hash_val]==None:
        arr[hash_val]=(key,1)
        return

    freq=arr[hash_val][1]
    arr[hash_val]=(key,freq+1)
    return



def plagiarism_check(s,t):

    if len(s)!=len(t):
        return False
    
    arr=[None]*26

    for key in s:
        insert(arr,key)

    for key in t:
        hash_val=hash_function(key)

        if arr[hash_val]==None or arr[hash_val][0]!=key:
            return False
        
        freq=arr[hash_val][1]
        arr[hash_val]=(key,freq-1)
    
    for i in range(len(arr)):
        if arr[i]!=None:
            if arr[i][1]!=0:
                return False
    
    return True


s=input("Enter first string: ")
t=input("Enter second string: ")

ans=plagiarism_check(s,t)
if ans:
    print("The strings are anagram")
else:
    print("the strings are not anagram")
    






    
    



    
    
    

