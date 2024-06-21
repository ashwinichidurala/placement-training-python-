def tree_fire(matrix,r,c,n):
    if r<0 or c<0 or r>=n or c>=n or matrix[r][c]!=1:
        return 
    if matrix[r][c]==1:
        matrix[r][c]=2
        tree_fire(matrix,r-1,c,n)
        tree_fire(matrix,r,c+1,n)
        tree_fire(matrix,r+1,c,n)
        tree_fire(matrix,r,c-1,n)
    
    
def count(matrix):
    c1=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==1:
                c1=c1+1
    return c1
        
n=int(input())
r=int(input("enter row value:"))
c=int(input("enter column value:"))
matrix=[]
c1=0
for i in range(n):
    li=[]
    for j in range(n):
        inp=int(input())
        li.append(inp)
    matrix.append(li)
tree_fire(matrix,r-1,c-1,n)
print("count of trees:",count(matrix))
print(matrix)

                    
                    


