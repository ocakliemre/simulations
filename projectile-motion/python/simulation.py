#!/usr/bin/env python3
# coding: utf-8

import sys, math
import time, pygame
import pygame.freetype

def map_(num, a, b, c, d):
    return int((d - c) * (num - a) / (b - a) + c)

class Object(object):
    def __init__(self, a, v, g, p=30):
        self.p = p
        self.g = g
        self.a = math.radians(a)
        self.v = [
            v * math.cos(self.a),
            v * math.sin(self.a)
        ]

        self.pos = (0, 0)
        self.passed_t = 0

        self._time = 2 * self.v[1] / g
        self.range = self.v[0] * self._time
        self.max_y = pow(self.v[1], 2) / (g * 2)

    def __str__(self):
        return 'Object(angle={}, velocity={}, gravity={})'.format(
            round(math.degrees(self.a)),
            list(map(round, self.v)),
            self.g
        )

    def __repr__(self):
        return self.__str__()

    def position(self, t):
        return (
            self.v[0] * t,
            self.v[1] * t - self.g * pow(t, 2) / 2
        )

    def update(self):
        if self.passed_t >= self._time:
            self.passed_t = 0

        self.passed_t += self._time / self.p
        self.pos = self.position(self.passed_t)

class Simulation(object):
    def __init__(self, size, a, v, g=10):
        self.size = size
        self.font = pygame.freetype.SysFont('Lucida Sans', 12)
        self.screen = pygame.display.set_mode(size)
        self.screen.fill([0] * 3)

        self.object = Object(a, v, g)

    def render_text(self, text, pos, color=(0, 0, 0)):
        self.font.render_to(self.screen, pos, text, color)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            self.screen.fill([255] * 3)
            pygame.draw.line(self.screen, [0] * 3, (0, self.size[1]), self.size, 4)

            x, y = self.object.pos
            x_ = map_(x, 0, self.object.range, 0, self.size[0])
            y_ = map_(y, 0, self.object.max_y, self.size[1], 0)
            
            self.render_text(str(self.object), (6, 6))
            self.render_text('range: {}'.format(round(self.object.range)), (6, 20))
            self.render_text('max_y: {}'.format(round(self.object.max_y)), (6, 34))
            self.render_text('curr pos: [{}, {}]'.format(*map(round, (x, y))), (6, 48))

            pygame.draw.circle(self.screen, [0] * 3, (x_, y_), 5, 1)
            pygame.display.update(); self.object.update()
            
            time.sleep(0.09)

if __name__ == '__main__':
    pygame.freetype.init()

    if not sys.argv[1:]:
        sys.argv[1:] = [37, 100, 10] # angle, velocity, gravitational_const

    simulation = Simulation(
        (640, 480),
        float(sys.argv[1]),
        eval(str(sys.argv[2])),
        float(sys.argv[3])
    )
    simulation.main(); input()