
# create a list, then iterate it with a get in the loop

import requests
import json
from pprint import pprint

response = requests.get("https://world.openfoodfacts.org/api/v0/product/737628064502.json")


if response.status_code == 200:
    print(response.status_code)
    data = pprint(response.json())
    dict = json.loads(data)