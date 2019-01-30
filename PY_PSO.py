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

#def fittness():

def partition(distance_from_centroid):
    partition = np.empty([particle_num,data_size])
    for i in range(particle_num):
        for m in range(data_size):
            min_distance = 100
            for j in range(k):
                if distance_from_centroid[i][j][m] < min_distance:
                    min_distance = distance_from_centroid[i][j][m]
                    partition[i][m] = j
    return partition

"""def evaluate_fitness(particle):
    fittness = []
    for i in range(particle_num):
        SSE=0.0
        for j in range(k):
            for m in range(data_size):
                distance=0.0
                for d in range(dim):
                    distance = distance + ((particle[i][j][d]-iris[m][d])**2)**0.5
                #print(distance)
                SSE = SSE + distance**2
        #print(i," ",SSE)        
        fittness.append(SSE)
    return fittness
"""
#def update_particle:

particle,velocity = init_partical()
distance_from_centroid = evaluate_distance_from_centroid(particle)
partition = partition(distance_from_centroid)


#for i in range(data_size):
#    print(partition[0][i])

    

