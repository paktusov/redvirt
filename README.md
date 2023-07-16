## RPC Сервер для получения статистики виртуальных машин

RPC сервер предоставляет метод `get_vm_statistic_rpc`, который позволяет получить статистику запущенных виртуальных машин. Сервер работает с использованием JSON-RPC протокола и принимает запросы на 8000 порту по адресу `/`.

### Методы

#### get_vm_statistic_rpc()

Метод `get_vm_statistic_rpc` возвращает статистику запущенных виртуальных машин.

**Пример запроса:**
```bash
curl -X POST http://localhost:8000 -d <тело запроса>
```

**Пример тела запроса:**
```json
{
  "jsonrpc": "2.0",
  "method": "get_vm_statistic_rpc",
  "id": 1
}
```

**Пример ответа (success):**

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "name": "ubuntu_server22.04",
      "cpus_usege": 2,
      "mem_usage": 4194304,
      "ip_addresses": ["192.168.122.94"]
    },
    {
      "name": "ubuntu22.04",
      "cpus_usege": 2,
      "mem_usage": 4194304,
      "ip_addresses": ["192.168.122.91"]
    }
  ],
  "id": 1
}
```

**Пример ответа (error):**

```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32600,
    "message": "Invalid request",
    "data": "The request failed schema validation"
  },
  "id": null
}
```

### Запуск сервера

Для запуска RPC сервера, выполните следующий код:

```bash
python -m app
```
