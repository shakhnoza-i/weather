Цель проекта:

Возвращать текущую температуру в любом городе и в любой точке планеты.

Реализовать используя Django, Django Rest Framework, Python.

Формат базового запроса:


REQUEST:

URL: http://localhost:8000/city
QUERY_PARAMS: city_name: Almaty, format: Celcius
METHOD: GET


RESPONSE:

JSON: {
    city: almaty, 
    temperature: 36, 
    descriptin: rain

}
