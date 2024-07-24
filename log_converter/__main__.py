from log_converter.config.config_manager import ConfigManager
from log_converter.converter.converter import Converter
from log_converter.window.window import Window

def main():
    # 設定を読み込む
    config_manager = ConfigManager()

    # 画面の初期化
    window = Window(**config_manager.get_window_config())

    # 変換ボタン押下時の処理を画面に設定
    converter = Converter()
    window.set_on_click_convert_button_handler(converter.convert)

    # 設定保存ボタン押下時の処理を画面に設定
    window.set_on_click_save_config_button_handler(config_manager.save_window_config)

    # 画面の表示
    window.run()

if __name__ == "__main__":
    main()
