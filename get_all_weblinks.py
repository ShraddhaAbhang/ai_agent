import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags and extract the href attributes
        raw_links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Process links: remove links with '#' and convert relative links to absolute URLs
        processed_links = set()  # Use a set to remove duplicates
        for link in raw_links:
            if link != "#" and not link.startswith("#"):
                full_link = urljoin(url, link) if not link.startswith(('http://', 'https://', 'mailto:')) else link
                processed_links.add(full_link)
        
        return list(processed_links)  # Convert back to a list if needed
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

# Example usage
url = "https://indiantecsolutions.com"
links = get_all_links(url)

print("Unique Processed Links found on the webpage:")
for link in links:
    print(link)
