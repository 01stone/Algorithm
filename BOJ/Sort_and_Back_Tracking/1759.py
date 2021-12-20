from itertools import combinations

l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

vowels = {'a', 'e', 'i', 'o', 'u'}
def vowels_check(word):
  x = set(word) - vowels
  y = set(word).intersection(vowels)
  if len(x) < 2 or len(y) < 1:
    return False
  else:
    return True

comb = combinations(sorted(alphabets), l)
for i in comb:
  if vowels_check(i):
    print(''.join(i))