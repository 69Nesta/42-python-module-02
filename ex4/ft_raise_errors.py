#! python3

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    '''
    Checks the health of a plant based on its attributes.
    :param plant_name: Name of the plant.
    :param water_level: Water level of the plant.
    :param sunlight_hours: Sunlight hours for the plant.
    :return: Health status of the plant.
    '''
    if (not plant_name):
        raise ValueError('Plant name cannot be empty!')
    if (water_level > 10):
        raise ValueError(f'Water level {water_level} is too high (max 10)')
    if (water_level < 1):
        raise ValueError(f'Water level {water_level} is too low (min 1)')
    if (sunlight_hours > 10):
        raise ValueError(f'Sunlight hours {sunlight_hours} is too low (min 2)')
    if (sunlight_hours < 2):
        raise ValueError(f'Sunlight hours {sunlight_hours} is too low (min 2)')
    return f'Plant \'{plant_name}\' is healthy!'


def test_plant_checks():
    '''
    Runs tests for plant health checks.
    '''
    print('=== Garden Plant Health Checker ===')
    print('\nTesting good values...')
    try:
        print(check_plant_health('Tomato', 1, 2))
    except ValueError as e:
        print(f'Error: {e}')
    print('\nTesting empty plant name...')
    try:
        print(check_plant_health(None, 1, 2))
    except ValueError as e:
        print(f'Error: {e}')
    print('\nTesting bad water level...')
    try:
        print(check_plant_health('Tomato', 15, 2))
    except ValueError as e:
        print(f'Error: {e}')
    print('\nTesting bad sunlight hours...')
    try:
        print(check_plant_health('Tomato', 1, 0))
    except ValueError as e:
        print(f'Error: {e}')
    print('\nAll error raising tests completed!')


if __name__ == '__main__':
    test_plant_checks()
