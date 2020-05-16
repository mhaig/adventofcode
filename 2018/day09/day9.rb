#!/usr/bin/env ruby

class Marble

  attr_accessor :points, :next, :prev

  def initialize(number, previous_marble=nil, next_marble=nil)
    @points = number
    @next = next_marble
    @prev = previous_marble
  end
end

def insert(current, new)

  # Save current next.
  tmp_next = current.next

  current.next = new
  new.prev = current
  new.next = tmp_next
  tmp_next.prev = new

end

def print(start)

  start_save = start
  a = start

  p_array = []
  loop do
    p_array << a.points
    a = a.next
    break if a == start_save
  end

  p p_array

end

input = ARGF.read.split("\n")

input.each do |i|

  players = i.split(' ')[0].to_i
  marbles = i.split(' ')[-2].to_i

  scores = Hash.new(0)
  current_marble = 0

  head = Marble.new(0)
  head.next = head
  head.prev = head
  position = head

  current_marble += 1

  while current_marble <= marbles

    (1..players).each do |p|

      if current_marble % 23 == 0
        # Special rule if current marble is a multiple of 23.
        # Player gets to keep this marble:
        scores[p] += current_marble

        # The marble 7 marbles counter-clockwise from the current marble is
        # removed and the points given to the player.
        (1...7).each do
          position = position.prev
        end

        # p position.points
        scores[p] += position.points
        tmp_prev = position.prev
        tmp_next = position.next
        tmp_next.prev = tmp_prev
        tmp_prev.next = tmp_next

        # Position becomes the center for the next marble.
        current_marble += 1

        break if current_marble > marbles
        next
      end

      # Marble gets inserted at index of last marble plus 2 but wrapped around
      # if greater than current count.
      # Move ahead two marbles in list.
      position = position.next
      position = position.next

      insert(position, Marble.new(current_marble))

      # print(head)

      current_marble += 1

      break if current_marble > marbles

    end

  end

  p scores.max_by { |k,v| v }

end
