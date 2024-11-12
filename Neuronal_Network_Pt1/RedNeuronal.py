import numpy
import math

class RedNeuronal():

    def __init__(self, arrayXLayer1):

        self.arrayX = arrayXLayer1
        self.arrayXLayer1 = numpy.array (arrayXLayer1)
        self.arrayWLayer1 = [1,1,1],[1,1,1]
        self.arrayWLayer1 = numpy.array(self.arrayWLayer1)

        self.bLayer1 = [1],[1],[1]
        self.zLayer1  = 0

        self.resultLayer1 = 0
        self.resultLayer2= 0

        self.arrayWLayer2 = [1,1,1],[1,1,1]
        self.arrayWLayer2 = numpy.array(self.arrayWLayer1)

        self.bLayer2 = [1],[1]
        self.zLayer2  = 0

        self.resultWanted = 0

        self.deltaW2 = 0
        self.deltaB2 = 0
        self.deltaW1 = 0
        self.deltaB2 = 0
        self.deltaZ1 = 0
        self.deltaZ2 = 0

    def changeInput (self, newInput):
        self.arrayXLayer1 = newInput
        self.arrayXLayer1 = numpy.array(self.arrayXLayer1)

    def changeWLayer1 (self, newArrayW):
        self.arrayWLayer1 = newArrayW

    def changeBLayer1 (self, newB):
        self.bLayer1 = newB


    def calculateXandWandBLayer1(self):

        self.zLayer1 = numpy.dot(self.arrayWLayer1.T, self.arrayXLayer1)
        self.zLayer1 = self.zLayer1 + numpy.transpose(self.bLayer1)

    def calculateSigmoidLayer1(self):

        self.calculateXandWandBLayer1()
        self.resultLayer1 = 1/(1+(math.e**(-1*(self.zLayer1))))
        return self.resultLayer1

    def calculateXandWandBLayer2(self):

        self.zLayer2 = numpy.dot(self.arrayWLayer2, numpy.transpose(self.resultLayer1))
        self.zLayer2 = self.zLayer2 + self.bLayer2

    def calculateSigmoidLayer2(self):

        self.calculateXandWandBLayer2()
        self.resultLayer2 = 1/(1+(math.e**(-1*(self.zLayer2))))
        return self.resultLayer2

    def backwardPropagation(self, resultWanted):


        #Ahora actualizamos el layer 2

            #Primero calculamos delta z2

        self.resultWanted = numpy.array(resultWanted)
        self.deltaZ2 = self.resultLayer2 - self.resultWanted
        self.deltaZ2 = numpy.array(self.deltaZ2)

            #Ahora calculamos delta w2

        self.resultLayer1 = numpy.array(self.resultLayer1)
        self.deltaW2 = numpy.dot(self.deltaZ2,self.resultLayer1)

            #Ahora calculamos la nueva w2 y la nueva b2

        self.arrayWLayer2 = self.arrayWLayer2 - 0.25 * self.deltaW2
        self.bLayer2 = self.bLayer2 - 0.25 * self.deltaZ2

        #Ahora actualizamos el layer 1

            #Primero calculamos delta z1

        a = numpy.transpose(self.arrayWLayer2) @ self.deltaZ2
        b = [[1],[1],[1]]
        c = self.resultLayer1 @ numpy.transpose((numpy.array(b) - self.resultLayer1))
        self.deltaZ1 = numpy.dot(c,a)

            # Primero calculamos delta delta z1

        self.arrayX = [[self.arrayXLayer1[0],self.arrayXLayer1[1]]]

            # Ahora calculamos delta delta w1 y b1

        self.deltaW1 = self.deltaZ1 @ self.arrayX
        self.arrayWLayer1 = self.arrayWLayer1.T - (0.25 * self.deltaW1)
        self.arrayWLayer1 = self.arrayWLayer1.T
        self.bLayer1 = self.bLayer1 - 0.25 * self.deltaZ1






        

