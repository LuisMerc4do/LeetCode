import requests
from bs4 import BeautifulSoup

def fetch_url_content(url):
    """Fetch the content of a URL and return it as a string."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_coordinates(content):
    """Extract coordinates and their corresponding characters from the content."""
    soup = BeautifulSoup(content, 'html.parser')
    text_content = soup.get_text(separator='\n').strip()

    start_extracting = False
    coordinates = []
    for line in text_content.splitlines():
        if start_extracting:
            coordinates.append(line.strip())
        if line.strip() == "y-coordinate":
            start_extracting = True

    # Group coordinates into triplets
    grouped_coordinates = [coordinates[i:i+3] for i in range(0, len(coordinates), 3)]

    return grouped_coordinates

def create_grid(coordinates):
    """Create a grid from the coordinates."""
    max_x, max_y = 0, 0

    # Find the maximum x and y values
    for coord in coordinates:
        if len(coord) != 3:
            continue
        try:
            x, char, y = coord
            x = int(x)  # Ensure that x is numeric
            y = int(y)  # Ensure that y is numeric
        except ValueError:
            continue  # Skip invalid coordinates where x or y isn't numeric

        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Create a grid with empty spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters on the grid based on coordinates
    for coord in coordinates:
        if len(coord) != 3:
            continue
        try:
            x, char, y = coord
            x = int(x)
            y = int(y)
        except ValueError:
            continue  # Skip invalid coordinates where x or y isn't numeric

        # Only place valid coordinates
        if 0 <= x <= max_x and 0 <= y <= max_y:
            grid[y][x] = char

    return grid

def display_grid(grid):
    """Display the grid."""
    for row in grid:
        print(''.join(row))

def main(url):
    """Main function to process the URL and display the grid."""
    content = fetch_url_content(url)
    if not content:
        print("Failed to fetch content from the URL.")
        return

    coordinates = parse_coordinates(content)
    grid = create_grid(coordinates)
    display_grid(grid)

# Example URL
url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
main(url)
