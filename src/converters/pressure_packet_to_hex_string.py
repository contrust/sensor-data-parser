from src.models.pressure_packet import PressurePacket


def pressure_packet_to_hex_string(packet: PressurePacket) -> str:
    return (
        packet.status
        + hex(packet.current_value_counter)[2:].zfill(2)
        + hex(int(packet.pressure_value))[2:].zfill(4)
    )
