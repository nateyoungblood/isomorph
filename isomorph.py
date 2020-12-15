word1="foo"
word2="egg"
word3="bar"

def split(word):
    li=[char for char in word]  
    return(li)

def structure(li):
    struc= list(li)
    for x in range(len(li)):
        if li[x]==li[x-1]:
            struc[x]="t"
        else: 
            struc[x]="f"
    return(struc)
    
def listToString(s):  
    str1 = ""  
    return (str1.join(s))     
    
def match(a,b):
    first=listToString(structure(split(a)))
    second=listToString(structure(split(b)))
    if first==second:
        print("match!")
    else:
        print("no match")    

# structure(split(word1))
match(word2,word1)