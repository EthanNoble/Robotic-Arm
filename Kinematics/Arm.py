from math import pi
from ArmParts import Vector
from ArmParts import Segment

class Arm:
    """
    An arm class initialized with a number of joints
    and a corresponding number of segments plus a base.
    """
    __joints = None
    __segments = []

    def __init__(self, joints):
        """
        Construct an arm class with a number of joints.
        The number of segments equals the number of joints
        plus a base angled indefinitely at 90 degrees.
        """
        self.__joints = joints
        self.__createSegments()
    
    def printSegments(self):
        for segment in self.__segments:
            segment.printSegment()

    def __createSegments(self):
        dAngle = 2
        child = None
        for i in range(0, self.__joints + 1):
            if (i != 0):
                child = self.__segments[i - 1]
            segment = Segment(Vector(5, pi/dAngle), child)
            segment.name = "Segment" + str(i + 1)
            self.__segments.append(segment)
            dAngle += 2