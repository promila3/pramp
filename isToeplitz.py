def isToeplitz(arr):
	"""
	@param arr: int[][]
	@return: bool
	"""
	pass #your code goes here
  m = len(arr)
  if m == 0: # rows
    return True
  if n == 1: # columns
    return True
  result = True
  for i in range(m-1,-1,0):
    currI = i
    currJ = 0
    item = arr[currI][currJ]
    
    while (currI < m and currJ < n):
      if item != arr[currI][currJ]:
        result = False
      currI +=1 
      currJ +=1
  
  for j in range(1, n):
    currI = 0
    currJ = j
    item = arr[currI][currJ]
    
    while (currI < m and currJ < n):
      if item != arr[currI][currJ]:
        result = False
      currI +=1 
      currJ +=1
  return result
