n=int(input())
arr = list(map(int, input("\nEnter the array elements : ").strip().split()))[:n]
result=list(reversed(arr))
print(result)