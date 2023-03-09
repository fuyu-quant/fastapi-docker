import requests
import json

def main():
    url = 'http://127.0.0.1:8040/item/'
    body = {
        "name": "white T-shirt",
        "description": "This is T-shirt",
        "price": 3300,
        "tax": 1.1
        }
    res = requests.post(url, json.dumps(body))
    print(res.json())

if __name__ == "__main__":
    main()