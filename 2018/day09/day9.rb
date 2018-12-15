#!/usr/bin/env ruby

input = ARGF.read.split("\n")

input.each do |i|

  players = i.split(' ')[0].to_i
  marbles = i.split(' ')[-2].to_i

  scores = Hash.new(0)
  current_marble = 0
  field = []

  field << 0
  current_marble += 1
  position = 0

  while current_marble <= marbles

    (1..players).each do |p|

      if current_marble % 23 == 0
        # Special rule if current marble is a multiple of 23.
        # Player gets to keep this marble:
        scores[p] += current_marble

        # The marble 7 marbles counter-clockwise from the current marble is
        # removed and the points given to the player.
        position -= 7
        position += field.count if position < 0
        scores[p] += field.delete_at(position)

        # Position becomes the center for the next marble.
        current_marble += 1

        break if current_marble > marbles
        next
      end

      # Marble gets inserted at index of last marble plus 2 but wrapped around
      # if greater than current count.
      position += 2
      position -= field.count if position > field.count
      field.insert(position, current_marble)
      current_marble += 1

      break if current_marble > marbles

      # spinner = Enumerator.new do |e|
      #   loop do
      #     e.yield '|'
      #     e.yield '/'
      #     e.yield '-'
      #     e.yield '\\'
      #   end
      # end

      percentage = ((current_marble/marbles) * 100)
      if percentage % 5 == 0 and percentage > 0
        # progress = "=" * percentage
        # printf("\rCombined: [%-20s] %d%% %s", progress, percentage, spinner.next)
        puts percentage
      end

    end

  end
  puts
  p scores.max_by { |k,v| v }

end
