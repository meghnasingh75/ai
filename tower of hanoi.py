# ALGORITHM:
# 1. START 
# 2. Procedure Hanoi(disk, source, dest, aux) 
#     a. IF disk == 1, THEN 
#         i. move disk from source to dest 
#     b. ELSE 
#         i. Hanoi(disk - 1, source, aux, dest) 
#         ii. move disk from source to dest 
#         iii. Hanoi(disk - 1, aux, dest, source) 
#     c. END IF 
# 3. END Procedure 
# 4. STOP




def tower_of_hanoi(rings,start, end, helper): 
    if rings==0: 
        return 
    tower_of_hanoi(rings - 1, start, helper, end) 
    print("Move from {} to {}".format(start, end)) 
    tower_of_hanoi(rings - 1, helper, end, start) 

def main(): 
    n=int(input()) 
    tower_of_hanoi(n,"A","C","B") 
main()