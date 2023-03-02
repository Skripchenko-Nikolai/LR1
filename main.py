from bs4 import BeautifulSoup
import requests


# Функция парсит сайт для получения факультетов
def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', id='pagecontent')
    description = ''
    for data in block:
        if data.find('a'):
            description = data.text
    save_result_in_file(description.splitlines())


# Фукнция записывает факультеты в файл faculties.txt
def save_result_in_file(faculties):
    file = open("faculties.txt", "w")
    for faculty in faculties:
        if faculty != "":
            file.write(faculty + "\n")
    file.close()


if __name__ == '__main__':
    parse()
