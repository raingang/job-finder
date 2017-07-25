from .data.GetCityID import choice_city
from .data.GetData import write


def scrap():
    city_id = choice_city()
    job = input('Введите искомую вакансию: ')
    url = 'https://rabota.ua/jobsearch/vacancy_list?regionId=' + \
        str(city_id) + '&keyWords=' + job
    write(url)
