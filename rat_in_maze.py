import copy

class RatMaze:
    def __init__(self):
        self.paths = []

    def rat_maze(self,N,maze):
        pos = [0,0]
        self.backtrack(N,maze,pos,None,'')
        print(self.paths)
        if len(self.paths) > 0 :
            return True
        else:
            return False
    
    def direction(self, N, maze, current_pos):
        row, col = current_pos[0], current_pos[1]
        up = row > 0 and maze[row-1][col] == 1
        down = row < N-1 and maze[row+1][col] == 1
        left = col > 0 and maze[row][col-1] == 1
        right = col < N-1 and maze[row][col+1] == 1
        return up,down,left,right
    
    def backtrack(self, N, maze, current_pos, prev_pos, current_path):
        # current_pos[0] : row, current_pos[1] : col
        
        # check if game ended
        if current_pos[0] == N-1 and current_pos[1] == N-1:
            self.paths.append(current_path) 
        
        if prev_pos: 
            maze[prev_pos[0]][prev_pos[1]] = 0 # update prev position = 0
        
        original_maze = copy.deepcopy(maze) # store the original maze configuration
        
        up, down, left, right = self.direction(N, maze,current_pos) # find which directions we can go

        if up == True:
            self.backtrack(
                           N,
                           maze,
                           [current_pos[0]-1,current_pos[1]],
                           current_pos,
                           current_path=current_path+'U')
        
        # restore maze configuration if changed
        maze = copy.deepcopy(original_maze)

        if down == True:
            self.backtrack(
                           N,
                           maze,
                           [current_pos[0]+1,current_pos[1]],
                           current_pos,
                           current_path=current_path+'D')
        
        # restore maze configuration if changed
        maze = copy.deepcopy(original_maze)       

        if left == True:
            self.backtrack(
                           N,
                           maze,
                           [current_pos[0],current_pos[1]-1],
                           current_pos,
                           current_path=current_path+'L')
        
        # restore maze configuration if changed
        maze = copy.deepcopy(original_maze)      
          
        if right == True:
            self.backtrack(
                           N,
                           maze,
                           [current_pos[0],current_pos[1]+1],
                           current_pos,
                           current_path=current_path+'R')
        return
    
solution = RatMaze()
res = solution.rat_maze(4,[
    [1,0,0,0],
    [1,1,0,1],
    [1,1,0,0],
    [0,1,1,1]
])
# res = solution.rat_maze(1,[
#     [1],
# ])
# res = solution.rat_maze(2,[
#     [1,0],
#     [1,0]

# ])
print(res)


# Time complexity: O(4^(N^2))
# Space complexity: O(N^2)