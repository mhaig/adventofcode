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

        print('Parsing: {}'.format(self._binary))

        self._version = int(self._binary[0:3],2)
        self._bit_length += 3
        self._type = int(self._binary[3:3+3],2)
        self._bit_length += 3

        if self._type == 4:
            print('Packet is of type 4, literal', end='')
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
            print(' with value {}'.format(self._literal_value))
        else:
            print('Packet is an operator version {}'.format(self._version))

            self._length_type = int(self._binary[6],2)
            self._bit_length += 1

            if self._length_type == 0:
                self._sub_packet_length = int(self._binary[7:7+15],2)
                start = 7+15
                self._bit_length += 15
                print('total length of sub-packets: {}'.format(self._sub_packet_length))
            else:
                self._sub_packet_count = int(self._binary[7:7+11],2)
                start = 7+11
                self._bit_length += 11
                print('number of sub-packets: {}'.format(self._sub_packet_count))

            while True:
                print('found a sub packet')
                sub_packet = Packet(self._binary[start:], True)
                self._sub_packets.append(sub_packet)
                self._bit_length += sub_packet.bit_length
                print('done!')

                if self._sub_packet_length:
                    remaining_length = self._sub_packet_length - sum([x.bit_length for x in self._sub_packets])
                    if remaining_length < 11:
                        break
                else:
                    if len(self._sub_packets) >= self._sub_packet_count:
                        break

                start += sub_packet.bit_length
