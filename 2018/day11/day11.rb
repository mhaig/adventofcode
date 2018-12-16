#!/usr/bin/env ruby

require 'matrix'

class Matrix
  def []=(i, j, x)
    @rows[i][j] = x
  end
end

def get_power_level(x, y, sn)

  rack_id = x + 10

  power_level = rack_id * y
  power_level = power_level + sn
  power_level = power_level * rack_id
  power_level = power_level.to_s.chars.map(&:to_i)[-3]
  power_level = power_level - 5

end

p get_power_level(3, 5, 8)
p get_power_level(122, 79, 57)
p get_power_level(217, 196, 39)
p get_power_level(101, 153, 71)

def get_max_sum_sub(matrix, k)

  return unless k < 300

  # 1. PREPROCESSING
  # To store sums of all strips of size k x 1.
  strip_sum = Matrix.zero(300)

  # Go column by column
  (0..299).each do |j|

    # Calculate sum of the first k x 1 rectangle in the column
    sum = 0
    (0...k).each do |i|
      sum += matrix[i, j]
    end
    strip_sum[0, j] = sum

    # Calculate sum of remaining rectangles
    (1...300-(k+1)).each do |i|
      sum += (matrix[i+k-1, j] - matrix[i-1, j])
      strip_sum[i, j] = sum
    end

  end

  max_sum = 0
  pos = []
  # 2. CALCULATE SUM of Sub-Squares using strip_sum[][]
  (0...300-(k+1)).each do |i|

    # Calculate and print sum of first subsquare in this row
    sum = 0
    (0...k).each do |j|
      sum += strip_sum[i, j]
    end

    # Update max_sum and position of result
    if sum > max_sum
      max_sum = sum
      pos = [i, 0]
    end

    # Calculate sum of remaining squares in current row by removing the leftmost
    # strip of previous sub-square and adding a new strip
    (1...300-(k+1)).each do |j|
      sum += (strip_sum[i, j+k-1] - strip_sum[i, j-1])
      if sum > max_sum
        max_sum = sum
        pos = [i,j]
      end
    end

  end

  return max_sum, pos
end

input = ARGF.read.split("\n").map(&:to_i)

input.each do |serial_number|

  m = Matrix.zero(300)
  (0...300).each do |x|
    (0...300).each do |y|

      m[x,y] = get_power_level(x, y, serial_number)

    end
  end

  # Sum all 3,3 matrices and add to a hash.
  x3_sums = {}

  0.step(297) do |x|
    0.step(297) do |y|

      x3_sums[[x,y]] = m.minor(x..x+2, y..y+2).reduce(:+)

    end
  end

  p x3_sums.max_by { |k,v| v }

  # Now the matrix size can change as well.  Run algorithm again looking for
  # best power.
  x3_sums = {}
  2.step(299) do |s|

    sum, pos = get_max_sum_sub(m, s)
    x3_sums[[pos[0],pos[1],s]] = sum

  end

  p x3_sums.max_by { |k,v| v }

end
