"""
add two questions in this category,
basically the same idea, use two pointers to in-place
operate on arrays
"""

def dutch_national_flag(arr):
	# sort three colors (0, 1, 2)
	# invariant: all elements < low are 0 and all elements > high are 2
	# all elements in between are 1
	low, high = 0, len(arr) - 1
	i = 0
	while i <= high:
		if arr[i] == 0:
			arr[low], arr[i] = arr[i], arr[low]
			low += 1
			i += 1
		elif arr[i] == 1:
			# do nothing
			i += 1
		else: # arr[i] == 2
			# can't increment i here because after swap
			# arr[i] can be anything
			arr[high], arr[i] = arr[i], arr[high]
			high -= 1
	return arr



def test_dutch_national_flag():
	print (dutch_national_flag([2, 2, 0, 1, 2, 0]))
	print (dutch_national_flag([1, 0, 2, 1, 0]))


def move_zeros(nums):
	i = 0
	while i < len(nums) and nums[i] != 0:
		i += 1
	j = i + 1
	while j < len(nums):
		if nums[j] != 0:
			nums[i] = nums[j]
			i += 1
		j += 1
	while i < len(nums):
		nums[i] = 0
		i += 1
	return nums

def test_move_zeros():
	print (move_zeros([1,0]))
	print (move_zeros([1,0,1,0,0,0,1]))


test_move_zeros()
test_dutch_national_flag()