class Point:
    def set_Coordinate(self,X,Y):
        self.X = X
        self.Y = Y
class New_Point(Point):
    def draw(self):
     print("Draw method")
     super().set_Coordinate(2,3)
     print(self.X,self.Y)
s = New_Point()
s.draw()
