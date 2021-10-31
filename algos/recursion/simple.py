def reverse(string):
    # Base Case: Empty String
    if string == "":
        return ""

    # Sub-problem: Take the first char of the string and put it in the last. 
    # Call reverser on the remaining string recursively. 
    return reverse(string[1:]) + string[0]


print(reverse("hello"))

def isPalindrome(string):
    if len(string) == 1 :
        return True

    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    
    return False

print('Kayak is palindrome ', isPalindrome('kayak'))
print('Naren is palindrome ', isPalindrome('Naren'))
print('racecar is palindrome ', isPalindrome('racecar'))


def decToBin(n, result=''):
    if n == 0:
        return result;
    
    result = '{}{}'.format(n%2, result)

    return decToBin(n/2, result)

print(decToBin(16))