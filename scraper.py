import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://remoteok.io/remote-dev-jobs"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find_all("tr", class_="job")

job_list = []
for job in jobs:
    try:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        tags = [tag.text for tag in job.find_all("span", class_="tag")]
        link = "https://remoteok.io" + job['data-href']
        job_list.append({
            "Title": title,
            "Company": company,
            "Tags": ", ".join(tags),
            "Link": link
        })
    except:
        continue

df = pd.DataFrame(job_list)
df.to_csv("data/jobs.csv", index=False)
print(df.head())
