k = int(input())
s = input()
 
if len(s) <= k:
    print(s)
else:
    ss = s[0:k]
    print(ss+"...")
