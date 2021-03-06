#possiblePosition=[[1,1],[6,1],[3,2],[2,3],[6,3],[4,4],[1,5],[3,5],[6,5],[5,6]] # Grid 1
#possiblePosition=[[5,1],[2,2],[4,2],[1,3],[2,3],[5,3],[4,4],[5,5],[1,6],[4,6]] # Grid 2
possiblePosition=[[2,1],[5,1],[4,2],[1,3],[3,3],[6,3],[2,4],[1,5],[3,5],[5,5]] # Grid 3
#possiblePosition=[[3,1],[6,1],[2,3],[4,3],[1,4],[3,4],[6,4],[5,5],[2,6],[4,6]] # Grid 4
#possiblePosition=[[1,1],[5,1],[3,2],[1,3],[2,4],[4,4],[6,4],[3,5],[5,5],[4,6]] # Grid 5 WORKING 
#possiblePosition=[[1,1],[6,1],[2,2],[4,3],[2,4],[5,4],[1,5],[4,5],[6,5],[3,6]] # Grid 6  
#possiblePosition=[[1,1],[6,1],[3,2],[5,2],[4,3],[2,4],[4,4],[6,4],[1,5],[3,5]] # Grid 7
#possiblePosition=[[1,1],[6,1],[2,3],[4,3],[6,3],[3,4],[2,5],[4,5],[1,6],[5,6]] # Grid 8
#possiblePosition=[[5,1],[2,2],[1,3],[5,3],[6,4],[2,5],[4,5],[1,6],[3,6],[5,6]] # Grid 9
#possiblePosition=[[1,1],[3,1],[5,1],[2,3],[4,3],[6,3],[3,4],[4,4],[1,6],[4,6]] # Grid 10
#possiblePosition=[[1,1],[5,1],[1,3],[5,3],[3,4],[6,4],[1,5],[4,5],[2,6],[5,6]] # Grid 11
#possiblePosition=[[5,1],[3,2],[2,3],[5,3],[2,4],[4,4],[6,4],[1,5],[3,5],[5,5]] # Grid 12
#possiblePosition=[[2,1],[6,1],[1,2],[5,2],[2,4],[6,4],[4,5],[1,6],[3,6],[5,6]] # Grid 19

#possiblePosition=[[x+1,y+1] for x in range(6) for y in range(6)] # all pos
#possiblePosition=[[1,1],[4,1],[1,3],[3,3],[6,3],[4,4],[6,4],[1,5],[2,5],[5,5]] #mine
#possiblePosition=[[1,1],[1,2],[4,2],[6,2],[2,3],[3,3],[1,4],[6,4],[4,5],[4,6]] #mine 2
#possiblePosition=[[3,1],[5,2],[1,3],[6,3],[2,4],[4,4],[1,5],[3,5],[6,5],[6,6]] #mine 3
#possiblePosition=[[2,1],[6,1],[3,2],[5,2],[1,4],[3,4],[6,4],[2,5],[3,6],[6,6]] # rama

# Pieces geometry definition (note that 0,0 represents the piece hole)

L1=[[-1,0],[-1,1],[-1,2]]
L2=[[0,-1],[0,-2],[1,-2]]
L3=[[1,0],[0,-1],[0,-2]]
L4=[[0,1],[0,-1],[1,-1]]
T1=[[-1,0],[-2,0],[-1,1]]
#T2=T1.copy() # Wrong T2 piece (what we physically have)
T2=[[0,1],[-1,1],[1,1]] # Correct T2 piece to solve the game (what we should have)
S1=[[0,1],[-1,1],[-1,2]]
S2=[[0,-1],[-1,-0],[-1,1]]
S3=S1.copy() # Other hole in -1 1 
S3other=S2.copy() # Other hole in -1 2
validationHole=[[-1,1] ,[-1,2]]
shapes=[L1,L2,L3,L4,T1,T2,S1,S2,S3]

# Create all pieceStates orientation from shapes

shapeOrientations=[]
for shape in shapes:
    shapeOrientations.append([
         [ [shape[i][0],shape[i][1]] for i in range(3)]   , # X Y 
         [ [-shape[i][0],shape[i][1]] for i in range(3)]  ,  # -X Y
         [ [-shape[i][0],-shape[i][1]] for i in range(3)] , # -X-Y
         [ [shape[i][0],-shape[i][1]] for i in range(3)]  , # X -Y
         [ [shape[i][1],shape[i][0]] for i in range(3)]   , # Y X
         [ [-shape[i][1],shape[i][0]] for i in range(3)]  ,  #  -Y X
         [ [-shape[i][1],-shape[i][0]] for i in range(3)] , # -Y-X
         [ [shape[i][1],-shape[i][0]] for i in range(3)]   #  Y -X
    ])
S3OtherOrientation=[]
S3OtherOrientation.append([
         [ [S3other[i][0],S3other[i][1]] for i in range(3)]   , # X Y 
         [ [-S3other[i][0],S3other[i][1]] for i in range(3)]  ,  # -X Y
         [ [-S3other[i][0],-S3other[i][1]] for i in range(3)] , # -X-Y
         [ [S3other[i][0],-S3other[i][1]] for i in range(3)]  , # X -Y
         [ [S3other[i][1],S3other[i][0]] for i in range(3)]   , # Y X
         [ [-S3other[i][1],S3other[i][0]] for i in range(3)]  ,  #  -Y X
         [ [-S3other[i][1],-S3other[i][0]] for i in range(3)] , # -Y-X
         [ [S3other[i][1],-S3other[i][0]] for i in range(3)]   #  Y -X
    ])
validationHoleOrientation=[]
for config in validationHole:
     validationHoleOrientation.append([
            [config[0],config[1]]    , # X Y 
            [-config[0],config[1]]  ,  # -X Y
            [-config[0],-config[1]] , # -X-Y
            [config[0],-config[1]]  , # X -Y
            [config[1],config[0]]   , # Y X
            [-config[1],config[0]]  ,  #  -Y X
            [-config[1],-config[0]] , # -Y-X
            [config[1],-config[0]]   #  Y -X
    ])

def printPiece(piece_num,orientation_num):
    indexToFill=[]
    for y in range(5):
        temp2=[]
        for x in range(5):
            isFound=False
            for square in shapeOrientations[piece_num][orientation_num]:          
                if x+1==square[0]+3 and y+1==square[1]+3:
                    isFound=True              
            if isFound:
                temp2.append(str(orientation_num+1))
            elif x+1==3 and y+1==3:
                temp2.append("0")
            else:
                temp2.append("x")    
        indexToFill.append(" ".join(temp2)) 
    print("Piece :",str(piece_num+1)," Orientation :",str(orientation_num))  
    for line in indexToFill[::-1]:
        print(line) 
    print("\n") 

def wallClearance(pos_num,orientation_num,piece_num):
    for square in shapeOrientations[piece_num][orientation_num]:
        if square[0]+possiblePosition[pos_num][0] > 6 or square[0]+possiblePosition[pos_num][0] <1 or square[1]+possiblePosition[pos_num][1] > 6 or square[1]+possiblePosition[pos_num][1] < 1:
            return False    
    return True

def faceClearance(pos_num,orientation_num,piece_num):
    for square in shapeOrientations[piece_num][orientation_num]:
        for otherPos in possiblePosition:
            if square[0]+possiblePosition[pos_num][0] == otherPos[0] and square[1]+possiblePosition[pos_num][1] == otherPos[1]:
                if piece_num ==8 and square == shapeOrientations[piece_num][orientation_num][2]:
                    return True
                else:
                    return False
    return True

def boardStateValidation(combinedStates):
    boardSquareOccupied=[]
    for index,pieceStates in enumerate(combinedStates):
        x_o=possiblePosition[pieceStates[0]][0]
        y_o=possiblePosition[pieceStates[0]][1]
        boardSquareOccupied.append(x_o+(y_o-1)*6)  #Indexage en ligne de la grille 6x6 de coordonnes d'origine (1,1)
        for square in shapeOrientations[index][pieceStates[1]]:
            x=x_o+square[0]
            y=y_o+square[1]
            boardSquareOccupied.append(x+(y-1)*6)           
            if len(boardSquareOccupied) != len( set(boardSquareOccupied)) : # Use a set to determine if there is any duplicates
                return False
    return True

def printBoard(combinedStates):
    boardline=["0" for x in range(6*6)]
    origins=['a','b','c','d','e','f','g','h','i']
    filling=['A','B','C','D','E','F','G','H','I']
    for piece,state in enumerate(combinedStates):
        pos = state[0]
        ori = state[1]
        x=possiblePosition[pos][0]
        y=possiblePosition[pos][1]
        loc=x+6*(y-1)
        boardline.pop(loc-1)
        boardline.insert(loc-1,origins[piece])
        for square in shapeOrientations[piece][ori]:
            x=possiblePosition[pos][0]+square[0]
            y=possiblePosition[pos][1]+square[1]
            loc=x+6*(y-1)
            boardline.pop(loc-1)
            boardline.insert(loc-1,filling[piece])    
    board=[]
    for y in range(6):
        temp=[]
        for x in range(6):
            loc=x+6*(y) 
            temp.append(boardline[loc])
        board.append(" ".join(temp))
    for line in board[::-1]:
        print(line)
    print("\n")

def boardStateLastHoleClearance(boardState,config):
    lastPiecePos=boardState[8][0]
    lastPieceOri=boardState[8][1]
    secondHolePos=[possiblePosition[lastPiecePos][0] + validationHoleOrientation[config][lastPieceOri][0],possiblePosition[lastPiecePos][1] + validationHoleOrientation[config][lastPieceOri][1]]
    for pos in possiblePosition:
        if secondHolePos[0]==pos[0] and secondHolePos[1]==pos[1]:
            return True
        else:
            return False

# Create all possible state for a piece (position , orientation)

statePossible = [[(pos,ori) for pos in range(len(possiblePosition)) for ori in range(len(shapeOrientations[0])) if wallClearance(pos,ori,piece) and faceClearance(pos,ori,piece)] for piece in range(len(shapeOrientations))] # In love with comprehension list 

# Create full board states combination

fullTable = [[firstPieceStates] for firstPieceStates in statePossible[0]]
for pieceStates in statePossible[1:]:
    temp = []
    for combinedState in fullTable:
        for states in pieceStates:
            temp.append(combinedState+[states])
    fullTable = list(filter(boardStateValidation,temp))

print("number of combination for first S piece configuration: :",len(fullTable))

for state in fullTable:
    if not boardStateLastHoleClearance(state,0):
        fullTable.remove

for state in fullTable:
    printBoard(state)

shapeOrientations[8]=S3OtherOrientation[0]

statePossible[8]=[(pos,ori) for pos in range(len(possiblePosition)) for ori in range(len(shapeOrientations[0])) if wallClearance(pos,ori,8) and faceClearance(pos,ori,8)]

fullTable = [[firstPieceStates] for firstPieceStates in statePossible[0]]
for pieceStates in statePossible[1:9]:
    temp = []
    for combinedState in fullTable:
        for states in pieceStates: 
            temp.append(combinedState+[states])
    fullTable = list(filter(boardStateValidation,temp))

for state in fullTable:
    if not boardStateLastHoleClearance(state,1):
        fullTable.remove(state)

print("number of combination for second S piece configuration:",len(fullTable))
for state in fullTable[:]:
    printBoard(state)