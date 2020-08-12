from os.path import splitext
import csv

def _search_file_ext(path):
    split_path = splitext(path)
    size = len(split_path)
    if size >= 2 and split_path[size - 1] in ['.jpg','.jpeg', '.png', '.gif']:
        return split_path[size - 1]
    else:
        return None

def _is_number(line):
    try:
        return float(line)
    except ValueError:
        return float(0)

def _split_bode_whl(bwl):
    spl_bwl = bwl.split('x') if len(bwl.split('x')) == 3 else None
    for i in range(3):
        yield _is_number(spl_bwl[i]) if spl_bwl else float(0)

class CarBase:    
    def __init__(self, brand, photo_file_name, carrying):
        if _search_file_ext(photo_file_name) and brand:
            self.photo_file_name = photo_file_name
        else:
            raise NameError
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return _search_file_ext(self.photo_file_name)
            
class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        whl_generator = _split_bode_whl(body_whl)
        self.body_length = next(whl_generator)
        self.body_width = next(whl_generator)
        self.body_height = next(whl_generator)
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if extra:
            self.extra = extra
        else:
            raise NameError
        self.car_type = 'spec_machine'

def get_car_list(csv_filename):
    cars_list = list()
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            size = len(row)
            if size != 7:
                continue
            try:
                if row[0] == 'car':
                    cars_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    cars_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    cars_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
            except:
                pass
    return cars_list