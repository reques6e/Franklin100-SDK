### Асинхронный клиент для Franklin API

Этот Python-код представляет собой асинхронный клиент для работы с Franklin API – сервисом для заказа и отслеживания социальных медиа-услуг. Код использует библиотеку `aiohttp` для асинхронных HTTP-запросов.

#### Использование

1. **Инициализация клиента**

    Создайте экземпляр класса `FranklinAPI`, передав в конструктор ключ API:

    ```python
    key = 'yourKey'
    franklin_api = FranklinAPI(key)
    ```

2. **Получение списка услуг**

    Для получения списка доступных услуг используйте метод `get_services()`:

    ```python
    services = await franklin_api.get_services()
    print(services)
    ```

3. **Создание заказа**

    Для создания заказа используйте метод `create_order()` и передайте параметры, такие как `service_id`, `link`, и `quantity`:

    ```python
    order_response = await franklin_api.create_order(service_id=1, link='instagram.com/instagram', quantity=100)
    order_id = order_response.get('order')
    print(f"Created Order ID: {order_id}")
    ```

4. **Получение статуса заказа**

    Для получения статуса заказа используйте методы `get_order_status()` или `get_orders_status()`:

    ```python
    status_response = await franklin_api.get_order_status(order_id)
    print(f"Order Status: {status_response}")
    ```

5. **Получение баланса аккаунта**

    Для получения текущего баланса аккаунта используйте метод `get_balance()`:

    ```python
    balance_response = await franklin_api.get_balance()
    print(f"Account Balance: {balance_response}")
    ```

6. **Отмена заказа**

    Для отмены заказа используйте метод `cancel_order()`:

    ```python
    cancel_response = await franklin_api.cancel_order(order_id)
    print(f"Cancel Order Response: {cancel_response}")
    ```

7. **Завершение сессии**

    Не забудьте закрыть сессию после завершения работы:

    ```python
    await franklin_api.session.close()
    ```

#### Замечание

Пожалуйста, замените `'yourKey'` на ваш реальный ключ API перед использованием. Код разработан для асинхронного взаимодействия с Franklin API, что обеспечивает эффективность в обработке множества запросов.

<details>
<summary>Код Python</summary>

```python
# async def main():
    key = 'yourKey'
    franklin_api = FranklinAPI(key)

    # Получение списка услуг
    services = await franklin_api.get_services()
    print(services)

    # Создание заказа
    order_response = await franklin_api.create_order(service_id=1, link='instagram.com/instagram', quantity=100)
    order_id = order_response.get('order')
    print(f"Created Order ID: {order_id}")

    # Получение статуса заказа
    status_response = await franklin_api.get_order_status(order_id)
    print(f"Order Status: {status_response}")

    # Получение баланса
    balance_response = await franklin_api.get_balance()
    print(f"Account Balance: {balance_response}")

    # Отмена заказа
    cancel_response = await franklin_api.cancel_order(order_id)
    print(f"Cancel Order Response: {cancel_response}")

    # Завершение работы сессии
    await franklin_api.session.close()
