#!/usr/bin/env ruby

INSTRUCTION = 0
A = 1
B = 2
C = 3

input = ARGF.read.split("\n")

registers = [1, 0, 0, 0, 0, 0]

ip = 0
ip_register = 0

program = []

input.each do |i|

  instruction = i.split(' ')

  if instruction[0][0] == '#'
    ip_register = instruction[1].to_i
    next
  end

  instruction[A] = instruction[A].to_i
  instruction[B] = instruction[B].to_i
  instruction[C] = instruction[C].to_i

  program << instruction

end

p ip_register

# Program loaded, start execution.
loop do

  instruction = program[registers[ip_register]]

  # p instruction
  break unless instruction

  case instruction[INSTRUCTION]
  when "addi"
    registers[instruction[C]] = registers[instruction[A]] + instruction[B]
  when "addr"
    registers[instruction[C]] = registers[instruction[A]] + registers[instruction[B]]
  when "eqrr"
    if registers[instruction[A]] == registers[instruction[B]]
      registers[instruction[C]] = 1
    else
      registers[instruction[C]] = 0
    end
  when "gtrr"
    if registers[instruction[A]] > registers[instruction[B]]
      registers[instruction[C]] = 1
    else
      registers[instruction[C]] = 0
    end
  when "seti"
    registers[instruction[C]] = instruction[A]
  when "setr"
    registers[instruction[C]] = registers[instruction[A]]
  when "muli"
    registers[instruction[C]] = registers[instruction[A]] * instruction[B]
  when "mulr"
    registers[instruction[C]] = registers[instruction[A]] * registers[instruction[B]]
  else
    p "Instruction #{instruction[INSTRUCTION]} not implemented!"
    break
  end

  registers[ip_register] += 1

end

p registers
