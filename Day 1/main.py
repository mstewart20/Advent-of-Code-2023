# Find a digit in a string
def findDigit(s):
  for char in s:
    if char.isdigit():
      return char
  return ""

def findNumber(s):
  x = findDigit(s)
  y = findDigit(s[::-1])

  return int(x + y)


# Using readlines()
inputFile = open('Day 1/input.txt', 'r')
lines = inputFile.readlines()

sum = 0

for line in lines:
  sum += findNumber(line)

print("Sum is: " + str(sum))