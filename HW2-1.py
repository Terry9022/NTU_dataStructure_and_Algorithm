from typing import List


class BoardGame:
    def __init__(self, h :int, w :int):
        """
        Set the width and height of the board
        
        Parameters:
            h (int): The height of the board
            w (int): The width of the board
        """
        global O
        global X
        O={}
        X={}
        global N
        N=h
        global size
        size=h*w
        global data
        data={}
     

    def putStone(self, x :List[int], y :List[int], stoneType :str):
        """
        Put the stones on (x[0],y[0]), (x[1], y[1]) ...
        
        We grantee that there are not stones at (x[i],y[i]) on the board.
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizotal position of the stone, 0 <= y < w
            stoneType (string): The type of the stones to be put ont the board, which has only two values {'O', 'X'}
        """
        global repeat
       
        if stoneType == 'O' :
            for i in range (len(x)):
                
                index =x[i]*N+y[i]+1
                data[index]=index
                O[index]=4 
                repeat=0  #判斷是否有重複union情況

                if y[i] != (N-1) and index+1 in (O): #right
                    self.union(index,index+1)
                    O[self.root(index+1)]=O[self.root(index+1)]+4-2-4+O[index]
                    repeat = repeat+1 #right union後給1值
                elif y[i] != (N-1) and index+1 in (X):
                    O[self.root(index)]=O[self.root(index)]-1
                    X[self.root(index+1)]=X[self.root(index+1)]-1

                if y[i] != 0 and index-1 in (O): #left
                    if repeat != 0:
                        if self.root(index)!=self.root(index-1): 
                            O[self.root(index)]=O[self.root(index)]+O[self.root(index-1)]-2                          
                            self.union(index-1,index)
                        else:
                            O[self.root(index)]=O[self.root(index)]-2
                    else :
                        self.union(index,index-1)
                        O[self.root(index)]=O[self.root(index)]+4-2-4+O[index] 
                        
                    repeat=repeat+1            
                elif y[i] != 0 and index-1 in (X):
                    O[self.root(index)]=O[self.root(index)]-1
                    X[self.root(index-1)]=X[self.root(index-1)]-1

                if  x[i] != 0 and index-N in (O): #up
                    
                    if repeat != 0:
                        if self.root(index)!=self.root(index-N): 
                            O[self.root(index)]=O[self.root(index)]+O[self.root(index-N)]-2                          
                            self.union(index-N,index)
                        else:
                            O[self.root(index)]=O[self.root(index)]-2
                    else :
                        self.union(index,index-N)
                        O[self.root(index)]=O[self.root(index)]+4-2-4+O[index] 
                    repeat=repeat+1   
                elif x[i] != 0 and index-N in (X):
                    O[self.root(index)]=O[self.root(index)]-1
                    X[self.root(index-N)]=X[self.root(index-N)]-1


                if x[i] != N-1 and index+N in (O): #down
                    if repeat != 0:
                        if self.root(index)!=self.root(index+N): 
                            O[self.root(index)]=O[self.root(index)]+O[self.root(index+N)]-2                          
                            self.union(index+N,index)
                        else:
                            O[self.root(index)]=O[self.root(index)]-2
                    else :
                        self.union(index,index+N)

                        O[self.root(index+N)]=O[self.root(index+N)]+4-2-4+O[index]
                        
                elif x[i] != N-1 and index+N in (X):
                    O[self.root(index)]=O[self.root(index)]-1
                    X[self.root(index+N)]=X[self.root(index+N)]-1

        if stoneType == 'X' :
            for i in range (len(x)):
                index =x[i]*N+y[i]+1
                data[index]=index
                X[index]=4 
                repeat=0  #判斷是否有重複union情況
                if y[i] != N-1 and index+1 in (X) : #right
                    self.union(index,index+1)
                    X[self.root(index+1)]=X[self.root(index+1)]+4-2-4+X[index]
                    repeat=repeat+1 #right union後給1值
                elif y[i] != N-1 and index+1 in (O):
                    X[self.root(index)]=X[self.root(index)]-1
                    O[self.root(index+1)]=O[self.root(index+1)]-1

                if y[i] != 0 and index-1 in (X): #left
                    if repeat != 0:
                        if self.root(index)!=self.root(index-1): 
                            X[self.root(index)]=X[self.root(index)]+X[self.root(index-1)]-2                          
                            self.union(index-1,index)
                        else:
                            X[self.root(index)]=X[self.root(index)]-2
                    else :
                        self.union(index,index-1)
                        X[self.root(index-1)]=X[self.root(index-1)]+4-2-4+X[index]
                    repeat=repeat+1  
                elif y[i] != 0 and index-1 in (O):
                    X[self.root(index)]=X[self.root(index)]-1
                    O[self.root(index-1)]=O[self.root(index-1)]-1

                if x[i] != 0 and index-N in (X): #up
                    if repeat != 0:
                        if self.root(index)!=self.root(index-N): 
                            X[self.root(index)]=X[self.root(index)]+X[self.root(index-N)]-2                          
                            self.union(index-N,index)
                        else:
                            X[self.root(index)]=X[self.root(index)]-2
                    else :
                        self.union(index,index-N)
                        X[self.root(index-N)]=X[self.root(index-N)]+4-2-4+X[index]
                        
                    repeat=repeat+1 
                elif x[i] != 0 and index-N in (O):
                    X[self.root(index)]=X[self.root(index)]-1
                    O[self.root(index-N)]=O[self.root(index-N)]-1


                if x[i] != N-1 and index+N in (X): #down
                                        
                    if repeat != 0:
                        if self.root(index)!=self.root(index+N): 
                            X[self.root(index)]=X[self.root(index)]+X[self.root(index+N)]-2                          
                            self.union(index+N,index)
                        else:
                            X[self.root(index)]=X[self.root(index)]-2
                    else :
                        self.union(index,index+N)
                        X[self.root(index+N)]=X[self.root(index+N)]+4-2-4+X[index]
                        
                elif x[i] != N-1 and index+N in (O):
                    X[self.root(index)]=X[self.root(index)]-1
                    O[self.root(index+N)]=O[self.root(index+N)]-1
       
    def root(self,i ):
        while (i != data[i]):
            data[i] = data[data[i]]
            i = data[i]
        return i
    def union(self,p,q) :
        i = self.root(p)
        j = self.root(q)
        data[i] = j
    def surrounded(self, x :int, y :int) -> bool:
        """
        Answer if the stone and its connected stones are surrounded by another type of stones, which means they are qualified to be flipped if we want.
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizaontal position of the stone, 0 <= y < w
        Returns:
            surrounded (bool): can be flipped of not.
        """

        if x*N+y+1 in O:
            
            if O[self.root(x*N+y+1)] > 0 :
                return False
            else :
                return True

        elif x*N+y+1 in X:
            if X[self.root(x*N+y+1)] > 0 :
                return False
            else :
                return True
        else: 
            return False 

    def getStoneType(self, x :int, y :int) -> str:
        """
        Get the type of the stone at (x,y)
            
        We grantee that there are stones at (x,y)
        
        Parameters:
            x (int): The vertical position of the stone, 0 <= x < h
            y (int): The horizaontal position of the stone, 0 <= y < w
        Returns:
            stoneType (string): The type of the stones, which has only two value {'O', 'X'}
        """
       
        if x*N+y+1 in O: 
            return 'O'
        elif x*N+y+1 in X:
            return 'X'



