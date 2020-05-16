#!/usr/bin/env ruby

input = ARGF.read.split("\n")

puts input.length

# Find the final frequency of the input.
initial_frequency = 0
input.each do |change|

  initial_frequency += change[1..-1].to_i if change[0] == '+'
  initial_frequency -= change[1..-1].to_i if change[0] == '-'

end

puts initial_frequency

# Now find the first frequency that is reached twice.
initial_frequency = 0
frequency_list = {}
index = 0
loop do

  change = input[index]

  initial_frequency += change[1..-1].to_i if change[0] == '+'
  initial_frequency -= change[1..-1].to_i if change[0] == '-'

  if frequency_list.has_key? initial_frequency
    puts initial_frequency
    break
  end

  frequency_list[initial_frequency] = initial_frequency
  index = (index + 1) % input.length

end
