LOG_COLUMNS = ["date", "time", "log_level", "class_name", "method_name", "line_number", "message"]

class LogData:
    def __init__(self, row_data, prev_log):
        '''ログデータの初期化'''
        self.row_data = row_data

    @classmethod
    def get_csv_header(cls):
        '''CSVヘッダを取得する'''
        return cls._get_xsv_header(",")

    @classmethod
    def get_tsv_header(cls):
        '''TSVヘッダを取得する'''
        return cls._get_xsv_header("\t")

    @classmethod
    def _get_xsv_header(cls, delimiter):
        '''[delimiter] Separated Valueのヘッダを取得する'''
        return delimiter.join(LOG_COLUMNS)

    def get_row_data(self):
        '''ログデータを取得する'''
        return self.row_data

    def get_csv_data(self):
        '''CSVデータを取得する'''
        return self.row_data
    
    def get_tsv_data(self):
        '''TSVデータを取得する'''
        return self.row_data
