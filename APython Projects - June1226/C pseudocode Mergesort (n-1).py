#n = int(input("Number of nums"))
#a = [int(input("Enter a number")) for i in range(n)]
import random

a = [random.randint(1,9) for i in range(5)]
b = [0,1,2,3]
print(a)
#print(b)

def Merge(A, left, mid, right):
  sizeL = mid-left+1
  sizeR = right-mid
  #print("Sizes",sizeL,sizeR)
  L = [0 for i in range(sizeL+1)]
  R = [0 for i in range(sizeR+1)]
  print(L,R)
  
  for i in range(sizeL):
    L[i] = A[left+i]
    
  for j in range(sizeR):
    R[j] = A[mid+j+1]
    
  L[sizeL] = max(A)+1
  R[sizeR] = max(A)+1
  
  #L = A[left:mid+1] + [max(A)+1]
  #R = A[mid+1:right+1] + [max(A)+1]
  print(L,R)

  i = 0
  j = 0
  for k in range(left,right+1):
    if (L[i] <= R[j]):
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

def mergeSort(A, left, right):
  mid = (left+right)//2
  #print(left,mid,right)
  #print(right-left)
  if (right-left > 0):
    #print(A[left:mid+1], mid+1-left)
    mergeSort(A,left,mid)
    #print(A[mid+1:right+1], right-mid)
    mergeSort(A,mid+1,right)
    Merge(A, left, mid, right)

mergeSort(a,0,len(a)-1)
print(a)


  
  
  

  
  