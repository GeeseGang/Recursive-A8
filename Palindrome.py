#  File: Palindrome.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    result = ''
    for x in range(len(str)):
        sub = str[0:len(str)-x]
        reverse = sub[::-1]
        #print(reverse)
        if(sub == reverse):
            #print(sub, reverse, '\n')
            addition = str[len(str)-x:]
            result = addition[::-1] + sub + addition
            #result = sub
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
