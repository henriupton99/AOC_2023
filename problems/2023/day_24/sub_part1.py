from itertools import combinations
FILENAME = "input.txt"
lines = [list(map(int, line.replace("@",",").split(","))) for line in open(FILENAME).read().splitlines()]

class Plane:
    def __init__(self, initial_position, velocity):
        # initial x,y,z coordinates :
        self.x, self.y, self.z = initial_position
        # velocity characteristics: 
        self.vx, self.vy, self.vz = velocity
        
        # constants that describe the equation of the representative curve :
        self.a, self.b, self.c = self.vy, -self.vx, self.vy*self.x-self.vx*self.y
    
    def intersection_point(self, a, b, c):
        if self.a*b - a*self.b == 0:
            return None
        x = self.c/self.a - (self.b/self.a)*((self.a*c-a*self.c)/(self.a*b - a*self.b))
        y = (self.a*c - a*self.c) / (self.a*b - a*self.b)
        return x, y

MIN_AREA = 200000000000000
MAX_AREA = 400000000000000
#MIN_AREA = 7
#MAX_AREA = 27

intersection_inside_area = 0
# Loop across all different pairs of planes :
for (l1,l2) in combinations(lines,2):
    p1 = Plane(initial_position=l1[:3], velocity=l1[3:])
    p2 = Plane(initial_position=l2[:3], velocity=l2[3:])
    # Get intersection point :
    intersection_point = p1.intersection_point(a=p2.a, b=p2.b, c=p2.c)
    # if there is one (ie not parallel):
    if intersection_point:
        x,y = intersection_point
        # if the point is in the area :
        if MIN_AREA<=x<=MAX_AREA and MIN_AREA<=y<=MAX_AREA:
            # if the point is not in the past (ie t>0):
            if (x-p1.x)*p1.vx >=0 and (y-p1.y)*p1.vy>=0:
                if (x-p2.x)*p2.vx >=0 and (y-p2.y)*p2.vy>=0:
                    intersection_inside_area += 1
            
print(intersection_inside_area)      