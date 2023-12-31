#define digits as strings
strDigits = {"one": "1",
             "two": "2",
             "three": "3",
             "four": "4", 
             "five": "5", 
             "six": "6",
             "seven": "7",
             "eight": "8", 
             "nine": "9",
             "zero": "0"}

# Find a digit in a string
def findDigit(s):
  for char in s:
    if char.isdigit():
      return char
  return ""

def findNumber(s):
  x = findDigit(replaceDigits(s))
  y = findDigit(replaceDigitsReverse(s)[::-1])

  return int(x + y)

def replaceDigits(s):
  for i, char in enumerate(s):
    for digit in strDigits.keys():
      if s.find(digit, i) == i:
        return replaceDigits(s.replace(digit, strDigits[digit]))

  return s

def replaceDigitsReverse(s):
  for i, char in reversed(list(enumerate(s))):
    for digit in strDigits.keys():
      if s.find(digit, i) == i:
        return replaceDigits(s.replace(digit, strDigits[digit]))
  
  return s
  
# Using readlines()
inputFile = open('Day 1/input.txt', 'r')
lines = inputFile.readlines()

sum = 0

for line in lines:
  print("line: " + line)
  num = findNumber(line)
  print("num: " + str(num))
  sum += num
#sum += findNumber("1oneightd");

print("Digit Sum is: " + str(sum))