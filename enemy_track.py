from os import close
from Parameter import *
'''

enemy 寻路模块

'''

class Point_direction:
    def __init__(self,position:tuple,father_position:tuple,mht_distance) -> None:
        self.position = position
        self.father_position = father_position
        self.mht_distance = mht_distance

'''Greed-Best-First-Search搜索最短路径'''
class Search:
    def __init__(self,enemy_position,target_position) -> None:
        self.enemy_position = enemy_position
        self.target_position = target_position
        self.openlist = [] # 优先队列:[points]
        self.closelist = [] # 经过队列:[points]
        self.positionlist = []  # [(r,c)] 防止走重复路
        self.is_over = False
        self.track = {}
        self.num = 0
        
        start_point = Point_direction(enemy_position,(-1,-1),self.mht_distance(enemy_position))
        self.openlist.append(start_point)
        self.positionlist.append(start_point.position)

    def mht_distance(self,position:tuple)->int:
        return abs(position[0]-self.target_position[0]) + abs(position[1]-self.target_position[1])

    def append_openlist(self,position,father_position):
        point = Point_direction(position,father_position,self.mht_distance(position))
        for i in range(len(self.openlist)):
            if self.mht_distance(position) <= self.openlist[i].mht_distance:
                self.openlist.insert(i,point)
                self.closelist.append(point)
                self.positionlist.append(point.position)
                return True
        self.openlist.append(point)
        self.closelist.append(point)
        self.positionlist.append(point.position)
        return True

    def search(self):
        if self.enemy_position == self.target_position:
            return False
        self.num += 1
        if self.num > 500:
            print('Out of the times')
            return False
        g_position = self.openlist[0].position
        if g_position == self.target_position: 
            self.is_over = True
            self.next_position = self.target_position
            self.next_direction = [0,0]
            return True
        N1,N2 = (g_position[0]+1,g_position[1]),(g_position[0],g_position[1]+1)
        N3,N4 = (g_position[0]-1,g_position[1]),(g_position[0],g_position[1]-1)
        n_list = [N1,N2,N3,N4]
        
        for n in n_list:
            if n not in available_point or n in self.positionlist:
                continue
            self.append_openlist(n,g_position)
        for point in self.openlist: 
            if point.position == g_position:
                self.openlist.remove(point)
        return self.search()
    
    def generate_track(self):
        if self.enemy_position == self.target_position:
            return False
        i = len(self.closelist) -1
        if self.closelist[i].position == self.next_position:
            # print('track position',self.next_position)
            self.next_position = self.closelist[i].father_position
            self.track.update({self.closelist[i].position:self.next_direction})
            self.next_direction = [self.closelist[i].position[1]-self.closelist[i].father_position[1],self.closelist[i].position[0]-self.closelist[i].father_position[0]]
            if self.next_position == self.enemy_position:
                self.track.update({self.enemy_position:[self.closelist[i].position[1]-self.enemy_position[1],self.closelist[i].position[0]-self.enemy_position[0]]})
                return True
        del self.closelist[i]
        return self.generate_track()
