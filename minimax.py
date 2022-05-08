# ALGORITHM:
# 1. In the first step, the algorithm generates the entire game-tree and apply the utility function 
# to get the utility values for the terminal states. In the below tree diagram, let's take A as 
# the initial state of the tree. Suppose maximizer takes the first turn which has worst-case 
# initial value =- infinity, and minimizer will take next turn which has worst-case initial 
# value = +infinity.
# 2. Now, first we find the utility value for the Maximizer, its initial 
# value is -∞, so we will compare each value in terminal state 
# with the initial value of the Maximizer and determine the higher 
# nodes values. It will find the maximum among them all.
# 3. In the next step, it's a turn for minimizer, so it will compare all 
# node values with +∞, and will find the 3rd layer node values.
# 4. Now it's a turn for Maximizer, and it will again choose the maximum of all node values 
# and find the maximum value for the root node. In this game tree, there are only 4 layers, 
# hence we reach immediately to the root node, but in real games, there will be more than 
# 4 layers.




import math 
def minimax (current_depth, node_idx, maxTurn, scores, target): 
    if (current_depth == target): 
        return scores[node_idx] 

    if (maxTurn): 
        return max(minimax(current_depth + 1, node_idx * 2, False, 
scores, target), 
 minimax(current_depth + 1, node_idx * 2 + 1, False, 
scores, target)) 
 
    else: 
        return min(minimax(current_depth + 1, node_idx * 2, True, 
scores, target), 
 minimax(current_depth + 1, node_idx * 2 + 1, True, 
scores, target))

scores = [3, 5, 2, 9, 12, 5, 23, 23] 
treeDepth = math.log(len(scores), 2) 
print("The optimal value is : ", end = "") 
print(minimax(0, 0, True, scores, treeDepth))