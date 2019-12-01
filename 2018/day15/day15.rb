#!/usr/bin/env ruby

class MapElement
  def initialize(char, map=nil)
    @char = char
    @map = map
  end

  def show
    print(@char)
  end

  def move; end
  def attack; end
  def turn; end
end

class Wall < MapElement
  def initialize map
    super("#")
  end
end

class Open < MapElement
  def initialize map
    super('.')
  end
end

class Goblin < MapElement
  def initialize map
    super("G", map)
  end

  def turn
    return unless @map.has?(Elf)

    # Get the adjacent open squares.
  end
end

class Elf < MapElement
  def initialize map
    super("E", map)
  end

  def turn
    @map.has?(Goblin)
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
        @map[[x, y]] = m.new(self)
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
    @map.values.any?{|v| v.turn}
  end

end

raw_map = ARGF.read

p raw_map
p raw_map.split("\n")

cavern = Cavern.new(raw_map)
puts cavern.inspect
cavern.show()

p cavern.turn
