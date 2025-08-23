a=("a","e","i","o","u","A","E","I","O","U")
n=input("enter the text")
vowels=[]
consonans=[]
for i in n:
    if i in a:
        vowels+=i
    else:
        consonans+=i
print("vowels",vowels)
print("consonants",consonans)
