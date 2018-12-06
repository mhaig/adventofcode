#!/usr/bin/env ruby

input = ARGF.read.split("\n")

sorted_entries = []
input.each do |entry|

  sorted_entries << [entry[1..16], entry[19..-1]]

end

sorted_entries.sort_by! { |entry| entry[0] }

class Shift

  def initialize(id)
    @id = id.to_i
    @minutes = Array.new(60)
  end

  def add_sleep_time(start_time, stop_time)

    (start_time...stop_time).each do |time|
      @minutes[time] = "#"
    end

  end

  def sleep_time
    @minutes.count("#")
  end

  attr_reader :id, :minutes
end

shifts = []

shift = nil
sleep_start = 0
sleep_end = 0

sorted_entries.each do |entry|

  if entry[1] =~ /Guard/
    shifts << shift if shift
    shift = Shift.new(entry[1].split(' ')[1].delete('#'))
  elsif entry[1] =~ /falls/
    sleep_start = entry[0].split(' ')[1].split(':')[1].to_i
  elsif entry[1] =~ /wakes/
    sleep_end = entry[0].split(' ')[1].split(':')[1].to_i
    shift.add_sleep_time(sleep_start, sleep_end)
  end

end

# Find the guard with the most total time slept.
guard_sleep = Hash.new(0)
shifts.each { |s| guard_sleep[s.id] += s.sleep_time }

# Sort the shifts by sleep time to find the guard who slept the most.
guard_id = guard_sleep.sort_by { |k,v| v }.last[0]

guard_minutes = Hash.new(0)
# Find what minute he was asleep the most.
shifts.select { |s| s.id == guard_id }.each do |s|

  (0...60).each do |m|
    guard_minutes[m] += 1 if s.minutes[m] == '#'
  end

end

answer_minutes = guard_minutes.sort_by { |k, v| v }.last[0]

puts "Answer #{guard_id * answer_minutes}"

# Now find what guard spent what minute the most asleep.
guard_minute = Hash.new(0)
shifts.each do |s|

  (0...60).each do |m|
    guard_minute[[s.id, m]] += 1 if s.minutes[m] == '#'
  end

end
answer = guard_minute.sort_by { |k, v| v }.last
puts "Answer: #{answer[0][0] * answer[0][1]}"
