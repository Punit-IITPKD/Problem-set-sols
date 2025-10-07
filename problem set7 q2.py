def hash_fun(key):
    int_val=0
    for i in key:
        int_val+=ord(i)
    
    return int_val

def compressed_val(int_val,N):
    a=5
    b=7
    y=int_val
    p=10000019

    return ((a*y+b)%p)%N


def insert(key,hash_map,N):
    
    signature="".join(sorted(key))
    hash_val=compressed_val(hash_fun(key),N)

    start_idx=hash_val

    while True:
        if hash_map[hash_val]==None:
            hash_map[hash_val]=[signature,[key]]
            return
        
        elif hash_map[hash_val][0]==signature:
            hash_map[hash_val][1].append(key)
            return
        
        else:
            hash_val=(hash_val+1)%N
            if hash_val==start_idx:
                break
    
    print("List is full")
    return
        


def String_Categorization_System(arr):
    N=len(arr)
    hash_map=[None]*N
    for i in arr:
        insert(i,hash_map,N)

    ans=[]
    for i in hash_map:
        if i!=None:
            ans.append(i[1])

    print(ans)

arr = ["ad", "bc"]                        # non-anagrams but same ASCII sum
arr1 = ["listen", "silent", "enlist"]      # big anagram group
arr2= ["stone", "tones", "notes"]         # another anagram group
arr3= ["bat", "tab", "cat"]               # mixed groups

arr4= ["listen", "silent", "enlist", "inlets", "stone", "tones", "notes", "bat", "tab", "cat"]

String_Categorization_System(arr)
String_Categorization_System(arr1)
String_Categorization_System(arr2)
String_Categorization_System(arr3)
String_Categorization_System(arr4)

