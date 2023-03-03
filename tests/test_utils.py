import pytest

from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677850838170&signature=XqhO-mChe1rnYcXtC7i60z_mMu0tExXvhpDQW5Jlzi8&downloadName=operations.json"
    assert get_data(url) is not None


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(get_filtered_data(data)) == 1
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 1

def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == "2021-07-03T18:35:29.512364"
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']
