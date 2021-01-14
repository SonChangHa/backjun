import sys
def put():
    return list(map(int,input().split()))
input = sys.stdin.readline

st = []

nlist = []
stlist = []

n = int(input())

last = 1

for _ in range(n):

    nlist.append(int(input()))

#try 안쓰고 괜히 조건으로 풀라하면 오히려 시간초과남
try:
    for i in range(n):

        k = nlist[i]

        while k >= last:
            st.append(last)
            last += 1
            stlist.append("+")

        else:
            while True:
                a = st.pop()
                if a == k:
                    stlist.append("-")
                    break
except:
    print("NO")
    sys.exit()

for t in stlist:
    print(t)
