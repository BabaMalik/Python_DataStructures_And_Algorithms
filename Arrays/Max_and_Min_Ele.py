n=int(input())
arr =  [int(x) for x in input().split()][:n]
arr.sort()
print("Minimum :", arr[0] )
print("Maximum :", arr[n-1] )