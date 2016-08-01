#This code emulates insertion sort on a user input array
#Time complexity: O(n(n+1)) ~ O(n^2)

a = []
n = int(input('Enter the size of array: '))
print ('Enter the array elements one by one')
for i in range(n):
  ni=int(input())
  a.append(ni)

print (a)

for i in range(n):              #pick an element
  for j in range(i):            
    if a[j]>a[i]:               #compare it with every element preceeding itself
      a[j],a[i] = a[i],a[j]     #keep swapping if the preceeding element is larger
      

print (a)