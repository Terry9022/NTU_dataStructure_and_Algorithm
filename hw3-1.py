#3-1

import functools
from typing import List

def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo
    
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo


class Restaurant(object):
    def __init__(self, id :int, rate :int, price :int, distance :int):
        
        self.id = id
        self.rate= rate
        self.price=price
        self.distance=distance
        self.compare_natural = round(distance * price / rate,5)

    def getID(self) -> int:
        
        return self.id 

    def __lt__(self, b) -> bool:
        """
        The natural comparator of Restaurant
        
        The comparator should compare the restaurants by the value calculated from the formula
        `distance * price / rate`
        and return True if the value of `self` is lower than `b`
        If the value is the same, keep the same order as input.
        """
         
        if self.compare_natural < b.compare_natural:
            return True
        else:
            return False

    @staticmethod
    def comparator1(a, b) -> int:
        """
        Compare two restaurants by restaurant object

        Order the restaurants by the rate in increasing order,
        distance in increasing order (if tied),and 
        id in decreasing order (if tied again).
        
        Parameters:
            a(Restaurant): The restaurant object
            b(Restaurant): The restaurant object

        Returns:
            result(int): -1 for restaurant a has smaller order, 1 for restaurant b has smaller order, 0 for equal.
        """
        if a.rate < b.rate:
            return -1
        elif b.rate < a.rate:
            return 1
        else:
            if a.distance < b.distance:
                return -1
            elif b.distance < a.distance:
                return 1
            else:
                if a.id > b.id:
                    return -1
                elif b.id > a.id:
                    return 1
                else:
                    return 0
                
   
        

class Restaurants(object):
    def __init__(self, restaurants :List[Restaurant]):
        
        self.restaurants=restaurants
        self.N=len(restaurants)
        self.rests=[]
        self.prices=[]
        
        for i in restaurants:
            self.rests.append([i.id, i.rate, i.price, i.distance])
            self.prices.append(i.price)
            
            
        self.sorted_by_price_index = sorted( self.prices )
        self.sorted_by_price = sorted( self.rests , key=lambda t: t[2])

    def filter(self, min_price: int, max_price :int, min_rate: int) -> List[int]:
        """
        Filter the restaurants, output the list of restaurant id that meet the condition.

        Output the list in in the increasing order of distance;
        If the distance is the same, order the restaurant ids from the highest to the lowest.

        Returns:
            restaurants (List[int]): The list of restaurant id.
        """
        
        left_index = bisect_left(self.sorted_by_price_index,min_price)
        right_index = bisect_right(self.sorted_by_price_index,max_price)
        
        pass_item_1 = self.sorted_by_price[left_index:right_index] 
        
        
        pass_item_2 = [] 
        
        
        
        
        
        if min_rate==1:
             pass_item_2=pass_item_1
            
        else:   
            
            n=len(pass_item_1)
        
            for i in range(n):
                if( min_rate <= pass_item_1[i][1] ):
                    pass_item_2.append(pass_item_1[i])
        
        

            
        
        
        
        
        ans = sorted(pass_item_2 , key = lambda t: t[0],reverse=True)
        ans = [ i[0] for i in sorted(ans , key=lambda t: t[3],reverse=False) ]
        
        
        
        return ans
