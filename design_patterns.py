#Singleton pattern

# you often want only one instance of a logger or config reader in your entire application.
class SingletonLogger:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self,msg):
        print(f"log : {msg}")


obj1 = SingletonLogger()
obj2 = SingletonLogger()
print(id(obj1))
print(id(obj2))
print(obj1.log("here is your log msg"))

# ✅ 2. Factory Pattern
# 🔸 Real-world use case: Object Creation Based on User Input or Config
# Imagine a notification system that sends either Email or SMS. we have privilage to implement email and sms in diifent way isolated from each other

class EmailNotification:
    def send(self, msg):
        print(f"Sending email: {msg}")

class SMSNotification:
    def send(self, msg):
        print(f"Sending SMS: {msg}")

def notification_factory(method):
    if method == "email":
        return EmailNotification()
    elif method == "sms":
        return SMSNotification()

notifier = notification_factory("sms")
notifier.send("OTP is 123456")  # Sending SMS: OTP is 123456


# ✅ 3. Observer
# 🛠 Use Case: When you want one object to notify others about changes (pub-sub system). E.g., Event systems, Django signals.
#
# ✅ Analogy: You subscribe to a YouTube channel — when a new video is posted, all subscribers are notified.
#
# 🔁 Behavior: Maintains a list of subscribers and notifies them.

class Observer:
    def update(self, data):
        raise NotImplementedError("Subclass must implement update method")


class EmailNotifier(Observer):
    def update(self, data):
        print(f"EmailNotifier received: {data}")


class SMSNotifier(Observer):
    def update(self, data):
        print(f"SMSNotifier received: {data}")


class Subject:
    def __init__(self):
        self._observers = []  # ✅ Storing observers

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)  # ✅ Notify all observers


# ✅ Usage
subject = Subject()

email = EmailNotifier()
sms = SMSNotifier()

subject.subscribe(email)
subject.subscribe(sms)

subject.notify("New QR Code Generated")


# ✅ 4. Strategy Pattern
# 🔸 Real-world use case: Payment Gateways / Sorting Algorithms
# Imagine a payment system where you want to switch between Razorpay and PayPal easily.
#
# python
# Copy
# Edit
class Razorpay:
    def pay(self, amount):
        print(f"Paid {amount} via Razorpay")

class PayPal:
    def pay(self, amount):
        print(f"Paid {amount} via PayPal")

class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway

    def process(self, amount):
        self.gateway.pay(amount)

pay = PaymentProcessor(Razorpay())
pay.process(500)

pay.gateway = PayPal()
pay.process(500)


# ✅ 5. Decorator Pattern
# 🔸 Real-world use case: Access Control / Logging / Caching
# In Django, decorators like @login_required are used to wrap views for authentication.
#
# Example: Logging every time a function runs.
#
# python
# Copy
# Edit
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def generate_qr():
    print("QR generated!")

generate_qr()

# 🔧 Creational Patterns – Object creation mechanisms
#
# 🧱 Structural Patterns – Object composition, relationships
#
# 🧠 Behavioral Patterns – Communication between objects


# Great question! Design patterns are categorized based on what they aim to solve:
#
# 🔧 Creational Patterns – Object creation mechanisms
#
# 🧱 Structural Patterns – Object composition, relationships
#
# 🧠 Behavioral Patterns – Communication between objects
#
# Let’s look at the patterns you’ve learned so far, how they’re categorized, and why:
#
# 🔧 1. Singleton Pattern → Creational
# Why?
#
# It controls how an object is created, ensuring only one instance exists.
#
# Focus is on creation logic and global access.
#
# Use case: Logging system, DB connection pool
#
# 🧠 2. Observer Pattern → Behavioral
# Why?
#
# It deals with how objects communicate.
#
# The subject notifies multiple observers about state changes — which is a behavioral coordination.
#
# Use case: UI event systems, Django signals, stock price trackers
#
# Let me also give you a few more examples for each category to strengthen the intuition:
#
# 🎯 Design Pattern Categories Summary
# Category	Pattern	Purpose/Focus	Example Use Case
# Creational	Singleton	Ensure only one object instance exists	Logger, config manager, thread pool
# Factory	Create objects without specifying exact class	serializers.new_from_model() in Django
# Builder	Build complex objects step by step	Report generator
# Structural	Adapter	Allow incompatible classes to work together	Wrapping legacy code
# Decorator	Add new behavior without modifying code	@login_required in Django
# Composite	Tree structure to represent part-whole	HTML, menus
# Behavioral	Observer	Notify objects of state change	Django signals, UI event listeners
# Strategy	Choose algorithm at runtime	Sorting strategies, payment methods
# Command	Encapsulate request as object	Undo/redo systems, task queues