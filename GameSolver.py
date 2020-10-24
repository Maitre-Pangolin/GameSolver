#possiblePosition=[[1,1],[6,1],[3,2],[2,3],[6,3],[4,4],[1,5],[3,5],[6,5],[5,6]] # Grid 1
#possiblePosition=[[5,1],[2,2],[4,2],[1,3],[2,3],[5,3],[4,4],[5,5],[1,6],[4,6]] # Grid 2
#possiblePosition=[[2,1],[5,1],[4,2],[1,3],[3,3],[6,3],[2,4],[1,5],[3,5],[5,5]] # Grid 3
#possiblePosition=[[3,1],[6,1],[2,3],[4,3],[1,4],[3,4],[6,4],[5,5],[2,6],[4,6]] # Grid 4
#possiblePosition=[[1,1],[5,1],[3,2],[1,3],[2,4],[4,4],[6,4],[3,5],[5,5],[4,6]] # Grid 5 WORKING 
#possiblePosition=[[1,1],[6,1],[2,2],[4,3],[2,4],[5,4],[1,5],[4,5],[6,5],[3,6]] # Grid 6  
#possiblePosition=[[1,1],[6,1],[3,2],[5,2],[4,3],[2,4],[4,4],[6,4],[1,5],[3,5]] # Grid 7
#possiblePosition=[[1,1],[6,1],[2,3],[4,3],[6,3],[3,4],[2,5],[4,5],[1,6],[5,6]] # Grid 8
#possiblePosition=[[5,1],[2,2],[1,3],[5,3],[6,4],[2,5],[4,5],[1,6],[3,6],[5,6]] # Grid 9
#possiblePosition=[[1,1],[3,1],[5,1],[2,3],[4,3],[6,3],[3,4],[4,4],[1,6],[4,6]] # Grid 10
#possiblePosition=[[1,1],[5,1],[1,3],[5,3],[3,4],[6,4],[1,5],[4,5],[2,6],[5,6]] # Grid 11
possiblePosition=[[5,1],[3,2],[2,3],[5,3],[2,4],[4,4],[6,4],[1,5],[3,5],[5,5]] # Grid 12
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
T2=T1.copy()
S1=[[0,1],[-1,1],[-1,2]]
S2=[[0,-1],[-1,-0],[-1,1]]
S3=S1.copy() # Other hole in -1 1 
S3other=S2.copy() # Other hole in -1 1
ValidHole=[-1,1] ######################### WIP
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

### Define wallClearance and faceClearance function to determine if pieceStates state are acceptable or not ( using index in arguments rather than full lists)

def wallClearance(pos_num,orientation_num,piece_num):
    for square in shapeOrientations[piece_num][orientation_num]:
        if square[0]+possiblePosition[pos_num][0] > 6 or square[0]+possiblePosition[pos_num][0] <1 or square[1]+possiblePosition[pos_num][1] > 6 or square[1]+possiblePosition[pos_num][1] < 1:
            return False    
    return True

def faceClearance(pos_num,orientation_num,piece_num):
    for square in shapeOrientations[piece_num][orientation_num]:
        for otherPos in possiblePosition:
            if square[0]+possiblePosition[pos_num][0] == otherPos[0] and square[1]+possiblePosition[pos_num][1] == otherPos[1]:
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
for state in fullTable[:]:
    printBoard(state)

#for t in fullTable:
#    print(t)

##### CREATE FULL BOARD STATE TABLE

#### check for repeated value in list function
#### create piece interference function argument should be (list of ocuppied square [1 to 36], pos_num,orientation_num,piece_num)
#### CREATE STATE ANALYSIS FUNCTION (return list of bool of length len(fullStates) base on piece re)
#### Create a possible state list by filtering using bool list
#### Create a display state function






