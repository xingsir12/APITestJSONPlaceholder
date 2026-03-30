# APITestJSONPlaceholder
# API Test Framework для JSONPlaceholder

Автоматизированные тесты для REST API с использованием pytest и requests.

## 🎯 Что тестируется

- **Users API** - создание, чтение, обновление, удаление пользователей
- **Posts API** - работа с постами пользователей
- **Comments API** - работа с комментариями к постам

## 🛠️ Технологии

- Python 3.8+
- pytest - фреймворк для тестирования
- requests - HTTP клиент
- pytest-html - генерация HTML отчётов
- logging - логирование тестов

## 📦 Установка
```bash
# Клонировать репозиторий
git clone <your-repo>
cd api-test-framework

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements.txt
```

## 🚀 Запуск тестов

### Все тесты
```bash
pytest -v
```

### По маркерам
```bash
# Smoke тесты (критические проверки)
pytest -m smoke -v

# Regression тесты
pytest -m regression -v

# Negative тесты
pytest -m negative -v

# Performance тесты
pytest -m performance -v

# API тесты
pytest -m api -v
```

### Комбинации маркеров
```bash
# Smoke ИЛИ regression
pytest -m "smoke or regression" -v

# API но НЕ negative
pytest -m "api and not negative" -v
```

### С HTML отчётом
```bash
pytest --html=reports/report.html --self-contained-html
```

## 📊 Структура проекта
```
api-test-framework/
├── tests/              # Тесты
│   ├── test_users.py   # ✅ 10 тестов
│   ├── test_posts.py   # ✅ 7 тестов
│   └── test_comments.py # ✅ 4 теста
├── utils/              # Утилиты
│   ├── api_client.py   # API клиент с логированием
│   ├── test_data.py    # Тестовые данные
│   └── logger.py       # Настройка логирования
├── logs/               # Логи тестов
├── reports/            # HTML отчёты
├── conftest.py         # Фикстуры pytest
├── pytest.ini          # Конфигурация pytest
└── requirements.txt    # Зависимости
```

## ✨ Особенности

- ✅ **Маркеры pytest** - запуск тестов по категориям
- ✅ **Логирование** - детальные логи всех запросов/ответов
- ✅ **Фикстуры** - переиспользование кода
- ✅ **Параметризация** - тесты с множественными данными
- ✅ **Проверка производительности** - время ответа API
- ✅ **Негативные тесты** - проверка обработки ошибок
- ✅ **HTML отчёты** - красивые отчёты о прогоне

## 📈 Покрытие

| Категория | Количество |
|-----------|------------|
| Smoke | 6 тестов |
| Regression | 10 тестов |
| Negative | 3 теста |
| Performance | 1 тест |
| API | 21 тест |
| **Всего** | **21 тест** |

## 📝 Логирование

Логи сохраняются в папке `logs/` с timestamp:
```
logs/test_run_20260212_153045.log
```

Каждый лог содержит:
- 🚀 Инициализацию сессии
- 📤 Все HTTP запросы
- 📥 Все HTTP ответы
- ✅ Результаты тестов
- ❌ Ошибки с деталями

## ⚠️ Особенности JSONPlaceholder API

JSONPlaceholder - это mock API, поэтому:
- POST запросы могут возвращать 200 вместо 201
- Операции с несуществующими ресурсами иногда возвращают 500
- Данные не сохраняются реально (симуляция)

В тестах это учтено - проверяются допустимые статус-коды.

## 🎓 Автор

Студент 3 курса, изучаю автоматизацию тестирования для стажировки
