def prefixsum(arr):     # prefix array
    pref = [arr[0], ]
    for i in range(1, n):
        pref.append(pref[i - 1] + arr[i])
    return pref
 
def suffixsum(arr):     # suffix array
    suff = [arr[n - 1], ]
    for i in range(n - 2, -1, -1):
        suff.append(suff[-1] + arr[i])
    suff = suff[::-1]
    return suff

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return a * b // gcd(a, b)

def arrayXOR(n):    # XOR of range [1, n]
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0
    
def checkprime(n):
    if(n > 1):
        for j in range(2, int(math.sqrt(n)) + 1):
            if (n % j == 0):
                return 0
        return 1
    else: return 0

def primesieve(n):
    array=[1]*n
    for j in range(4,n,2): array[j]=0
    for j in range(2,n):
        for j in range(j*j,n,j):
            array[j]=0
    return array

def binarySearch(arr, key):   # search lower bound(key)
    beg, end = 0, len(arr) - 1
    found = False
    ind = -1
    while beg <= end:
        mid = beg + (end - beg) // 2    # to avoid mid overflow
        if key == arr[mid]:             # condition
            found = True
            ind = mid
            # end = mid - 1     # lower bound
            break                  # traditional BS
        elif key < arr[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    if not found:     # insertion point = beg (beg < end == True)
        return -1 
    else:
        return ind

def findtype(nums):
    if type(nums) == type(1):
        return 1
    elif type(nums) in (type([0,1]), type((0,1))):
        return 2
    else:
        return 3

def bfs(G, src, dest = -1):
    q = []
    bfs_path = []
    dist = [0] * G.V
    parent = [0] * G.V
    visited = [False] * G.V
    q.append(src)
    dist[src] = 0
    parent[src] = src
    visited[src] = True
    while q:
        x = q.pop(0)
        bfs_path.append(x)
        for nbr in G.ADJ[x]:
            if not visited[nbr]:
                q.append(nbr)
                dist[nbr] = dist[x] + 1
                parent[nbr] = x
                visited[nbr] = True
    return bfs_path

def dfs(G, src):
    dfs_path = []
    visited = [False] * G.V
    def dfsUtil(node):
        dfs_path.append(node)
        visited[node] = True
        for nbr in G.ADJ[node]:
            if not visited[nbr]:
                dfsUtil(nbr)
        return
    dfsUtil(src)
    return dfs_path
