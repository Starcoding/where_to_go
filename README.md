# Куда пойти — Москва глазами Юры

Фронтенд для будущего сайта о самых интересных местах в Москве. Авторский проект Юры.
Сайт представляет из себя площадку, на которой можно просмотреть интересные места на карте (на карте стоят отметки, при клике по отметке - откроется карточка места, с подробной информацией о нём).
Места можно добавлять как вручную (Через панель администратора их также можно изменять), так и из заранее подготовленных источников.


## Как запустить
Откройте консоль и следуйте по шагам:
* Создайте папку и перейдите в неё (```mkdir *название папки*``` -> ```cd *название папки*```);
* Создайте виртуальное окружение venv (```python -m venv .``` - для создания виртуального пространства внутри текущей папки);
* Запустите виртуальное окружение ```Scripts\activate```;
* Скачайте код к себе в папку ```git clone https://github.com/Starcoding/where_to_go```;
* Создать в корне файл ```.env```;
* Поместить в этот файл значение для секретного ключа (Генератор ключа https://djecrety.ir/) ```SECRET_KEY=*ваш новый сгенерированный ключ*``` а также значение переменной ```DEBUG= *True или False в зависимости от надобности функций дебага*```;
* Установите необходимые библиотеки ```pip install -r requirements.txt```;
* Сделайте необходимые миграции для базы данных ```python manage.py migrate --run-syncdb```;
* Создайте учетную запись для администратора ```python manage.py createsuperuser``` - следуйте инструкциям в консоли;
* Запустите проект ```python manage.py runserver```;
* Зайдите в админку ```http://127.0.0.1:8000/admin``` и добавьте новые места (```Places```). После их добавления на главное странице появятся новые места.
Для широкого использования рекомендуется использовать любой веб-сервер отличный от сервера для разработки который предоставляет Django -```python manage.py runserver```.

Также есть возможность добавлять места не вручную - ```python manage.py loadplace *ссылка на json*``` [Пример](https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json)
## Подробнее о настройках окружения
В файле ```.env``` должны находится настройки окружения:
* SECRET_KEY - Секретный ключ для шифрования пользовательских данных в Django (рекомендуется использовать криптостойкий ключ, можно взять например на https://djecrety.ir/)
* DEBUG - имеет значения True или False, нужен для включения режима отладки на сервере (Будет показывать вам ошибки детально, а не просто ошибкe)

## Настройки

Внизу справа на основной странице можно включить отладочный режим логгирования.

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Источники данных

Фронтенд получает данные из двух источников. Первый источник — это JSON, запечённый внутрь HTML. Он содержит полный список объектов на карте. И он прячется внутри тега `script`:

```javascript
<script id="places-geojson" type="application/json">
  {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [37.62, 55.793676]
        },
        "properties": {
          // Специфичные для этого сайта данные
          "title": "Легенды Москвы",
          "placeId": "moscow_legends",
          "detailsUrl": "./places/moscow_legends.json"
        }
      },
      // ...
    ]
  }
</script>
```

При загрузке страницы JS код ищет тег с id `places-geojson`, считывает содержимое и помещает все объекты на карту.

Данные записаны в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные, кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важна лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.

Второй источник данных — это те самые адреса в поле `detailsUrl` c подробными сведениями о локации. Каждый раз, когда пользователь выбирает локацию на карте JS код отправляет запрос на сервер и получает картинки, текст и прочую информацию об объекте. Формат ответа сервера такой:

```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
