#----------------GRAPHS-----------------------

"""def dfs(n, d, l):
    if n not in l:
        print(n, end=" ")  
        l.append(n) 
        for ne in d[n]:
            dfs(ne, d, l)"""  
#d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
#l=[]
#dfs(5, d, l)

"""def all_path(x,l):
    l.append(x)
    if(x==2):
        print(l)
        l.pop()
        return
    for i in d[x]:
        if(i not in l):
            all_path(i,l)
    l.pop()
all_path(5,l)"""


"""sp = []

def dfs_shortest_path(x):
    global sp
    l.append(x)
    if x == 2:
        if not sp or len(l) < len(sp):
            sp = l.copy()
    else:
        for i in d[x]:
            if i not in l:
                dfs_shortest_path(i)
    l.pop()

dfs_shortest_path(5)
print(sp)"""

"""import heapq

# Graph with weights
d = {
    5: [(7, 1), (3, 4)],
    7: [(5, 1), (4, 2), (3, 3)],
    4: [(7, 2), (8, 1), (2, 5)],
    8: [(3, 2), (4, 1), (2, 3)],
    3: [(5, 4), (7, 3), (8, 2)],
    2: [(4, 5), (8, 3)]
}


def dijkstra(start, end):
    
    pq = [(0, start, [])]

    visited = set()
    
    while pq:
        (cost, current, path) = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        path = path + [current]
        
        if current == end:
            return (cost, path)
        
        for (neighbor, weight) in d[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))
    
    return (float('inf'), [])


cost, sp = dijkstra(5, 2)
print("Shortest path:", sp)
print("Total cost:", cost)"""

#-----------graph paths with costs  and count of paths----------------------------------
"""def  fun(d,x,e,c):
    l.append(x)
    if(x==e):
        print(l,c)
        l.pop()
        return c
    for i in d[x]:
        if i[0] not in l:
            fun(d,i[0],e,c+i[1])
    l.pop()"""

l=[]
d = {
    5: [(7, 1), (3, 4)],
    7: [(5, 1), (4, 2), (3, 3)],
    4: [(7, 2), (8, 1), (2, 5)],
    8: [(3, 2), (4, 1), (2, 3)],
    3: [(5, 4), (7, 3), (8, 2)],
    2: [(4, 5), (8, 3)]
}
#print(fun(d,5,2,0))

#------------------------least cost path---------------------------
"""def fun(d,x,e,c,m,l1):
    l.append(x)
    if(x==e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=fun(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
print(fun(d,5,2,0,9999,[]))


d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}"""
#----------------------------breadth first search 1406---------------------------------
"""def bfs(d,n):
    vi=[]
    q=[n]
    while(q):
        for i in d[q[0]]:#d[q[0]]
            if(i not in q and i not in vi):
                q.append(i)
        vi.append(q.pop(0))
        print(vi[-1])
d= {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
l=[]
bfs(d,5)"""

#----------------------dijakshtras algorithm 1406------------------------------------------

def dijkstra(s):
    d1={1:999,2:999,3:999,4:999,5:999}
    d1[s]=0
    v=[]
    q=[s]
    while(q):
        m=9999
        for i in q:
            if d1[i]<m:
                m=d1[i]
                s=i
        for i in d[s]:
            if i[0] not in v:
                if d1[i[0]]>(d1[s]+i[1]):
                    d1[i[0]]=d1[s]+i[1]
                if i[0] not in q:
                    q.append(i[0]) 
        v.append(s)  
        q.remove(s)
    return (d1)

d={1:[(2,2),(3,2),(4,1)],2:[(1,2),(4,2),(5,3)],3:[(1,2),(4,3)],4:[(1,1),(2,2),(3,3),(5,2)],5:[(2,3),(4,2)]}
print("Dijkstra:",dijkstra(1))



      

        
    
    





