#Two Sums Problem
#-------------------------

#Read the input file
f = open("2020/day1-data.txt", "r")
items = f.readlines()
f.close()
puzzleInput = []
for item in items:
    integer = int(item); 
    puzzleInput.append(integer)


# Define the work to be done
def twoSum (puzzleInput, goalSum):
  sums = []
  hashTable = {}

  for i in range(len(puzzleInput)): 
    match = goalSum - puzzleInput[i]
    if match in hashTable:
        print(match," + ",puzzleInput[i]," = ", goalSum)
        answer = match * puzzleInput[i]
        print("The answer is:", answer)
    hashTable[puzzleInput[i]] = puzzleInput[i]

# Execute the code
twoSum(puzzleInput, goalSum)
