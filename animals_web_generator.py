import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals(data):
    """Prints selected animal information"""
    for animal in data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                print(f"Diet: {animal['characteristics']['diet']}")
            if "type" in animal["characteristics"]:
                print(f"Type: {animal['characteristics']['type']}")
        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")
        print()  # Leerzeile zwischen den Tieren

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)
