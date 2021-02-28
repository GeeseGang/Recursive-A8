#  File: Palindrome.py

#  Description: finds the shortest palindrome that can be made by adding
#  letters to the beginning of a string

#  Student Name: Samantha De Figueiredo

#  Student UT EID: mfd592

#  Partner Name: David Easter

#  Partner UT EID: dme792

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 2/26/2021

#  Date Last Modified: 2/28/2021

import sys


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    result = ''
    for x in range(len(str)):

        # Checks if the current longest substring is a palindrome
        sub = str[0:len(str)-x]
        reverse = sub[::-1]
        if(sub == reverse):

            # Adds on the end to the beginning
            addition = str[len(str)-x:]
            result = addition[::-1] + sub + addition
            break

    return result



# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''
    f = sys.stdin.read()
    lineByLineList = f.split('\n')

    for before in lineByLineList:
        print(smallest_palindrome(before))
    # read the data
    # print the smallest palindromic string that can be made for each input

if __name__ == "__main__":
  main()
