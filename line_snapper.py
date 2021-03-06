import math

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'


class Segment:

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    #funkce spocita delku segmentu
    def length(self):
        x = self.p2.x - self.p1.x 
        y = self.p2.y - self.p1.y
        length = math.sqrt(x**2 + y**2)
        return length

    #funkce rozdeli segment na pul tolikrat, dokud nebude jeho delka mensi nebo rovna max. delce
    #a vrati seznam zkracenych segmentu
    def divide(self, max_value, container):
        start_point = Point(self.p1.x, self.p1.y)
        end_point = Point(self.p2.x, self.p2.y)
        if self.length() > max_value:
            midx =  (start_point.x + end_point.x)/2
            midy =  (start_point.y + end_point.y)/2
            pmid = Point(midx,midy)
            new_seg_1 = Segment(start_point,pmid)
            new_seg_1.divide(max_value,container)
            new_seg_2 = Segment(pmid,end_point)
            new_seg_2.divide(max_value,container)
        else:
           container.append(self)
        return container

    def __str__(self):
        return f'[{self.p1}, {self.p2}]'
        
class Polyline:

    def __init__(self,*segments):
        self.segments = segments
    
    #funkce projde vsechny segmenty linii a zavola na ne funkci divide
    def divide_long_segments(self, max_value):
        container = []
        for seg in self.segments:
            seg.divide(max_value, container)
        return Polyline(*container)

    #funkce vrati list bodu ze ktrerych se skladaji segmenty, ktere tovri polylinii
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