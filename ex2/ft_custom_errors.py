#! python3

class GardenError(Exception):
    """Exception raised for custom error in the garden."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Raised when the tomato plant is wilting."""
    def __init__(self, message='The tomato plant is wilting!'):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    """Raised when there is not enough water in the tank."""
    def __init__(self, message='Not enough water in the tank!'):
        self.message = message
        super().__init__(self.message)


def test_all_errors():
    """Function to test all custom error types."""
    print('=== Custom Garden Errors Demo ===\n')
    print('Testing PlantError...')
    try:
        raise PlantError()
    except PlantError as e:
        print(f'Caught PlantError: {e}\n')
    print('')
    print('Testing WaterError...')
    try:
        raise WaterError()
    except WaterError as e:
        print(f'Caught WaterError: {e}')
    print('')
    print('Testing catching all garden errors...')
    try:
        raise PlantError()
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    try:
        raise WaterError()
    except GardenError as e:
        print(f'Caught a garden error: {e}')
    print('')
    print('All custom error types work correctly!')


if __name__ == '__main__':
    test_all_errors()
