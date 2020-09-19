import random
import numpy as np

#generating random balance matrix
memb=int(input("HI "))
import time
random.seed(0)
bal=np.random.random_integers(-2000, 2000, size=(memb, memb))
bal=(bal-bal.T)/2

#print balance matrix
print('balance: \n', bal)

#getting final balance of each person
def get_final_bal(bal):

    finalBal=np.sum(bal, axis=1, keepdims=True)
    finalBal=np.squeeze(finalBal)
    return finalBal

#Note: final balance is the amount which a person PAYS.
finalBal=get_final_bal(bal)
print('final balance individual: \n', finalBal)


#try to increase components
def comps(bala):
    pos=[]
    neg=[]
    for i in range(len(bala)):
        if bala[i]>0: pos.append([bala[i],i])
        elif bala[i]<0: neg.append([-1*bala[i],i])
    pos.sort(reverse = True)
    neg.sort(reverse = True)
    return pos,neg
    
pos,neg = comps(finalBal)

def balancing(pos,neg):
    payt = []
    inpayt = []
    j = 0
    i=0
    while(i < len(pos)):
        if pos[i][0] > neg[j][0]:
            inpayt.append((neg[j][1],neg[j][0]))
            pos[i][0]-=neg[j][0]
            j+=1
        elif pos[i][0] == neg[j][0]:
            inpayt.append((neg[j][1],neg[j][0]))
            payt.append((pos[i][1],inpayt))
            j+=1
            i+=1
            inpayt = []
        else:
            inpayt.append((neg[j][1],pos[i][0]))
            neg[j][0]-=pos[i][0]
            payt.append((pos[i][1],inpayt))
            i+=1
            inpayt = []
    return payt
    
payto = balancing(pos,neg)
print(payto)
j = 0
for i in range(len(payto)):
    j+=len(payto[i][1])
print(payto)
print(len(payto),memb - len(payto))
print(j)
print(time.process_time())
