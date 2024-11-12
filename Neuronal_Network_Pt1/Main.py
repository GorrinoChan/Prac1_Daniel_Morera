import Perceptron
import PerceptronMejorado
import RedNeuronal

print("---------")
arrayX = [0,0]
print("Input [0,0]")

redNeuronal = RedNeuronal.RedNeuronal(arrayX)

for i in range(10000):

    result = redNeuronal.calculateSigmoidLayer1()
    result = redNeuronal.calculateSigmoidLayer2()
    redNeuronal.backwardPropagation([[0],[0]])

print("Result")
print(result)
print("---------")

redNeuronal.changeInput([0,1])
print("Input [0,1]")

for i in range(10000):

    result = redNeuronal.calculateSigmoidLayer1()
    result = redNeuronal.calculateSigmoidLayer2()
    redNeuronal.backwardPropagation([[1],[0]])

print("Result")
print(result)
print("---------")

redNeuronal.changeInput([1,0])
print("Input [1,0]")

for i in range(10000):

    result = redNeuronal.calculateSigmoidLayer1()
    result = redNeuronal.calculateSigmoidLayer2()
    redNeuronal.backwardPropagation([[1],[0]])

print("Result")
print(result)
print("---------")

redNeuronal.changeInput([1,1])
print("Input [1,1]")

for i in range(10000):
  
    result = redNeuronal.calculateSigmoidLayer1()
    result = redNeuronal.calculateSigmoidLayer2()
    redNeuronal.backwardPropagation([[0],[1]])

print("Result")
print(result)
print("---------")