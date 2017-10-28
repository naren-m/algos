# Visualization of call stack @ https://goo.gl/5xrBAv


def permute(string, start, end, answer):
    if start == end:
        return

    for i in range(start, end + 1):
        string = swap(string, start, i)
        answer.add(string)
        permute(string, start + 1, end, answer)

    return


def swap(string, idx1, idx2):
    if idx1 == idx2:
        return string
    l_str = list(string)
    l_str[idx1], l_str[idx2] = l_str[idx2], l_str[idx1]
    swapped = ''.join(l_str)
    return swapped


inp = "abc"
answer = set()
permute(inp, 0, len(inp) - 1, answer)
print(answer)

print("Visualization of call stack @ https://goo.gl/5xrBAv", end='\n')
