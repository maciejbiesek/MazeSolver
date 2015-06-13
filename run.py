import sys
import Point
import Maze

inputList = []

while True:
    singleLine = input()
    if singleLine == "]":
        break
    elif singleLine == "[":
        continue
    else:
        inputList.append(singleLine)

startLine = input()
startList = [int(x) for x in startLine if x.isdigit()] # extract start point's coordinates

startPoint = Point.Point(startList[0], startList[1]) # init start point
maze = Maze.Maze(startPoint) # init maze
maze.convertInput(inputList) # convert input to binary list

print(maze.passTheMaze()) # find the shortest path between start and end points
