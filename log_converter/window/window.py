from pathlib import Path
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window:
    def __init__(self, framework_session_id, start_time_hour, start_time_minute, end_time_hour, end_time_minute, output_format, input_dir, output_dir):
        '''画面の初期化'''
        # ウィンドウの初期化
        self.app = tkinter.Tk()
        self.app.title("IFAポータル ログ変換ツール")
        self.app.resizable(False, False)
        self.app.geometry("410x235")

        # アイコンを設定
        icon = tkinter.PhotoImage(file=str(Path().cwd() / "resource" / "icon.png")) 
        self.app.iconphoto(True, icon)

        # 画面全体フレーム
        base_frame = tkinter.Frame(self.app)
        base_frame.grid(row=0, column=0, padx=20, pady=30)

        # フレームワークセッションIDの指定
        framework_session_id_label = tkinter.Label(base_frame, text="フレームワークセッションID")
        framework_session_id_label.grid(row=0, column=0, sticky=tkinter.E)
        self.framework_session_id_entry = tkinter.Entry(base_frame)
        self.framework_session_id_entry.delete(0, tkinter.END)
        self.framework_session_id_entry.insert(0, framework_session_id)
        self.framework_session_id_entry.grid(row=0, column=2, columnspan=4, sticky=tkinter.EW)

        # 開始時刻の指定
        start_time_label = tkinter.Label(base_frame, text="開始時刻")
        start_time_label.grid(row=1, column=0, sticky=tkinter.E)
        start_time_required_label = tkinter.Label(base_frame, text="※", foreground="red")
        start_time_required_label.grid(row=1, column=1, padx=(0, 5))
        self.start_time_hour_entry = tkinter.Spinbox(base_frame, width=4, from_=0, to=23)
        self.start_time_hour_entry.delete(0, tkinter.END)
        self.start_time_hour_entry.insert(0, start_time_hour)
        self.start_time_hour_entry.grid(row=1, column=2)
        start_time_hour_label = tkinter.Label(base_frame, text="時")
        start_time_hour_label.grid(row=1, column=3)
        self.start_time_minute_entry = tkinter.Spinbox(base_frame, width=4, from_=0, to=59)
        self.start_time_minute_entry.delete(0, tkinter.END)
        self.start_time_minute_entry.insert(0, start_time_minute)
        self.start_time_minute_entry.grid(row=1, column=4)
        start_time_minute_label = tkinter.Label(base_frame, text="分")
        start_time_minute_label.grid(row=1, column=5)

        # 終了時刻の指定
        end_time_label = tkinter.Label(base_frame, text="終了時刻")
        end_time_label.grid(row=2, column=0, sticky=tkinter.E)
        end_time_required_label = tkinter.Label(base_frame, text="※", foreground="red")
        end_time_required_label.grid(row=2, column=1, padx=(0, 5))
        self.end_time_hour_entry = tkinter.Spinbox(base_frame, width=4, from_=0, to=23)
        self.end_time_hour_entry.delete(0, tkinter.END)
        self.end_time_hour_entry.insert(0, end_time_hour)
        self.end_time_hour_entry.grid(row=2, column=2)
        end_time_hour_label = tkinter.Label(base_frame, text="時")
        end_time_hour_label.grid(row=2, column=3)
        self.end_time_minute_entry = tkinter.Spinbox(base_frame, width=4, from_=0, to=59)
        self.end_time_minute_entry.delete(0, tkinter.END)
        self.end_time_minute_entry.insert(0, end_time_minute)
        self.end_time_minute_entry.grid(row=2, column=4)
        end_time_minute_label = tkinter.Label(base_frame, text="分")
        end_time_minute_label.grid(row=2, column=5)

        # 出力形式の選択
        self.output_format = tkinter.StringVar()
        self.output_format.set(output_format)
        output_format_label = tkinter.Label(base_frame, text="出力形式")
        output_format_label.grid(row=3, column=0, sticky=tkinter.E)
        output_format_required_label = tkinter.Label(base_frame, text="※", foreground="red")
        output_format_required_label.grid(row=3, column=1, padx=(0, 5))
        output_format_radio_row = tkinter.Radiobutton(base_frame, text="ROW", value="ROW", variable=self.output_format)
        output_format_radio_row.grid(row=3, column=2)
        output_format_radio_csv = tkinter.Radiobutton(base_frame, text="CSV", value="CSV", variable=self.output_format)
        output_format_radio_csv.grid(row=3, column=3)
        output_format_radio_tsv = tkinter.Radiobutton(base_frame, text="TSV", value="TSV", variable=self.output_format)
        output_format_radio_tsv.grid(row=3, column=4)

        # 入力ディレクトリの指定
        input_dir_label = tkinter.Label(base_frame, text="入力ディレクトリ")
        input_dir_label.grid(row=4, column=0, sticky=tkinter.E)
        input_dir_required_label = tkinter.Label(base_frame, text="※", foreground="red")
        input_dir_required_label.grid(row=4, column=1, padx=(0, 5))
        self.input_dir_entry = tkinter.Entry(base_frame)
        self.input_dir_entry.delete(0, tkinter.END)
        self.input_dir_entry.insert(0, input_dir)
        self.input_dir_entry.grid(row=4, column=2, columnspan=3, sticky=tkinter.EW)
        input_dir_button = tkinter.Button(base_frame, text="参照", command=self._on_click_input_dir_button)
        input_dir_button.grid(row=4, column=5)

        # 出力ディレクトリの指定
        output_dir_label = tkinter.Label(base_frame, text="出力ディレクトリ")
        output_dir_label.grid(row=5, column=0, sticky=tkinter.E)
        output_dir_required_label = tkinter.Label(base_frame, text="※", foreground="red")
        output_dir_required_label.grid(row=5, column=1, padx=(0, 5))
        self.output_dir_entry = tkinter.Entry(base_frame)
        self.output_dir_entry.delete(0, tkinter.END)
        self.output_dir_entry.insert(0, output_dir)
        self.output_dir_entry.grid(row=5, column=2, columnspan=3, sticky=tkinter.EW)
        output_dir_button = tkinter.Button(base_frame, text="参照", command=self._on_click_output_dir_button)
        output_dir_button.grid(row=5, column=5)

        # 変換ボタン
        convert_button = tkinter.Button(base_frame, text="変換", width=20, command=self._on_click_convert_button)
        convert_button.grid(row=6, column=0, columnspan=4, pady=10)

        # 設定保存ボタン
        save_config_button = tkinter.Button(base_frame, text="設定保存", width=10, command=self._on_click_save_config_button)
        save_config_button.grid(row=6, column=4, columnspan=2, pady=10, sticky=tkinter.E)

    def run(self):
        '''画面の表示'''
        self.app.mainloop()
    
    def set_on_click_convert_button_handler(self, handler):
        '''変換ボタンのクリックイベントハンドラの設定'''
        self.on_click_convert_button_handler = handler

    def set_on_click_save_config_button_handler(self, handler):
        '''設定保存ボタンのクリックイベントハンドラの設定'''
        self.on_click_save_config_button_handler = handler

    def _on_click_input_dir_button(self):
        '''入力ディレクトリ参照ボタンのクリックイベント'''
        input_dir = tkinter.filedialog.askdirectory()
        if input_dir:
            self.input_dir_entry.delete(0, tkinter.END)
            self.input_dir_entry.insert(0, input_dir)
    
    def _on_click_output_dir_button(self):
        '''出力ディレクトリ参照ボタンのクリックイベント'''
        output_dir = tkinter.filedialog.askdirectory()
        if output_dir:
            self.output_dir_entry.delete(0, tkinter.END)
            self.output_dir_entry.insert(0, output_dir)

    def _on_click_convert_button(self):
        '''変換ボタンのクリックイベント'''
        if self.on_click_convert_button_handler is None:
            raise NotImplementedError("on_click_convert_button_handler is not implemented.")

        convert_success, title, message = self.on_click_convert_button_handler(
            self.framework_session_id_entry.get(),
            self.start_time_hour_entry.get(),
            self.start_time_minute_entry.get(),
            self.end_time_hour_entry.get(),
            self.end_time_minute_entry.get(),
            self.output_format.get(),
            self.input_dir_entry.get(),
            self.output_dir_entry.get()
        )

        if convert_success:
            print("\a")
            tkinter.messagebox.showinfo(title, message)
        else:
            print("\a")
            tkinter.messagebox.showerror(title, message)

    def _on_click_save_config_button(self):
        '''設定保存ボタンのクリックイベント'''
        if self.on_click_save_config_button_handler is None:
            raise NotImplementedError("on_click_save_config_button_handler is not implemented.")

        save_success, title, message = self.on_click_save_config_button_handler(
            self.framework_session_id_entry.get(),
            self.start_time_hour_entry.get(),
            self.start_time_minute_entry.get(),
            self.end_time_hour_entry.get(),
            self.end_time_minute_entry.get(),
            self.output_format.get(),
            self.input_dir_entry.get(),
            self.output_dir_entry.get()
        )

        if save_success:
            print("\a")
            tkinter.messagebox.showinfo(title, message)
        else:
            print("\a")
            tkinter.messagebox.showerror(title, message)
