from airflow.providers.telegram.hooks.telegram import TelegramHook # импортируем хук телеграма

def send_telegram_success_message(context): # на вход принимаем словарь с контекстными переменными
    hook = TelegramHook(token='{7669814284:AAGvNBglev6aMXVOjsR57vkDn-6Feao27RI}', chat_id='{4824444239}')
    dag = context['dag'].dag_id
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!' # определение текста сообщения
    hook.send_message({
        'chat_id': '{вставьте ваш chat_id}',
        'text': message
    }) # отправление сообщения