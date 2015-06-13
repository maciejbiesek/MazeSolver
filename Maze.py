import Point

class Maze:
    def __init__(self, point): # init maze
        self.start = point	     										    

    def convertInput(self, inputList): # convert input line to binary list
        matrix = []
        for line in inputList:
            singleLine = []
            for char in line:
                if char.isdigit():
                    singleLine.append(int(char))
            matrix.append(singleLine)
        self.mazeList = matrix

    def findEnd(self): # find end point's coordinates
        flag = False
        for i in range(0, len(self.mazeList)):
            for j in range(0, len(self.mazeList[i])):
                if self.mazeList[i][j] == 0 and i != self.start.x and j != self.start.y and (i in [0, len(self.mazeList)-1] or j in [0, len(self.mazeList[i])-1]):
                    self.end = Point.Point(i, j)
                    flag = True

        if flag:
            return True
        else:
            return False

    def passTheMaze(self): # find the shortest path between start and end points using BFS
        if(self.findEnd()):   
            queue = []
            self.mazeList[self.start.x][self.start.y] = "X"
            queue.append(self.start)

            while queue:
                point = queue.pop(0)
                
                if point == self.end: # extract points from found path
                    x = point.x
                    y = point.y
                    self.path = []
                    while self.mazeList[x][y] != "X":
                        # (Unfortunaly there's no switch-case statement in Python)
                        self.path.append(Point.Point(x, y))
                        case = self.mazeList[x][y]
                        if case == "t":
                            self.mazeList[x][y] = "X"
                            x += 1
                        elif case == "l":
                            self.mazeList[x][y] = "X"
                            y += 1
                        elif case == "b":
                            self.mazeList[x][y] = "X"
                            x -= 1
                        elif case == "r":
                            self.mazeList[x][y] = "X"
                            y -=1
                    self.path.append(self.start)
                    
                else: # find the path
                    # (BFS implementation)
                    if point.x - 1 >= 0 and self.mazeList[point.x - 1][point.y] == 0:
                        self.mazeList[point.x - 1][point.y] = "t"
                        queue.append(Point.Point(point.x - 1, point.y))
                    if point.y - 1 >= 0 and self.mazeList[point.x][point.y - 1] == 0:
                        self.mazeList[point.x][point.y - 1] = "l"
                        queue.append(Point.Point(point.x, point.y - 1))
                    if point.x + 1 < len(self.mazeList) and self.mazeList[point.x + 1][point.y] == 0:
                        self.mazeList[point.x + 1][point.y] = "b"
                        queue.append(Point.Point(point.x + 1, point.y))
                    if point.y + 1 < len(self.mazeList[point.x]) and self.mazeList[point.x][point.y + 1] == 0:
                        self.mazeList[point.x][point.y + 1] = "r"
                        queue.append(Point.Point(point.x, point.y + 1))
                    
        try: # display list of points' coordinates
            return "[{0}]".format(",".join(str(x) for x in reversed(self.path)))
        except:
            return "There's no escape, you'll never ever leave this place!"

    def __str__(self): # display the maze in a nice way
        mazeToDisplay = ""
        for line in self.mazeList:
            mazeToDisplay += str(line) + "\n"
        return mazeToDisplay
