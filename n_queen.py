def printboard(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                print('Q',end=" ")
            else:
                print('-',end=" ")
        print("\n")
    print("\n")

def isSafe(board,row,col,n):
    i=row
    j=col
    while j>=0:
        if board[i][j]:
            return False
        j-=1

    i=row
    j=col
    while j>=0 and i>=0:
        if board[i][j]:
            return False
        j-=1
        i-=1
    
    i=row
    j=col
    while i<n and j>=0:
        if board[i][j]:
            return False
        j-=1
        i+=1

    return True

def solve(board,col,n):
    if(col>=n):
        printboard(board,n)
        return True
    else:
        for row in range(n):
            if isSafe(board,row,col,n):
                board[row][col]=1
                solve(board,col+1,n)
                board[row][col]=0  
        
if __name__=="__main__":
    n=int(input("Enter size :"))
    board=[]
    for row in range(n):
        row=[0]*n
        board.append(row)
    index=int(input("Enter row to place 1st queen"))
    board[index][0]=1
    if (solve(board,1,n))==False:
        print("Solution not exist")
