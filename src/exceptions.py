class OutOfRangeColumnsList(Exception):
    def __init__(self, filepath: str, min_columns_cnt: int, realy_columns_cnt: int):
        message = f'File "{filepath}" contains {realy_columns_cnt} columns, expected {min_columns_cnt} at least'
        super().__init__(message)
