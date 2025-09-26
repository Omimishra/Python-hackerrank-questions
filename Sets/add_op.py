# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

# Find the total number of distinct country stamps.
# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

n = int(input())
country_stamps = set()

for i in range(n):
    country_stamps.add(input())

print(len(country_stamps))