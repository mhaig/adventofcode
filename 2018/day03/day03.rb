#!/usr/bin/env ruby

class Claim
  def initialize(s)
    # A claim looks like: #1 @ 1,3: 4x4
    # Parse into applicable sections for processing.
    @id = s.split(' ')[0][1..-1]
    @x = s.split(' ')[2].split(',')[0].to_i
    @y = s.split(' ')[2].split(',')[1].delete(':').to_i
    @x_size = s.split(' ')[-1].split('x')[0].to_i
    @y_size = s.split(' ')[-1].split('x')[1].to_i
    @overlap = false
  end

  attr_reader :id, :x, :y, :x_size, :y_size, :overlap
  attr_writer :overlap
end

input = ARGF.read.split("\n")

fabric = Hash.new(0)

claims = input.map{ |i| Claim.new(i) }

p claims.count

claims.each do |claim|

  # Fill the claim into the fabric.

  # First build a local hash table of the claim itself.
  claim_hash = {}
  (0...claim.x_size).each do |x|
    (0...claim.y_size).each do |y|
      claim_hash[[claim.x + x, claim.y + y]] = claim
    end
  end

  # Merge the new claim with the fabric, using an array where there is more than
  # one claim and marking all overlapped claims appropriately.
  fabric.merge!(claim_hash) do |k, o, n|
    o = [o] unless o.is_a?(Array)
    o.each { |c| c.overlap = true }
    n.overlap = true
    o << n
  end

end

# Count sections of fabric that have more than one claim.
puts fabric.values.count { |v| v.is_a?(Array) }
p claims.select { |c| c.overlap == false }
