from typing import List
import heapq

class Cluster:
    
    def euclidean_distance(self, data_point_one, data_point_two):
        """
        euclidean distance: https://en.wikipedia.org/wiki/Euclidean_distance
        assume that two data points have same dimension
        """
        
        result = 0.0
        for i in range(2):
            f1 = data_point_one[i]   # feature for data one
            f2 = data_point_two[i]   # feature for data two
            result += (f1-f2)**2
        
        return result
    
    def compute_pairwise_distance(self, dataset):
        result = []
        dataset_size = len(dataset)
        for i in range(dataset_size-1):    # ignore last i
            for j in range(i+1, dataset_size):     # ignore duplication
                dist = self.euclidean_distance(dataset[i], dataset[j])
                # duplicate dist, need to be remove, and there is no difference to use tuple only
                # leave second dist here is to take up a position for tie selection
                result.append( (dist, [dataset[i], dataset[j]] )  )

        return result

    
    def compute_centroid(self,  min_item):
        total_size = 0
        centroid = [0,0]
        for item in min_item:
            
            if str(item) in self.size_dict.keys():
                size = self.size_dict[str(item)]
            else:
                
                self.size_dict[str(item)] = 1
                size=self.size_dict[str(item)]
            

            centroid[0] += float(item[0])*size
            centroid[1] += float(item[1])*size
            
            total_size+=size
                
        centroid[0] /= total_size
        centroid[1] /= total_size
            
        return centroid , total_size
    
 
    
    def cluster(self, points: List[List[int]], cluster_num: int) -> List[List[float]]:
        """ 
        Cluster the points to cluster_num clusters.
        Output the sorted center coordination of those clusters.
        """ 

        k = cluster_num
        current_clusters = {}
        self.size_dict = {}
        data = self.compute_pairwise_distance(points)
        heapq.heapify(data)
        old_clusters = {}
        data_len=len(points)
        
        for i in points:
            current_clusters[str(i)]=i
      
        
        while data_len > k:
            
            dist, min_item = heapq.heappop(data)
            
             # judge if include old cluster
            first = min_item[0]
            second = min_item[1]
            if str(first) in old_clusters.keys() or str(second) in old_clusters.keys():
                continue
            
            new_cluster_cendroid , new_size = self.compute_centroid(min_item)
            
           
            if str(new_cluster_cendroid) in self.size_dict.keys():
                self.size_dict[str(new_cluster_cendroid)]+=1
            else:
                self.size_dict[str(new_cluster_cendroid)]=new_size
                
            
            old_clusters[str(min_item[0])]=min_item[0]
            old_clusters[str(min_item[1])]=min_item[1]
            
            del self.size_dict[str(min_item[0])]
            del self.size_dict[str(min_item[1])]
            
            del current_clusters[str(min_item[0])]
            del current_clusters[str(min_item[1])]
            
            #current_clusters=[i for i in current_clusters if i not in min_item]
            
            #current_clusters.remove(min_item[0])
            #current_clusters.remove(min_item[1])
           
            
            for key in current_clusters.keys():
                dist = self.euclidean_distance(current_clusters[key] , new_cluster_cendroid )
                heapq.heappush( data, (dist, [current_clusters[key], new_cluster_cendroid])  )  
                #print([current_clusters[key], new_cluster_cendroid])
                
            #current_clusters.append(new_cluster_cendroid )
            current_clusters[str(new_cluster_cendroid)]=new_cluster_cendroid
            
            
            if str(new_cluster_cendroid) in old_clusters.keys():
                del old_clusters[str(new_cluster_cendroid)]
                
            data_len-=1
                
        #for i in self.size_dict.keys():
            #print( "size:",i,self.size_dict[i])
        
        ans=[ current_clusters[key] for key in current_clusters.keys() ]
        
        return sorted(ans)
