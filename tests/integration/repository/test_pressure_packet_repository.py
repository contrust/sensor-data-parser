def test_count_increases_after_save_all(
    pressure_packet_repository, correct_pressure_packet
):
    assert pressure_packet_repository.count() == 0
    pressure_packet_repository.save_all([correct_pressure_packet])
    assert pressure_packet_repository.count() == 1


def test_save_all_adds_the_same_models(
    pressure_packet_repository, correct_pressure_packet
):
    assert (
        pressure_packet_repository.get(
            correct_pressure_packet.current_value_counter
        )
        is None
    )
    pressure_packet_repository.save_all([correct_pressure_packet])
    assert (
        pressure_packet_repository.get(
            correct_pressure_packet.current_value_counter
        )
        == correct_pressure_packet
    )
