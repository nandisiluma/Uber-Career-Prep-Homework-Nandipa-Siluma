def isStringPermutation(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		for i in range(len(s1)):
			if s1[i] in s2:
				continue
			else:
				return False
	return True

assert isStringPermutation("abc", "cba") == True
assert isStringPermutation("nandi", "Siluma") == False

def pairsThatEqualSum(inputArray, targetSum):
	result = []
	i = 0
	j = i + 1
	while i < len(inputArray) - 1:
		if inputArray[i] + inputArray[j] == targetSum:
			result.append((inputArray[i],inputArray[j]))
			j += 1
		else:
			j += 1
		i += 1  
	return result

assert pairsThatEqualSum([1,2,3,4,2,3], 6) == [(2,4), (3,3), (4,2)]
assert pairsThatEqualSum([0,0,0,0,1], 1) == [(0,1)]



	
