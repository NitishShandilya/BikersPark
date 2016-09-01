"""
Given a non palindromic number, find a palindromic number that has minimal absolute difference with the given number
"""
def findNextBestPalindrome(number):
    numberArray = []
    while number > 0:
        numberArray.append(number%10)
        number /= 10
    numberArray.reverse()

    for i in range(len(numberArray)/2):
        j = len(numberArray) - i -1
        if numberArray[i] != numberArray[j]:
            numberArray[j] = numberArray[i]

    initial = 10 ** (len(numberArray)-1)
    sumNum = 0
    for i in range(len(numberArray)):
        sumNum += initial*numberArray[i]
        initial /= 10

    return sumNum

# Test
number = 12345
print findNextBestPalindrome(number)