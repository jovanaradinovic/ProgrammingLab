import random
import time

#------------------
#| Classe Errori  |
#------------------
class ExamException(Exception):
    pass

#------------------
#| Classe Automa  |
#------------------
class Automa():
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None

    #-------------------
    #| Metodi/Funzioni |
    #-------------------
    def biancheria_f(self):
        #--------------
        #| Biancheria |
        #--------------
        #Non posso indossarla se ho già pantaloni o la maglia!
        if self.pantaloni == None and self.maglia == None:
            if self.biancheria == None: #Il capo non è stato indossato ancora
                todo = random.randint(0,1) #scelgo un valore tra 0 ed 1
                if todo == 1: #se devo mettere il capo
                    self.biancheria = True
                    return todo
                else: #Non devo mettere il capo
                    return todo
            else:
                pass #ho già quel capo!
        else:
            if self.pantaloni == True and self.maglia == None:
                raise ExamException("E r r o r e! E r r o r e! Forse avrei dovuto mettere la biancheria prima dei pantaloni...")
            if self.pantaloni == None and self.maglia == True:
                raise ExamException("E r r o r e! E r r o r e! Forse avrei dovuto mettere la biancheria prima della maglia...")
            if self.pantaloni == True and self.maglia == True:
                raise ExamException("E r r o r e! E r r o r e! Forse avrei dovuto mettere la biancheria prima della maglia e dei pantaloni...")           

    def calzini_f(self):
        #--------------
        #|  Calzini   |
        #--------------
        #Non posso indossarla se ho già le scarpe!
        if self.calzatura == None:
            if self.calzini == None: #Il capo non è stato indossato ancora
                todo = random.randint(0,1) #scelgo un valore tra 0 ed 1
                if todo == 1: #se devo mettere il capo
                    self.calzini = True
                    return todo
                else: #Non devo mettere il capo
                    return todo
            else:
                pass #ho già quel capo!
        else:
            raise ExamException("E r r o r e! E r r o r e! Forse avrei dovuto mettere i calzini prima delle calzature...")
        
    def maglia_f(self):
        #--------------
        #|   Maglia   |
        #--------------
        #Posso indossarla, niente me lo vieta!
        if self.maglia == None: #Il capo non è stato indossato ancora
            todo = random.randint(0,1) #scelgo un valore tra 0 ed 1
            if todo == 1: #se devo mettere il capo
                self.maglia = True
                return todo
            else: #Non devo mettere il capo
                return todo
        else:
            pass #ho già quel capo!
        
    def pantaloni_f(self):
        #--------------
        #| Pantaloni  |
        #--------------
        #Non posso indossarlo se ho le scarpe, come faccio!
        if self.calzatura == None:
            if self.pantaloni == None: #Il capo non è stato indossato ancora
                todo = random.randint(0,1) #scelgo un valore tra 0 ed 1
                if todo == 1: #se devo mettere il capo
                    self.pantaloni = True
                    return todo
                else: #Non devo mettere il capo
                    return todo
            else:
                pass #ho già quel capo!
        else:
            raise ExamException("E r r o r e! E r r o r e! Forse avrei dovuto mettere i pantaloni prima delle calzature...")

    def calzatura_f(self):
        #--------------
        #| Calzatura  |
        #--------------
        #Sebbene a fatica, posso metterle senza nessun prerequisito particolare.
        if self.calzatura == None: #Il capo non è stato indossato ancora
            todo = random.randint(0,1) #scelgo un valore tra 0 ed 1
            if todo == 1: #se devo mettere il capo
                self.calzatura = True
                return todo
            else: #Non devo mettere il capo
                return todo
        else:
            pass #ho già quel capo!

#----------
#| Esegui |
#----------
def esegui(automa, capo, lista_capi):
    '''
    es. value = esegui(robot, 1, capi_vestiario)
    '''
    value = None
    #controllo di capo, non si sa mai
    try:
        t = lista_capi[capo]
    except:
        capo = 0 # se non va bene metto 0
        print("Errore nell'immissione, ho messo 0 per salvare l'esecuzione")
    
    #BIANCHERIA
    if lista_capi[capo] == "biancheria" and automa.biancheria != True:
        value = automa.biancheria_f()
    #CALZINI
    if lista_capi[capo] == "calzini" and automa.calzini != True:
        value = automa.calzini_f()
    #MAGLIA
    if lista_capi[capo] == "maglia" and automa.maglia != True:
        value = automa.maglia_f()
    #PANTALONI
    if lista_capi[capo] == "pantaloni" and automa.pantaloni != True:
        value = automa.pantaloni_f()
    #CALZATURA
    if lista_capi[capo] == "calzatura" and automa.calzatura != True:
        value = automa.calzatura_f()
    #ritorno
    else:
        pass
    return value

#-------------------------
#| Comandi ed Esecuzione |
#-------------------------
        
capi_vestiario = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"]
vestito = False #All'inizio non ho indumenti

#---------------------
#| Controllo Vestito |
#---------------------
def controllo(automa, i):
    if automa.biancheria==True and automa.calzini==True and automa.maglia==True and automa.pantaloni==True and automa.calzatura==True:
        return 1
    else:
        if i%2==0:#se lo faccio sempre è troppo incasinato e salto il primo caso
            stampa(automa)
            return 0
        else:
            return 0

#--------------------
#| Stampa Variabili |
#--------------------
def stampa(automa):
    print("-  SITUAZIONE  -")
    print("- biancheria |", automa.biancheria)
    print("- calzini    |", automa.calzini)    
    print("- maglia     |", automa.maglia)
    print("- pantaloni  |", automa.pantaloni)
    print("- calzatura  |", automa.calzatura)

#-----------------
#| Reset Attrib. |
#-----------------
def reset(automa):
    automa.biancheria = None
    automa.calzini = None
    automa.maglia = None
    automa.pantaloni = None
    automa.calzatura = None

#------- ISTANZA -------
Robot = Automa()
#-----------------------

i = 0
while controllo(Robot, i)!=1: #Finché non sarà ben vestito:
    '''
     1. Scelgo casualmente un capo, tra quelli non indossati.
     2. Lancio la funzione esegui. Se ritorna 1, il robot è vestito e l'ha fatto ordinatamente.
        Se 0, non è riuscito, non avrò escluso quel vestito da quelli da provare a mettere.
     3. Se riesco a indossare tutto, non ho problemi: esco ed ho finito.
    '''
    
    scelta_capo = random.randint(0, len(capi_vestiario)-1) #scelgo casualmente un capo
    print("O p e r a z i o n e  i n  c o r s o! (Numero", i, "; numero estratto", scelta_capo)
    try:
        esegui(Robot, scelta_capo, capi_vestiario)
    except Exception as e:
        print("Robot: {}".format(e))
        time.sleep(3)
        print("\nRiprovo:")
        reset(Robot)
        time.sleep(1)
        
    i = i + 1

stampa(Robot)
print("Fatto!!!")
    
    
