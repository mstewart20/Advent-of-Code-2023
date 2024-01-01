numberIndex = []
symbolIndex = {}
offsets = [-1,0,1]
 
def readInput():
  
  # Using readlines()
  inputFile = open('Day 3/input.txt', 'r')
  lines = inputFile.readlines()
  
  row = 0
  isNumber = False
  
  for line in lines:

    currentNumber = {}
    
    for i, char in enumerate(line):
      if char.isdigit():
        if isNumber:
          currentNumber["number"] += char
        else:
          isNumber = True
          currentNumber = {"row": row,
                          "column": i,
                          "number": char}
          numberIndex.append(currentNumber)
      else:
        isNumber = False

        if char != "." and not char.isspace():
          symbolIndex[str(row) + "x" + str(i)] = {"row": row, "column": i}
    
    row += 1

def calculateNumber(number):
  row = number["row"]
  column = number["column"]
  value = number["number"]

  #print("checking number " + value)

  for i, char in enumerate(value):
    for rowOffset in offsets:
      for colOffset in offsets:
        key = str(row + rowOffset) + "x" + str(column + colOffset + i)
        #print("checking key " + key)
        if key in symbolIndex:
          #print("found key for value " + value)
          return int(value)

  #print("did not find number " + value)
  return 0
  
def findParts():
  sum = 0

  for number in numberIndex:
    sum += calculateNumber(number)
    
  return sum


#Start the main program
readInput()
print(findParts())

#print("symbols")
#print(symbolIndex)

#print("numbers")
#print(numberIndex)


  