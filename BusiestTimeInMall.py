def find_busiest_period(data):
  pass # your code goes here
  tempResult = []
  numInMall = 0
  prev = data[0][0]
  maxTS = data[0][0]
  lenD = len(data)
  maxVal = -(sys.maxint) - 1
  i = 0
  previ = i
  '''
  while i < lenD:
    
    while prev == data[i][0]:
      if data[i][2]:
        numInMall += data[i][1]
      else:
        numInMall -= data[i][1]
      prev = data[i][0]
      previ = i
      i += 1
    if numInMall > maxVal:
      maxVal = numInMall
      maxTS = data[i-1][0]
    
[[1487799425,21,0],[1487799427,22,1],[1487901318,7,0]]
  '''
  for i in range(lenD):
    if data[i][2]:
      numInMall += data[i][1]
    else :
      numInMall -= data[i][1]
    print i,numInMall, maxVal
    if (i < lenD-1) and data[i][0] == data[i+1][0]:
      continue
    
    if numInMall > maxVal:
      maxVal = numInMall
      maxTS = data[i][0]
  return maxTS
      
  
 
    
