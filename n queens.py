#n queen problem
"""def Nqueen(board,r):
    if r==len(board):
        return True
    for c in range(len(board)):
        if issafe(board,r,c):
            board[r][c]="1"
            if Nqueen(board,r+1):
                return True
            board[r][c]='0'
    
def issafe(board,r,c):
    for i in range(r):
        if board[i][c]=="1":
            return False
    i,j=r,c
    while i>=0 and j<len(board):
        if board[i][j]=="1":
            return False
        i=i-1
        j=j+1
    i,j=r,c
    while i>=0 and j>=0:
        if board[i][j]=="1":
            return False
        i=i-1
        j=j-1
    return True
n=int(input("enter num of queens:"))
board=[["0" for i in range(n)] for j in range(n)]
if Nqueen(board,0):
    for i in board:
        print("".join(i))
else:
    print(False)"""

def Nqueen(board,r,r1,c1):
    if r==len(board):
        return 
    if r!=r1:
        for c in range(len(board)):
            if issafe(board,r,c,c1):
                board[r][c]="1"
                break
        
            board[r][c]='0'
        return Nqueen(board,r+1,r1,c1)

    else:
        Nqueen(board,r+1,r1,c1)
def issafe(board,r,c,c1):
    for i in range(r):
        if c==c1:
            return False
        if board[i][c]=="1":
            return False
        
    i,j=r,c
    while i>=0 and j<len(board):
        if board[i][j]=="1":
            return False
        i=i-1
        j=j+1
    i,j=r,c
    while i>=0 and j>=0:
        if board[i][j]=="1":
            return False
        i=i-1
        j=j-1
    return True
n=int(input("enter number of queens:"))
r1=int(input("num of rows:"))
c1=int(input("nim of columns:"))
board=[["0" for i in range(n)] for j in range(n)]
Nqueen(board,0,r1,c1)
for i in board:
        print("".join(i))
