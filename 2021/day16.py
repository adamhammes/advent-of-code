import lib
import enum
from typing import Iterable, Optional
import typing

Bytes = list[int]


class PacketType(enum.IntEnum):
    Literal = 4


class Packet(typing.NamedTuple):
    packet_version: int
    packet_type: int
    sub_packets: list["Packet"]
    literal_value: Optional[int]

    def sum_version(self) -> int:
        return self.packet_version + sum(map(Packet.sum_version, self.sub_packets))

    def sum_value(self) -> int:
        sub_values = list(map(Packet.sum_value, self.sub_packets))
        return {
            0: lambda: sum(sub_values),
            1: lambda: lib.product(sub_values),
            2: lambda: min(sub_values),
            3: lambda: max(sub_values),
            4: lambda: self.literal_value,
            5: lambda: int(sub_values[0] > sub_values[1]),
            6: lambda: int(sub_values[0] < sub_values[1]),
            7: lambda: int(sub_values[0] == sub_values[1]),
        }[self.packet_type]()


def unpack(bit_string: str) -> Bytes:
    return list(map(int, bit_string))


def hex_to_bytes(hex_str: str) -> list[int]:
    return [int(c) for letter in hex_str.strip() for c in f"{int(letter, 16):04b}"]


def bits_to_int(bits: Iterable[int]) -> int:
    return int("".join(map(str, bits)), 2)


def get_version(b: Bytes) -> tuple[int, Bytes]:
    return bits_to_int(b[:3]), list(b[3:])


get_packet_type = get_version


def parse_literal(b: Bytes) -> tuple[int, Bytes]:
    bits = []
    while True:
        first_five_bits, b = list(b[:5]), list(b[5:])
        bits += first_five_bits[1:]

        if not first_five_bits[0]:
            break

    return bits_to_int(bits), b


def parse_packet(b: Bytes) -> tuple[Packet, Bytes]:
    version, b = get_version(b)
    packet_type, b = get_packet_type(b)

    if packet_type == PacketType.Literal:
        num, b = parse_literal(b)
        return (
            Packet(
                packet_version=version,
                packet_type=packet_type,
                sub_packets=[],
                literal_value=num,
            ),
            b,
        )
    else:
        # subpackets
        length_type, b = b[0], b[1:]
        if length_type == 0:
            # The next 15 bits are a number that represents the total length in bits of
            # the sub-packets contained by this packet.
            total_subpacket_bit_length, b = bits_to_int(b[:15]), b[15:]
            sub_b, b = (
                b[:total_subpacket_bit_length],
                b[total_subpacket_bit_length:],
            )

            subpackets = []
            while sub_b:
                packet, sub_b = parse_packet(sub_b)
                subpackets.append(packet)

            return (
                Packet(
                    packet_version=version,
                    packet_type=packet_type,
                    sub_packets=subpackets,
                    literal_value=None,
                ),
                b,
            )
        else:
            # the next 11 bits are a number that represents the number of sub-packets
            # immediately contained by this packet
            num_subpackets, b = bits_to_int(b[:11]), b[11:]
            subpackets = []
            for _ in range(num_subpackets):
                packet, b = parse_packet(b)
                subpackets.append(packet)

            return (
                Packet(
                    packet_type=packet_type,
                    packet_version=version,
                    sub_packets=subpackets,
                    literal_value=None,
                ),
                b,
            )


def part_1(raw: str) -> int:
    b = hex_to_bytes(raw)
    packet, _ = parse_packet(b)
    return packet.sum_version()


def part_2(raw: str) -> int:
    b = hex_to_bytes(raw)
    packet, _ = parse_packet(b)
    return packet.sum_value()


if __name__ == "__main__":
    print(part_1(lib.get_input(16)))
    print(part_2(lib.get_input(16)))
