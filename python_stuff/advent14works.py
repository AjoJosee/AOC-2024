from __future__ import annotations
import re
from dataclasses import dataclass
import collections
import gzip
import itertools
import functools
import operator

width, height=101, 103

@dataclass
class Robot:
    x : int
    y: int
    vx: int
    vy: int

    def move(self, n: int) -> Robot:
        return Robot((self.x + self.vx * n) % width, (self.y + self.vy * n) % height, self.vx, self.vy)
    
    @property
    def quadrant(self)-> tuple[bool, bool] | None:
        if self.x == width // 2 or self.y == height // 2:
            return None
        return (self.x < width // 2, self.y < height // 2)


robo_re = re.compile(r"p=([\-0-9]+),([\-0-9]+) v=([\-0-9]+),([\-0-9]+)")

def read_input():
    with open("advent14.txt") as f:
        for line in f:
            if (m:= robo_re.match(line)):
                yield Robot(*map(int, m.groups()))

def safety_factor(robots)-> int:
    quads = collections.Counter(r.quadrant for r in robots)
    del quads[None]
    return functools.reduce(operator.mul, quads.values(), 1)

def part1(robots) -> int:
    return safety_factor(r.move(100) for r in robots)

def plot(robots)-> str:
    grid = {(r.x,r.y) for r in robots}
    return "\n".join(''.join("#" if (x,y) in grid else " " for x in range(width)) for y in range(height))

def part2(robots) -> None:
    minsize= None
    for i in itertools.count():
        p = plot(robots)
        size = len(gzip.compress(p.encode('utf8')))
        if minsize is None or size < minsize:
            minsize = size
            print("-"*75, size, i)
            print(p)
            print("-"*75)
        robots = [r.move(1) for r in robots]

robots = list(read_input())

print(part1(robots))
part2(robots)
