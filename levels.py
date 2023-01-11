from classes import *

levels = [Level(45, 150, Rect(100, 250, 450, 500, (0, 0, 255)),
                [Rect(250, 500, 0, 500, (0, 255, 0)),
                 Rect(200, 250, 200, 245, (0, 255, 0)),
                 Rect(150, 175, 200, 245, (0, 255, 0))], []),
          Level(25, 150, Rect(100, 250, 450, 500, (0, 0, 255)),
                [Rect(250, 500, 0, 150, (0, 255, 0)),
                 Rect(250, 500, 300, 500, (0, 255, 0)),
                 Rect(400, 500, 150, 300, (0, 255, 0))],
                [Rect(250, 400, 150, 300, (200, 150, 0))]),
          Level(45, 150, Rect(225, 250, 475, 500, (0, 0, 255)),
                [Rect(250, 500, 0, 150, (0, 255, 0)),
                 Rect(250, 500, 250, 500, (0, 255, 0)),
                 Rect(400, 500, 150, 300, (0, 255, 0))],
                [Rect(250, 400, 150, 250, (200, 150, 0)),
                 Spike(300, 220, 290, 250, 310, 250)])]

