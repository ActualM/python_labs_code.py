class Publisher:
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)


class EmailSubscriber:
    def update(self, message):
        print(f"EmailSubscriber received message: {message}")


class SMSSubscriber:
    def update(self, message):
        print(f"SMSSubscriber received message: {message}")


class PushNotificationSubscriber:
    def update(self, message):
        print(f"PushNotificationSubscriber received message: {message}")



if __name__ == "__main__":
    # Создаем объект Publisher
    publisher = Publisher()

    # Создаем несколько объектов Subscriber
    email_subscriber = EmailSubscriber()
    sms_subscriber = SMSSubscriber()
    push_notification_subscriber = PushNotificationSubscriber()

    # Добавляем подписчиков к издателю
    publisher.add_subscriber(email_subscriber)
    publisher.add_subscriber(sms_subscriber)
    publisher.add_subscriber(push_notification_subscriber)

    # Издатель отправляет уведомление подписчикам
    publisher.notify_subscribers("Hello, subscribers!")

    # Удаляем одного из подписчиков
    publisher.remove_subscriber(sms_subscriber)

    # Издатель отправляет уведомление оставшимся подписчикам
    publisher.notify_subscribers("Message after removing a subscriber.")
