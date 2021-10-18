import datetime


global ts
ts = datetime.datetime.now


class SMS_store:
    def __init__(self, read, sender, timeStamp, body):
        self._read = False
        # if 'sender' in args:
        #     self._sender = args['sender']
        self._sender = sender
        # if 'timeStamp' in args:
        #     self._timeStamp = args['timeStamp']
        self._timeStamp = timeStamp
        # if 'body' in args:
        #     self._body = args['body']
        self._body = body

    def read(self, r=False):
        if read:
            self._read = read
        try:
            return self._read
        except TypeError:
            return False

    def storage(self):
        message_count()
        return tuple(({self._read}, {self.sender}, {self.timeStamp}, {self.body}))

    def __str__(self):
        return f"({self._read}, {self._sender}, {self._timeStamp}, {self._body})"

    def read(self):
        return self._read

    def sender(self, s=None):
        if s:
            self.sender = s
        try:
            return self._sender
        except AttributeError:
            return None

    def timeStamp(self, t=None):
        if t:
            self.timeStamp = t
        try:
            return self._timeStamp
        except AttributeError:
            return None

    def body(self, b=None):
        if b:
            self.body = b
        try:
            return self._body
        except AttributeError:
            return None

    def message_count(self):
        # count = 0
        # c = self.storage
        # for x in c:
        #     count += 1
        #     return count
        pass


def main():
    my_inbox = SMS_store(False, 639985507531,
                         ts(), "Hello World")
    print(my_inbox)
    print(my_inbox.sender())
    # print(my_inbox.message_count())


if __name__ == "__main__":
    main()
