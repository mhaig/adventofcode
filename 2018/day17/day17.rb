#!/usr/bin/env ruby

def get_xy(parts)

  x = 0
  y = 0

  parts.each do |p|
    letter = p.split('=')[0]
    numbers = p.split('=')[1].split("..")

    if letter == "x"
      p numbers
      x = numbers.map(&:to_i)
    else
      y = numbers.map(&:to_i)
    end

  end

  return x, y

end

def print_map(m)

  p m

  min_x = m.keys.map { |a| a[0] }.sort.first - 1
  max_x = m.keys.map { |a| a[0] }.sort.last + 1
  min_y = m.keys.map { |a| a[1] }.sort.first
  max_y = m.keys.map { |a| a[1] }.sort.last

  p "min_x #{min_x} max_x #{max_x} min_y #{min_y} max_y #{max_y}"

  (min_y..max_y).each do |y|
    row = ''
    (min_x..max_x).each do |x|
      row += m[[x,y]]
    end
    print(row + "\n")
  end

end

input = ARGF.read.split("\n")

map = Hash.new(".")

input.each do |i|

  p i.split(',').map(&:strip)

  x, y = get_xy(i.split(',').map(&:strip))

  # x.each do |a|
  #   y.each do |b|
  #     map[[a, b]] = "#"
  #   end
  # end

  if x.count > 1
    (x[0]..x[1]).each do |a|
      map[[a, y[0]]] = "#"
    end
  else
    (y[0]..y[1]).each do |a|
      map[[x[0], a]] = "#"
    end
  end

end

# Add the water.
water_x = 500
water_y = 0
map[[water_x, water_y]] = "+"

print_map(map)

# Now let the water go.
while (1)

  (min_y..max_y).each do |y|



  end

end
