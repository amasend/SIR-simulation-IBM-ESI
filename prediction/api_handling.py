__all__ = [
    'get_countries_names',
    'get_data_from_country',
    'save_to_csv'
]

import requests
import csv


def get_countries_names() -> list:
    """
    Function for getting list of all countries names procived by public
    COVID-19 api on site "https://api.covid19api.com"

    Returns
    -------
    List with all countries names.

    Example
    -------
    >>> countries_names = get_countries_names()
    """

    countries_names = []
    url = "https://api.covid19api.com/countries"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    for element in response.json():
        countries_names.append(element['Slug'])

    return countries_names


def get_data_from_country(country_name: str) -> list:
    """
    Function for geting data from api for specific country.

    Parameters
    ----------
    country_name: str, required
        Name of countr to get data about. It must be slug value provided by
        api site.

    Returns
    -------
    List with data from begining of virus in country of specified status.

    Example
    -------
    >>> poland_data = get_data_from_country('poland')
    """

    url = f"https://api.covid19api.com/total/dayone/country/{country_name}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    return data


def prepare_data_to_save(raw_data: list, status: str) -> list:
    """
    Change data from function get_data_from_country() to format ready to save as
    .csv file.

    Parameters
    ----------
    raw_data: list, required
        List of data produced by get_data_from_country() function.
    status: str, required
        Status of group to get, it could be Confirmed, Active, Deaths, Recovered.

    Returns
    -------
    List with changed data structure.

    Example
    -------
    >>> prepare_data = prepare_data_to_save(poland_data, 'Active')
    """

    data = []

    for element in raw_data:
        data.append([element['Country'], element['Date'], element[status]])

    return data


def save_to_csv(data: list, file_name: str) -> bool:
    """
    Saved given data to .csv file.

    Parameters
    ----------
    data: list, required
        Data produced by function prepare_data_to_save().
    file_name: str, required
        Path and file name to where save file. It should not include ".csv" at
        the end.

    Returns
    -------
    True if file created or false if not.

    Example
    -------
    >>> save_to_csv(prepare_data, 'test')
    """

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
