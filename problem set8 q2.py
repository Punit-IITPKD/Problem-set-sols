text="aaabaadaabaaa"
pattern="aabaaa"

def last_occurrence_table(pattern):
    dic={}
    for i in range(len(pattern)):
        dic[pattern[i]]=i

    return dic


print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"last ocuurence table: {last_occurrence_table(pattern)}")

def bad_characte_match(text,pattern):

    total=0
    idx=len(pattern)-1
    table=last_occurrence_table(pattern)

    while idx<len(text):
        
        st_idx=idx-(len(pattern)-1) 
        print(f"\nAlignment at index {st_idx}")

        match=True 
        for i in range(len(pattern)-1,-1,-1):

            if pattern[i]==text[st_idx+i]:
                total+=1
                print(f"Compare text{st_idx+i} vs pattern{i}    '{text[st_idx+i]}' vs '{pattern[i]}   match")
            
            else:
                match=False
                total+=1
                print(f"Compare text{st_idx+i} vs pattern{i}    '{text[st_idx+i]}' vs '{pattern[i]}   mismatch")
    
                if text[st_idx+i] in table:
                    shift=max(1,i-table[text[+i]])
                    print(f"shift=max(1, last('{text[st_idx+i]}')) = max(1,{i} - {table[text[st_idx+i]]}) = {shift}")
                    idx+=shift
                    break

                else:
                    shift=len(pattern)
                    print(f"shift=max(1, last('{text[st_idx+i]}')) = max(1,{i} - (-1)) = {shift}")
                    idx+=shift
                    break
        
        if match==True:
            print(f"Pattern found at index {st_idx} \n")
            print(f"Total comparison = {total}")
            return

    print("no match found")
    return -1
        
bad_characte_match(text,pattern)
                    



       
