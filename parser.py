#from bash pip install zeep
from zeep import Client

# Создаем клиента SOAP
client = Client('http://api.rossko.ru/service/v2.1/GetOrders?wsdl')

# Вызываем метод GetOrders с переданными параметрами
response = client.service.GetOrders(
    KEY1='your_key1',
    KEY2='your_key2',
    start_date='date_start format YYYY-mm-DD',
    end_date='date_end format YYYY-mm-DD'
)

if response['success']:
    # Получаем список заказов
    orders_list = response['OrdersList']['Order']
    
    # Инициализируем переменную для хранения общей суммы
    total_sum = 0.0
    
    # Проходим по каждому заказу и суммируем цены
    for order in orders_list:
        # Приводим цену к float и добавляем ее к общей сумме
        total_sum += float(order['total_price'])
    
    # Выводим результат в консоль
    print(f"Общая сумма всех заказов: {total_sum}")
else:
    # Выводим сообщение об ошибке, если запрос не был успешным
    print("Ошибка при выполнении запроса:", response['message'])