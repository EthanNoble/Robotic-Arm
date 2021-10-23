import math

class Vector:
    """
    A vector class initialized with a magnitude and angle
    containing the cartesian equivalent.
    """
    __precision = None
    #Polar
    __magnitude = None
    __angle = None
    #Cartesian
    __x = None
    __y = None

    def __init__(self, magnitude, angle, precision=4):
        '''
        Construct a new vector object with a length (magnitude)
        and an angle (measured in radians) with a default precision
        of 4.
        '''
        self.__magnitude = magnitude
        self.__angle = round(angle, precision)
        self.__precision = precision
        self.__calculateX()
        self.__calculateY()
    
    def setAngle(self, theta):
        '''
        Set the vector angle to theta (in radians) with cartesian
        coordinates adjusted appropriately.
        '''
        self.__angle = theta
        self.__calculateX()
        self.__calculateY()
    
    def printVector(self):
        print("Vector - \n\tMagnitude: " + str(self.__magnitude) +
            "\n\tAngle: " + str(self.__angle) + " (" + str(round(math.degrees(self.__angle), 1)) + ")")
        print("Cartesian - \n\tX: " + str(self.__x) + "\n\tY: " + str(self.__y))
        print("\n")
    
    def __calculateX(self):
        self.__x = self.__magnitude * math.cos(self.__angle)
        self.__x = round(self.__x, self.__precision)
    
    def __calculateY(self):
        self.__y = self.__magnitude * math.sin(self.__angle)
        self.__y = round(self.__y, self.__precision)

class Segment:
    '''
    A segment class initialized with a representative
    vector and a child segment.
    '''
    name = None
    vector = None
    __child = None

    def __init__(self, vector, child):
        '''
        Construct a new segment object with a vector
        and a child segment.
        '''
        self.vector = vector
        self.__child = child
    
    def printSegment(self):
        print("Name - " + self.name +
            "\nChild - " + (self.__child.name if self.__child != None else "None"))
        self.vector.printVector()