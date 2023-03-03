import pytest

@pytest.fixture
def test_data():
    return [
        {"date": "2019-08-26T10:50:58.294041",
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "id": 441945886,
         "operationAmount": {"amount": "31957.58",
                       "currency": {"name": "руб.","code": "RUB"}},
         "to": "Счет 64686473678894779589"},
         {"date": "2021-07-03T18:35:29.512364",
          "description": "Перевод организации",
          "id": 41428829,
          "operationAmount": {"amount": "8221.37",
                        "currency": {"name": "USD","code": "USD"}},
          "state": "CONCELED",
          "to": "Счет 35383033474447895560"},
          {"date": "2018-06-30T02:08:58.425572",
           "description": "Перевод организации",
           "from": "Счет 75106830613657916952",
           "id": 939719570,
           "operationAmount": {"amount": "9824.07",
                         "currency": {"name": "USD","code": "USD"}},
           "state": "EXECUTED",
           "to": "Счет 11776614605963066702"}
    ]
