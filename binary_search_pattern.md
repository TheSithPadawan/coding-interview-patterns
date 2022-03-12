
# Binary Search Pattern
The pattern that we are looking for: 
- there is some range that search can be done 
- there’s some check that we can perform when validating an answer
- there’s some elimination that we can assert to drop some range of the search space

Very obvious questions fitting this pattern
## Finding insert position
Basically implementing bisect.bisect_left for python, and lower_bound() for cpp 
```py
def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        ans = len(nums)
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        return ans
```

## Search in RSA
Binary search to determine if mid is in first or second sequence 
```py
A[start] <= A[mid] # left side is sorted
A[mid] <= A[end] # right side is sorted
```

Code 
```py
def search_rotated_array(arr, key):
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return mid
    if arr[start] <= arr[mid]:  # left side is sorted in ascending order
      if key >= arr[start] and key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1
    else:  # right side is sorted in ascending order
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid - 1
  # we are not able to find the element in the given array
  return -1

```

## Find min in RSA
Pass

## Find peak
Pass 

Not so obvious questions
