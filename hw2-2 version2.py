class Percolation:
    def __init__(self, N :int):
        """ Create N-by-N grid, with all sites blocked """
        #設定A為頭的
        global head
        head=[]
        global tail
        tail=[]
        
        id_column=[]
        list_percolation_column=[]
        size=[]
        for i in range(N):
            id_row=[]
            list_percolation_row=[]
            for j in range(N): 
                id_row.append(i*N+j )
                list_percolation_row.append(0)
                size.append(1)
            id_column=id_column+id_row
            list_percolation_column.append(list_percolation_row)
           
        self.matrix=list_percolation_column
        self.id=id_column
        self.N=N
        self.sz = size
        
        
        

    def open(self, i :int, j :int):
        """ Open site (row i, column j) if it is not open already """
        self.matrix[i][j]=1
        N=self.N

        if i != 0:
            if self.matrix[i-1][j] != 0 :
                self.union( N*i+j,  N*(i-1)+j )
        else:
            head.append(i*N+j)
        if i != N-1:
            if self.matrix[i+1][j] != 0 :
                self.union( N*i+j,  N*(i+1)+j )
        else:
            tail.append(i*N+j)
        if j != 0:
            if self.matrix[i][j-1] != 0 :
                self.union( N*i+j,  N*(i)+(j-1))
        if j != N-1:
            if self.matrix[i][j+1] != 0 :
                self.union( N*i+j,  N*(i)+(j+1))
        #print(self.id)
                
    def isOpen(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) open? """
        if self.matrix[i][j]==1:
            return True
        else:
            return False
        
    def root(self,i ):
        while (i != self.id[i]):
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    
    def boolean_connected(self,p,  q):
        return self.root(p) == self.root(q)
    
    def union(self,p,q):    # point p to q
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return 
        
        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        
        
        
    def isFull(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) full? """
        N=self.N
        id_number= N*i+j
        for i in (head):
            if self.boolean_connected(id_number,i):
                return True
        return False
            
    def percolates(self) -> bool:
        """ Does the system percolate? """
        N=self.N
        for i in (tail):
            for j in (head):
                
                if self.boolean_connected(j,i):
                    return True
                
        return False 
