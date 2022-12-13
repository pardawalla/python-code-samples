# Author: Hussain A. Pardawalla
# Date: March 7, 2022
# Description: The aim of the fucntion is to find the longest palindrome from a given string
# Tested out in Python 3.10 (64bit)
# Out of scope:
#   - Validation that the given input string fromat is correct
#   - Words with spaces i.e. 'tit for tata'
#   - Non-English alphabets
#   - words with special characters i.e. tit-for*-tat, 
#   - alphanumeric words e.g. G33G
#   Note: In some cases it might work, but then in some cases it could lead to undefined results


# To test out the code in the python terminal enter
# >>> import os
# >>> os.chdir('C:\\test') --- this is the directory where the code resides
# >>> import longest-palindrome as lp
# >>> lp.testSuite()

import datetime


def findTheLongestPalindrome(myString):
    # We check if the given string is a palnidrome
    # if it is, then we have our longest palindrome.
    if isPalindrome(myString):
        #print('Longest Palindrome found ' + myString)
        return(myString)
    else:
    # We now need to traverse.
        tmp = ''
        storedValue = ''
        for i in range(len(myString)-1):
            # We will now keep on going through the given string, from
            # left to right. And will keep on repeating the process till we either
            # find the biggest palindrome, or we reach the end. 
            # We do this as the biggest palindrome could be later on 
            # e.g. given ABCCBABCCB we would want to return BCCBABCCB
            # and not ABCCBA. Once the substring is twp words long we stop.
            tmp = containsPalindrome(myString[i:])
            # We ensure we only save the longest palindrome we find
            if(len(tmp)>len(storedValue)):
                storedValue = tmp
        # end of for loop
    # end of else statement
 
    if(storedValue != ''):
        #print('Longest palindrome is:'+storedValue)
        return(storedValue)
    else:
        #print('No Palindrome found')
        return ''
#end of def findTheLongestPalindrome(myString)        

# helper function 1
def containsPalindrome(myString):
    # We start from the end of the string and move upwards
    # That is we start getting the substring from right to left
    # E.g if the work is Arkd, we'll first use Arkd, then Ark, 
    # then Ar. 
    # Since our substring is getting shorter and shorter we 
    # just return the first palindrome we find, as that would be 
    # the largest. 
    for i in range(len(myString), 1, -1):
        if(isPalindrome(myString[:i])):
            return(myString[:i])
        
    # if no palindrome is found, return an empty string
    return ''     
#end of def containsPalindrome()

# helper function 2
def isPalindrome(testStr):
    isPalindrome = False
    # We get the reverse of the input string
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    myReverseTestStr = testStr[::-1]
    
    # A palindrome string has to be greater than 1
    if (len(testStr)<=1):
         print('ERROR: String has to be greater than 1')
         
    # if the string is a palindrome set isPalindrome to True
    # It shouldn't be case sensitive. I.e. Aba is a planidrome.
    # So making sure comparison isn't case sensitive. 
    if( testStr.lower() == myReverseTestStr.lower() ):
        isPalindrome = True
        
    return(isPalindrome)
# end of def isPalindrome(testStr):
        

# Test function to help test the function findTheLongestPalindrome().    
def testPalindrome(testString, expected):
    result = findTheLongestPalindrome(testString)
    currentDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if(result.lower()==expected.lower()):
        print('['+currentDateTime+'] PASS: Expected:"'+expected+'" AND got:"'+result+'" for "'+testString+'"\n\n')
    else:
        print('['+currentDateTime+'] FAIL: Expected:"'+expected+'" BUT got:"'+result+'" for "'+testString+'"\n\n')

def testSuite():
    # Just a function used to test the various scenarios. 
    
    # Case 1: No planidrome
    testPalindrome(testString='Palindrome', expected='')
    
    # Simple test cases
    # Case 2: Palindrome in the middle KABOOBAD
    testPalindrome(testString='KABOOBAD', expected='ABOOBA')

    # Case 3: Palindrome is at the end xyzABCCBA
    testPalindrome(testString='xyzABCCBA', expected='ABCCBA')
    
    # Case 4: Palindrome is at the beginning XYZoZYXab
    testPalindrome(testString='XYZoZYXab', expected='xyzozyx')

    # Harder scenarios
    # Case 5: Multiple palindromes of different sizes AAAsoulBCDEEDCBmachinesNOON
    testPalindrome(testString='AAAsoulBCDEEDCBmachinesNOON', expected='BCDEEDCB')
    
    # Case 6: Plaindromes within a planidrome AbccbAbccb
    testPalindrome(testString='AbccbAbccb', expected='bccbAbccb')
    
    # Case 7: Mulitiple palindromes of the same size. e.g abctitfortatisbob. In  
    #         this case it should return the first one that's found.
    testPalindrome(testString='abctitfortatisbob', expected='tit')
#end of def testSuite():

# testSuite()
# by uncommenting the line above you can execute the code by entering
# c:\test>py longest-palindrome.py 
# in the terminal. 



#references
#1. https://www.w3schools.com/python/python_howto_reverse_string.asp
#2. https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
#3. https://stackoverflow.com/questions/663171/how-do-i-get-a-substring-of-a-string-in-python
#4. https://www.programiz.com/python-programming/datetime/current-time
#5. https://www.programiz.com/python-programming/datetime/strftime
#6. https://stackoverflow.com/questions/3987041/run-function-from-the-command-line