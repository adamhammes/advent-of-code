from day16 import *


def test_hex_to_bytes():
    byte_list = unpack("110100101111111000101000")
    assert hex_to_bytes("D2FE28") == byte_list


def test_version():
    byte_list = unpack("110100101111111000101000")
    version, rest = get_version(byte_list)

    assert version == 6
    assert rest == unpack("100101111111000101000")


def test_parse_literal():
    num, rest = parse_literal(unpack("101111111000101000"))
    assert num == 2021
    assert rest == unpack("000")


def test_literal_packet():
    packet, rest = parse_packet(unpack("110100101111111000101000"))
    assert packet == Packet(
        packet_version=6, packet_type=4, sub_packets=[], literal_value=2021
    )
    assert rest == unpack("000")


def test_subpackets_1():
    packet, rest = parse_packet(
        unpack("00111000000000000110111101000101001010010001001000000000")
    )

    assert packet == Packet(
        packet_version=1,
        packet_type=6,
        literal_value=None,
        sub_packets=[
            Packet(packet_version=6, packet_type=4, literal_value=10, sub_packets=[]),
            Packet(packet_version=2, packet_type=4, literal_value=20, sub_packets=[]),
        ],
    )


def test_subpackets_2():
    packet, rest = parse_packet(
        unpack("11101110000000001101010000001100100000100011000001100000")
    )

    assert packet == Packet(
        packet_version=7,
        packet_type=3,
        literal_value=None,
        sub_packets=[
            Packet(packet_version=5, packet_type=4, sub_packets=[], literal_value=1),
            Packet(packet_version=2, packet_type=4, sub_packets=[], literal_value=2),
            Packet(packet_version=1, packet_type=4, sub_packets=[], literal_value=3),
        ],
    )


def test_part_1():
    assert part_1("8A004A801A8002F478") == 16
