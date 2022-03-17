# k sum pattern
This covers 2 sum, 3 sum, 4 sum, etc…
Different types of question:
(1) count the number of arrays with sum = …
(2) output all the arrays with sum = …
(3) check if there exists an array with sum =… 

All solvable using one template:
```py
def ksum(start, target, k):
            results = []
            if k > 2:
                for i in range(start, len(nums)):
                    if (i > 0 and i > start and nums[i] == nums[i-1]):
# this is for counting unique subarrays
                        continue
                    result = ksum(i+1, target - nums[i], k-1)
                    if result:
                        for r in result:
                            r.append(nums[i])
                        results += result
                return results
            
            # reduce to two sum problem, base case
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    results.append([nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            return results
```

In the previous templates, if it is counting the # of subarrays,  this line is changed to, also change the return type of the original caller function respectively (from list -> int)
```py
results += r - l + 1
```