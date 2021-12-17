# 6996 : 애너그램

n = int(input())

for _ in range(n):
  a, b = map(str, input().split())
  a_list_sorted = sorted(list(a))
  b_list_sorted = sorted(list(b))

  if a_list_sorted == b_list_sorted:
    print(a + " & " + b + " are anagrams.")
  else:
    print(a + " & " + b + " are NOT anagrams.")