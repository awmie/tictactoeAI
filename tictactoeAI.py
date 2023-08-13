def printBoard(board):
    print('Current State of the board:\n\n')
    for i in range(9):
        if i > 0 and i%3==0:
            print("\n")
        if board[i]==0:
            print("_ ",end=" ")
        if board[i]==-1:
            print("X ",end=" ")
        if board[i]==1:
            print("O ",end=" ")
    print('\n\n')

def user1turn(board):
    pos = int(input("Enter X's position from 1,2,3...9:"))
    if board[pos-1]!=0:
        print('Invalid move!!')
        exit(0)
    board[pos-1] = -1 #for x player it is -1

def user2turn(board):
    pos = int(input("Enter O's position from 1,2,3...9:"))
    if board[pos-1]!=0:
        print('Invalid move!!')
        exit(0)
    board[pos-1] = 1 #for O player it is +1
    
def minmax(board, player):
    x = analyzeBoard(board)
    if x != 0:
        return x*player
    pos = -1
    value = -2
    for i in range(9):
        if board[i]==0:
            board[i] = player
            score = -minmax(board, -1*player)
            board[i] = 0
            if score > value:
                value = score
                pos=i
    return 0 if pos == -1 else value
                
def compTurn(board):
    pos = -1
    value = -2
    for i in range(9):
        if board[i]==0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos=i
    board[pos]=1
def analyzeBoard(board):
        superList = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in range(8):
            if board[superList[i][0]] != 0 and board[superList[i][0]]==board[superList[i][1]] and board[superList[i][0]]== board[superList[i][2]]:
                return board[superList[i][0]]
        return 0
    
def main():
    choice = int(input('Enter 1:Single Player\nEnter 2:Multiplayer'))
    board = [0,0,0,0,0,0,0,0,0]
    if choice == 1:
        #againt ai
        print("\n--Computer(O) vs You(X)--")
        player = int(input('Enter 1: play first\nEnter 2: play 2nd'))
        for i in range(9):
            if analyzeBoard(board)!=0:
                break
            if (i+player)%2==0:
                compTurn(board)
            else:
                printBoard(board)
                user1turn(board)
    else:
        for i in range(9):
            if analyzeBoard(board)!=0:
                break
            if i%2==0:
                user1turn(board)
            else:
                printBoard(board)
                user2turn(board)
            
    x = analyzeBoard(board)
    if x==0:
        printBoard(board)
        print("It's a tie!")
    if x==-1:
        printBoard(board)
        print("player X wins!")
    if x==1:
        printBoard(board)
        print("player O wins")
        
main()