import tkinter as tk

TEXT_FONT = ("Arial", 20, 'normal')
LABEL_FONT = ("Arial", 35, "italic")
BG_COLOR = '#00092C'
RED = "#e7305b"
GREEN = "#9bdeac"
HEIGHT = 800
WIDTH = 800


class TextWriterGUI:
    """Typing Speed GUI
    """

    def __init__(self) -> None:

        self.last_word_check_length: int = 0
        self.current_work_check_length: int = 0

        # Window setup
        self.app_window = tk.Tk()
        self.app_window.title("Disappearing Text Writer")
        self.app_window.geometry(f"{HEIGHT}x{WIDTH}")
        self.app_window.config(padx=100, pady=50, bg=BG_COLOR)

        # timer
        self.timer_label = tk.Label(text='Start Typing!', font=LABEL_FONT, pady=5, bg=BG_COLOR, fg=GREEN)
        self.timer_label.pack()

        # text_input
        self.typing_input = tk.Text(self.app_window, font=TEXT_FONT, wrap=tk.WORD, width=100, height=20,
                                    state=tk.NORMAL, padx=10, pady=10, bg='white')
        self.typing_input.pack()
        self.typing_input.focus()

        self.__count_down()

    @property
    def typing_input_length(self) -> int:
        """extract the length of the typing input box

        Returns:
            int: Length of typing input box
        """
        return len(self.typing_input.get('1.0', 'end').strip())

    @property
    def __has_user_stopped_typing(self) -> bool:
        """Check if the user has stopped typing by comparing last checked lengths with current lengths

        Returns:
            bool: True if the user has stopped. False if not.
        """
        self.current_work_check_length = self.typing_input_length
        if self.last_word_check_length < self.current_work_check_length:
            self.last_word_check_length = self.current_work_check_length
            return False
        return True

    @property
    def __has_user_started_typing(self) -> bool:
        """Check if the input box length is greater than 0. If so user has started typing.

        Returns:
            bool: True if user has started typing, Else False.
        """
        if self.typing_input_length > 0:
            return True
        return False

    def __count_down(self, count=5):
        """Check text length every second.
        * If the user has not started typing, prompt them to Start.
        * Elif the user has begun typing and also stopped typing, begin the count down from 5 seconds.
        * Else the user is actively typing, so tell them to keep typing.

        Args:
            count (int): seconds to count down from. Defaults to 60
        """
        if not self.__has_user_started_typing:
            self.timer_label.config(text='Start Typing!', fg=GREEN)
            self.app_window.after(1000, self.__count_down)

        elif self.__has_user_stopped_typing:
            # update timer text:
            self.timer_label.config(text=f'Timer: {count}', fg=RED)
            # call counter
            if count > 0:
                self.app_window.after(1000, self.__count_down, count - 1)
            else:
                self.timer_label.config(text='Times Up', fg=RED)
                self.typing_input.delete('1.0', 'end')
                self.current_work_check_length = 0
                self.last_word_check_length = 0
                self.app_window.after(1000, self.__count_down, 0)

        else:
            self.timer_label.config(text='Keep Typing!', fg=GREEN)
            self.app_window.after(1000, self.__count_down)

    def run(self):
        """Main loop
        """
        self.app_window.mainloop()


if __name__ == "__main__":
    win = TextWriterGUI()
    win.run()
