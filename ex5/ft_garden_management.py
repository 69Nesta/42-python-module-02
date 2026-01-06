#! python3

class GardenError(Exception):
    """Exception raised for custom error in the garden."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    """Raised when there is not enough water in the tank."""
    def __init__(self, message='Not enough water in the tank!'):
        self.message = message
        super().__init__(self.message)


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.set_name(name)
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def set_name(self, name: str) -> None:
        if (not name or name.isspace()):
            raise ValueError('Plant name cannot be empty!')
        self._name = name

    def get_name(self) -> str:
        return self._name


class GardenManager:
    def __init__(self, water_left: int):
        self.plant_list: list[Plant] = []
        self.water_left = water_left

    def add_plant(self, name: str, water_lvl: int, sunlight: int) -> None:
        try:
            plant = Plant(name, water_lvl, sunlight)
            self.plant_list.append(plant)
            print(f'Added {name} successfully')
        except Exception as e:
            print(f'Error adding plant: {e}')

    def water_plants(self) -> None:
        try:
            print('Opening watering system!')
            for plant in self.plant_list:
                if self.water_left <= 0:
                    raise WaterError()
                plant.water_level += 1
                self.water_left -= 1
                print(f'Watering {plant.get_name()} - success')
            print('Watering completed successfully!')
        except GardenError as e:
            print(f'Caught GardenError: {e}')
        finally:
            print('Closing watering system! (cleanup)')

    @staticmethod
    def __check_plant_health(plant: Plant) -> str:
        if (not plant.get_name()):
            raise ValueError('Plant name cannot be empty!')
        if (plant.water_level > 10):
            raise ValueError(f'Water level {plant.water_level}'
                             ' is too high (max 10)')
        if (plant.water_level < 1):
            raise ValueError(f'Water level {plant.water_level}'
                             ' is too low (min 1)')
        if (plant.sunlight_hours > 10):
            raise ValueError(f'Sunlight hours {plant.sunlight_hours}'
                             'is too low (min 2)')
        if (plant.sunlight_hours < 2):
            raise ValueError(f'Sunlight hours {plant.sunlight_hours}'
                             ' is too low (min 2)')
        return (f'{plant.get_name()}: healthy'
                f' (water: {plant.water_level}, sun: {plant.sunlight_hours})')

    def check_plants_health(self) -> None:
        for plant in self.plant_list:
            try:
                print(self.__check_plant_health(plant))
            except ValueError as e:
                print(f'Error checking {plant.get_name()}: {e}')

    def recovery_test(self):
        try:
            raise WaterError()
        except Exception as e:
            print(f'Caught GardenError: {e}')


def demo():
    print('=== Garden Management System ===\n')
    garden_manager = GardenManager(2)
    print('Adding plants to garden...')
    garden_manager.add_plant('tomato', 4, 8)
    garden_manager.add_plant('lettus', 14, 8)
    garden_manager.add_plant(None, 2, 8)

    print('\nWatering plants')
    garden_manager.water_plants()

    print('\nChecking plant health...')
    garden_manager.check_plants_health()

    print('\nTesting error recovery...')
    garden_manager.recovery_test()
    print('System recovered and continuing...')

    print('\nGarden management system test complete!')


if __name__ == "__main__":
    demo()
