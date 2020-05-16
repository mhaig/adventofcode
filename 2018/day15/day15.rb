#!/usr/bin/env ruby

class CavernElement
  def initialize char
    @char = char
  end

  def show
    print(@char)
  end

  def is_unit?
    false
  end
end

class Wall < CavernElement
  def initialize
    super("#")
  end
end

class Open < CavernElement
  def initialize
    super('.')
  end
end

class Goblin < CavernElement
  def initialize
    super("G")
  end

  def is_unit?
    true
  end
end

class Elf < CavernElement
  def initialize
    super("E")
  end

  def is_unit?
    true
  end
end

class Cavern

  attr_accessor :height, :width

  def initialize(map)
    @height = map.split("\n").length()
    @width = map.split("\n")[0].length()

    @map = Hash.new()

    flat_input = map.delete("\n")

    # 012 345 678
    # ### ### ###
    #
    (0...@height).each do |y|
      (0...@width).each do |x|
        print(x+(y*@width))
        print(flat_input[x+(y*@width)])
        case flat_input[x+(y*@width)]
        when "#" then m = Wall
        when "." then m = Open
        when "G" then m = Goblin
        when "E" then m = Elf
        end
        @map[[x, y]] = m.new
      end
      print("\n")
    end
  end

  def show
    (0...@height).each do |y|
      (0...@width).each do |x|
        @map[[x,y]].show()
      end
      print "\n"
    end
  end

  def has? a_class
    @map.values.any?{|v| v.kind_of? a_class}
  end

  def turn
    # Make a copy of the map to put the moves into?

    (0...@height).each do |y|
      (0...@width).each do |x|

        # Only execute a turn on the space if it is a unit.
        next unless @map[[x,y]].is_unit?

        p "Unit at #{x},#{y}"
      end
    end
  end

end

raw_map = ARGF.read

p raw_map
p raw_map.split("\n")

cavern = Cavern.new(raw_map)
puts cavern.inspect
cavern.show()

cavern.turn
