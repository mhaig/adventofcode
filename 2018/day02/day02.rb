#!/usr/bin/env ruby

input = ARGF.read.split("\n")

puts input.length

# For each input, create a hash of each letter with the count of times it
# appears.  Then look through the hash to see if it has any exactly 2 or exactly
# 3 repeating characters.

def count_letters(s)
  Hash[s.delete(' ').split('').group_by{ |c| c }.map{ |k, v| [k, v.size] }]
end

twos = 0
threes = 0

input.each do |id|

  counts = count_letters(id)
  twos = twos + 1 if counts.detect { |k, v| v == 2 }
  threes = threes + 1 if counts.detect { |k, v| v == 3 }

end

puts "checksum: #{twos * threes}"

def common_letters(s1, s2)

  common = []

  s1.split('').zip(s2.split('')).each do |a, b|
    if a == b
      common << a
    else
      common << " "
    end
  end

  return common.join('')
end

found = false
input.each do |id|

  input.each do |id2|

    next if id == id2

    common = common_letters(id, id2)

    next unless common.scan(' ').count == 1

    # Found two IDs with only one difference (white space)
    puts "Correct box IDs: #{id} and #{id2}!"
    puts "Minus difference: #{common}"
    puts "(for game input: #{common.delete(' ')})"
    found = true

  end

  if found then break end
end
