#! python3

def water_plants(plant_list: list[str]) -> None:
    '''
    Waters a list of plants, demonstrating the use of a finally block.
    :param plant_list: List of plant names to water.
    '''
    try:
        print('Opening watering system!')
        for plant in plant_list:
            print('Watering ' + plant)
        print('Watering completed successfully!')
    except Exception as e:
        print(f'Error: cannot watering {e.__cause__} - invalid plant')
    finally:
        print('Closing watering system! (cleanup)')


def test_watering_system() -> None:
    '''
    Tests the watering system with and without errors.
    '''
    print('=== Garden Watering System ===\n')
    print('Testing normal watering...')
    water_plants(['tomato', 'lettuce', 'carrots'])
    print('')
    print('Testing with error...')
    water_plants(['tomato', None, 'carrots'])
    print('')
    print('Cleanup always happens, even with errors!')


if __name__ == '__main__':
    test_watering_system()
