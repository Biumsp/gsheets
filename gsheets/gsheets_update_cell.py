from biumsputils.filesIO import read
from gsheets_update_request import 
from json import loads, dumps

templates = read('templates.json', loads=True)

class GSheetsUpdateCell(GSheetsUpdateRequest):
    """A single request of type updateCell, to be add to an update list"""

    def __init__(self, type):
        assert type in templates
        self.type = type
        self.body = templates[type]

    def range(self, srow, scol, erow, ecol):
        self._replace('$start_row', srow)
        self._replace('$end_row', erow)
        self._replace('$start_col', scol)
        self._replace('$end_col', ecol)
    
    def sheet_id(self, sheet_id):
        self._replace('$start_row', sheet_id)

    def _replace(self, old, new):
        body = dumps(self.body)
        body = body.replace(old, new)
        self.body = loads(body)
