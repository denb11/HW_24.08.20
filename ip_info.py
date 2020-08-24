import json
import requests


def idr():
    query = input("Enter an IP or DOMAIN name: ")

    if query == "":
        print(f"\n nu ati introdus nimic...")
    else:
        endpoint = f"http://ip-api.com/json/{query}"
        response = requests.get(endpoint)
        data = json.loads(response.text)
        if data['status'] != "fail":
            country = data['country']
            city = data['city']
            status = data['status']
            print(f"The domain is located in:  {country}/{city}\nStatus:{status}")
        else:
            print(f'Domian or IP Adress INCORRECT')

    def menu():
        print("#" * 30)
        print("1. repeat")
        print("2. exit")
        option = None
        while option != 1 or 2 or "":
            option = input()
            if option == 1:
                idr()
            if option == "":
                idr()
            if option == 2:
                break
            break

    menu()


idr()
