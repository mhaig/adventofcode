#!/usr/bin/env ruby

def manhattan_distance(x1, y1, x2, y2)

  (x1 - x2).abs + (y1 - y2).abs

end

def closest_coordinate(coordinates, x, y)

  # With a point, find the closest point based on Manhattan distance.
  distances = coordinates.map { |c| manhattan_distance(c[0], c[1], x, y) }

  sorted = distances.sort

  if sorted[0] == sorted[1]
    return -1
  end

  distances.find_index(sorted.first)

end

input = ARGF.read.split("\n")

# Find the max x, y of input to build grid.  For now treat it as a square grid
# so just find the largest number.
xs = input.map { |a| a.split(", ")[0].to_i }
ys = input.map { |a| a.split(", ")[1].to_i }

corner = (xs + ys).sort.last

p corner

grid = {}
coordinates = xs.zip(ys)



(-1..(corner + 1)).each do |x|
  (-1..(corner + 1)).each do |y|

    grid[[x,y]] = closest_coordinate(coordinates, x, y) + 1

  end
end

count_hash = Hash.new(0)
grid.each do |k, v|

  count_hash[v] += 1

end
p count_hash

infinite_coordinates = []
# Coordinates are infinite if they appear on the -1 or corner + 1.
(-1..(corner + 1)).each do |p|

  infinite_coordinates << grid[[-1, p]]
  infinite_coordinates << grid[[corner + 1, p]]

  infinite_coordinates << grid[[p, -1]]
  infinite_coordinates << grid[[p, corner + 1]]

end

infinite_coordinates.uniq!

p infinite_coordinates

count_hash.delete_if { |k, v| infinite_coordinates.include?(k) }
p count_hash.sort_by { |k, v| v }

# Part 2...
def within_10000?(coordinates, x, y)

  coordinates.reduce(0) { |sum, c| sum + manhattan_distance(c[0], c[1], x, y) } < 10000

end

grid = Hash.new(0)
(0..corner).each do |x|
  (0..corner).each do |y|

    grid[[x,y]] = within_10000?(coordinates, x, y) ? 1 : 0

  end
end

p grid.values.reduce(:+)
