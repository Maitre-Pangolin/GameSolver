
possiblePosition=[[1,1],[6,1],[3,2],[2,3],[6,3],[4,4],[1,5],[3,5],[6,5],[5,6]]

# Pieces geometry definition (note that 0,0 represents the piece hole)

L1=[[-1,0],[-1,1],[-1,2]]
L2=[[0,-1],[0,-2],[1,-2]]
L3=[[1,0],[0,-1],[0,-2]]
L4=[[0,1],[0,-1],[1,-1]]
T1=[[-1,0],[-2,0],[-1,1]]
T2=T1.copy()
S1=[[0,1],[-1,1],[-1,2]]
S2=[[0,-1],[-1,-0],[-1,1]]
#S3=S1.copy() # Other hole in -1 1 
S3=S2.copy() # Other hole in -1 1
ValidHole=[-1,1] ######################### WIP
shapes=[L1,L2,L3,L4,T1,T2,S1,S2,S3]

# Create all pieceStates orientation from shapes

shapeOrientations=[]
for shape in shapes:
    shapeOrientations.append([
         [   [shape[0][0],shape[0][1]] , [shape[1][0],shape[1][1]] , [shape[2][0],shape[2][1]]   ], # X Y
         [   [-shape[0][0],shape[0][1]] , [-shape[1][0],shape[1][1]] , [-shape[2][0],shape[2][1]]   ],  # -X Y
         [   [-shape[0][0],-shape[0][1]] , [-shape[1][0],-shape[1][1]] , [-shape[2][0],-shape[2][1]]   ], # -X-Y
         [   [shape[0][0],-shape[0][1]] , [shape[1][0],-shape[1][1]] , [shape[2][0],-shape[2][1]]   ], # X -Y
         [   [shape[0][1],shape[0][0]] , [shape[1][1],shape[1][0]] , [shape[2][1],shape[2][0]]   ], # Y X
         [   [-shape[0][1],shape[0][0]] , [-shape[1][1],shape[1][0]] , [-shape[2][1],shape[2][0]]   ],  #  -Y X
         [   [-shape[0][1],-shape[0][0]] , [-shape[1][1],-shape[1][0]] , [-shape[2][1],-shape[2][0]]   ], # -Y-X
         [   [shape[0][1],-shape[0][0]] , [shape[1][1],-shape[1][0]] , [shape[2][1],-shape[2][0]]   ], #  Y -X
    ])

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


# Create all possible state for a piece (position , orientation)

statePossible = [[(pos,ori) for pos in range(len(possiblePosition)) for ori in range(len(shapeOrientations[0])) if wallClearance(pos,ori,piece) and faceClearance(pos,ori,piece)] for piece in range(len(shapeOrientations))] # In love with comprehension list 

# Create full board states combination

fullTable = [[firstPieceStates] for firstPieceStates in statePossible[0]]

for pieceStates in statePossible[1:2]:
    temp = []
    for combinedState in fullTable:
        for states in pieceStates:
            temp.append(combinedState+[states])
    fullTable = temp[:]

# FULL TABLE might be too big too derive entirely / try to build in state validation and table cleaning after fullTable assignment 

#for t in fullTable:
#    print(t)

##### CREATE FULL BOARD STATE TABLE

#### check for repeated value in list function
#### create piece interference function argument should be (list of ocuppied square [1 to 36], pos_num,orientation_num,piece_num)
#### CREATE STATE ANALYSIS FUNCTION (return list of bool of length len(fullStates) base on piece re)
#### Create a possible state list by filtering using bool list
#### Create a display state function






