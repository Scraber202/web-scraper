# Imports
import requests
from bs4 import BeautifulSoup

# Website URL to scrape
URL = "https://realpython.github.io/fake-jobs/"

# URL page data
page = requests.get(URL)

# Print the page data
print(page.text)

# Parse page data to interact with it
soup = BeautifulSoup(page.content, "html.parser")

# Find element by id
results = soup.find(id="ResultsContainer")

# Print parsed data (.prettify is optional)
print(results.prettify())

# Find all divs in results that contain the class card-content
job_elements = results.find_all("div", class_="card-content")

# Print all elements from job_elements
for job_element in job_elements:
    print(job_element, end="\n"*2)
    
# Find titles, companies, and locations, print the text (.strip() is optional)
for job_element in job_elements:
  title_element = job_element.find("h2", class_="title")
  company_element = job_element.find("h3", class_="company")
  location_element = job_element.find("p", class_="location")
  print(f'{title_element.text.strip()}\n{company_element.text.strip()}\n{location_element.text.strip()}\n')

# Find all mentions of python in h2 tags
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

# Move up the hierarchy to a parent element to access other target information
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Find titles, companies, and locations, print the text (.strip is optional)
for job_element in python_job_elements:
  title_element = job_element.find("h2", class_="title")
  company_element = job_element.find("h3", class_="company")
  location_element = job_element.find("p", class_="location")
  print(f'{title_element.text.strip()}\n{company_element.text.strip()}\n{location_element.text.strip()}\n')

# Find all a tags, extract and print every href attribute
for job_element in python_job_elements:
  links = job_element.find_all("a")
  for link in links:
    link_url = link["href"]
    print(f'Apply Here: {link_url}\n')  