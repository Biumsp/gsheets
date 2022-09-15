from biumsputils.filesIO import read
from .gsheets_update_request import GSheetsUpdateRequest
from json import loads, dumps

templates = read('templates.json', loads=True)

class GSheetsUpdateCell(GSheetsUpdateRequest):
    """A single request of type updateCell: 
        must be added to an update list"""

    def __init__(self, type):
        assert type in templates
        self.type = type
        self.body = templates[type]

    def range(self, srow, erow, scol, ecol):
        self._replace('$start_row', srow)
        self._replace('$end_row', erow)
        self._replace('$start_col', scol)
        self._replace('$end_col', ecol)
    
    def sheet_id(self, sheet_id):
        self._replace('$sheet_id', sheet_id)

    def value_list(self, values):
        values = [{"userEnteredValue": v} for v in values]
        self._replace('$values_list', values)

    def _replace(self, old, new):
        body = dumps(self.body)
        body = body.replace(f'\"{old}\"', dumps(new))
        self.body = loads(body)
