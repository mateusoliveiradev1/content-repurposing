import sys, requests
from bs4 import BeautifulSoup
def scrape(url):
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        text = BeautifulSoup(res.text, 'html.parser').get_text(separator=' ', strip=True)
        print(text[:4000])
    except Exception as e: print(f"Failed: {e}")
if __name__ == "__main__":
    if len(sys.argv) > 1: scrape(sys.argv[1])
