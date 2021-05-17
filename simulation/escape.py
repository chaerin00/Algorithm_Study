def print_map(map):
  for r in range(R):
    for c in range(C):
        print(map[r][c],end='')
    print('\n')  

R,C=map(int,input().split())
print(R,C)
map=[]
for r in range(R):
    row=[]
    for c in range(C):
        row.append('.')
    map.append(row)

indexD_x,indexD_y=0,0
indexS_x,indexS_y=R-1,C-1
map[indexD_x][indexD_y]='D'
map[indexS_x][indexS_y]='S'

waters=[[0,2]]
dx=[0,-1,0,1]
dy=[1,0,-1,0]

for water in waters:
    x,y=water[0],water[1]
    map[x][y]='*'
    print_map(map)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<R and ny>=0 and ny<C and map[nx][ny]=='.':
            new=[nx,ny]
            waters.append(new)
            map[nx][ny]='*'

print_map(map)

shortcut=abs(indexD_x-indexS_x)+abs(indexD_y-indexS_y)
print(shortcut)
