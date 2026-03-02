class Menu:
    def __init__(self, item):
        self.item = item
        self.items = []

    def addItem(self, item):
        self.items.append(item)
        print(f'{item} added')

    def removeItem(self, item):
        print(f'{item} removing...')

        for i in item:
            self.items.remove(item)
        
    def showItem(self):
        for i in self.items:
            print(f'{i} ')


menu1 = Menu('BreakFast')
menu1.addItem('Idly')
menu1.addItem('Dosa')
menu1.showItem();            