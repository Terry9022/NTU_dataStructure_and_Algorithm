from typing import List
import math

class Airport:
    def airport(self, houses: List[List[int]]) -> float:
        self.houses = houses
        self.equivalent_point ()
        self._hull_points = []
        if not self._hull_points :
            self.get_convexhull(self.houses)
        """
        Find the best place to build airport and
        calculate the average distance from all the house to airport

        Parameters:
            houses(list[list[int]]): List of houses.
                Each house contains [x,y] coordination.

        Returns:
            distance(float)
        """
        return self.distance()
    def get_convexhull(self, points: List[List[int]]) -> List[List[int]]:
    # value of 0 means points are colinear; < 0, cw; > 0, ccw
    # CCW implement
        def ccw(p1, p2, p3):
            return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

        # Computes slope of line between p1 and p2
        def slope(p1, p2):
            return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0]) if p1[0] != p2[0] else float('inf')

        # distance of p1 and p2
        def dis(p1, p2):
            return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    
        # Find the smallest left point and remove it from points
        start = self.houses[0]
        for p in self.houses[1:]:
            if p[0] < start[0]:
                start = p
            elif p[0] == start[0] and p[1] < start[1]:
                start = p
                
        self.houses.remove(start)

        # Sort points so that traversal is from start in a ccw circle.
        points_slopes = [(p, slope(p, start)) for p in self.houses]
        points_slopes.sort(key=lambda e: e[1])
        points = []
        i = 0
        for j in range(1,len(points_slopes)):
            if points_slopes[j][1] != points_slopes[i][1]:
                if j-i == 1:
                    points.append(points_slopes[i])
                else:
                    #if the slpoe of i,j points are the same 
                    points_cl = sorted(points_slopes[i:j], key=lambda e: dis(start, e[0]))
                    points.extend(points_cl)
                i = j
        #if the slope of the last  points are the same 
        points_cl = sorted(points_slopes[i:], key=lambda e: -dis(start, e[0]))
        points.extend(points_cl)
        #print("points",points)
        points = [p[0] for p in points]

    # Add each point to the convex hull.
    # If the last 3 points make a cw turn, the second to last point is wrong. 
        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and ccw(ans[-3], ans[-2], ans[-1]) < 0:
                #pop the wrong point
                ans.pop(-2)
        self._hull_points = ans
        return ans
    
    def distance(self):
        
        length=len(self._hull_points)
        #line between last point and start point 
        line =  [self._hull_points[0][0]-self._hull_points[length-1][0] ,self._hull_points[0][1]- self._hull_points[length-1][1]]
        distance_to_line = (abs((self.eqpoint[0]-self._hull_points[length-1][0]) * line[1] - (self.eqpoint[1]-self._hull_points[length-1][1]) * line[0])) / (math.sqrt(line[0]*line[0]+line[1]*line[1]))
        min_distance = distance_to_line
        for i in range (length-1):
            #choose two ponts on convex hull
            line = [self._hull_points[i+1][0]-self._hull_points[i][0] , self._hull_points[i+1][1]- self._hull_points[i][1]]
            distance_to_line = (abs((self.eqpoint[0]- self._hull_points[i][0])* line[1] - (self.eqpoint[1]-self._hull_points[i][1]) * line[0])) / (math.sqrt(line[0]*line[0]+line[1]*line[1]))
            #find min distance
            if distance_to_line < min_distance:
                min_distance = distance_to_line

        return min_distance
    def equivalent_point (self):
        addx = 0
        addy = 0
        eqlen = len(self.houses)
        for i in self.houses :
            addx = addx + i[0]
            addy = addy + i[1]
        eqpoint = [addx/eqlen,addy/eqlen]
        self.eqpoint = eqpoint


    






if __name__ == "__main__":
    print(Airport().airport([[0,0],[1,0]]))
    """
    0.0
    """
    print(Airport().airport([[0,0],[1,0],[0,1]]))
    """
    *.
    **
    # Convex: [[0, 0], [1, 0], [0, 1]]
    0.2357022603955159
    """
    print(Airport().airport([[0,0],[2,0],[0,2],[1,1],[2,2]]))
    """
    *.*
    .*.
    *.*
    # Convex: [[0, 0], [2, 0], [2, 2], [0, 2]]
    1.0
    """
    print(Airport().airport([[1,1],[2,2],[0,2],[2,0],[2,4],[3,3],[4,2],[4,1],[4,0]]))
    """
    ..*..
    ...*.
    *.*.*
    .*..*
    ..*.*
    # Convex: [[0, 2], [2, 0], [4, 0], [4, 2], [2, 4]]
    1.3356461422412562
    """
