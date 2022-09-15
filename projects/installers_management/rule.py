class Rule():
    def __init__(self, funk):
        self.funk = funk
    
    def __call__(self, spreadsheet, *args, **kwargs):
        update = self.funk(spreadsheet, *args, **kwargs)
        if update.is_empty(): return
        spreadsheet.batch_update(update.body)
