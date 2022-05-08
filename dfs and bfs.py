# ALGORITHM:
# BFS:
# Step 1: Start. 
# Step 2: SET STATUS = 1 (ready state) for each node in G. 
# Step 3: Enqueue the starting node A and set its STATUS = 2 (waiting state) 
# Step 4: Repeat Steps 4 and 5 until QUEUE is empty 
# Step 5: Dequeue a node N. Process it and set its STATUS = 3 (processed state). 
# Step 6: Enqueue all the neighbours of N that are in the ready state (whose STATUS = 
# 1) and set their STATUS = 2 (waiting state) [END OF LOOP] 
# Step 7: End. 
# DFS 
# Step 1: Start.
# Step 2: SET STATUS = 1 (ready state) for each node in G 
# Step 3: Push the starting node A on the stack and set its STATUS = 2 (waiting state) 
# Step 4: Repeat Steps 4 and 5 until STACK is empty 
# Step 5: Pop the top node N. Process it and set its STATUS = 3 (processed state) 
# Step 6: Push on the stack all the neighbors of N that are in the ready state (whose 
# STATUS = 1) and set their STATUS = 2 (waiting state) [END OF LOOP] 
# Step 7: End. 





graph = { 
 'A' : ['B','C'], 
 'B' : ['D', 'E'], 
 'C' : ['F'], 
 'D' : [],
 'E' : ['F'], 
 'F' : [] 
} 

visited =[] 
queue=[]
def bfs(visited,graph,node): 
    visited.append(node) 
    queue.append(node)

    while queue: 
        P=queue.pop(0) 
        print(P,end=" ")

        for neighbour in graph[P]:
            if neighbour not in visited: 
                visited.append(neighbour) 
                queue.append(neighbour)

avisit=set()
def dfs(avisit,graph,node): 
    if node not in avisit:
        print(node,end=" ") 
        avisit.add(node)
    for neighbour in graph[node]: 
        dfs(avisit,graph,neighbour)
        
        
print("Breadth first search") 
bfs(visited,graph,'A') 
print("\nDepth first search") 
dfs(avisit,graph,'A')