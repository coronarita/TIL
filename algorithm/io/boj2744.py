import sys
s = sys.stdin.readline()
res = ''
for st in s :
    if st.islower():
        res += st.upper()
    else :
        res += st.lower()
        
print(res)