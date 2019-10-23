'''
Author: <Yifan Zhang>
Date: <09/12/2017
Class: ISTA 311
'''
import random
import matplotlib.pyplot as plt

#This method describe each time of the coin flip.
def flipcoins():
    if random.random()<=0.6:
        return 'Head'
    else:
        return 'Tail'

#This method use flipcoins() for 1000 times and count for the number times of 
#a sequence of Heads come up, two Heads come up, and three Heads come up.
def playgame(number):
    coins={}
    countForOne=0
    countForTwo=0
    countForThree=0
    for i in range(number):
        coins[i]=str(flipcoins())
    
    for i in range(len(coins)):
        if coins[i]=='Head' :
            countForOne+=1
            
    for i in range(len(coins)-1):
        if coins[i]=='Head' and coins[i+1]=='Head' :
            countForTwo+=1
    
    for i in range(len(coins)-2):
        if coins[i]=='Head' and coins[i+1]=='Head' and coins[i+2]=='Head' :
            countForThree+=1
    output(countForOne,countForTwo,countForThree,number)      
 
#This method print out the numbers as a graph     
def output(countForOne,countForTwo,countForThree,number):
    plt.bar(1,countForOne, label = 'HEADS', color = 'b')
    plt.bar(2,countForTwo, label = 'TWO HEADS', color = 'r')
    plt.bar(3,countForThree, label = 'THREE HEADS', color = 'g')
    plt.axis([0, 6, 0, number])
    plt.ylabel('Count')
    plt.title('Results of 1000 flips')
    plt.legend()
    plt.show()
    


def main():
    '''
    '''
    playgame(1000)

if __name__ == '__main__':
    main()
        