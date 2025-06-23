import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def extract_text(soup):
    if soup:
        return soup.get_text(separator='\n', strip=True)
    else:
        return None


def main():
    url = input("Enter the URL of the website to scrape: ")
    soup = scrape_website(url)
    text = extract_text(soup)
    if text:
        print("Extracted Text:")
        print(text)
    else:
        print("No text could be extracted from the website.")


if __name__ == "__main__":
    main()
# This code is a simple web scraper that extracts text from a given URL.
# It uses the requests library to fetch the webpage and BeautifulSoup to
# parse the HTML.
# The extracted text is printed to the console.
# Make sure to install the required libraries before running the code:
# pip install requests beautifulsoup4
