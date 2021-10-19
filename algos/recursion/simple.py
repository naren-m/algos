def reverse(string):
    # Base Case: Empty String
    if string == "":
        return ""

    # Sub-problem: Take the first char of the string and put it in the last. 
    # Call reverser on the remaining string recursively. 
    return reverse(string[1:]) + string[0]


print(reverse("hello"))
