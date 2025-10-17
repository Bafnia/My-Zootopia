import json


def load_data(file_path):
    """Loads a JSON file and returns the data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts a single animal object into an HTML <li> string."""
    output = '<li class="cards__item">\n'

    # Title
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    # Details
    output += '  <p class="card__text">\n'
    if "characteristics" in animal_obj:
        if "diet" in animal_obj["characteristics"]:
            output += (
                f'      <strong>Diet:</strong> '
                f'{animal_obj["characteristics"]["diet"]}<br/>\n'
            )
        if "type" in animal_obj["characteristics"]:
            output += (
                f'      <strong>Type:</strong> '
                f'{animal_obj["characteristics"]["type"]}<br/>\n'
            )
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        output += (
            f'      <strong>Location:</strong> '
            f'{animal_obj["locations"][0]}<br/>\n'
        )
    output += "  </p>\n"

    output += "</li>\n"
    return output


def generate_animals_html(data):
    """Generates HTML for a list of animals."""
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


def main():
    """Main program: load data, generate HTML and save the file."""
    # JSON laden
    animals_data = load_data("animals_data.json")

    # HTML erzeugen
    animals_html = generate_animals_html(animals_data)

    # Template einlesen
    with open("animals_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Platzhalter ersetzen
    filled_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Neue HTML-Datei schreiben
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(filled_html)

    print("animals.html wurde erfolgreich erstellt.")


if __name__ == "__main__":
    main()