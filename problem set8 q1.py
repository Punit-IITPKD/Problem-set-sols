text="aaabaadaabaaa"
pattern="aabaaa"


######################### Brute force for comparing left to right ##############################

# total=0
# for i in range(len(text)-len(pattern)+1):
#     print (f"Alignment {i}:")
#     match=True
#     for j in range(len(pattern)):
        
#         if pattern[j]==text[j+i]:
#             total+=1
#             print (f"Comparing text[{j+i}] vs pattern[{j}]     match")

#         else:
#             match=False
#             total+=1
#             print (f"Comparing text[{j+i}] vs pattern[{j}]     mismatch")
#             print("shift by 1 \n")
#             break
    
#     if match==True:
#         print(f"Pattern found at index {i} \n")
#         break


# print(f"Total comparison = {total}")



######################### Brute force for comparing right to left ##############################

total=0
for i in range(len(text)-len(pattern)+1):
    print (f"Alignment {i}:")
    match=True

    for j in range(len(pattern)-1,-1,-1):

        if pattern[j]==text[i+j]:
            total+=1
            print (f"Comparing text[{j+i}] vs pattern[{j}]     match")

        else:
            match=False
            total+=1
            print (f"Comparing text[{j+i}] vs pattern[{j}]     mismatch")
            print("shift by 1 \n")
            break
    
    if match==True:
        print(f"Pattern found at index {i} \n")
        break


print(f"Total comparison = {total}")
