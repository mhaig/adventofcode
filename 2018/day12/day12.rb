#!/usr/bin/env ruby

input = ARGF.read.split("\n")

plants = []
key = Hash.new(".")

input.each do |i|

  next if i == ""

  if i =~ /initial state/
    plants = i.split(": ")[1].chars
    next
  end

  line_parts = i.split(" => ")
  key[line_parts[0]] = line_parts[1]

end

p key

def calculate_sum(plants, start)
  sum = 0
  plants.each do |p|
    sum += start if p == "#"
    start += 1
  end

  return sum
end

def run_algorithm(plants, key, generations)

  start = 0
  previous_sum = 0
  previous_sum_diff = 0
  pattern_count = 0
  sum = 0

  p "0 : #{plants.join('')}"

  generation = 1
  loop do

    next_plants = []
    if plants[0] == "#"
      plants.unshift(".", ".")
      start -= 2
    end
    plants.push(".", ".") if plants[-1] == "#"

    plants.each_with_index do |p, i|

      if i == 0
        pattern = plants[i..i+2]
        pattern.unshift(".", ".")
      elsif i == 1
        pattern = plants[i-1..i+2]
        pattern.unshift(".")
      else
        pattern = plants[i-2..i+2]

        while pattern.count < 5
          pattern.push(".")
        end
      end

      next_plants << key[pattern.join('')]

    end

    # p "%02d: #{next_plants.join('')}" % c
    plants = next_plants
    plants.push(".", ".")

    # Generate a sum for the generation and add to a hash table.
    sum = calculate_sum(plants, start)

    # Hints indicate some kind of pattern in the output but it does not appear
    # to be a repeating one.  Is it some pattern just in the sum value?
    diff = sum - previous_sum
    if diff == previous_sum_diff
      puts "Starting at #{generation}, sum is #{sum} and grows by #{diff}"
      pattern_count += 1

      break if pattern_count >= 5
    else
      pattern_count = 0
    end
    previous_sum_diff = diff
    previous_sum = sum

    # There is, seems to grow but a set value after a point.  Need to find the
    # point and the value it grows by for the math.

    break if generation == generations
    generation += 1

  end

  puts "Sum after 20 generations: #{calculate_sum(plants, start)}" if generations == 20

  puts "Sum after #{generations} generations: #{((generations - generation) * previous_sum_diff) + sum}"

end

run_algorithm(plants.dup, key, 20)
run_algorithm(plants.dup, key, 50000000000)
