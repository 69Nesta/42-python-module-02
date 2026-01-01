#! python3

def garden_operations(number: str, divsor: int, file: str, id: str):
    """Trigger a series of common errors based on provided inputs."""
    # error : ValueError
    int_number = int(number)
    # error : ZeroDivisionError
    int_number / divsor
    # error : FileNotFoundError
    open(file, 'r')
    # error : KeyError
    dictionary: dict[str, str] = {'Hello': 'World'}
    dictionary[id]


def test_garden_operations(number: str, divsor: int, file: str, id: str):
    """Execute garden_operations and print the caught exception type if any."""
    try:
        garden_operations(number, divsor, file, id)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print(f'Caught {type(e).__name__}: {e}\n')


def test_error_types():
    """Demonstrate how different exceptions are raised and handled."""
    print('=== Garden Error Types Demo ===\n')
    print('Testing ValueError...')
    test_garden_operations('', 1, 'ex1/ft_different_errors.py', 'Hello')
    print('Testing ZeroDivisionError...')
    test_garden_operations('10', 0, 'ex1/ft_different_errors.py', 'Hello')
    print('Testing FileNotFoundError...')
    test_garden_operations('10', 1, 'missing.txt', 'Hello')
    print('Testing KeyError...')
    test_garden_operations('10', 1, 'ex1/ft_different_errors.py', 'World')
    print('Testing multiple errors together...')
    try:
        garden_operations('abc', 0, 'missing.txt', 'World')
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print('Caught an error, but program continues!\n')
    print('All error types tested successfully!')


if __name__ == '__main__':
    test_error_types()
