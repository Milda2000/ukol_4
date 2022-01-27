import math

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[ {self.x}, {self.y} ]'


class Segment:

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def divide(self, max_value):
        start_point = Point(self.p1.x, self.p1.y)
        end_point = Point(self.p2.x, self.p2.y)
        midx =  (start_point.x + end_point.x)/2
        midy =  (start_point.y + end_point.y)/2
        pmid = Point(midx,midy)
        new_seg_1 = Segment(start_point,pmid)
        new_seg_2 = Segment(pmid, end_point)
        return Polyline(new_seg_1,new_seg_2)

    def __str__(self):
        return f'[{self.p1}, {self.p2}]'
        
class Polyline:

    def __init__(self,*segments):
        #segments = []
        #for i in range(len(points)-1):
        #    segments.append(Segment(points[i],points[i+1]))
        self.segments = segments
    
    def addSegment(segment):
        pass


    def divide_long_segments(self, max_value, container = []):
        for seg in self.segments:
            x = seg.p2.x - seg.p1.x 
            y = seg.p2.y - seg.p1.y
            lenght = math.sqrt(x**2 + y**2)
       
            if lenght > max_value:
                new_line = seg.divide(max_value)
                new_line.divide_long_segments(max_value, container)
            else:
                container.append(seg)
                #print(seg)
        return Polyline(*container)

    def points(self):
        points = []
        for seg in self.segments:
            point = [seg.p1.x,seg.p1.y]
            points.append(point)
        last_point = [self.segments[-1].p2.x,self.segments[-1].p2.y]
        points.append(last_point)
        return points

    def __str__(self):
        return f'[{self.segments}]'