# ALGORITHM:
# 1) Start. 
# 2) Enter LOCATION A/B in capital letters where A and B are the two adjacent 
# rooms respectively. 
# 3) Enter Status 0/1 accordingly where 0 means CLEAN and 1 means DIRTY. 
# 4) Vacuum Cleaner senses the status of the other room before performing any 
# action, also known as Environment sensing. In the vacuum cleaner problem, we 
# have two rooms and one vacuum cleaner. There is dirt in either room and it is to 
# be cleaned. The vacuum cleaner is present in any one of these rooms. So, we 
# have to reach a state in which both the rooms are clean and are dust free. 
# 5) End




import random
score = 0
list = [1,0]
vaccumloc = random.choice(list)
print(vaccumloc)
if vaccumloc == 0:
    print ("Current location in A")
    envloc = random.choice(list)
    print(envloc)
    if envloc == 0:
        print("Current location in A is clean")
    elif envloc == 1:
        print("Current location in A is dirty")
        score= -1
        print("Current location in A is clean")
        score = 1
else :
    print ("Current location in B")
    envloc = random.choice(list)
    print(envloc)
    if envloc == 0:
        print("Current location in B is clean")
    elif envloc == 1:
        print("Current location in B is dirty")
        score= -1
        print("Current location in B is clean")
        score = 1