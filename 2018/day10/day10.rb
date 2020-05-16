#!/usr/bin/env ruby

class Point

  attr_accessor :x, :y

  def initialize(x, y, vx, vy)
    @x = x
    @y = y
    @vx = vx
    @vy = vy
  end

  def update_position(t)
    @x = @x + (@vx * t)
    @y = @y + (@vy * t)
  end
end

def print_array(point_array)

  # Find the start point of the grid.
  sorted_x = point_array.map { |p| p.x }.sort
  sorted_y = point_array.map { |p| p.y }.sort

  min_x = sorted_x.first - 1
  min_y = sorted_y.first - 1
  max_x = sorted_x.last + 1
  max_y = sorted_y.last + 1

  p "#{min_x}, #{min_y} #{max_x}, #{max_y}"

  (min_y..max_y).each do |y|
    (min_x..max_x).each do |x|
      if point_array.detect { |p| p.x == x and p.y == y }
        print "#"
      else
        print "."
      end
    end
    print "\n"
  end
end

input = ARGF.read.split("\n")

points = []
input.each do |i|

  position = i[/position=<(.*?)>/m, 1]
  velocity = i[/velocity=<(.*?)>/m, 1]

  points << Point.new(position.split(',')[0].to_i,
                      position.split(',')[1].to_i,
                      velocity.split(',')[0].to_i,
                      velocity.split(',')[1].to_i)

end

timer = 0
while (true)


  # See if a "bunch" of points have the same X value and close Ys.
  h = Hash.new(0)
  points.each { |p| h[p.x] += 1 }
  same_x = h.max_by { |k,v| v }
  # p points.select { |p| p.x == same_x }.sort{ |p| p.y }
  if same_x[1] >= 8

    # Make sure all the Y associated y values are 1 off.
    break if points.select {
      |p| p.x == same_x[0] }.map {
        |p| p.y }.sort.each_cons(2).all? {
          |a| (a[0] == a[1]) or (a[1] - a[0] == 1) }

  end

  points.each { |p| p.update_position(1) }
  timer += 1

end

p timer
print_array(points)
