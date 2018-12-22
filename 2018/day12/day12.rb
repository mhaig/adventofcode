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

p plants
p key

def run_algorithm(plants, key, generations)
  start = 0
  p "0 : #{plants.join('')}"
  (1..generations).each do |c|

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

    if c % 1000 == 0
      p c
    end

    # p "%02d: #{next_plants.join('')}" % c
    plants = next_plants
    plants.push(".", ".")

  end

  sum = 0
  plants.each do |p|

    sum += start if p == "#"
    start += 1

  end
  p sum
end

run_algorithm(plants, key, 20)
run_algorithm(plants, key, 50000000000)
