from typing import List
import heapq as hq

class Mountains:
    def mountains(self, mountains_height: List[List[int]]) -> int:
        n, m = len(mountains_height), len(mountains_height[0])
        if n>0:
            seen = set()
            dictionary={}
            Q = [(0, (0, 0))]
            while Q:
                u = hq.heappop(Q)
                #print("--------------------")
                #print("pop :",u)
                current_consumption=u[0]
                #print("consumption :",current_consumption)

                current_height=mountains_height[u[1][0]][u[1][1]]
                seen.add((0, 0))

                if u[1] == (n-1, m-1):
                    #print(seen)
                    return current_consumption


                r, c = u[1]
                seen.add((r, c))

                for rr, cc in [ (r - 1, c),(r + 1, c), (r, c - 1),(r, c + 1)]:  
                    if rr < 0 or rr >= n or cc < 0 or cc >= m:
                        continue
                    if (rr,cc) in seen:
                        continue

                    next_height=mountains_height[rr][cc]
                    if next_height>=current_height:
                        consumption=2*(next_height-current_height)
                    else:
                        consumption=current_height-next_height
                    
                    
                    total_consumption=current_consumption+consumption
                    
                    if str([rr, cc]) not in dictionary.keys() or total_consumption < dictionary[str([rr, cc])] :
                        hq.heappush(Q, ((total_consumption), (rr, cc)))
                        dictionary[str([rr, cc])]=total_consumption   
                        #print("now :",next_height,((total_consumption), (rr, cc)))
