class Percolation:
    def __init__(self, N :int):
    
        N2=N*N
        self.matrix= [0] * (N2)
        self.id=list(range(0,N2))
        self.N=N
        self.sz = [1] * (N2)
        self.cc = (N2)
        
        
    def open(self, i :int, j :int):
        
        N=self.N
        self.matrix[ N*i+j ]=1
        
        
        if i != 0:
            if self.matrix[N*(i-1)+j ] != 0 :
                self.union( N*i+j, N*(i-1)+j)
        if i != N-1:
            if self.matrix[N*(i+1)+j] != 0 :
                self.union(N*i+j,   N*(i+1)+j  )
        if j != 0:
            if self.matrix[N*(i)+(j-1)]!= 0 :
                self.union(  N*i+j,  N*(i)+(j-1) )
        if j != N-1:
            if self.matrix[N*(i)+(j+1)] != 0 :
                self.union(  N*i+j,  N*(i)+(j+1) )
        
        print()
    
                

    def isOpen(self, i :int, j :int) -> bool:
        
        N=self.N
        
        if self.matrix[N*i+j]!= 0:
            return True
        else:
            return False
        
    def root(self,i ):
        j = i
        while (j != self.id[j]):
            self.id[j] = self.id[self.id[j]]
            j = self.id[j]
        return j
    
    def boolean_connected(self,q,p):
        return self.root(p) == self.root(q)
    
    def union(self,p,q):    # point p to q
        i= self.root(p)
        j = self.root(q)
       
        self.id[i] = j
        '''
        if i == j:
            return 
        
        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.cc -= 1
        '''
        
    def isFull(self, i :int, j :int) -> bool:
        
        N=self.N
        isFullorNot = False

        for k in range(N):
            if self.boolean_connected(N*i+j,k):
                isFullorNot = True
                break
                
        return isFullorNot
            
    def percolates(self) -> bool:
        
        isPercolatesorNot = False
        N=self.N
        for h in range(N):
                
            if self.isFull(N-1,h):
                isPercolatesorNot  = True
                break
                
        return isPercolatesorNot 
