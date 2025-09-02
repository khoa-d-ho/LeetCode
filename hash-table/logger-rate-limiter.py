class Logger:

    def __init__(self):
        self.unique_messages = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.unique_messages:
            if timestamp <  self.unique_messages[message] + 10:
                return False
        
        self.unique_messages[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)