import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_url_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            return title
        else:
            return None
    except Exception as e:
        print(f"Error fetching title for {url}: {e}")
        return None

def convert_urls_to_markdown(input_file, output_file, output_html):
    try:
        with open(input_file, 'r') as file:
            urls = file.readlines()

        with open(output_file, 'w') as file:
            for url in tqdm(urls, desc="Converting URLs", unit=" URL"):
                # Remove leading and trailing whitespaces and newline characters
                url = url.strip()
                title = get_url_title(url)
                if title:
                    # Write Markdown formatted URL with title to the output file
                    file.write(f"[{title}]({url})\n")
                else:
                    # Write Markdown formatted URL without title if title couldn't be fetched
                    file.write(f"[{url}]({url})\n")
                    
        with open(output_html, 'w') as file:
            for url in tqdm(urls, desc="Converting URLs", unit=" URL"):
                # Remove leading and trailing whitespaces and newline characters
                url = url.strip()
                title = get_url_title(url)
                if title:
                    # Write Markdown formatted URL with title to the output file
                    file.write(f"<a href='{url}'>{title}</a>\n")
                else:
                    # Write Markdown formatted URL without title if title couldn't be fetched
                    file.write(f"<a href='{url}'>{url}</a>\n")

        print(f"\nURLs converted successfully to Markdown format and saved to {output_file}")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
input_file_path = 'input_urls.txt'
output_file_path = 'output_urls.md'
output_file_path_for_html = "output.html"
convert_urls_to_markdown(input_file_path, output_file_path, output_file_path_for_html)
