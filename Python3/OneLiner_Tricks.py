# to get an array from STDIN
arr = list(map(int, input().split()))
# arr = [1, 3, 5, 7, 8, 6, 4, 2,]

# to print the array without [,]
print(*arr) # 1 3 5 ..... 6 4 2

# to add seperator between different elements in the output array
print(*arr, sep = "--->") # 1--->3--->5 ..... 6--->4--->2

# single line if-else statement
res = "YES" if flag == 1 else "NO"  # res = "YES"

# single line for loop
arr = [(i + 1) * 10 for i in range(10)] # [10 20 30 ..... 80 90 100]
