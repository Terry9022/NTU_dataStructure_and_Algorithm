class Calendar:
    def __init__(self):
        
        self.date={}

    def book(self, start: int, end: int) -> bool:
        """
        Book the event where interval started from start(included) to end(excluded)

        If availble: book it and return True
        else: return False
        """
        
        for i in range(start,end):
            if i in self.date.keys() and self.date[i]=="X":
                return False
        
        for i in range(start,end):
            self.date[i]="X"
        return True


