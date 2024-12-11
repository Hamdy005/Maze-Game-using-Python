class MazeGame:
  
    neighbour_rows = [-1, 0, 1, 0]
    neighbour_cols = [0, -1, 0, 1]
    path_grid = [[]]
    def __init__(self, maze):
    
        self.m = len(maze)
        self.n = len(maze[0])
        
        self.maze = maze
        self.__escape_path = self.__bfs()
        
    def is_valid(self, row, col):
        return row >= 0 and row < self.m and col >= 0 and col < self.n
    
    def escaped(self, row, col):
        return row == self.m - 1 and col == self.n - 1
    
    def can_escape(self):
        return self.__escape_path != None
    
    def get_escape_path(self):
        return self.__escape_path
    
    # To do   
    def draw_escape_path(self):
        pass
        
    
    def __bfs(self):
      
        init_path = [(0, 0,'s')]
        visited = [[False for j in range(self.n)] for i in range(self.m)]
        queue = [[init_path, 0, 0,'start']]
        
        while queue != []:
            
            curr_item = queue.pop(0)
            
            path = curr_item[0]
            row= curr_item[1]
            col = curr_item[2]
            
            visited[row][col] = True
            
            if self.escaped(row, col):
                self.path_grid=path
                return path
                
            for i in range(4):
              
                new_row = row + MazeGame.neighbour_rows[i]
                new_col = col + MazeGame.neighbour_cols[i]
               
                if self.is_valid(new_row, new_col) and self.maze[new_row][new_col] == ' ' and visited[new_row][new_col] == False:
                    x =""
                    if i == 0:
                        x = "|"
                        #print("up")
                    elif i == 1:
                        x = "-"
                        #print("left")
                    elif i == 2:
                        x = "|"
                        #print("down")
                    elif i == 3:
                        x = "-"
                        #print("right")
                    new_path = path + [(new_row, new_col,x)]
                    queue.append([new_path, new_row, new_col,x])

    
                    
if __name__ == "__main__":
    
    maze = [
      
    [' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', ' ', ' '],
    ['#', '#', '#', '#', '#', '#', '#', ' ']
    
]
    maze_game = MazeGame(maze)
    
    if maze_game.can_escape() == True:
      
        print("The player can escape the maze") 
        print("Escape path is:", maze_game.get_escape_path())

        for i in maze_game.path_grid:
            maze[i[0]][i[1]]=i[2]
        for i in maze:
            print(i)

    else:
        print("The player can't escape the maze")
