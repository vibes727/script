import requests
import time
import schedule
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def visit_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Successfully visited {url}")
        else:
            logging.warning(f"Failed to visit {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"An error occurred while visiting {url}: {e}")

def main():
    urls = ["https://poveditor.onrender.com/", "https://celeb-0j7w.onrender.com/"]  # URLs to visit

    logging.info("Starting site visitor script")
    
    # Schedule visiting both URLs every 25 minutes
    for url in urls:
        schedule.every(25).minutes.do(visit_site, url=url)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
