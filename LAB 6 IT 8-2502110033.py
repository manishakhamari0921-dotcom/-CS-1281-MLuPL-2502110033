
# IT8 - The Parts Catalogue

# Parsed production log lines
log_lines = [
    {"code": "P101", "diameter": 15},
    {"code": "P102", "diameter": 25},
    {"code": "P103", "diameter": 35},
    {"code": "P104", "diameter": 45},
    {"code": "P105", "diameter": 8},
    {"code": "P106", "diameter": 20}
]


# Build parts catalogue
def build_catalogue(log_lines):

    catalogue = {}

    for line in log_lines:
        code = line["code"]
        diameter = line["diameter"]

        catalogue[code] = diameter

    return catalogue


# Tool 1: Lookup part diameter
def lookup(catalogue, code):

    return catalogue.get(code, "Part Not Found")


# Tool 2: Find scrap part codes
def scrap_codes(catalogue):

    scrap = set()

    for code, diameter in catalogue.items():

        if diameter < 10 or diameter > 40:
            scrap.add(code)

    return scrap


# Main program
if __name__ == "__main__":

    catalogue = build_catalogue(log_lines)

    print("PARTS CATALOGUE")
    print(catalogue)

    print("\nPART LOOKUP")
    print("P101:", lookup(catalogue, "P101"))
    print("P999:", lookup(catalogue, "P999"))

    print("\nSCRAP PART CODES")
    print(scrap_codes(catalogue))
