__all__ = [
    'get_countries_names',
    'get_data_from_country',
    'save_to_csv'
]

import requests
import csv


def get_countries_names() -> list:
    countries_names = []
    url = "https://api.covid19api.com/countries"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    for element in response.json():
        countries_names.append(element['Slug'])

    return countries_names


def get_data_from_country(country_name: str, status: str) -> list:
    url = f"https://api.covid19api.com/dayone/country/{country_name}/status/{status}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    return data


def prepare_data_to_save(raw_data: list) -> list:
    data = []

    for element in raw_data:
        data.append([element['Country'], element['Date'], element['Cases']])

    return data


def save_to_csv(data: list, file_name: str) -> bool:
    with open(f'{file_name}.csv', 'w+', newline='') as csvfile:
        fieldnames = ['name', 'date', 'amount']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for value in data:
            writer.writerow(value)

    if writer:
        return True
    else:
        return False


if __name__ == '__main__':
    countries = get_countries_names()
    print(countries)
    # for country in countries:
    #     result = get_data_from_country(country, 'confirmed')
    #     save_to_csv(result, f'./countries_data/{country}')

    result = get_data_from_country('poland', 'confirmed')
    res = prepare_data_to_save(result)
