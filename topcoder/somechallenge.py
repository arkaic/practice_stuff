class ABCPath:
    def length(self, grid):
        if len(grid) == 0:
            return 0
        print(grid)
        if not isinstance(grid, list):
            newgrid = []
            for word in grid:
                newgrid.append(word)
            grid = newgrid
        length = len(grid)
        width = len(grid[0])

        print(grid)
        
        count = 0
        for j, word in enumerate(grid):
            for i, c in enumerate(word):
                if c == 'A':
                    current_ascii = ord('A')
                    stack = [(c, i, j)]
                    while stack:
                        a, x, y = stack.pop()
                        current_ascii = ord(a)
                        print("current={}, ({},{})".format(a, x, y))
                        end_not_reached = False
                        if y - 1 > 0:
                            if ord(grid[y-1][x]) == current_ascii + 1:
                                stack.append((grid[y-1][x], x, y-1))
                                end_not_reached = True
                            if x - 1 > 0 and ord(grid[y-1][x-1]) == current_ascii + 1:
                                stack.append((grid[y-1][x-1], x-1, y-1))
                                end_not_reached = True
                            if x + 1 < len(grid[0]) and ord(grid[y-1][x+1]) == current_ascii + 1:
                                stack.append((grid[y-1][x+1], x+1, y-1))
                                end_not_reached = True

                        lower_y = None
                        left_x = None
                        right_x = None
                        if y + 1 < len(grid):
                            right_y = y + 1
                        if x - 1 > 0:
                            left_x = x - 1
                        if x + 1 < len(grid[0]):
                            right_x = x + 1

                        if lower_y is not None:
                            if ord(grid[lower_y][x]) == current_ascii + 1:
                                stack.append((grid[lower_y][x], x, lower_y))
                                end_not_reached = True
                            if left_x is not None and ord(grid[lower_y][left_x]) == current_ascii + 1:
                                stack.append((grid[lower_y][left_x], left_x, lower_y))
                                end_not_reached = True
                            if right_x is not None and ord(grid[lower_y][right_x]) == current_ascii + 1:
                                stack.append((grid[lower_y][right_x], right_x, lower_y))
                                end_not_reached = True

                        if left_x is not None and ord(grid[y][left_x]) == current_ascii + 1:
                            stack.append((grid[y][left_x], left_x, y))
                            end_not_reached = True
                        if right_x is not None and ord(grid[y][right_x]) == current_ascii + 1:
                            stack.append((grid[y][right_x], right_x, y))
                            end_not_reached = True

                        if not end_not_reached:
                            # end is reached
                            print("end reached")
                            if current_ascii - ord('A') + 1 > count:
                                count = current_ascii - ord('A') + 1
        return count

        
if __name__ == '__main__':
    a = ABCPath()
    arg = ["ABE", 
           "CFG", 
           "BDH", 
           "ABC"]

    print("arg {}".format(arg))
    print(a.length(arg))