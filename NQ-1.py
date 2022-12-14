import time
class NQ(object):
    def __init__(self,N):
        self.N = N 
        self.estado = [0]
        self.check_filas = [0]*(N+1)
        self.solved = False

    def solv(self,j):
        
        for i in range(1,self.N + 1):
            if(len(self.estado) == self.N + 1 ):
                self.solved = True
                return
            if(self.Check(self.estado,i,j)): 
                self.estado.append(i)  
                self.check_filas[i] = i 
                self.solv(j+1)
               
        if(len(self.estado) > 1 and self.solved == False):
            self.check_filas[self.estado.pop()] = 0
            
        return

                

    def Check(self,estado,nueva_fila, nueva_columna): 
        if(self.check_filas[nueva_fila] != 0): 
            return False
        else:
            for x in range(1, len(estado)): 
                if ((estado[x] - nueva_fila == x - nueva_columna) or  (estado[x] - nueva_fila == nueva_columna - x)):
                    return False 
    
        return True



inicio = time.time()

N_reinas = NQ(10)
N_reinas.solv(1)

fin = time.time()
tiempo = fin - inicio

print('\n' + "Reinas" ,N_reinas.N,"  ", N_reinas.estado," Tiempo ", tiempo)
