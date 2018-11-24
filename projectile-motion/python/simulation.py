#!/usr/bin/env python3
# coding: utf-8

__author__ = 'l0x6c'

import sys
import math
import time

import pygame
import pygame.freetype

'''
Object(angle=37, velocity=20, gravity=10)

V_x = velocity * cos(37) = 16
V_y = velocity * sin(37) = 12

flight_time = 2 * V_y / g           = 2.4
max_height  = pow(V_y, 2) / (2 * g) = 7.2
max_range   = V_x * flight_time     = 38.4
'''

class Object(object):
    def __init__(self, a, v, g, p=60):
        self.p = p
        self.g = g
        self.a = math.radians(a)
        self.v = list(map(
            lambda x: round(x * v), 
            [math.cos(self.a), math.sin(self.a)]
        ))

        self.pos = (0, 0)
        self.passed_t = 0

        self._time = 2 * self.v[1] / g
        self.range = self.v[0] * self._time
        self.max_y = pow(self.v[1], 2) / (g * 2)

    def __str__(self):
        return 'Object(angle={}, velocity={}, gravity={})'.format(
            round(math.degrees(self.a)),
            self.v,
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

    def render_text(self, text, pos, color=(255, 255, 255)):
        self.font.render_to(self.screen, pos, text, color)

    def map_(self, num, a, b, c, d):
        return int((d - c) * (num - a) / (b - a) + c)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            self.screen.fill([0] * 3)

            x, y = self.object.pos
            x_ = self.map_(x, 0, self.object.range, 0, self.size[0])
            y_ = self.map_(y, 0, self.object.max_y, self.size[1], 0)
            
            self.render_text(str(self.object), (6, 6))
            self.render_text('range: {}'.format(self.object.range), (6, 20))
            self.render_text('max_y: {}'.format(self.object.max_y), (6, 34))
            self.render_text('curr pos: [{}, {}]'.format(*map(round, (x, y))), (6, 48))

            pygame.draw.circle(self.screen, [255] * 3, (x_, y_), 5, 1)
            pygame.display.update(); self.object.update()
            
            time.sleep(0.09)

if __name__ == '__main__':
    pygame.freetype.init()

    simulation = Simulation(
        (800, 600),
        int(sys.argv[1]),
        eval(sys.argv[2]), 
        int(sys.argv[3])
    )
    simulation.main(); input()
