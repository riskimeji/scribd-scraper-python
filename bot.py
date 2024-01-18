import requests
import json

page_str = input("Page: ")
query_str = input("Kata Kunci: ")
filter_str = input("Filter: ")
query_str = query_str.replace(" ", "+")
page = int(page_str)
prefix_str = "https://www.scribd.com/document/"

url = "https://www.scribd.com/search/query?query={}&page={}".format(query_str, page)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    data = data.get("results", {}).get("documents", {}).get("content", {}).get("documents",{})
    documents_info = [{"url": prefix_str+str(doc["id"]), "title": doc["title"]} for doc in data if filter_str.lower() in doc["title"].lower()]
   
    with open('result.json', 'w') as file:
        json.dump(documents_info, file, indent=2)

    print("Sukses simpan.")
else:
    print(f"Gagal mengambil data. Status code: {response.status_code}")