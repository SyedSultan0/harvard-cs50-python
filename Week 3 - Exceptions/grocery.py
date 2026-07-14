l = []
d = {}
while True:
    try:
        a = input().lower().strip()
        l.append(a)
    except EOFError:
        break
for items in l:
    if items in d:
        d[items] +=1
    else:
        d[items] = 1

for key in sorted(d):
    print(d[key] , key.upper() )
