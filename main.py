import random

class MazeGame:
    def __init__(self, size=10):
        self.size = size
        self.maze = [['#' for _ in range(size)] for _ in range(size)]
        self.player_pos = (1, 1)
        self.exit_pos = (size - 2, size - 2)
        self.generate_maze()
    
    def generate_maze(self):
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                self.maze[i][j] = '.' if random.random() > 0.2 else '#'
        self.maze[self.player_pos[0]][self.player_pos[1]] = 'P'
        self.maze[self.exit_pos[0]][self.exit_pos[1]] = 'E'
    
    def print_maze(self):
        for row in self.maze:
            print(" ".join(row))
    
    def move_player(self, direction):
        x, y = self.player_pos
        moves = {'W': (-1, 0), 'S': (1, 0), 'A': (0, -1), 'D': (0, 1)}
        if direction in moves:
            dx, dy = moves[direction]
            new_x, new_y = x + dx, y + dy
            if self.maze[new_x][new_y] != '#':
                self.maze[x][y] = '.'
                self.player_pos = (new_x, new_y)
                if self.player_pos == self.exit_pos:
                    print("You escaped the maze! 🎉")
                    return True
                self.maze[new_x][new_y] = 'P'
        return False

def main():
    game = MazeGame()
    while True:
        game.print_maze()
        move = input("Move (WASD): ").upper()
        if move in ['W', 'A', 'S', 'D']:
            if game.move_player(move):
                break
        else:
            print("Invalid move. Use W, A, S, or D.")

if __name__ == "__main__":
    main()
