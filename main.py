from requests import get

if __name__ == "__main__":
    # Change the URL to your desired endpoint
    response = get("https://api.example.com/data")
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        print(data)
    else:
        print("Error: Failed to get data from the API.")
