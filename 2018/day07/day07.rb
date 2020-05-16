#!/usr/bin/env ruby

input = ARGF.read.split("\n")

# Turn the input steps into a hash.
$instructions = {}
input.each do |i|

  key = i.split(' ')[1]

  if $instructions[key]
    $instructions[key] << i.split(' ')[-3]
  else
    $instructions[key] = [i.split(' ')[-3]]
  end

end

ifs = $instructions.keys.uniq
thens = $instructions.values.flatten.uniq

non_blocked_steps = ifs - thens

# Sort the arrays in the hash first.
$instructions.each { |k, v| v.sort! }

# At this point we have a hash of KEY must be finished before VALUE.  The VALUE
# is an array when multiple things can be run.
# Also have the first letter.
#
# How to traverse the steps though when multiple things need to be done and you
# could have to "go back".

# Start with the "start_step" and build a list of possible next steps based on
# what has been completed.
#
# Each loop take the first possible_step, add possible steps, sort, and
# continue.
correct_order = []

def get_possible_next_steps(done_steps)
  # Possible next steps from here are any value of the start_step key that are not
  # also values of another key that is not in correct_order and not already in
  # correct_order.

  return unless $instructions[done_steps[-1]]

  $instructions[done_steps[-1]].select do |pns|

    next false if done_steps.include?(pns)

    next true if $instructions.all? do |k, v|
      if v.include?(pns)
        if done_steps.include?(k)
          next true
        else
          next false
        end
      else
        next true
      end
    end

    next false

  end

end

next_list = non_blocked_steps.sort

while next_list.count > 0

  correct_order << next_list.delete_at(0)

  possible_next_steps = get_possible_next_steps(correct_order)
  next_list += possible_next_steps if possible_next_steps

  next_list.sort!

end

p correct_order.join('')

correct_order = []
# Approach here is similar except steps go from next_list into worker queues and
# then into correct_order.
next_list = non_blocked_steps.sort

workers = {0 => nil, 1 => nil, 2 => nil, 3 => nil, 4 => nil}

timer = 0

while true

  # First tick the clock and move tasks as appropriate.
  (0...workers.count).each do |i|
    next unless workers[i]

    workers[i][1] -= 1
    if workers[i][1] == 0
      correct_order << workers[i][0]
      workers[i] = nil
    end
  end

  # Build available task list.
  possible_next_steps = get_possible_next_steps(correct_order)
  next_list += possible_next_steps if possible_next_steps

  next_list.sort!
  # Remove any tasks in work!
  next_list -= workers.values.map{ |v| v[0] if v }

  # Try to assign the list to workers.
  (0...workers.count).each do |i|

    break unless next_list.count > 0
    next if workers[i]

    task = next_list.delete_at(0)
    workers[i] = [task, task.ord - 'A'.ord + 1 + 60]

  end

  # p "#{timer}: #{workers}"

  # See if we're done
  break if workers.values.all? { |v| v == nil }

  timer += 1
end

p timer
