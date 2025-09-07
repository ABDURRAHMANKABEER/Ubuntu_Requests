import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        # Step 1: Making directory if it doesn’t exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Step 2: Fetching image
        response = requests.get(url, timeout=10)
        response.raise_for_status() 

        # Step 3: Extracting filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # default filename if name don't exist
        if not filename:
            filename = "downloaded_image.jpg"

        # Step 4: Checking for duplicates
        filepath = os.path.join("Fetched_Images", filename)
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(filepath):
            filename = f"{base}_{counter}{ext}"
            filepath = os.path.join("Fetched_Images", filename)
            counter += 1

        # Step 5: Saving file
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.MissingSchema:
        print("✗ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("✗ Connection error. Please check your internet.")
    except requests.exceptions.Timeout:
        print("✗ Request timed out. Try again later.")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Asking for multiple URLs separated by commas
    urls = input("Please enter image URLs (separated by commas): ").strip().split(",")

    for url in urls:
        url = url.strip()
        if url:  # Only process non-empty strings
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
