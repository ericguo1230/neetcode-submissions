class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.subscribers: set[Observer] = set()

    def subscribe(self, observer: Observer) -> None:
        self.subscribers.add(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribers.remove(observer)

    def updateStock(self, newStock: int) -> None:
        if newStock > 0 and self.stock == 0:
            for subscriber in self.subscribers:
                subscriber.notify(self.itemName)
        self.stock = newStock
        
