import random
import string
import numpy as np



def seleccion(population):
   return 50

def crossover(population,sel):
  
   for gen in range(sel/2):
        WordLen=len(population[i])
        hijo= population[i][:WordLen//2]+ population[i+25][WordLen//2]
        population.append(hijo)
        return population

   

def mutacion(population, mutIdx):
    res=[]
    for indiv in population:
       if (random.uniform(0,1)<mutIdx):
          randoIdx=(round.len(indiv)* random.uniform(0,1)) - 1
          indiv[randoIdx]=random.choices(string.ascii_letters)
    res.append(indiv)
    return res

def evaluacion(population,target):
   eval=[]
   for indiv in population:
      score=0
      for i in range (len(indiv)):
         if indiv[i] != target[i]:
            score -=1
         eval.append(score)
         return eval

def reemplazo(population,eval):
   eval=np.array()
   



if __name__ =="__main__":
    population=[]
    pop_size=100
    mutIdx=0.5
    target=input()

    for i in range (pop_size):
     population.append(''.join(random.choices(string.ascii_letters, k=len(target))))

     print(population)

    for i in range (20):
       x=seleccion(population)
       population=crossover(population, x)
       population=mutacion(population, mutIdx)
       population=evaluacion(population)
       population=reemplazo(population, eval)
       print(population)