'''     // -- Template by A_*_A -- //       '''
import sys, math, bisect, heapq, collections, itertools, functools
inum = lambda: int(sys.stdin.readline())
imap = lambda: map(int, sys.stdin.readline().split())
itup = lambda: tuple(map(int, sys.stdin.readline().split()))
isor = lambda: sorted(map(int, sys.stdin.readline().split()))
isor2 = lambda nums: sorted(nums, key = lambda num1: (num1[0], num1[1]))
ilis = lambda: [int(zz) for zz in sys.stdin.readline().split()]
hp = lambda: collections.defaultdict(lambda:0)
adjlist = lambda: collections.defaultdict(lambda:[])
lcm = lambda num1, num2: num1 * num2 // math.gcd(num1, num2)
npr = lambda num1, num2: math.factorial(num1) // math.factorial(num1 - num2)
ncr = lambda num1, num2: math.factorial(num1) // (math.factorial(num2) * math.factorial(num1 - num2))
even = lambda nums: list(filter(lambda num1: num1 % 2 == 0, nums))
oddd = lambda nums: list(filter(lambda num1: num1 % 2 != 0, nums))
fact = lambda num1: functools.reduce(lambda num2, num3: num2 * num3, range(1, num1 + 1))
freq = lambda nums: collections.Counter(nums)
bitset = lambda nums: [int(num1) for num1 in bin(nums)[2:]]
minheap = lambda nums: 1 if heapq.heapify(nums) == None else 0
maxheap = lambda nums: 1 if heapq._heapify_max(nums) == None else 0   # maybe deprecated!!!
lowerbound = lambda nums, key, start, stop: bisect.bisect_left(nums, key, lo=start, hi=stop)
upperbound = lambda nums, key, start, stop: bisect.bisect_right(nums, key, lo=start, hi=stop)
inorder = lambda root: inorder(root.left) + [root.val] + inorder(root.right) if root else []
prefixsum = lambda nums: list(itertools.accumulate(nums, lambda num1, num2: num1 + num2))
suffixsum = lambda nums: prefixsum(reversed(nums))
grid = lambda rows, cols: [[0 for j in range(cols)] for i in range(rows)]
onum = lambda num1: '%d'%num1
omap = lambda num1, num2: '%d %d'%(num1,num2)
olis = lambda nums: ' '.join((str(nums[i]) for i in range(len(nums))))
# odict = lambda nums: str(dict(nums))[1:-1]
odict = lambda nums: "\n".join((str("%i: %s"%(num1[0], " ".join((str(num2) for num2 in num1[1])))) for num1 in zip(nums.keys(), nums.values())))
ogrid = lambda grid: '\n'.join((' '.join((str(num1) for num1 in nums)) for nums in grid))
input = lambda: sys.stdin.readline()
print = lambda nums: sys.stdout.write(nums + "\n")
'''     // -- Template by A_*_A -- //       '''
