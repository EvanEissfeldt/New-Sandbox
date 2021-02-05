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

def function():
  
  with open('test', 'r') as file:
    x = file.read()
    for char in x:
      if char.isalnum() == False:
        x = x.replace(char, f' {char}')
    print(x)
    

function()
  







