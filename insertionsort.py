a=[57,96,45,91]
for i in range(len(a)):
    j=i-i
    next_element=a[1]
while (a[j]>next_element) and j>=0:
    a[j+1]=a[j]
    j=j-1
a[j+1]=next_element
print(a)
