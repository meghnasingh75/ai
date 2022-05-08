# ALGORITHM: 
# STEP 1: Initialize the open list 
# STEP 2: Initialize the closed list put the starting node on the open 
#  list (you can leave its f at zero) 
# STEP 3: while the open list is not empty 
#  a) find the node with the least f on the open list, call it "q" 
#  b) pop q off the open list 
#  c) generate q's 8 successors and set their parents to q 
#  d) for each successor 
    #  i) if a successor is the goal, stop search 
    #  ii) else, compute both g and h for successor.g = q.g + distance between successor and q 
#  successor.h = distance from goal to successor 
#  successor.f = successor.g + successor. 
#  iii) if a node with the same position as a successor is in the OPEN list which has a lower f 
# than successor, skip this successor. 
#  iv) if a node with the same position as successor is in the CLOSED list which has a 
# lower f than successor, skip this successor otherwise, add the node to the open list end (for 
# loop). 
#  e) push q on the closed list end (while loop)






class Graph:
    def __init__(self, adjacent_list):
        self.adjacent_list = adjacent_list
 
    def neighbours(self, v):
        return self.adjacent_list[v]
     
    def hht(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]
 
    def astar_algo(self, start, stop):
        onl = set([start])
        cdl = set([])
        nodes = {}
        nodes[start] = 0
 
        par = {}
        par[start] = start
        while len(onl) > 0:
            n = None
            for v in onl:
                if n == None or nodes[v] + self.hht(v) < nodes[n] + self.hht(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            if n == stop:
                new_path = []
                while par[n] != n:
                    new_path.append(n)
                    n = par[n]
 
                new_path.append(start)
                new_path.reverse()
 
                print('Path found:')
                return new_path
 
            for (m, weight) in self.neighbours(n):
                if m not in onl and m not in cdl:
                    onl.add(m)
                    par[m] = n
                    nodes[m] = nodes[n] + weight
 
                else:
                    if nodes[m] > nodes[n] + weight:
                        nodes[m] = nodes[n] + weight
                        par[m] = n
                        if m in cdl:
                            cdl.remove(m)
                            onl.add(m)
 
            onl.remove(n)
            cdl.add(n)
 
        print('Path does not exist!')
        return None


adjacent_list = {
    'A': [('B', 4), ('C', 8), ('D', 10)],
    'B': [('D', 12)],
    'C': [('D', 9)]
}

gp = Graph(adjacent_list)
gp.astar_algo('A','D')