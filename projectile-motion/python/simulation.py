#!/usr/bin/env python3
# coding: utf-8

__author__ = 'l0x6c'

import sys, math
import time, numpy

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
    def __init__(self, a, v, g):
        self.g = g
        self.a = math.radians(a)
        self.v = list(map(
            lambda x: round(x * v), 
            [math.cos(self.a), math.sin(self.a)]
        ))

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

class Simulation(object):
    def __init__(self, size, a, v, g=10):
        self.size = size
        
        self.font = pygame.freetype.Font('/usr/share/fonts/TTF/Hack-Regular.ttf', 12)
        self.screen = pygame.display.set_mode(size)
        self.screen.fill([0] * 3)

        self.object = Object(a, v, g)
        self.values = list(map(
            lambda t: self.object.position(t),
            numpy.linspace(0, 2 * self.object.v[1] / g)
        ))

    def __call__(self):
        while True:
            frame = []

            for x, y in self.values:
                frame.append((float(x) * 5, -float(y) * 5))
                yield frame

    def render_text(self, text, pos, color=(255, 255, 255)):
        self.font.render_to(self.screen, pos, text, color)

    def main(self):
        max_x = self.values[-1][0]
        max_y = sorted(self.values, key=lambda x: x[1])[-1][1]
        
        step_x = 0 if max_x == 0 else self.size[0] / max_x
        step_y = self.size[1] / max_y

        values = [
            (x * step_x, self.size[1] - y * step_y)
            for x, y in self.values
        ]
        
        for index in range(2, len(values) + 1):
            self.screen.fill([0] * 3)

            x, y = values[:index][-1]
            x, y = 0 if x == 0 else x / step_x, (self.size[1] - y) / step_y
            
            self.render_text(str(self.object), (6, 6))
            self.render_text('range: {}'.format(max_x), (6, 20))
            self.render_text('max_y: {}'.format(max_y), (6, 34))
            self.render_text('curr pos: [{}, {}]'.format(x, y), (6, 48))

            pygame.draw.lines(self.screen, [255] * 3, False, values[:index])
            pygame.display.update()
            
            time.sleep(0.09)

if __name__ == '__main__':
    pygame.freetype.init()

    simulation = Simulation(
        (480, 320),
        int(sys.argv[1]),
        eval(sys.argv[2]), 
        int(sys.argv[3])
    )
    simulation.main(); input()
