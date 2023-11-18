import requests
import pytest


def check_endpoint(url):
    response = requests.get(url)
    assert response.status_code == 200

    return response.json()


urls_for_test = [
    "https://dog.ceo/api/breeds/list/all",
    "https://dog.ceo/api/breeds/image/random",
    "https://dog.ceo/api/breeds/image/random/3",
    "https://dog.ceo/api/breed/hound/images/random/3",
    "https://dog.ceo/api/breed/hound/images",
    "https://dog.ceo/api/breed/hound/images/random",
    "https://dog.ceo/api/breed/hound/list",
    "https://dog.ceo/api/breed/hound/afghan/images",
    "https://dog.ceo/api/breed/hound/afghan/images/random/3",
    "https://dog.ceo/api/breed/hound/afghan/images/random",
]

tests_list = []


@pytest.mark.parametrize("url", urls_for_test)
def test_urls(url):
    response = check_endpoint(url)
    tests_list.append((url, response))


def make_report_string(index, url, result):
    report_string = (
        f"Тест №{index+1}:\nТестируемая ссылка: {url} .\n\nРезультат: {result}\n\n"
    )

    return report_string


def test_make_report():
    with open("Отчет по тестированию.txt", "w", encoding="utf8") as report:
        report.write(f"Количество тестов: {len(tests_list)}\n\n")
        for index, test in enumerate(tests_list):
            report_string = make_report_string(index, *test)
            report.write(report_string)