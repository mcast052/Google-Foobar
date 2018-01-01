import collections 

class Node: 
    def __init__(self, wallRemoved, x, y, distance): 
        self.x = x
        self.y = y
        self.wallRemoved = wallRemoved 
        self.dist = distance
    
    
def isValid(x, y, width, height):
    if x >= 0 and x < height and y >=0 and y < width: 
        return True 
    else: 
        return False 

def nextNode(currNode, x, y, maze, q, visited): 
    if not isValid(x, y, len(maze[0]), len(maze)): 
        return
    
    nextNode = None
    if maze[x][y] == 0: 
        # print "0", x, y
        newNode = Node(currNode.wallRemoved, x, y, currNode.dist+1)
    elif not currNode.wallRemoved: 
        # print "1", x, y
        newNode = Node(True, x, y, currNode.dist+1)
    else: 
        return
        
    if visited[x][y] == 0: 
        q.append(newNode)
        
    return 
    
def answer(maze): 
    # Starting node (0, 0)
    start = Node(False, 0, 0, 0)
    q = collections.deque()
    q.append(start)
    visited = []
    for i in range(len(maze)): 
        arr = []
        for j in range(len(maze[0])): 
            arr.append(0)
        visited.append(arr)
    
    while q:
        curr = q.popleft()
        visited[curr.x][curr.y] = 1
        # print visited
        if curr.x == len(maze) - 1 and curr.y == len(maze[0]) - 1:
            return curr.dist + 1
        # Valid moves: 
        # Go up: (x-1, y) 
        # print "start: ", curr.x, curr.y
        nextNode(curr, curr.x-1, curr.y, maze, q, visited)
        # Go down: (x + 1, y) 
        # print curr.x+1, curr.y
        nextNode(curr, curr.x+1, curr.y, maze, q, visited)
        # Go left: (x, y-1) 
        # print curr.x, curr.y-1
        nextNode(curr, curr.x, curr.y-1, maze, q, visited)
        # Go right: (x, y + 1)
        # print curr.x, curr.y+1
        nextNode(curr, curr.x, curr.y+1, maze, q, visited)
    
print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
