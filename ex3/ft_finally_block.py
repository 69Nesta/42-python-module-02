#! python3

def water_plants(plant_list: list[str]) -> None:
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