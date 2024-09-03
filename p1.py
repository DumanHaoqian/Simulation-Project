import numpy as np
import matplotlib.pyplot as plt

def J(p1,p2):# In order to make things easier we decrease the amount of the variable: 3->2
    p3=round(1-p1-p2,7) #Get the value of p3
    #Generating the random variables
    eta1 = np.random.normal(0, 1, 10000)
    eta2 = np.random.normal(0, np.sqrt(2), 10000)
    eta3 = np.random.normal(0, np.sqrt(3), 10000)
    w = np.random.exponential(0.3, 10000)
    V = np.random.normal(0, 1, 10000)
    #Calculate the Xi
    X1 = (0.6 * V + 0.8 * eta1) / np.maximum(w, 1)
    X2 = (0.6 * V + 0.8 * eta2) / np.maximum(w, 1)
    X3 = (0.6 * V + 0.8 * eta3) / np.maximum(w, 1)
    
    scale=[]#To calculate the sum of three companies 
    for i in range(10000):
        scale1,scale2,scale3=0,0,0
        if X1[i]>=2: #To get Xi>=xi
            scale1=round(np.random.uniform(0,X1[i])*p1,7)
        if X2[i]>=3:
            scale2=round(np.random.uniform(0,X2[i])*p2,7)
        if X3[i]>=1:
            scale3=round(np.random.uniform(0,X3[i])*p3,7)
        scale.append(round(scale1+scale2+scale3,7))
    summary=sum(scale)/10000 #calculate the Sharpe ratio
    std=np.std(scale)
    expect=round(summary/std,9)
    return -expect #To find the maxima of the J(theta) could be convert to find the minima of -J(tehta)
def J_graint(J,p1,p2,i): #Use the SPSA algorithm to calculate the gradient
    y1,y2=0,0 #gradient from the two directions
    r1=np.random.choice([1,-1])
    r2=np.random.choice([1,-1])
    theta=1/(i+10000)**0.3 #Using the decrasing theta
    y1=(J(p1+theta*r1,p2+theta*r2)-J(p1-theta*r1,p2-r2*theta))/(2*theta*r1)
    y2=(J(p1+theta*r1,p2+theta*r2)-J(p1-theta*r1,p2-r2*theta))/(2*theta*r2)
    return y1,y2
def SA(J_graint,J,theta_list1,theta_list2,number): # The stochastic approximation algorithm
    for i in range(number):
        step_size=10/(i+100) #Uing the decreasing learning rate
        Jvalue.append(J(theta_list1[i],theta_list2[i]))
        y1,y2=J_graint(J,theta_list1[i],theta_list2[i],i)
        suml=theta_list2[i]+theta_list1[i]
        if suml>1: #In this case we do the projection
            theta_list2[i]=theta_list2[i]-(suml-1)/2
            theta_list1[i]=theta_list1[i]-(suml-1)/2
        theta_list1.append(max(theta_list1[i]-step_size*y1,0))
        theta_list2.append(max(theta_list2[i]-step_size*y2,0))
    return theta_list1,theta_list2

p1_list=[] #It records the last 500 experiments' mean of p1
p2_list=[] #It records the last 500 experiments' mean of p2
Experiment_number=4#The total experiment times
for num in range(Experiment_number): 
    Jvalue=[] #To record the J(theta) values
    number=3000 #iteration times
    theta_list1=[0.5] #The starting point of p1
    theta_list2=[0.5] #The starting point of p2
    p1s,p2s=SA(J_graint,J,theta_list1,theta_list2,number)
    p1s=np.array(p1s[-501:-1]) #Get the final 500 points
    p2s=np.array(p2s[-501:-1])
    mean_p1 = np.mean(p1s) #Get the mean of the converge data
    mean_p2 = np.mean(p2s)
    p1_list.append(np.mean(p1s))
    p2_list.append(np.mean(p2s))
    file_path1 = r"point.txt"  
    with open(file_path1, 'a') as f:
        f.write(f'Experiment {num}: Mean p1 = {mean_p1}, Mean p2 = {mean_p2}\n')#Write the p1 and p2 to a txt file
    fig, axs = plt.subplots(1,3, figsize=(20,5))
    axs[0].plot(theta_list1, color="green")
    axs[0].set_xlabel("Iteration")
    axs[0].set_ylabel(r"$\theta1_n$")
    axs[0].set_title(r"$\theta1_n$")
    axs[1].plot(theta_list2, color="blue")
    axs[1].set_xlabel("Iteration")
    axs[1].set_ylabel(r"$\theta2_n$")
    axs[1].set_title(r"$\theta2_n$")
    axs[2].plot(Jvalue, color="red")
    axs[2].set_xlabel("Iteration")
    axs[2].set_ylabel("J value")
    axs[2].set_title("The J function")
    save_path = f"{num}.png"
    fig.savefig(save_path) #Get the diagram
    plt.close(fig)
