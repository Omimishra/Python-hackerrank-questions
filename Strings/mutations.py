# Read a given string, change the character at a given index and then print the modified string.
# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    arr = []
    for s in string:
        arr.append(s)
    arr[position] = character
    string = ""
    for t in arr:
        string += t
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)