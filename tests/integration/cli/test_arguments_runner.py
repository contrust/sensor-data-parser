from io import StringIO

import pytest
import sqlalchemy
from _pytest.fixtures import FixtureRequest
from sqlalchemy import Engine

from sensor_data_parser.cli import CommandsRunner
from sensor_data_parser.internal.parsers import HexStringParser


@pytest.fixture()
def stream_input(request: FixtureRequest) -> str:
    if hasattr(request, "param"):
        return request.param
    raise NotImplementedError


@pytest.fixture()
def commands_runner(engine: Engine) -> CommandsRunner:
    runner = CommandsRunner()
    runner._engine = engine
    runner._set_engine = lambda *_: None
    return runner


@pytest.fixture()
def commands_runner_with_mocked_stream(
        commands_runner,
        stream_input) -> CommandsRunner:
    commands_runner._stream = StringIO(stream_input)
    return commands_runner


def test_creates_tables_when_creates_tables_option(engine, commands_runner):
    commands_runner.parse_arguments(['--create-tables'])
    commands_runner.run()
    assert sqlalchemy.inspect(engine).has_table('pressure_packet')


@pytest.mark.parametrize('stream_input',
                         ('34ffffff80490000804a0000804b'
                          '0000804c0000804d000079f3ffff',))
def test_saves_parsed_packets(
        commands_runner_with_mocked_stream,
        pressure_packet_repository,
        stream_input):
    commands_runner_with_mocked_stream.parse_arguments([])
    commands_runner_with_mocked_stream.run()
    packets = HexStringParser(stream_input).to_pressure_packets()
    for i in range(len(packets)):
        packet = packets[i]
        db_packet = pressure_packet_repository.get(i + 1)
        assert db_packet
        assert packet.current_value_counter == db_packet.current_value_counter
        assert packet.status == db_packet.status
        assert packet.pressure_value == db_packet.pressure_value


@pytest.mark.parametrize('stream_input', ('80000000',))
def test_does_not_raise_exception_when_no_db_tables(
        commands_runner_with_mocked_stream, stream_input):
    commands_runner_with_mocked_stream.parse_arguments([])
    commands_runner_with_mocked_stream.run()
