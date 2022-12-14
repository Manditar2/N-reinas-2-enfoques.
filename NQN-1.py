import time
class NQN(object):
    
    def __init__(self,N):
        self.N = N
        self.estado = [ [0] * N for _ in range(N)]
        self.check_filas = [0]*N
        self.check_columnas = [0]*N
        self.down_diag = [0]*(2*N - 1)
        self.up_diag = [0]*(2*N - 1)
        self.mitad = len(self.down_diag) // 2
        self.success = False
        self.count_Q = 0

    def solve(self,j):
        for  i in range(self.N):
            

            if(self.check(i,j) == True):
                
                self.check_filas[i] = 1
                self.check_columnas[j] = 1
                self.down_diag[self.mitad + (i-j)] = 1
                self.up_diag[i+j] = 1
                self.estado[i][j] =  1
                self.count_Q +=1

                if(self.solve(j+1) == False):
                    self.check_filas[i] = 0
                    self.check_columnas[j] = 0
                    self.down_diag[self.mitad + (i-j)] = 0
                    self.up_diag[i+j] = 0
                    self.estado[i][j] =  0
                    self.count_Q -=1
            
            
            if(self.count_Q == self.N):
                self.success == True
                return True
            
        return self.success

    def check(self,i,j):

        if(self.check_filas[i] > 0 or self.check_columnas[j] > 0):
            return False
        
        else:
            down_diag = i - j   #Centro del arreglo = diagonal central
            if(self.down_diag[self.mitad + down_diag] > 0):
                return False
            if(self.up_diag[ i + j ] > 0):
                return False

        return True

inicio = time.time()    
test = NQN(11)
test.solve(0)
fin = time.time()
tiempo = fin - inicio 

"""f = open('./NQN.txt','a')
f.write('\n' + f"{tiempo}")
f.close()"""

print('Solucion' + '\n')

for x in range (test.N):
    print(test.estado[x])

print('\n' + "Reinas" , test.N,"  Tiempo ", tiempo)




