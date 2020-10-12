import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio

from _viewers.viewer import Viewer


class Lcd1602(Viewer):

    """Lcd display 16x2 characters."""

    lcd_rs = digitalio.DigitalInOut(board.D26)
    lcd_en = digitalio.DigitalInOut(board.D19)
    lcd_d7 = digitalio.DigitalInOut(board.D27)
    lcd_d6 = digitalio.DigitalInOut(board.D22)
    lcd_d5 = digitalio.DigitalInOut(board.D24)
    lcd_d4 = digitalio.DigitalInOut(board.D25)

    lcd_columns = 16
    lcd_rows = 2

    def __init__(self):
        self._lcd = self._initialize_display()

    def _initialize_display(self):
        lcd = characterlcd.Character_LCD_Mono(self.lcd_rs, self.lcd_en, self.lcd_d4,
                                              self.lcd_d5, self.lcd_d6, self.lcd_d7,
                                              self.lcd_columns, self.lcd_rows)
        lcd.message = 'Initialized\nwaiting for data'
        return lcd

    def update_view(self, input_line_1, input_line_2):
        self._lcd.message = '{}\n{}'.format(input_line_1, input_line_2)