import math
def rectangle(perimeter, area):
	if type(perimeter) != int or type(area) != int:
		return False
	else:
		side1 = (perimeter/4) + (1/4)*math.sqrt((perimeter*perimeter)-(16*area))
		side2 = (perimeter/4) - (1/4)*math.sqrt((perimeter*perimeter)-(16*area))
		if side1.is_integer() == True and side2.is_integer() == True:
			if side1 >= side2:
				return int(side1)
			else:
				return int(side2)
		else:
			return False


def frequency(numList):
	freq_dict = {}
	current = 0
	for element in numList:
		if numList.count(element) > numList.count(current):
			current = element
		if element not in freq_dict:
			freq_dict[element] = 1
		else:
			freq_dict[element] += 1
	return (current, freq_dict)


def getUniques(aList):
  newList = []
  for x in aList:
    if x not in newList:
      newList.append(x)
  return newList

def successors(file):
  ans_dict = {}
  with open(str(file), 'r') as File:
    content = File.read()
    for char in content:
      if char != ' ':
        if char.isalnum() == False:
          content = content.replace(char, f' {char} ')   
    content = content.split()
    i = 0
    ans_dict['.'] = [content[0]]
    for element in content:
      if element not in ans_dict:
        try:
          ans_dict[element] = [content[i + 1]]
          i += 1
        except IndexError:
          continue
      else:
        if content[i+1] not in ans_dict[element]:
          ans_dict[element].append(content[i + 1])
        i += 1
  print(ans_dict)
  
    
    
    

successors('test')