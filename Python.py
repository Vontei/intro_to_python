class Python:
    applicationCount = 0

    def __init__(self, isOO, isMultiThreaded, isStatic, isDynamic):
        self.isOO = isOO
        self.isMultiThreaded = isMultiThreaded
        self.isStatic = isStatic
        self.isDynamic = isDynamic
        Python.applicationCount += 1


    def displaySelf(self):
      print "Object Oriented: " + str(self.isOO)
      print "Multi Threaded: "  + str(self.isMultiThreaded)
      print "Staticly Typed: "  + str(self.isStatic)
      print "Dynamicly Typed: " + str(self.isDynamic)


class Point:
    def __init( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)
del pt1
del pt2
del pt3

project1 = Python(True,True,False,True)
project1.displaySelf()
