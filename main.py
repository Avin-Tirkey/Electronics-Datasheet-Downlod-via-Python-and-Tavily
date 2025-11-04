# To install: pip install tavily-python
import urllib.request
import time
import requests
import os
import urllib3

from tavily import TavilyClient
cmp=[ "st.com", "alldatasheet.com", "datasheet","nrf","nordicsemi", "book", "millionaire"]
client = TavilyClient("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")
response = client.search(
    query="stm32f411re datasheet filetype:pdf"
)
print(response.keys())
#print(response)
#print("RESULTS$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
resp_list=list(response.get('results'))
c=0
for i in resp_list:
    if c==1:
        break
    url=i.get('url')
    for comp in cmp:
        if comp.lower() in url.lower():
            print(comp)
            print(url)
            pdf_url=url
            local_filename = "dnd101.pdf"
            c+=1
            break
    

    
    
        
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

download_directory = os.path.abspath(os.path.join(os.getcwd(), "downloads"))

os.makedirs(download_directory, exist_ok=True)

# Full path for the file
file_path = os.path.join(download_directory, local_filename)

try:
   # print(f"Downloading PDF from: {pdf_url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # Add verify=False to bypass SSL verification
    response = requests.get(pdf_url, headers=headers, stream=True, timeout=30, verify=False)
    response.raise_for_status()
    
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    #print(f"✅ PDF downloaded successfully to: {file_path}")
    #print(f"File size: {os.path.getsize(file_path) / 1024:.2f} KB")

except requests.exceptions.RequestException as e:
    print(f"❌ Download failed: {e}")
