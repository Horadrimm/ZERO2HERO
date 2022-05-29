
def btc_math(rate, btc_count):

    # Валидация данных
    if not isinstance(rate, float):
        return "rate must be a float"
    if not isinstance(btc_count,int):
        return "btc_count must be a int"
    
    # Бизнес логика
    return rate * btc_count



# Тесты
def test_btc_math():
    test_cases = {
        "Базовый вариант" : {
            "input_data" : (10.0,50),
            "result" : 500.0,
        },
        "Ошибка rate должен быть флоат №1" : {
            "input_data" : ("10",50),
            "result" : "rate must be a float",
        },
        "Ошибка btc_count должен быть int №1" : {
            "input_data" : (10.0, "50"),
            "result" : "btc_count must be a int",
        },
    }

    for i in test_cases:
        print(f"test: {i}")
        print(f"input data :{test_cases[i]['input_data']}")
        print(f"result data :{test_cases[i]['result']}")

        rate, btc_count = test_cases[i]["input_data"]
        btc_match = btc_math(rate, btc_count)
        print(f"func result : {btc_match}")
        print( 30 * "*")
        print( "\n")

        assert btc_match == test_cases[i]["result"], test_cases[i]



if __name__ == "__main__":
    test_btc_math()