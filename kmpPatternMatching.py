def computeLps(patternArr, patternArrLength):
    lps = [0] * patternArrLength
    i = 1
    j = 0
    while i < patternArrLength:
        if patternArr[i] == patternArr[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j-1]

    return lps

def kmp(mainArr, patternArr):
    mainArrLength = len(mainArr)
    patternArrLength = len(patternArr)
    lps = computeLps(patternArr, patternArrLength)
    i = 0
    j = 0
    while i < mainArrLength and j < patternArrLength:
        if mainArr[i] == patternArr[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]

    if j == patternArrLength:
        return "Pattern found starting at index " + str(i - patternArrLength) + " in the main String"
    return "Pattern not found"


mainStr = "abcxabcdabcdabcy"
pattern = "dabcy"
print kmp(list(mainStr), list(pattern))
