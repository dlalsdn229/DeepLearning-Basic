import copy

def Left(X):
    X = copy.copy(X)
    idx = X.index(0)
    if idx % 3 == 0:
        return X
    else:        
        X[idx] = X[idx-1]
        X[idx-1] = 0
        return X

def Right(X):
    X = copy.copy(X)
    idx = X.index(0)
    if idx % 3 == 2:
        return X
    else:        
        X[idx] = X[idx+1]
        X[idx+1] = 0
        return X

def Up(X):
    X = copy.copy(X)
    idx = X.index(0)
    if idx < 3:
        return X
    else:        
        X[idx] = X[idx-3]
        X[idx-3] = 0
        return X

def Down(X):
    X = copy.copy(X)
    idx = X.index(0)
    if idx > 5:
        return X
    else:        
        X[idx] = X[idx+3]
        X[idx+3] = 0
        return X

#깊이 우선 탐색
def depth():
    open = []
    closed = []

    start = [3,1,2,4,0,5,6,7,8]
    goal = [0,1,2,3,4,5,6,7,8]

    open = [start]
    X=[]
    while len(open) != 0:
    
        X = open.pop(0) #open list의 앞에서 꺼내기    
    
        if X == goal:
            print("success")
            print("X =",X)
            break
        else:        
            #1 자식노드 생성
            children=[]#자식 리스트 초기화
            children.insert(0,Left(X))        
            children.insert(0,Right(X))
            children.insert(0,Up(X))
            children.insert(0,Down(X))
        
            #2 X를 closed에 추가
            closed.insert(0,X)
        
            #3 X의 자식노드가 Open이나 Closed에 있으면 버린다.
            children = [x for x in children if not x in open]
            children = [x for x in children if not x in closed]
        
            #4 남은 자식노드 open의 처음에 추가
            for i in range(0,len(children)):
                open.insert(0,children.pop())

        
            if len(closed) % 1000 == 0:
                print("open =",len(open))
                print("closed =",len(closed))

#너비 우선 탐색
def width():
    open = []
    closed = []

    start = [3,1,2,4,0,5,6,7,8]
    goal = [0,1,2,3,4,5,6,7,8]

    open = [start]
    X=[]
    while len(open) != 0:
    
        X = open.pop(0) #open list의 앞에서 꺼내기    
        
        if X == goal:
            print("success")
            print("X =",X)
            print("goal =",goal)
            break
        else:        
            #1 자식노드 생성
            children=[]#자식 리스트 초기화
            children.insert(0,Left(X))        
            children.insert(0,Right(X))
            children.insert(0,Up(X))
            children.insert(0,Down(X))
        
            #2 X를 closed에 추가
            closed.insert(0,X)
        
            #3 X의 자식노드가 Open이나 Closed에 있으면 버린다.
            children = [x for x in children if not x in open]
            children = [x for x in children if not x in closed]
        
            #4 남은 자식노드 open의 뒤에 추가
            for i in range(0,len(children)):
                open.append(children.pop(0))
           
            print("open =",len(open))
            print("closed =",len(closed))

width()
    
        
