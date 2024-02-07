"""lst = [1,9,3,7,1,9,8,3,5,6,2,8,9,1,3]
print (chr(ord('a')+(list({i for i in lst if sum([j for j in lst if j>i])==0})[0])))"""

"""print ("www.google.com/ana/are/mere/si/pere".split ("/",2) [2] ).rsplit("/",2) [0].replace ("/"," ")"""

"""import re
s = "Azi am examenul la python !"
print (re.sub("\w{8}", "c++", s))"""

"""print (sorted(sorted(list(set([5,2,10,2,15,1,3,7,9,3,11,1]))), key = lambda i: 3-i%3))
print(list(3 - i % 3 for i in sorted(set([5, 2, 10, 2, 15, 1, 3, 7, 9, 3, 11, 1]))))
print(-12%3)"""

"""import re
print (re.split("[2357]+","97318526"))"""

"""class A:
x = {1:1,2:2,3:3}
def Set(self,n): self.x[n] = n
def Keys(self): return [i for i in self.x]
a1 = A();a2 = A()
a1.Set(4)
print (a1.Keys() + a2.Keys())"""

"""print (sorted(list({i for i in "anaaremere"} & {j for j in "pythonexam"})))"""


#print("restantapython"[2:-3:3])
#print([x^y for x in range(1,5) for y in range(1,5) if x%y==1])
"""
for k in [-1, 4, 2]:
    # Your code here
    print(k)"""

"""x={1,2,3}
y=x           #nu stiu cum dar devin una si aceeasi
x &= {2,3,4}  #intersectia
print(x)
y |= {1,2}    #reuniunea
print(x)
print(y)"""

"""1 2 3 4 5
d[1] = 1,3,5
d[0] = 2,4"""

import re
print(len(re.split("[abc]","We have python examination today")[2]))
"""
0000 0
0001 1
0010 2
0011 3
0100 4
0101 5
0110 6
0111 7
1000 8
1001 9
1010 10
1011
1100
1101
1110
1111

1 25 73 17
1 5   3  7  #mod10"""

#print(10/3)
"""print("ABC"*4)
A A ABCABC"""


"""x = 50 25 12

x= 100
while x>0:
    x = x//2
    if x==6:break;
    print(x)
else:print("0")"""

"""import re
print(re.sub("(\d\d)",lambda x:x.group(0)[0],"10+20=30"))
#\d -> inseamna digit"""

"""import struct
s=""
for i in struct.pack("@bhi",3,1,2):
    s+=hex(i)+" "
print(s)"""

"""s="s=\"exec(s)\""
exec(s)
print(s)"""

"""a=[5,4,3,2,1]
a[1:-3]=[1,2,3]
print(a)"""

#print([x+y for x in range(1,5) for y in range(1,5) if x%y==0])

#print([1,*([0]*3),2])

"""import struct
s=""
for i in struct.pack("@bhbib",3,1,2,4,5):
    s+=hex(i)+" "
print(s)"""

""""@"
indicates
native
byte
order.
"b"
packs
an
integer as a
signed
char(1
byte).
"h"
packs
an
integer as a
short(2
bytes).
"i"
packs
an
integer as an
int(4
bytes)."""

"""import struct
s=""
for i in struct.pack("@bhh",1,2,3):
    s+=str(i)+" "
print(s)"""

"""x = {"A","a","B","b",1,2,3}
print (x)
print (x.pop())"""

"""import re
print (re.split("\d\d+", "12345"))"""