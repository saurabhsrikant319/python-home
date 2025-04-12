# a=input("string name:")
# b=a.split()
# c=""
# for i in range(1,len(b)+1):
#     c+=(b[-i]+" ")
# print(c)
from os.path import split

# a=input("string name:")
# b=a.split()
# c=""
# for i in range(len(b)):
#     c+=(b[i])
# print(c)

# a=input("string name:")
# b=a.split()
# c=""
# for i in b:
#     if len(i)%2==0:
#         c+=(i+" ")
# print(c)
a=input("string name:")
b=a.split()
c=""
for i in b:
    if len(i)%2!=0:
        c+=(i+" ")
print(c)