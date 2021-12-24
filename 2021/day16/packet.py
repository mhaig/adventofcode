import math

class Packet(object):

    def __init__(self, raw_packet, binary=False):
        self._raw_packet = raw_packet

        self._version = None
        self._type = None
        self._literal_value = None
        self._bit_length = 0
        self._sub_packets = []
        self._sub_packet_length = 0

        self._parse(self._raw_packet.strip(), binary)

    @property
    def bit_length(self):
        return self._bit_length

    @property
    def type(self):
        return self._type

    @property
    def version(self):
        return self._version

    @property
    def sub_packets(self):
        return self._sub_packets

    def _parse(self, raw_packet, binary):

        # Convert packet to binary.
        if binary:
            self._binary = raw_packet
        else:
            self._binary = ''
            for c in raw_packet:
                b = bin(int(c, 16))[2:]
                b = ((4 - len(b)) * '0') + b
                self._binary += b

        self._version = int(self._binary[0:3],2)
        self._bit_length += 3
        self._type = int(self._binary[3:3+3],2)
        self._bit_length += 3

        if self._type == 4:
            literal_value_string = ''
            start = 6
            length = 5
            # Parse rest for literal value
            while True:
                literal_value_string += self._binary[start+1:start+length]
                self._bit_length += 5
                if self._binary[start] == '0':
                    break
                start += length
            self._literal_value = int(literal_value_string, 2)
        else:
            self._length_type = int(self._binary[6],2)
            self._bit_length += 1

            if self._length_type == 0:
                self._sub_packet_length = int(self._binary[7:7+15],2)
                start = 7+15
                self._bit_length += 15
            else:
                self._sub_packet_count = int(self._binary[7:7+11],2)
                start = 7+11
                self._bit_length += 11

            while True:
                sub_packet = Packet(self._binary[start:], True)
                self._sub_packets.append(sub_packet)
                self._bit_length += sub_packet.bit_length

                if self._sub_packet_length:
                    remaining_length = self._sub_packet_length - sum([x.bit_length for x in self._sub_packets])
                    if remaining_length < 11:
                        break
                else:
                    if len(self._sub_packets) >= self._sub_packet_count:
                        break

                start += sub_packet.bit_length


    def get_value(self):
        # Literal value
        if self.type == 4:
            return self._literal_value

        # Greater than
        if self.type == 5:
            return int(self.sub_packets[0].get_value() >
                       self.sub_packets[1].get_value())
        # Less than
        elif self.type == 6:
            return int(self.sub_packets[0].get_value() <
                       self.sub_packets[1].get_value())
        # Equal
        elif self.type == 7:
            return int(self.sub_packets[0].get_value() ==
                       self.sub_packets[1].get_value())

        values = [x.get_value() for x in self.sub_packets]
        if self.type == 0:
            return sum(values)
        elif self.type == 1:
            return math.prod(values)
        elif self.type == 2:
            return min(values)
        elif self.type == 3:
            return max(values)
