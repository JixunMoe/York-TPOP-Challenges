#!/usr/bin/env python3

import struct, turtle, os
from collections import namedtuple

__DEBUG__ = 0

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
    turtle.tracer(__DEBUG__)

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
    t.setposition(self.size / 2, -self.size / 2 - 4)
    t.write('S', False, 'center')

    # Draw E
    t.setposition(mh.width * self.size - self.size / 2, -self.size * mh.height + self.size / 2)
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
        if __DEBUG__:
          pos_cell = t.pos()
          t.penup()
          t.setheading(0)
          t.forward(self.size / 2)
          t.right(90)
          t.forward(self.size)
          t.write(str(cell))
          t.setpos(pos_cell)

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

maze = Maze()
maze.load_maze('./data/sample1.maze')

turtle.mainloop()