from PyQt5.QtCore import QSize
from PyQt5.QtGui import (QColor, QIcon, QPalette)
from PyQt5.QtWidgets import (QFrame, QGridLayout, QHBoxLayout, QVBoxLayout,
                             QMessageBox, QPushButton, QWidget)

import src.apps.const as const
import src.apps.translate as tr
from src.apps.numgenerator import NumGenerator


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.set_game_params()
        self.set_app_options()

    def set_game_params(self):
        self.num_gen = NumGenerator()
        self.buttons = []

    def set_app_options(self):
        self.setWindowTitle(tr.TITLE)
        self.setWindowIcon(QIcon(const.ICON_PATH))
        self.setMaximumSize(QSize(*const.WIDGET_SIZE))
        self.create_menu()
        self.create_main_frame()
        self.setting_layout()

    def setting_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.menu_layout)
        self.main_layout.addWidget(self.main_frame)
        self.setLayout(self.main_layout)

    def create_menu(self):
        self.menu_layout = QHBoxLayout()
        for button_sets in [
            {'text': 'Новая игра', 'action': self.start_new_game},
            {'text': 'Справка', 'action': self.show_about_program_message}
        ]:
            self.menu_layout.addWidget(self.create_menu_button(button_sets))

    def create_menu_button(self, buttons):
        button = QPushButton(buttons['text'])
        button.clicked.connect(buttons['action'])
        return button

    def show_about_program_message(self):
        QMessageBox.information(self, tr.TITLE, tr.ABOUT_PROGRAM_MESSAGE, QMessageBox.Ok)

    def create_main_frame(self):
        self.main_frame = QFrame()
        self.main_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.main_frame.setLineWidth(2)
        self.set_element_palette(self.main_frame, const.BACKGROUND_COLOR)
        self.main_frame.setLayout(self.set_frame_layout())

    def set_element_palette(self, element, color):
        palette = QPalette()
        palette.setColor(element.backgroundRole(), QColor(color))
        element.setPalette(palette)
        element.setAutoFillBackground(True)

    def set_frame_layout(self):
        main_frame_layout = QGridLayout()
        numbers = self.num_gen.numbers

        for i in range(0, len(numbers)):
            pb = self.create_num_button(numbers[i])
            self.buttons.append(pb)
            main_frame_layout.addWidget(pb, i // 4, i % 4)
            if numbers[i] == 0:
                pb.setVisible(False)

        return main_frame_layout

    def create_num_button(self, button_text):
        button = QPushButton(str(button_text))
        button.setMinimumSize(*const.BUTTON_SIZE)
        button.setCheckable(False)
        button.setFlat(True)
        self.set_element_palette(button, const.BUTTON_COLOR)
        button.clicked.connect(self.change_button_position)
        return button

    def change_button_position(self):
        pressed_num = int(self.sender().text())
        pressed_num_index = self.num_gen.index(pressed_num)
        empty_num_index = self.num_gen.find_empty_element(pressed_num_index)
        if empty_num_index == -1:
            return

        self.buttons[pressed_num_index].setVisible(False)
        self.buttons[pressed_num_index].setText(str(0))
        self.buttons[empty_num_index].setVisible(True)
        self.buttons[empty_num_index].setText(str(pressed_num))

        self.num_gen.swap(pressed_num_index, empty_num_index)
        self.check_end_game()

    def start_new_game(self):
        self.set_game_params()
        self.main_layout.removeWidget(self.main_frame)
        self.create_main_frame()
        self.main_layout.addWidget(self.main_frame)

    def check_end_game(self):
        if not self.num_gen.is_sorted():
            return

        variant = QMessageBox.question(
            self, tr.WIN_TITLE, tr.WIN_MESSAGE, QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if variant == QMessageBox.Yes:
            self.start_new_game()
        else:
            self.exit_game()

    def exit_game(self):
        super().close()
