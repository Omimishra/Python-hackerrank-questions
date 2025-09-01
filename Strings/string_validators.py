# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    ans = any(char.isalnum() for char in s)
    print(ans)
    ans = any(char.isalpha() for char in s)
    print(ans)
    ans = any(char.isdigit() for char in s)
    print(ans)
    ans = any(char.islower() for char in s)
    print(ans)
    ans = any(char.isupper() for char in s)
    print(ans)
    
