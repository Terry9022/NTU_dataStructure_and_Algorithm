from typing import List
    
class Warriors: 
    def warriors(self, strength :List[int], attack_range :List[int]):
        """
        Given the attributes of each warriors and output the minimal and maximum
        index of warrior can be attacked by each warrior.

        Parameters:
          strength (List[int]): The strength value of N warriors
          attack_range (List[int]): The range value of N warriors

        Returns:
          attack_interval (List[int]):
              The min and the max index that the warrior can attack.
              The format of output is 2N int array `[a0, b0, a1, b1, ...]`
        """
        
        
       #prints element and NGE pair for all elements of arr[] 
        N=len(strength)
        n=N-1

        
        
        #找右邊
        # Stores the required distances
        ans1 = list(range(N))
        st = [0]
        
        # Maintain a stack of elements
        # in non-increasing order
        for i in range(1, N):  

            # If the current element exceeds 
            # the element at the top of the stack
            while(st and strength[i] >= strength[st[-1]]):  
                pos = st.pop()
                
                if attack_range[pos] < i-1-pos:
                    ans1[pos]=pos+attack_range[pos]
                else:
                    ans1[pos] = i-1

            # Push the current index to the stack
            st.append(i)
            
        while(len(st)!=0):
            pos = st.pop()
            if attack_range[pos] < N-1-pos:
                ans1[pos]=pos+attack_range[pos]
            else:
                ans1[pos] = N-1
                
        # 找左邊       
        # Stores the required distances
        strength.reverse()
        attack_range.reverse()
        
        ans2 = list(range(N))
        st = [0]
        
        # Maintain a stack of elements
        # in non-increasing order
        for i in range(1, N):  

            # If the current element exceeds 
            # the element at the top of the stack
            while(st and strength[i] >= strength[st[-1]]):  
                pos = st.pop()
                
                if attack_range[pos] < i-1-pos:
                    ans2[n-pos]=n-(pos+attack_range[pos])
                else:
                    ans2[n-pos] =n-( i-1)

            # Push the current index to the stack
            st.append(i)
            
        while(len(st)!=0):
            pos = st.pop()
            if attack_range[pos] < N-1-pos:
                ans2[n-pos]= n-(pos+attack_range[pos])
            else:
                ans2[n-pos] = n-(N-1)
        
        ans3=[]
        for i in range(N):
            ans3.append(ans2[i])
            ans3.append(ans1[i])
            
            

            
        return ans3