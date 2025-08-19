import requests


def create_transfer(transfer_data: dict):
    base_url = "http://127.0.0.1:8155"
    end_point = "/transfer"
    response = requests.post(f'{base_url}{end_point}', json=transfer_data)
    status = response.status_code
    print(status)
    print(response.text)