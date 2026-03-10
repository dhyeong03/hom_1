# Pro7(미래도시)
INF = int(1e9)
n,m = map(int, input().split())

graph = [ [INF]*(n+1) for _ in range(n+1)]

for _ in range(m) :
  com1, com2 = map(int,input().split())
  graph[com1][com2] = 1 
  graph[com2][com1] = 1 

x,k = map(int,input().split())

for middle in range(1,n+1) :
  for start in range(1,n+1) :
    for end in range(1,n+1) :
      graph[start][end] = min(graph[start][end], graph[start][middle]+graph[middle][end])

result = graph[1][k] + graph[k][x] 

if result >= INF : print(-1)
else : print(result)
