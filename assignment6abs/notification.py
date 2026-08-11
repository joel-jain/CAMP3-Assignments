from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(sellf):
        pass
class EmailNotification(Notification):
    def send(self):
        print('Email noti')
class SMSNotification(Notification):
    def send(self):
        print("SMS NOti")
class PushNotification(Notification):
    def send(self):
        print("Push noti")
email=EmailNotification()
sms= SMSNotification()
push= PushNotification()

email.send()
sms.send()
push.send()