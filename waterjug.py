# ALGORITHM:
# 1. Start. 
# 2. Empty a Jug, (X, Y)->(0, Y) Empty Jug 1. 
# 3. Fill a Jug, (0, 0)->(X, 0) Fill Jug 1. 
# 4. Pour water from one jug to the other until one of the jugs is either empty or full, 
# (X, Y) -> (X-d, Y+d). 
# 5. End. 




class water_jug(): 
    def pour(self, jug3, jug9): 
        max1, max2, fill = 3, 5, 4 
        print("%d\t%d" % (jug3, jug9)) 
        if jug9 == fill: 
            return 
        elif jug9 == max2: 
            self.pour(0, jug3) 
        elif jug3 != 0 and jug9 == 0: 
            self.pour(0, jug3) 
        elif jug3 == fill: 
            self.pour(jug3, 0) 
        elif jug3 < max1: 
            self.pour(max1, jug9) 
        elif jug3 < (max2-jug9): 
            self.pour(0, (jug3+jug9)) 
        else: 
            self.pour(jug3-(max2-jug9), (max2-jug9)+jug9) 
            
print("JUG3\tJUG9") 
water_jug().pour(0, 0)