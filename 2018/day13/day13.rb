#!/usr/bin/env ruby

class Cart
  TURN_STATES = [:left, :straight, :right]

  attr_accessor :x, :y, :direction, :mark_delete

  def initialize(x, y, direction)
    @x = x
    @y = y
    @direction = direction
    @turns = 0
    @mark_delete = false
  end

  def turn

    t = TURN_STATES[@turns % TURN_STATES.count]

    if @direction == "^"
      if t == :left
        @direction = "<"
      elsif t == :right
        @direction = ">"
      end
    elsif @direction == "v"
      if t == :left
        @direction = ">"
      elsif t == :right
        @direction = "<"
      end
    elsif @direction == "<"
      if t == :left
        @direction = "v"
      elsif t == :right
        @direction = "^"
      end
    elsif @direction == ">"
      if t == :left
        @direction = "^"
      elsif t == :right
        @direction = "v"
      end
    else
      p "Turn ERROR!"
      exit
    end

    @turns += 1

  end
end

class Map

  attr_accessor :rows, :columns, :map, :carts

  def initialize(columns, rows)
    @map = Hash.new(0)
    @rows = rows
    @columns = columns
    @carts = []
  end

  def show
    (0...@rows).each do |y|
      (0...@columns).each do |x|
        cart = @carts.select { |c| c.x == x and c.y == y }.first
        if cart
          print "#{cart.direction} "
        else
          print "#{@map[[x,y]]} "
        end
      end
      print ("\n")
    end
  end

  def row(index)
    @map.select { |k, v| k[1] == index }.values
  end

  def column(index)
    @map.select { |k, v| k[0] == index }.values
  end

  def [](x, y)
    @map[[x,y]]
  end

  def []=(x, y, v)
    @map[[x,y]] = v
  end

  def load_carts
    # Go row-by-row finding the carts and replacing with the correct map piece.
    return if carts.count > 0

    (0...@rows).each do |y|
      (0...@columns).each do |x|
        next unless ["<", ">", "v", "^"].include? self[x,y]

        @carts << Cart.new(x, y, self[x,y])
        case self[x,y]
        when "<", ">"
          self[x,y] = "-"
        when "v", "^"
          self[x,y] = "|"
        end
      end
    end
  end

  def collision?
    # Just detect if there are any carts occupying the same location.
    detected = @carts.group_by { |c| [c.x, c.y] }.any? { |k, v| v.size > 1 }

    # Mark the ones that crashed for deletion.
    crashed = @carts.group_by { |c| [c.x, c.y] }.select { |k, v| v.size > 1}
    crashed.values.each { |v| v.each { |c| c.mark_delete = true } }

    return detected
  end
end

class Point

  attr_accessor :x, :y

  def initialize(x, y)
    @x = x
    @y = y
  end
end

class Track

  attr_accessor :corner, :length_x, :length_y, :cart, :direction

  def initialize(corner, length_x, length_y, cart, direction)
    @corner = corner
    @length_x = length_x
    @length_y = length_y
    @cart = cart
    @direction = direction
  end
end

def find_cart(map, corner, length_x, length_y)

  # Navigate track looking for the cart (<, >, V, ^)

  [corner.x, corner.x + length_x].each do |x|
    (corner.y...(corner.y + length_y)).each do |y|
      if ["<", ">", "v", "^"].include? map[x, y]
        p "Found cart at #{x},#{y}"
        return Point.new(x, y), map[x,y]
      end
    end
  end

  (corner.x...(corner.x + length_x)).each do |x|
    [corner.y, corner.y + length_y].each do |y|
      if ["<", ">", "v", "^"].include? map[x, y]
        p "Found cart at #{x},#{y}"
        return Point.new(x, y), map[x,y]
      end
    end
  end

  return nil, nil

end

input = ARGF.read.split("\n")

rows = input.count
columns = input.map(&:length).max
p columns
p rows

map = Map.new(columns, rows)

(0...map.columns).each do |x|
  (0...map.rows).each do |y|
    map.map[[x,y]] = input[y][x]
  end
end

# p map
# map.show

track_list = []

# Go row by row through the input looking for upper left corners of tracks.
(0...map.rows).each do |r|

  row = map.row(r)

  length_x = 0
  length_y = 0

  corner = nil
  (0...columns).each do |c|

    if row[c] == "/" and ["|", "+"].include? map[c,r+1]
      p "Found a corner at #{c}, #{r}"
      corner = Point.new(c, r)

      # Find the length in y by looking in this column for '\'.
      column = map.column(c)
      length_y = column.each_with_index.select { |e, i| e == '\\' and i > r }.first[1]

    end

    if row[c] == '\\' and corner
      # Calculate length in x for this track.
      length_x = c - corner.x
    end

    if corner and length_x > 0 and length_y > 0
      # Got an entire track.
      # Find the cart
      cart, direction = find_cart(map, corner, length_x, length_y)
      p cart, direction
      track_list << Track.new(corner, length_x, length_y, cart, direction)
      p "Done with #{corner}"
      corner = nil
    end

  end

end

p track_list

map.load_carts
# map.show

# I think I over-complicated the solution, at least to part 1.  For Part 1 try
# just iterating the carts following the turn rules and detecting a collision.
counter = 0
first_crash = false
loop do

  counter += 1
  # map.show
  # p "Turn #{counter}"
  map.carts.sort_by! { |c| [c.y, c.x] }
  map.carts.each_with_index do |cart, index|

    x = cart.x
    y = cart.y

    if cart.direction == "^"
      cart.y -= 1

      # First check for a collision
      if map.collision? and not first_crash
        p "First collision! #{x}, #{y-1}"
        first_crash = true
        next
      end

      if map[x,y-1] == "/"
        cart.direction = ">"
      elsif map[x,y-1] == "\\"
        cart.direction = "<"
      elsif map[x,y-1] == "+"
        cart.turn
      elsif not map[x,y-1] == "|"
        p "Up ERROR!"
        exit
      end
    elsif cart.direction == "v"
      cart.y += 1

      # First check for a collision
      if map.collision? and not first_crash
        p "First collision! #{x}, #{y+1}"
        first_crash = true
        next
      end

      if map[x,y+1] == "/"
        cart.direction = "<"
      elsif map[x,y+1] == "\\"
        cart.direction = ">"
      elsif map[x,y+1] == "+"
        cart.turn
      elsif not map[x,y+1] == "|"
        p "Down ERROR!"
        exit
      end
    elsif cart.direction == "<"
      cart.x -= 1

      if map.collision? and not first_crash
        p "First collision! #{x-1}, #{y}"
        first_crash = true
        next
      end

      if map[x-1,y] == "/"
        cart.direction = "v"
      elsif map[x-1,y] == "\\"
        cart.direction = "^"
      elsif map[x-1,y] == "+"
        cart.turn
      elsif not map[x-1,y] == "-"
        p "Left ERROR! #{map[x-1,y]} in next space!"
        exit
      end
    elsif cart.direction == ">"
      cart.x += 1

      if map.collision? and not first_crash
        p "First collision! #{x+1}, #{y}"
        first_crash = true
        next
      end

      if map[x+1,y] == "/"
        cart.direction = "^"
      elsif map[x+1,y] == "\\"
        cart.direction = "v"
      elsif map[x+1,y] == "+"
        cart.turn
      elsif not map[x+1,y] == "-"
        p "Right ERROR!"
        exit
      end
    end

  end

  map.carts.delete_if { |c| c.mark_delete }

  if map.carts.count == 1
    p "One cart left!"
    p map.carts
    # map.show
    break
  end

end
