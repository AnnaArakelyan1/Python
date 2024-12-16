import requests
import json
import os


URL = "http://127.0.0.1:5000/cars"


def create_empty_json_file():
    if not os.path.exists('cars.json'):
        with open('cars.json', 'w') as f:
            json.dump([], f) 


def create_car(data):
    response = requests.post(URL, json=data)
    print("Create Car Response:", response.status_code, response.json())


def get_all_cars():
    response = requests.get(URL)
    print("Get All Cars Response:", response.status_code, response.json())


def get_car_by_id(car_id):
    response = requests.get(f"{URL}/{car_id}")
    print(f"Get Car with ID {car_id} Response:", response.status_code, response.json())


def update_car(car_id, updated_data):
    response = requests.put(f"{URL}/{car_id}", json=updated_data)
    print(f"Update Car with ID {car_id} Response:", response.status_code, response.json())


def delete_car(car_id):
    response = requests.delete(f"{URL}/{car_id}")
    print(f"Delete Car with ID {car_id} Response:", response.status_code)



def test_api():

    create_empty_json_file()

    cars_data = [
        {"make": "Toyota", "model": "Corolla", "year": 2020, "price": 20000},
        {"make": "Honda", "model": "Civic", "year": 2022, "price": 25000},
        {"make": "Ford", "model": "Focus", "year": 2021, "price": 22000},
    ]
    
    for car_data in cars_data:
        create_car(car_data)

    get_all_cars()

    get_car_by_id(1)

    updated_car_data = {"make": "Toyota", "model": "Corolla", "year": 2021, "price": 21000}
    update_car(1, updated_car_data)

    get_car_by_id(1)

    delete_car(2)

    get_car_by_id(2)


if __name__ == "__main__":
    test_api()
