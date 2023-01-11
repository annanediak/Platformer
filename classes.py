import pygame

class Rect:
    def __init__(self, top, bottom, left, right, color):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.color = color
    
    def move_down(self, shift):
        self.top += shift
        self.bottom += shift

    def move_right(self, offset):
        self.left += offset
        self.right += offset

    def intersects(self, other):
        dst, der = self.test_intersect(other)
        return dst > 0

    def test_intersect(self, other):
        lst = [other.right - self.left, self.right - other.left,
               other.bottom - self.top, self.bottom - other.top]
        index_min = min(range(4), key=lst.__getitem__)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return lst[index_min], dirs[index_min]

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.left, self.top,
                self.right - self.left, self.bottom - self.top))

class Spike:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def getAxes(self):
        return [(self.y1 - self.y2, -self.x1 - self.x2), (self.y2 - self.y3, -self.x2 - self.x3), (self.y3 - self.y1, -self.x3 - self.x1)]
    
    def intersects(self, other):
        axes = self.getAxes() + [(-other.top-other.bottom, 0), (0, -other.left-other.right)]
        others = [(other.left, other.top), (other.left, other.bottom), (other.right, other.top), (other.right, other.bottom)] 
        selfs = [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)]
        for j in range(5):
            axis = axes[j]
            lst_other = []
            for ver in others:
                lst_other.append(axis[0]*ver[0]+axis[1]*ver[1])
            other_min = min(lst_other)
            other_max = max(lst_other)
            lst_self = []
            for ver in selfs:
                lst_self.append(axis[0]*ver[0]+axis[1]*ver[1])
            self_min = min(lst_self)
            self_max = max(lst_self)
            if self_min > other_max or self_max < other_min:
                return False
        return True
    
    def draw(self, win):
        pygame.draw.polygon(win, (105,105,105), [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)])

class Level:
    def __init__(self, start_x, start_y, portal_rect, platforms, lavas):
        self.start_x = start_x
        self.start_y = start_y
        self.portal_rect = portal_rect
        self.platforms = platforms
        self.lavas = lavas

    # 0 - normal, 1 - level clear, 2 - lava, 3 - crushed
    def update_player(self, player_rect):
        on_ground = False
        abuntahead = False
        for i in range(10):
            clip_out = False
            for plat in self.platforms:
                dist, der = player_rect.test_intersect(plat)
                if dist >= 0 and der == (0, 1):
                    on_ground = True
                if dist >= 0 and der == (0, -1):
                    abuntahead = True
                if dist > 0:
                    player_rect.move_right(-dist * der[0])
                    player_rect.move_down(-dist * der[1])
                    clip_out = True
                    break
        if clip_out:
            return 3, on_ground, abuntahead

        for lava in self.lavas:
            if lava.intersects(player_rect):
                return 2, on_ground, abuntahead
        dist, der = player_rect.test_intersect(self.portal_rect)
        if dist > 0:
            return 1, on_ground, abuntahead
        return 0, on_ground, abuntahead

    def draw(self, win):
        for plat in self.platforms:
            plat.draw(win)
        for lava in self.lavas:
            lava.draw(win)
        self.portal_rect.draw(win)

