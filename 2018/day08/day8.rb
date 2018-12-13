#!/usr/bin/env ruby

input = ARGF.read.split("\n")

class Node

  def initialize(id)
    @id = id
    @child_nodes = []
    @metadata = []
  end

  attr_reader :metadata, :child_nodes, :id
  attr_writer :metadata, :child_nodes

end

$node_hash = {}
$node_id = 0

# Redo this parsing code to return child nodes to build an actual tree.
def sum_metadata(s)

  child_nodes = s[0].to_i
  metadata_count = s[1].to_i
  consumed = 2
  n = $node_id
  node = Node.new(n)

  if child_nodes > 0

    c = 0
    while c < child_nodes do

      $node_id += 1
      ate, child = sum_metadata(s[consumed..-1])
      consumed += ate
      node.child_nodes << child
      c += 1

    end

  end

  $node_hash[n] = s[consumed, metadata_count].map(&:to_i)
  node.metadata = s[consumed, metadata_count].map(&:to_i)

  return (consumed + metadata_count), node
end

$sum = 0
def sum_child_metadata(node)

  return 0 unless node

  sum = 0
  if node.child_nodes.count > 0
    # Node has children, traverse them if they exist.
    node.metadata.sort.each { |i| sum += sum_child_metadata(node.child_nodes[i-1]) }
  else
    sum = node.metadata.reduce(:+)
  end

  return sum

end

input.each do |i|
  _, node = sum_metadata(i.split(' '))
  p $node_hash
  p $node_hash.reduce(0) { |sum, (k, v)| sum + v.reduce(:+) }
  p node

  # For part 2 traverse the tree returning the sum of the child node metadata
  # based on using the metadata as an index.

  p sum_child_metadata(node)

end

