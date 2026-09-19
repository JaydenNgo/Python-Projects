#n = int(input("Number of nums"))
#a = [int(input("Enter a number")) for i in range(n)]
a = [5,3,8,1,3,4,7,8,5]


def Merge(A, left, mid, right):
  L = [0 for i in range(mid-left+1)]
  R = [0 for i in range(right-mid+1)]
  
  for i in range(left,mid):
    L[i-left] = A[i]
    
  for j in range(mid,right):
    R[j-mid] = A[j]
    
  L[mid-left] = max(A)+1
  R[right-mid] = max(A)+1
  
  print(L,R)

  i,j  = 0,0
  for k in range(left,right):
    if (L[i] < R[j]):
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1

def mergeSort(A, left, right):
  mid = (right+left)//2
  if (right-left > 1):
    mergeSort(A,left,mid)
    mergeSort(A,mid,right)
    Merge(A, left, mid, right)

mergeSort(a,0,len(a))
print(a)


  
  
  

  
  