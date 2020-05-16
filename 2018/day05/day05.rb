#!/usr/bin/env ruby

def is_upper? c
  /[[:upper:]]/.match(c)
end

def is_lower? c
  /[[:lower:]]/.match(c)
end

def is_throwaway?(a, b, match = nil)

  if a.downcase == b.downcase
    if (is_upper?(a) and is_lower?(b)) or
        (is_lower?(a) and is_upper?(b))
      return true
    end
  end

  false
end

def compute_polymer_length(polymer)

  new_array = []

  polymer.each do |c|

    if new_array.size == 0
      new_array << c
      next
    end

    # puts "test if #{c} == #{new_array[-1]}"
    if is_throwaway?(c, new_array[-1])
      new_array.pop
      next
    end

    new_array << c

  end

  new_array.size

end

input = ARGF.read.split("\n")


input.each do |i|

  # puts new_array
  puts compute_polymer_length(i.chars)

  lengths = {}
  ('a'..'z').each do |a|
    lengths[a] = compute_polymer_length(i.chars - [a.downcase] - [a.upcase])
  end

  p lengths

  p lengths.sort_by { |k, v| v }.first

end
