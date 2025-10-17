import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def generate_animals_string(data):
    """Generates a string with animal information"""
    output = ""
    for animal in data:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                output += f"Diet: {animal['characteristics']['diet']}\n"
            if "type" in animal["characteristics"]:
                output += f"Type: {animal['characteristics']['type']}\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"
        output += "\n"  # Leerzeile nach jedem Tier
    return output

if __name__ == "__main__":
    # JSON laden
    animals_data = load_data("animals_data.json")
    animals_string = generate_animals_string(animals_data)

    # Template einlesen
    with open("animals_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Platzhalter ersetzen
    filled_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    # Neue HTML-Datei schreiben
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(filled_html)

    print("animals.html wurde erstellt. Öffne sie im Browser, um das Ergebnis zu sehen!")
