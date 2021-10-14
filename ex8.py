l="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
l1=""
l2=""
l3=""
print("Sirul initial= ", l)

for i in l:
    a=chr(ord(i)+1)
    l1+=a
    b=l1.replace("!"," ")
    c=b.replace("[","A")
print("Sirul1=",c)


l2=l1
for i in l:
    e=l2.replace(("Z"), ("A"))
print("Sirul2:", e) 

l3=e
for i in l:
    f=l3.replace(' ','-')
print("Sirul3:", f)