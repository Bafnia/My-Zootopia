import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def generate_animals_html(data):
    """Generates HTML <li> items with animal information"""
    output = ""
    for animal in data:
        output += '<li class="cards__item">\n'
        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
            if "type" in animal["characteristics"]:
                output += f"Type: {animal['characteristics']['type']}<br/>\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}<br/>\n"
        output += "</li>\n"
    return output

if __name__ == "__main__":
    # JSON laden
    animals_data = load_data("animals_data.json")
    animals_html = generate_animals_html(animals_data)

    # Template einlesen
    with open("animals_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Platzhalter ersetzen
    filled_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Neue HTML-Datei schreiben
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(filled_html)

    print("✅ animals.html mit <li>-Elementen wurde erstellt. Im Browser öffnen, um das Design zu sehen!")
