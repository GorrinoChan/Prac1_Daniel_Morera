import numpy
import math

class Perceptron ():

    def __init__(self, arrayX):

        self.arrayX = arrayX
        self.arrayW = [1,1]
        self.b  = 1
        self.z = 0

    def changeW (self, newArrayW):
        self.arrayW = newArrayW

    def changeB (self, newB):
        self.b = newB

    def calculateXandWandB(self):

        self.z = 0
        for i in range(len(self.arrayX)):
            self.z = self.z + (self.arrayX[i] * self.arrayW[i])

        self.z = self.z + self.b



    def calculateSigmoid(self):

        self.calculateXandWandB()
        print(self.z)
        result = 1/(1+(math.e**(-1*(self.z))))
        return result


        