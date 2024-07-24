class Converter:
    def __init__(self):
        pass

    def convert(self, framework_session_id, start_time_hour, start_time_minute, end_time_hour, end_time_minute, output_format, input_dir, output_dir):
        '''ログ変換処理'''
        print(f"framework_session_id: {framework_session_id}, start_time_hour: {start_time_hour}, start_time_minute: {start_time_minute}, end_time_hour: {end_time_hour}, end_time_minute: {end_time_minute}, output_format: {output_format}, input_dir: {input_dir}, output_dir: {output_dir}")

        return True, "変換完了", "変換に成功しました。"