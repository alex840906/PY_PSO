import numpy as np
import random
data_size = 150
dim = 4
particle_num=10
k = 3
c_1=2
c_2=2
v_min=-4
v_max=4
w=0.9
iris = np.loadtxt('PY_PSO\iris.txt', delimiter=' ')

def init_partical():
    index_list=[]
    for i in range(data_size):
        index_list.append(i)
    cp_index_list=[]
    particle = []

    #粒子起始重心
    for i in range(particle_num):
        cp_index_list = index_list.copy()
        centroid_point = []
        for j in range(k):
            r = random.randint(0,len(cp_index_list)-1)
            centroid_point.append(cp_index_list[r])
            del cp_index_list[r]
            particle.append([])
            particle[i].append(iris[centroid_point[j]])
    #粒子起始速度        
    velocity = []
    for i in range(particle_num):
        r = random.uniform(-4,4)
        velocity.append(r)
    return (particle , velocity)   

def evaluate_distance_from_centroid(particle):
    distance_from_centroid = []
    for i in range(particle_num):
        distance_from_centroid.append([])
        for j in range(k):
            distance_from_centroid[i].append([])
            for m in range(data_size):
                tmp_distance = 0.0
                for d in range(dim):
                    tmp_distance = tmp_distance + ((particle[i][j][d]-iris[m][d])**2)
                distance_from_centroid[i][j].append(tmp_distance**0.5)   
    return distance_from_centroid


def partition(distance_from_centroid):
    partition = np.empty([particle_num,data_size])
    for i in range(particle_num):
        for m in range(data_size):
            min_distance = 100
            for j in range(k):
                if distance_from_centroid[i][j][m] < min_distance:
                    min_distance = distance_from_centroid[i][j][m]
                    partition[i][m] = j
    
    centroid_of_particle = np.empty([particle_num,k,dim])
    partition = partition.tolist()
    
    for i in range(particle_num):
        #centroid_of_particle.append([])
        tmp = np.zeros([k,dim])
        count = np.zeros(k)
        for j in range(data_size):
            for m in range(dim):
                tmp[int(partition[i][j])][m] = tmp[int(partition[i][j])][m] + iris[j][m]
            count[int(partition[i][j])] = count[int(partition[i][j])] + 1    
        
        for j in range(k):
            tmp[j] /= count[j]
        tmp = tmp.tolist()
        for j in range(k):
            for m in range(dim):
                centroid_of_particle[i][j][m] = tmp[j][m]      

    return centroid_of_particle,partition

def centroid_of_iris():
    centroid_of_iris = np.zeros([k,dim])
    for i in range(data_size):
        list_iris = iris.tolist()
        for j in range(dim):    
            centroid_of_iris[int(list_iris[i][4]-1)][j] = centroid_of_iris[int(list_iris[i][4]-1)][j] + iris[i][j]
                
    for i in range(k):
        for j in range(dim):
            centroid_of_iris[i][j] = centroid_of_iris[i][j]/50
    
    return centroid_of_iris



def classify_centroid(centroid_of_particle,centroid_of_iris,partition):
    
    for i in range(particle_num):
        
        console = np.zeros([k])
        tmp = centroid_of_iris.copy().tolist()
        
        for j in range(k):
            distance = np.zeros([k])
            tmp_distance=0.0
            
            for m in range(k):
                for d in range(dim):
                    tmp_distance += (centroid_of_particle[i][j][d] - tmp[m][d])**2
                tmp_distance = tmp_distance**0.5    
                distance[m] = tmp_distance

            min_distance = 100
            
            flag = -1
            for m in range(k):
                if min_distance > distance[m]:
                    min_distance = distance[m]
                    flag = m
            
            console[j] = flag + 1
            for d in range(dim):
                tmp[flag][d] = 1000 

        for j in range(data_size):
            for m in range(k):
                if partition[i][j] == m:
                    partition[i][j] = console[m]
    print(console)
    return partition
                        
        
                    

#def evaluate_fitness(particle):

#def update_particle:

particle,velocity = init_partical()
distance_from_centroid = evaluate_distance_from_centroid(particle)
centroid_of_particle,partition = partition(distance_from_centroid)
centroid_of_iris = centroid_of_iris()
print(partition[9])

partition = classify_centroid(centroid_of_particle,centroid_of_iris,partition)
print(partition[9])





    

