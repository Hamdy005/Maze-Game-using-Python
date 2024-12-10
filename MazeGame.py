class MazeGame:
  
    neighbour_rows = [-1, 0, 1, 0]
    neighbour_cols = [0, -1, 0, 1]
  
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
      
        init_path = [(0, 0)]
        visited = [[False for j in range(self.n)] for i in range(self.m)]
        queue = [[init_path, 0, 0]]
        
        while queue != []:
            
            curr_item = queue.pop(0)
            
            path = curr_item[0]
            row, col = curr_item[1:]
            
            visited[row][col] = True
            
            if self.escaped(row, col):
                return path
                
            for i in range(4):
              
                new_row = row + MazeGame.neighbour_rows[i]
                new_col = col + MazeGame.neighbour_cols[i]
               
                if self.is_valid(new_row, new_col) and self.maze[new_row][new_col] == ' ' and visited[new_row][new_col] == False:
                    
                    new_path = path + [(new_row, new_col)]
                    queue.append([new_path, new_row, new_col])

    
                    
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
        maze_game.draw_escape_path()
     
    else:
        print("The player can't escape the maze")
