from CALCULATOR import app
from functools import wraps
from CALCULATOR.model import (
    Process_sql,
)

def retrieve_data(*tables):
    def _inner(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):
            def retrieve_process(id, **kwargs):
                return Process_sql.query.get_or_404(id)
            mapping = {
                'process': retrieve_process,
            }
            stored_records={}
            for table in tables:
                stored_records[table]=mapping[table](**kwargs)
            return f(*args, dbvalues=stored_records, **kwargs)
        return _wrapper
    return _inner