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

def init_particle:
    

def evaluate_distance_from_centroid(particle):
    distance_from_centroid = []
    for i in range(particle_num):
        for j in range(k):
            distance_from_centroid.append([])
            for m in range(data_size):
                tmp_distance = 0.0
                for d in range(dim):
                    tmp_distance = tmp_distance + ((particle[i][j][d]-iris[m][d])**2)
                distance_from_centroid[j].append(tmp_distance**0.5)   
    return distance_from_centroid




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

distance_from_centroid = evaluate_distance_from_centroid(particle)
#fittness = evaluate_fitness(particle)

#for i in range(data_size):
#    print(distance_from_centroid[0][i])

    

