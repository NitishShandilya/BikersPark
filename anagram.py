import sys
def Permutation(inputString):
    outputArray = []
    if len(inputString) <= 1:
        outputArray.append(inputString)
    elif len(inputString) > 1:
        firstIndex = 0;
        firstEntry = inputString[firstIndex]
        restEntries = inputString[firstIndex+1:]
        outputArray = Combine(Permutation(restEntries),firstEntry)
    return outputArray
           
def Combine(permutedEntries,firstEntry):
    result = []
    for entry in permutedEntries:
        for i in range(len(entry)+1):           
            result.append(entry[:i]+ firstEntry + entry[i:])
           
    return result          
sortedArray = sorted(Permutation(sys.argv[1]))
anagramFile = open('anagram_out.txt','w')

for result in sortedArray:
    anagramFile.write(result)
    anagramFile.write('\n')
    
anagramFile.close()
