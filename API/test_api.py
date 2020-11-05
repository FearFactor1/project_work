import requests
import pytest
from datetime import datetime
import cerberus
import allure


schema = {
    'updatedAt': {"type": "string", "required": True},
}


class TestClassApi:

    #1 тест
    @allure.feature('get')
    @allure.story('Проверяем запрос get')
    @pytest.mark.parametrize("num", ["2", "3", "4"])
    def test_get(self, url_api, num):
        res = requests.get(f'{url_api}api/users/{num}')
        with allure.step("Перевод в формат json"):
            js = res.json()
        with allure.step("Запрос отправлен, посмотрим код ответа"):
            assert res.status_code == 200
        assert res.json()
        with allure.step("Условие = если юзер 2 то имя Janet"):
            if num == "2":
                assert js['data']['first_name'] == 'Janet'

    #2 тест
    @allure.feature('put')
    @allure.story('Проверяем запрос put')
    @pytest.mark.parametrize("num", ["2", "3", "4"])
    def test_put(self, url_api, num):
        with allure.step("Создаём текущую дату"):
            dt = f"{datetime.today():%Y-%m-%d}"
        res = requests.put(f'{url_api}api/users/{num}')
        js = res.json()
        sp = str(js).split()
        with allure.step("Проверяем что в ответе дата текущая"):
            assert dt in sp[1]
        v = cerberus.Validator()
        with allure.step("проверяем, что ответ в правильном формате пришёл"):
            assert v.validate(js, schema)

    #3 тест
    @allure.feature('post')
    @allure.story('Проверяем запрос post')
    def test_post(self, url_api):
        res = requests.post(f'{url_api}api/register', data=f'"email": "sydney@fife"')
        js = res.json()
        with allure.step("проверяем статус код"):
            assert res.status_code == 400
        with allure.step("проверяем текст ошибки"):
            assert js['error'] == 'Missing email or username'

    #4 тест
    @allure.feature('delete')
    @allure.story('Проверяем запрос delete')
    @pytest.mark.parametrize("num", ["2", "3", "4"])
    def test_delete(self, url_api, num):
        res = requests.delete(f'{url_api}api/users/{num}')
        with allure.step("проверяем статус код, пользоветель удалён"):
            assert res.status_code == 204