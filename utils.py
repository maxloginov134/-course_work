import requests
from datetime import datetime


def get_data(url):
    """
    Получение данных по ссылке, формат данных: json
    :param url: ссылка на данные
    :return: файл json
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), "INFO: Данные получены успешно!"
    return None, f"WORNING: Статус ответа {response.status_code}"


def get_filtered_data(data, filtered_empty_from=False):
    """
    Фильтрация списка, если значение state == executed
    :param data: данные
    :param filtered_empty_from: если в списке данных нет параметра from
    :return: отфильтрованные данные по статусу операции - одобрена
    """
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values):
    """
    Сортировка данных по дате и получение последних пяти (или другого заданного количества)
    :param data: данные
    :param count_last_values: количество вывода данных
    :return: вывод последних 5 (или другого количества) операций
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    """
    Возвращает отформатированный список
    :param data: данные
    :return: заданный формат вывода по операции
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        sender = row["from"].split()
        sender_bill = sender.pop(-1)
        sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        sender_info = " ".join(sender)

        recipiend = f"**{row['to'][-4:]}"
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> Счет {recipiend}
{amount}
""")
    return formatted_data
