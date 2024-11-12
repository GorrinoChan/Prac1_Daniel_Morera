import numpy
import math

class Perceptron ():

    def __init__(self, arrayX):

        self.arrayX = numpy.array (arrayX)
        self.arrayW = [1,1,1],[1,1,1]
        self.arrayW = numpy.array(self.arrayW) 
        self.b  = [1],[1],[1]
        self.z = 0


    def changeW (self, newArrayW):
        self.arrayW = newArrayW

    def changeB (self, newB):
        self.b = newB

    def calculateXandWandB(self):

        self.z = numpy.dot(self.arrayW.T, self.arrayX)
        self.z = self.z + numpy.transpose(self.b)

    def calculateSigmoid(self):

        self.calculateXandWandB()
        print(self.z)
        result = 1/(1+(math.e**(-1*(self.z))))
        return result














