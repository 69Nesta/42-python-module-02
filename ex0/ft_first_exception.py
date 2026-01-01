#! python3

def check_temperature(temp_str: str) -> int | None:
    """Validate a temperature string and report if it suits plant needs."""
    try:
        temp = int(temp_str)
    except ValueError:
        return print(f'Error: \'{temp_str}\' is not a valid number')
    else:
        if (temp > 40):
            print(f'Error: {temp}°C is too hot for plants (max 40°C)')
        elif (temp < 0):
            print(f'Error: {temp}°C is too cold for plants (min 0°C)')
        else:
            print(f'Temperature {temp}°C is perfect for plants!')
            return temp


def test_input(value: str):
    """Run a single temperature check with friendly console output."""
    print(f'Testing temperature: \'{value}\'')
    check_temperature(value)
    print('')


def test_temperature_input() -> None:
    """Demonstrate several temperature inputs and their outcomes."""
    print('=== Garden Temperature Checker ===\n')
    test_input("25")
    test_input("abc")
    test_input("100")
    test_input("-50")
    print('All tests completed - program didn\'t crash!')


if __name__ == '__main__':
    test_temperature_input()
