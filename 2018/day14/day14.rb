#!/usr/bin/env ruby

class Recipe

  attr_accessor :score, :prev, :next

  def initialize(score)
    score = score.to_i if score.kind_of? String
    @score = score
  end

end

def print_list(head, tail)

  current = head

  loop do

    printf("#{current.score} ")
    current = current.next

    break if current == head
  end

  printf("\n")

end

input_string = ARGF.read.split("\n")[0]
input = input_string.to_i

# Add the first two recipes
first = Recipe.new(3)
second = Recipe.new(7)

first.next = second
first.prev = second
second.next = first
second.prev = first

head = first
tail = second

elf1 = first
elf2 = second

list_size = 2
part1 = true
part2 = true

count = 0
ahead = head
digits_to_get = input_string.chars.count
ahead_array = []

loop do

  # Sum elf1 and elf2 and create new recipes based on the digits.
  new_recipes = (elf1.score + elf2.score).to_s.chars.map{ |s| Recipe.new(s) }
  new_recipes.each do |r|

    tail.next = r
    r.prev = tail
    r.next = head
    head.prev = r

    tail = r
    list_size += 1

  end

  # Move the elfs
  (0..elf1.score).each { elf1 = elf1.next }
  (0..elf2.score).each { elf2 = elf2.next }

  # print_list(head, tail)
  # p "#{list_size} >= #{input + 10}"

  if list_size >= (input + 10) and part1
    # Entire list for this part built.
    # Move the current position to input + 10.
    current = tail
    (0...(list_size - (input + 10))).each { current = current.prev }

    # Get the score by grabbing recipe scores from tail
    # backwards 10.
    final_score = []
    (0...10).each do
      final_score.unshift(current.score.to_s)
      current = current.prev
    end
    p final_score.join('')
    part1 = false
  end

  # Part 2 is slow.  See if there is a way to speed this up.  Some kind of
  # static memory instead of arrays and strings, etc.
  if list_size > digits_to_get and part2
    if ahead_array.count == 0
      p list_size
      p digits_to_get
      (0...digits_to_get).each do
        ahead_array << ahead.score
        ahead = ahead.next
        if ahead == head
          p "fail first!"
          exit
        end
      end
    else
      # Drop out the first element of array.
      ahead_array.delete_at(0)
      # Get ahead
      ahead_array << ahead.score
      # Move ahead
      ahead = ahead.next
      if ahead == head
        p "fail second!"
        exit
      end
      count += 1
    end
    if ahead_array.join('') == input_string
      p count
      part2 = false
    end
  end

  break unless (part1 or part2)

end
