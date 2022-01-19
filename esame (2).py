class ExamException(Exception):
    pass

class  MovingAverage():

   def __init__ (self,lenght):
     if type (lenght) is not int: 
       raise ExamException("Errore, valore non intero")
       
     if lenght <= 0: 
       raise ExamException("Errore, valore  negativo")
     self.lenght = lenght

   def compute (self, lista):
    if type (lista) is not list:
       raise ExamException("Errore, non è una lista")

    if lista is None:
       raise ExamException("Errore, lista vuota")

    if len (lista) < self.lenght:
       raise ExamException("Errore, valore lista minore di window") 

    for j in lista:
      if type (j) != int and type (j) != float: 
       raise ExamException("Errore, valori non sommabili")
    i=[]
    for j in range (0,len(lista)-self.lenght+1):
      somma =  (sum (lista[j:j+self.lenght])/self.lenght)
      i.append(somma)
    return i   

class Diff:

  def __init__(self,ratio=1) -> None:
    if type(ratio) is not int and type(ratio) is not float:
      raise ExamException("Errore, valore non computabile")
    if ratio <= 0:
      raise ExamException("Errore, valore non intero")  

    self.ratio = ratio
  
  def compute(self,lista):
    if type(lista) is not list:
      raise ExamException("Errore, non è una lista")
    if list is None:
      raise ExamException("Errore, lista è vuota ")
    if len(lista) < 2:
      raise ExamException("Errore, dimensione lista insufficente")  

    for i in lista:
      if type(i) is not int and type(i) is not float:
        raise ExamException("Errore, elemento non un numero")  


    i = []
    for j in range (0,len(lista)-1):
      differenza = (lista[j+1]-lista[j])/self.ratio
      i.append(differenza)
    return i   

def main ():
 # esame1  moving_average = MovingAverage(-2)
 # esame 1 result = moving_average.compute([2,4,8,16])
 # esame 1 print(result) # Deve stampare a schermo [3,6,12]
 
  diff = Diff()


  result = diff.compute([2,4,8,16])


  print(result) # Deve stampare a schermo [2,4,8]


    
