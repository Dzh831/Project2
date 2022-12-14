import requests
upload_url = ''
file_path = ''

headers = {'Content-Type': "text/plain"}


def connect_to_endpoint(url):
    response = requests.put(url, data=open(file_path, 'rb'), headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.text


def main():
    response = connect_to_endpoint(upload_url)
    print(response)


if __name__ == "__main__":
    main()