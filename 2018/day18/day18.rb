#!/usr/bin/env ruby

OPEN_AREA = "."
TREES = "|"
LUMBERYARD = "#"

def print_area(area)

  min_x = area.keys.map { |a| a[0] }.sort.first
  max_x = area.keys.map { |a| a[0] }.sort.last
  min_y = area.keys.map { |a| a[1] }.sort.first
  max_y = area.keys.map { |a| a[1] }.sort.last

  (min_y..max_y).each do |y|
    row = ''
    (min_x..max_x).each do |x|
      row += area[[x,y]]
    end
    print(row + "\n")
  end

end

def get_adjacent_counts(area, x, y)
  adjacent = []
  (-1..1).each do |xo|
    (-1..1).each do |yo|
      next if xo == 0 and yo == 0
      adjacent << area[[x+xo, y+yo]]
    end
  end
  Hash.new(0).tap { |h| adjacent.each { |a| h[a] += 1 } }
end

input = ARGF.read.split("\n")

lumber_area = {}

input.each_with_index do |i, y|

  i.chars.each_with_index do |c, x|

    lumber_area[[x, y]] = c

  end

end

print_area(lumber_area)

def solve_puzzle(lumber_area, mins)

  min_x = lumber_area.keys.map { |a| a[0] }.sort.first
  max_x = lumber_area.keys.map { |a| a[0] }.sort.last
  min_y = lumber_area.keys.map { |a| a[1] }.sort.first
  max_y = lumber_area.keys.map { |a| a[1] }.sort.last

  (1..mins).each do |minute|

    new_lumber_area = {}

    (min_y..max_y).each do |y|
      (min_x..max_x).each do |x|

        adj = get_adjacent_counts(lumber_area, x, y)

        if lumber_area[[x,y]] == OPEN_AREA
          # Check the adjacent area.  If 3 or more acres are TREES, it becomes a
          # tree.
          if adj[TREES] >= 3
            new_lumber_area[[x,y]] = TREES
          else
            new_lumber_area[[x,y]] = OPEN_AREA
          end
        elsif lumber_area[[x,y]] == TREES
          # Check the adjacent area.  If 3 or more acres are LUMBERYARD, it
          # becomes a LUMBERYARD.
          if adj[LUMBERYARD] >= 3
            new_lumber_area[[x,y]] = LUMBERYARD
          else
            new_lumber_area[[x,y]] = TREES
          end
        else # LUMBERYARD
          # If it is adjacent to one other LUMBERYARD and one TREE it stays a
          # LUMBERYARD.
          if adj[LUMBERYARD] >= 1 and adj[TREES] >= 1
            new_lumber_area[[x,y]] = LUMBERYARD
          else
            new_lumber_area[[x,y]] = OPEN_AREA
          end
        end

      end
    end

    lumber_area = new_lumber_area

  end

  p lumber_area.values.count(LUMBERYARD) * lumber_area.values.count(TREES)
end

solve_puzzle lumber_area, 10
solve_puzzle lumber_area, 1000000000
