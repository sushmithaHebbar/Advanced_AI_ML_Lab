def grid_layout(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                if j==n-1:
                    print(str('|'),end="")
                else:
                    print(str('|')+" -", end=" ")
            else:
                if j==n-1:
                    print(str('|'),end="")
                else:
                    print(str(0)+" |", end=" ")
        print()

def create_grid_matrix(n):
    """Create and return a 2D grid matrix instead of printing"""
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append('|')
                if j < n-1:
                    row.append('-')
            else:
                row.append('0')
                if j < n-1:
                    row.append('|')
        grid.append(row)
    
    # Add start position 'S' at the bottom-left area
    if n >= 4:
        grid[n-2][1] = 'S'
    
    # Add task positions 'T' at strategic locations
    if n >= 4:
        grid[1][n-2] = 'T'  # Top-right area
        grid[n-3][n-3] = 'T'
        grid[n-5][n-3]='T'  # Middle area
    
    return grid

if __name__ == "__main__":
    n=6
    grid_layout(n)