class Rule():
    spreadsheet = ''

    def __init__(self, funk):
        self.funk = funk
    
    def __call__(self, *args, **kwargs):
        update = self.funk(self.spreadsheet, self.update, *args, **kwargs)
        self.spreadsheet.batch_update(update)

