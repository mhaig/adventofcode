#!/usr/bin/env ruby

class Array
  def deep_dup
    map {|x| x.deep_dup}
  end
end

class Object
  def deep_dup
    dup
  end
end

class Numeric
  # We need this because number.dup throws an exception
  # We also need the same definition for Symbol, TrueClass and FalseClass
  def deep_dup
    self
  end
end

INSTRUCTION = 0
A = 1
B = 2
C = 3

def get_registers(line)

  line[line.index("[")+1...line.index("]")].split(',').map(&:to_i)

end

$methods = []

def addr(a, b, c, r)
  r[c] = r[a] + r[b]
  return r
end
$methods << method(:addr)

def addi(a, b, c, r)
  r[c] = r[a] + b
  return r
end
$methods << method(:addi)

def mulr(a, b, c, r)
  r[c] = r[a] * r[b]
  return r
end
$methods << method(:mulr)

def muli(a, b, c, r)
  r[c] = r[a] * b
  return r
end
$methods << method(:muli)

def banr(a, b, c, r)
  r[c] = r[a] & r[b]
  return r
end
$methods << method(:banr)

def bani(a, b, c, r)
  r[c] = r[a] & b
  return r
end
$methods << method(:bani)

def borr(a, b, c, r)
  r[c] = r[a] | r[b]
  return r
end
$methods << method(:borr)

def bori(a, b, c, r)
  r[c] = r[a] | b
  return r
end
$methods << method(:bori)

def setr(a, b, c, r)
  r[c] = r[a]
  return r
end
$methods << method(:setr)

def seti(a, b, c, r)
  r[c] = a
  return r
end
$methods << method(:seti)

def gtir(a, b, c, r)
  if a > r[b]
    r[c] = 1
  else
    r[c] = 0
  end
  return r
end
$methods << method(:gtir)

def gtri(a, b, c, r)
  if r[a] > b
    r[c] = 1
  else
    r[c] = 0
  end
  return r
end
$methods << method(:gtri)

def gtrr(a, b, c, r)
  if r[a] > r[b]
    r[c] = 1
  else
    r[c] = 0
  end
  return r
end
$methods << method(:gtrr)

def eqir(a, b, c, r)
  if a == r[b]
    r[c] = 1
  else
    r[c] = 0
  end
  return r
end
$methods << method(:eqir)

def eqri(a, b, c, r)
  if r[a] == b
    r[c] = 1
  else
    r[c] = 0
  end
  return r
end
$methods << method(:eqri)

def eqrr(a, b, c, r)
  if r[a] == r[b]
    r[c] = 1
  else
    r[c] = 0
  end
  return r
end
$methods << method(:eqrr)

def execute_instruction(instruction, input_register, output_register)

  # Execute all the instructions on the input register.  Use the result as a
  # hash.
  results = $methods.map { |m| m.call(instruction[1], instruction[2], instruction[3], input_register.deep_dup) }

  # Only select the ones that match the expected output.
  results.count { |r| r == output_register }

end

input = ARGF.read.split("\n\n")

duplicate_instruction_count = []

input.each do |i|

  break if i == ""
  p i

  start_register = get_registers(i.split("\n")[0])
  end_register = get_registers(i.split("\n")[2])
  instruction = i.split("\n")[1].split(" ").map(&:to_i)

  duplicate_instruction_count << execute_instruction(instruction, start_register, end_register)

end

p duplicate_instruction_count.count { |x| x >= 3 }
