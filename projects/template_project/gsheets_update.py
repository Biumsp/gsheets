class GSheetsUpdate():
    def __init__(self):
        self.body = {"requests": []}

    def add_request(self, request):
        self.body["requests"].append(request.body)

    def is_empty(self):
        return not self.body["requests"]
