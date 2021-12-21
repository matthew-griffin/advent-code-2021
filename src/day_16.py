from functools import reduce

from src.timer import Timer

VERSION_SLICE = slice(3)
TYPE_SLICE = slice(3, 6)
LITERAL_SLICE = slice(6, None)
LENGTH_INDEX = 6
ZERO_LENGTH_SLICE = slice(7, 22)
ZERO_REMAINING_SLICE = slice(22, None)
ONE_LENGTH_SLICE = slice(7, 18)
ONE_REMAINING_SLICE = slice(18, None)

REDUCE_METHODS = {
    0: lambda a, b: a+b,
    1: lambda a, b: a*b,
    2: min,
    3: max,
    5: lambda a, b: 1 if a > b else 0,
    6: lambda a, b: 1 if a < b else 0,
    7: lambda a, b: 1 if a == b else 0
}


class Packet:
    def __init__(self, packet_version, packet_type, sub_packets=(), literal_value=None):
        if sub_packets is None:
            sub_packets = []
        self.packet_version = packet_version
        self.packet_type = packet_type
        self.sub_packets = sub_packets
        self.literal_value = literal_value

    def calcVersionSum(self):
        result = self.packet_version
        for packet in self.sub_packets:
            result += packet.calcVersionSum()
        return result

    def calcExpression(self):
        if self.packet_type == 4:
            return self.literal_value

        return reduce(REDUCE_METHODS[self.packet_type], [packet.calcExpression() for packet in self.sub_packets])


def toBinaryString(hex_string):
    the_bytes = bytes.fromhex(hex_string)
    as_number = int.from_bytes(the_bytes, "big")
    return bin(as_number)[2:].zfill(len(hex_string * 4))


def parseLiteralValueAndBitLength(binary_string):
    bits_parsed = 0
    value_string = ""
    while binary_string[0] == '1':
        value_string += binary_string[1:5]
        binary_string = binary_string[5:]
        bits_parsed += 5
    value_string += binary_string[1:5]
    bits_parsed += 5
    return int(value_string, 2), bits_parsed


def recParsePacketsAndBitLength(binary_string):
    packet_version = int(binary_string[VERSION_SLICE], 2)
    packet_type = int(binary_string[TYPE_SLICE], 2)
    bits_parsed = 6
    if packet_type == 4:
        value, literal_bits_parsed = parseLiteralValueAndBitLength(binary_string[LITERAL_SLICE])
        return Packet(packet_version, packet_type, literal_value=value), bits_parsed+literal_bits_parsed

    sub_bits_parsed = 0
    sub_packets = []
    if binary_string[LENGTH_INDEX] == '0':
        sub_packet_length = int(binary_string[ZERO_LENGTH_SLICE], 2)
        sub_packet_string = binary_string[ZERO_REMAINING_SLICE]
        bits_parsed += 16

        while sub_bits_parsed < sub_packet_length:
            sub_packet, sub_packet_bits = recParsePacketsAndBitLength(sub_packet_string)
            sub_packets.append(sub_packet)
            sub_bits_parsed += sub_packet_bits
            sub_packet_string = sub_packet_string[sub_packet_bits:]
    else:
        sub_packet_count = int(binary_string[ONE_LENGTH_SLICE], 2)
        sub_packet_string = binary_string[ONE_REMAINING_SLICE]
        bits_parsed += 12
        for _ in range(sub_packet_count):
            sub_packet, sub_packet_bits = recParsePacketsAndBitLength(sub_packet_string)
            sub_packets.append(sub_packet)
            sub_bits_parsed += sub_packet_bits
            sub_packet_string = sub_packet_string[sub_packet_bits:]

    return Packet(packet_version, packet_type, sub_packets), bits_parsed+sub_bits_parsed



def calcVersionSum(input_text):
    packet, _ = recParsePacketsAndBitLength(toBinaryString(input_text))
    return packet.calcVersionSum()


def calcVersionSumFromFile(input_file):
    with open(input_file) as file:
        return calcVersionSum(file.readline())


def calcExpression(input_text):
    packet, _ = recParsePacketsAndBitLength(toBinaryString(input_text))
    return packet.calcExpression()


def calcExpressionFromFile(input_file):
    with open(input_file) as file:
        return calcExpression(file.readline())


if __name__ == '__main__':
    with Timer("Part 1"):
        part1_result = calcVersionSumFromFile("../input/day_16.txt")
    print(f"Part 1 Result: {part1_result}")
    with Timer("Part 2"):
        part2_result = calcExpressionFromFile("../input/day_16.txt")
    print(f"Part 2 Result: {part2_result}")
