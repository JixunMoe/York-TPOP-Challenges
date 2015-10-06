#!/usr/bin/env python3

import struct, turtle, os
from collections import namedtuple

MazeHeader = namedtuple('MazeHeader', 'magic width height')

class NotValidMazeFileException(Exception): pass

class Maze():
  def __init__(self):
    self.turtle = turtle.Turtle()
    self.turtle.hideturtle()
    self.struct_header = '>III'
    self.size = 40
    self.mh = None
    self.reset()
    turtle.tracer(False)

  def reset(self):
    self.maze = []

  def load_maze(self, path):
    turtle.title('Maze: %s' % os.path.basename(path))
    with open(path, 'rb') as f:
      header = f.read(struct.calcsize(self.struct_header))
      mh = MazeHeader._make(struct.unpack(self.struct_header, header))
      self.mh = mh
      if mh.magic != 0x4D5A4500:
        raise NotValidMazeFileException('Magic incorrect: Not a Maze file.')

      self.reset()
      for row in range(mh.height):
        row = f.read(mh.width)
        if len(row) != mh.width:
          raise NotValidMazeFileException('Unexpected EOF in maze file.')
        self.maze.append(row)

    self.print_maze()

  def set_pen_mode(self, mode):
    if mode:
      self.turtle.pendown()
    else:
      self.turtle.penup()

  def fill_square(self, color, pos):
    t = self.turtle
    c = t.color()
    h = t.heading()
    p = t.pos()

    t.setheading(0)
    t.color('white', color)
    t.setposition(pos)
    t.begin_fill()
    for x in range(4):
      t.forward(self.size)
      t.right(90)
    t.end_fill()

    t.setposition(p)
    t.setheading(h)
    t.color(c[0], c[1])

  def print_maze(self):
    mh = self.mh
    t = self.turtle
    t.reset()
    t.penup()

    self.fill_square('lightblue', (0, 0))
    self.fill_square('lightcoral',  (mh.width * self.size - self.size, self.size - mh.height * self.size))

    # Draw S
    #t.setheading(270)
    t.setposition(6, -18)
    t.write('S', False)

    # Draw E
    t.setposition(mh.width * self.size - 8, -self.size * mh.height + 2)
    t.write('E', False, 'center')

    t.setposition(0, 0)
    t.setheading(0)
    t.pendown()
    sizes = (mh.width, mh.height)


    # Draw the outside border
    for x in range(4):
      t.forward(self.size * sizes[x % 2])
      t.right(90)

    # Paint row
    for row in range(mh.height):
      pos_row = t.pos()

      row = self.maze[row]
      # Paint cell
      for cell in row:
        t.setheading(0)
        t.forward(self.size)
        pos_cell = t.pos()

        for i in [1, 2]:
          t.right(90)
          self.set_pen_mode(cell & i)
          t.forward(self.size)

        t.penup()
        t.setpos(pos_cell)

      t.penup()
      t.setpos(pos_row)
      t.setheading(270)
      t.forward(self.size)

  def is_pos_valid(self, pos):
    return False if -1 in pos else (pos[0] < self.mh.width) and (pos[1] < self.mh.height)


  def can_I_go(self, pos, direction):
    if not self.is_pos_valid(pos): return False

    if direction is 'left':
      return self.can_I_go((pos[0] - 1, pos[1]), 'right')
    elif direction is 'up':
      return self.can_I_go((pos[0], pos[1] - 1), 'down')
    elif direction is 'down':
      return not (self.maze[pos[1]][pos[0]] & 2)
    elif direction is 'right':
      return not (self.maze[pos[1]][pos[0]] & 1)
    else:
      return False


  def solve(self):
    mh = self.mh
    target = (mh.width - 1, mh.height - 1)
    # Find best route first!
    rules = [
      {
        'direction': 'up',
        'offset': [0, -1]
      },
      {
        'direction': 'down',
        'offset': [0, +1]
      },
      {
        'direction': 'left',
        'offset': [-1, 0]
      },
      {
        'direction': 'right',
        'offset': [+1, 0]
      }
    ]
    routes = []
    next_routes = [(0, 0)]
    sandbox = [[0] * mh.width for i in range(mh.height)]
    sandbox[0][0] = 1

    found_route = False
    for i in range(16):
      routes.append(next_routes)
      nodes = []
      for node in next_routes:
        for rule in rules:
          pos_after = (node[0] + rule['offset'][0], node[1] + rule['offset'][1], node)
          if not self.is_pos_valid(pos_after):
            continue

          if sandbox[pos_after[0]][pos_after[1]]:
            continue

          if self.can_I_go(node, rule['direction']):
            sandbox[pos_after[0]][pos_after[1]] = 1
            nodes.append(pos_after)
            if pos_after[0] == target[0] and pos_after[1] == target[1]:
              found_route = pos_after
              break

      if found_route: break

      next_routes = nodes

    if found_route:
      result = []
      print('Found a route!')
      print(found_route)
      while 1:
        result.append((found_route[0], found_route[1]))
        if len(found_route) != 3:
          result.reverse()
          self.draw_solution(result)
          break
        found_route = found_route[2]

  def move_to_pos(self, t, pos):
    t.setposition(pos[0] * self.size + self.size / 2, -(pos[1] * self.size + self.size / 2))

  def draw_solution(self, points):
    turtle.tracer(True)
    t = turtle.Turtle()
    t.reset()
    t.color('red', 'white')
    t.pensize(5)
    t.penup()
    t.hideturtle()
    self.move_to_pos(t, points[0])
    t.pendown()
    for pt in points:
      self.move_to_pos(t, pt)


maze = Maze()
maze.load_maze('./data/sample1.maze')

# TODO: More reasonable code
maze.solve()

turtle.mainloop()