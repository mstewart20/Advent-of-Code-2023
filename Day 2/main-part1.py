def splitSet(s):
  print("Parsing attempt: " + s);
  set = {
    "blue":0,
    "red":0,
    "green":0
  }
  colors = s.split(",")

  for color in colors:
    print("got color: " + color)
    values = color.strip().split(" ")
    set[values[1]] = int(values[0])

  return set

def checkGame(s):
  
  gameSplit = s.split(":")
  print(gameSplit)
  id = int(gameSplit[0].replace("Game ", ""))

  sets = gameSplit[1].split(";")
  for set in sets:
    colorValues = splitSet(set)

    print(colorValues)
    if(colorValues["red"] > 12 or colorValues["green"] > 13 or colorValues["blue"] > 14):
      return 0

  return id

# Using readlines()
inputFile = open('Day 2/test-input.txt', 'r')
lines = inputFile.readlines()

sum = 0

for line in lines:
  num = checkGame(line)
  print("num: " + str(num))
  sum += num

print("Sum: " + str(sum))
  
  