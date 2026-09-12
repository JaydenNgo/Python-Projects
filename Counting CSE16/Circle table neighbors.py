a = [1,2,3,4,5]
for ind,num in enumerate(a):
    if ind+1 >= len(a):
        print(num,':', a[ind-1],a[0])
    else:    
        print(num,':', a[ind-1],a[ind+1])