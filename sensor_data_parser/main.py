from sensor_data_parser.cli import CommandsRunner


def main() -> None:
    commands_runner = CommandsRunner()
    commands_runner.parse_arguments()
    commands_runner.run()


if __name__ == "__main__":
    main()
