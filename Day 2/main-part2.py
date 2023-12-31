def splitSet(s):
  set = {
    "blue":0,
    "red":0,
    "green":0
  }
  colors = s.split(",")

  for color in colors:
    values = color.strip().split(" ")
    set[values[1]] = int(values[0])

  return set

def checkGame(s):
  
  gameSplit = s.split(":")
  print(gameSplit)
  id = int(gameSplit[0].replace("Game ", ""))

  sets = gameSplit[1].split(";")

  maxSet = {
    "blue":0,
    "red":0,
    "green":0
  }
  
  for set in sets:
    colorValues = splitSet(set)

    print(colorValues)

    maxSet["blue"] = max(maxSet["blue"], colorValues["blue"])
    maxSet["red"] = max(maxSet["red"], colorValues["red"])
    maxSet["green"] = max(maxSet["green"], colorValues["green"])

  print("Id: " + str(id) + " Max Set: " + str(maxSet))
  print("Id: " + str(id) + " Power: " + str(maxSet["blue"] * maxSet["red"] * maxSet["green"]))
  return maxSet["blue"] * maxSet["red"] * maxSet["green"]

# Using readlines()
inputFile = open('Day 2/input.txt', 'r')
lines = inputFile.readlines()

sum = 0

for line in lines:
  num = checkGame(line)
  print("num: " + str(num))
  sum += num

print("Sum: " + str(sum))
  
  