import configparser
from pathlib import Path

CONFIG_PATH = Path().cwd() / "resource" / "config.yaml"

class ConfigManager:
    def __init__(self):
        self.config = self.load()

    def load(self):
        '''設定ファイルを読み込む'''
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        return config

    def save(self):
        '''設定ファイルに保存する'''
        self.config.write(str(CONFIG_PATH))

    def get_window_config(self):
        '''画面設定を取得する'''
        try:
            return {
                "framework_session_id": self.config.get("WINDOW", "framework_session_id"),
                "start_time_hour": self.config.get("WINDOW", "start_time_hour"),
                "start_time_minute": self.config.get("WINDOW", "start_time_minute"),
                "end_time_hour": self.config.get("WINDOW", "end_time_hour"),
                "end_time_minute": self.config.get("WINDOW", "end_time_minute"),
                "output_format": self.config.get("WINDOW", "output_format"),
                "input_dir": self.config.get("WINDOW", "input_dir"),
                "output_dir": self.config.get("WINDOW", "output_dir")
            }

        except KeyError:
            return {
                "framework_session_id": "",
                "start_time_hour": "",
                "start_time_minute": "",
                "end_time_hour": "",
                "end_time_minute": "",
                "output_format": "",
                "input_dir": "",
                "output_dir": ""
            }

    def save_window_config(self, framework_session_id, start_time_hour, start_time_minute, end_time_hour, end_time_minute, output_format, input_dir, output_dir):
        '''
        画面設定を保存する
        return: (保存成否, タイトル, メッセージ)
        '''
        if self.config.has_section("WINDOW") is False:
            self.config.add_section("WINDOW")

        self.config.set("WINDOW", "framework_session_id", framework_session_id)
        self.config.set("WINDOW", "start_time_hour", start_time_hour)
        self.config.set("WINDOW", "start_time_minute", start_time_minute)
        self.config.set("WINDOW", "end_time_hour", end_time_hour)
        self.config.set("WINDOW", "end_time_minute", end_time_minute)
        self.config.set("WINDOW", "output_format", output_format)
        self.config.set("WINDOW", "input_dir", input_dir)
        self.config.set("WINDOW", "output_dir", output_dir)

        try:
            with open(CONFIG_PATH, "w") as f:
                self.config.write(f)

        except Exception as e:
            return False, "設定保存エラー", "設定の保存に失敗しました。"

        else:
            return True, "設定保存完了", "設定の保存が完了しました。"
