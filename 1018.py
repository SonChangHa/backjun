import sys, math, copy
def put():
    return list(map(int,input().split()))
#input = sys.stdin.readline


#2차원 배열은 m,n로 접근해야함 li[m][n] 가로 n 세로 m

n, m = put()
li = []

for _ in range(n):
    k = list(input())
    li.append(k)

ch = [[False for i in range(m)]for j in range(n)]

ch2 = copy.deepcopy(ch)

for i in range(n):
    for j in range(m):
        if i == 0 or i % 2 == 0:
            if j == 0 or j % 2 == 0:
                if li[i][j] != 'W':
                    ch[i][j] = True
            else:
                if li[i][j] != 'B':
                    ch[i][j] = True
        else:
            if j == 0 or j % 2 == 0:
                if li[i][j] != 'B':
                    ch[i][j] = True
            else:
                if li[i][j] != 'W':
                    ch[i][j] = True

for i in range(n):
    for j in range(m):
        if i == 0 or i % 2 == 0:
            if j == 0 or j % 2 == 0:
                if li[i][j] != 'B':
                    ch2[i][j] = True
            else:
                if li[i][j] != 'W':
                    ch2[i][j] = True
        else:
            if j == 0 or j % 2 == 0:
                if li[i][j] != 'W':
                    ch2[i][j] = True
            else:
                if li[i][j] != 'B':
                    ch2[i][j] = True


che = 65
for x in range(n-7):
    for y in range(m-7):
        che2 = 0
        for k in [row[y:y+8] for row in ch[x:x+8]]:
            che2 += k.count(True)

        if che > che2:
            che = che2

for x in range(n-7):
    for y in range(m-7):
        che2 = 0
        for k in [row[y:y+8] for row in ch2[x:x+8]]:
            che2 += k.count(True)

        if che > che2:
            che = che2


print(che)
            

