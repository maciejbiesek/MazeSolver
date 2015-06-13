class Point:
    def __init__(self, x, y): # init point
        self.x = x	     											#pozycja x obiektu
        self.y = y
        
    def __str__(self): # display the point in a nice way
        return "[%d,%d]" % (self.x, self.y)

    def __eq__(self, point): # check whether two points are equal
        return self.x == point.x and self.y == point.y
