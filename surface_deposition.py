import numpy as np
from random import seed
from random import random
import statistics
import math
import matplotlib.pyplot as plt

# seed random number generator
seed(1)



def model(deposition_model,length,total_time_steps):
    height_surface = [0]*length 
    average_heigth = [0]*total_time_steps
    W = [0]*total_time_steps
    logW = [0]*total_time_steps
    logtime = [0]*total_time_steps

    #Random Deposition
    if (deposition_model == "Random"):
        W_sum = 0
        for time in range(1,total_time_steps):
            i = int(random()*length)
            height_surface[i] += 1
            average_heigth[time] = statistics.mean(height_surface)
            W_sum = 0
            for l in range(length):
                W_sum += (height_surface[l] - average_heigth[time])**2
            W[time] = math.sqrt(W_sum / length)
            logW[time] = math.log(W[time])
            logtime[time] = math.log(time)
        plt.plot(logtime[1:], logW[1:])
    #Ballistic Deposition
    elif (deposition_model == "Ballistic"):
        W_sum = 0
        for time in range(1,total_time_steps):
            #Updating Procedure
            i = int(random()*length)
            if (i == 0):
                a = length-1
                b = 0
                c = 1
            elif (i == length-1):
                a = i-1
                b = i
                c = 0
            elif( i != length):
                a = i-1
                b = i
                c = i+1
            
            temp_list = [height_surface[a],height_surface[b],height_surface[c]]
            if height_surface[a] < height_surface[b] and height_surface[c] < height_surface[b] and height_surface[a] == height_surface[c]:
                r = random()
                sel_index = math.floor(r-0.5) + math.ceil(r-0.5)
            else: 
                sel_index = np.argmin(np.array(temp_list))-1
            
            print(i+sel_index)
            height_surface[i+sel_index] += 1
            
            average_heigth[time] = statistics.mean(height_surface)
            W_sum = 0
            for l in range(length):
                W_sum += (height_surface[l] - average_heigth[time])**2
                
            W[time] = math.sqrt(W_sum / length)
           # print(W[time])
            logW[time] = math.log(W[time])
            logtime[time] = math.log(time)
        
        plt.loglog(range(1,total_time_steps),W[1:]) #basex=np.e, basey=np.e)
        m, b = np.polyfit(np.array(range(1,int(total_time_steps/10**3))), np.array(W[1:int(total_time_steps/10**3)]), 1)
        plt.plot(np.array(range(1,int(total_time_steps/10**3))), m*np.array(range(1,int(total_time_steps/10**3))) + b)
        #plt.plot(logtime[1:], logW[1:])
        #plt.plot(range(1,total_time_steps), logW[1:])
        print(m,b)
    #NNModified
    elif (deposition_model == "NNModified"):
            for time in range(1,total_time_steps):
                #Updating Procedure
                i = int(random()*length)
                if (i == 0):
                    a = length-1
                    b = 0
                    c = 1
                elif (i == length-1):
                    a = i-1
                    b = i
                    c = 0
                else:
                    a = i-1
                    b = i
                    c = i+1
                


            