import json
from flask import Flask, jsonify, request

app = Flask(__name__)


def load_cars():
    try:
        with open('cars.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_cars(cars):
    with open('cars.json', 'w') as f:
        json.dump(cars, f, indent=4)


@app.route('/cars', methods=['GET'])
def get_cars():
    cars = load_cars()
    return jsonify(cars)


@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    cars = load_cars()
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    return jsonify(car)


@app.route('/cars', methods=['POST'])
def create_car():
    new_car = request.get_json()
    cars = load_cars()

    new_car_id = max([car['id'] for car in cars], default=0) + 1
    new_car['id'] = new_car_id
    
    cars.append(new_car)
    save_cars(cars)
    return jsonify(new_car), 201


@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    updated_data = request.get_json()
    cars = load_cars()
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    car.update(updated_data)
    save_cars(cars)
    return jsonify(car)


@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    cars = load_cars()
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    cars.remove(car)
    save_cars(cars)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
