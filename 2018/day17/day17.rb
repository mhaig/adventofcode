#!/usr/bin/env ruby

class Map

  def initialize
    @map = Hash.new('.')
    @rows = 0
    @columns = 0
    @start_column = nil
  end

  def show
    (0...self.row_count).each do |y|
      (self.start_column...self.column_count+self.start_column).each do |x|
        print "#{self[x,y]}"
      end
      print "\n"
    end
  end

  def row(index)
    @map.select { |k, v| k[1] == index}.values
  end

  def [](x, y)
    @map[[x,y]]
  end

  def []=(x, y, v)
    @map[[x,y]] = v
  end

  def row_count
    load_row_column
    @rows
  end

  def start_column
    load_row_column
    @start_column
  end

  def column_count
    @columns
  end

  def start_column
    @start_column
  end

  def water_at_row(row)
    @map.select { |k, v| v == "|" or v == "+" and k[1] == row }.keys.map { |k| k[0] }
  end

  def count_water
    @map.count { |k,v| v == "|" or v == "~" }
  end

  private
  def load_row_column
    if @rows == 0
      sorted_rows = @map.keys.sort_by { |k| k[1] }
      @rows = sorted_rows.last[1] - sorted_rows.first[1] + 1
    end

    if @columns == 0
      sorted_columns = @map.keys.sort_by { |k| k[0] }
      @columns = sorted_columns.last[0] - sorted_columns.first[0] + 1
      if not @start_column
        @start_column = sorted_columns.first[0]
      end
    end

  end

end

def get_xy(parts)

  x = 0
  y = 0

  parts.each do |p|
    letter = p.split('=')[0]
    numbers = p.split('=')[1].split("..")

    if letter == "x"
      x = numbers.map(&:to_i)
    else
      y = numbers.map(&:to_i)
    end

  end

  return x, y

end

input = ARGF.read.split("\n")

map = Map.new

input.each do |i|

  p i.split(',').map(&:strip)

  x, y = get_xy(i.split(',').map(&:strip))

  if x.count > 1
    (x[0]..x[1]).each do |a|
      map[a, y[0]] = "#"
    end
  else
    (y[0]..y[1]).each do |a|
      map[x[0], a] = "#"
    end
  end

end

def blank? block
  block == "."
end

def clay? block
  block == "#"
end

def water? block
  block == "|"
end

def standing_water? block
  block == "~"
end

def clay_or_water? block
  clay?(block) or standing_water?(block) or water?(block)
end

def clay_or_standing_water? block
  clay?(block) or standing_water?(block)
end

# Add the water.
map[500, 0] = "+"

map.show

# Now let the water go.
current_row = 1

loop do

  puts "At row #{current_row}"
  forward = false
  puts "There is water at columns: #{map.water_at_row(current_row - 1)}"
  fetched_row = current_row - 1
  map.water_at_row(current_row - 1).each do |wx|

    current_row += 1 if current_row == fetched_row

    # puts "Working on water at column #{wx}"
    # puts "looking at row #{current_row} for decision"

    # Iterating on a list of water sources from previous row.

    if blank? map[wx, current_row]
      puts "Adding water!"
      map[wx, current_row] = "|"
      forward = true
    elsif clay_or_standing_water? map[wx, current_row]
      # puts "Hit sand or existing water!"
      converted_to_water = []
      left_blocked = false
      right_blocked = false
      # Hit clay or standing water, move up a row and spread to the left until
      # clay is hit or no more clay or standing water below.
      current_column = wx - 1
      current_row -= 1
      loop do
        if not clay_or_water? map[current_column, current_row]
          map[current_column, current_row] = "|"
          converted_to_water << [current_column, current_row]
          current_column -= 1
          # See if there is still clay below.
          if blank? map[current_column, current_row + 1]
            map[current_column, current_row] = "|"
            forward = true
            break
          end
        else
          # Hit clay, stop going left.
          left_blocked = true
          break
        end
      end
      # Repeat above but go right.
      current_column = wx + 1
      loop do
        if not clay_or_water? map[current_column, current_row]
          map[current_column, current_row] = "|"
          converted_to_water << [current_column, current_row]
          current_column += 1
          # See if there is still water below.
          if blank? map[current_column, current_row + 1]
            map[current_column, current_row] = "|"
            forward = true
            break
          end
        else
          # Hit clay, stop going right.
          right_blocked = true
          break
        end
      end
      if right_blocked and left_blocked
        # Switch all new water to "~".
        converted_to_water.each { |c| map[c[0], c[1]] = "~" }
        map[wx, current_row] = "~"
      end
    end

  end

  current_row += 1 if forward

  # map.show

  break if current_row == map.row_count

end

map.show

# Count all water.
puts map.count_water

