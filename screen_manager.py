import logging
import pyautogui
import cv2
import win32gui

class ScreenManager:

    @staticmethod
    def is_app_focused(app_title_name: str):
        foregoundWindow = win32gui.GetForegroundWindow()
        activeWindowTitle = win32gui.GetWindowText(foregoundWindow).lower()
        return app_title_name == activeWindowTitle

    @staticmethod
    def search_image_on_screen(image_to_search: str):
        try:
            coordinate = pyautogui.locateOnScreen(image=image_to_search, grayscale=False, confidence=0.85)
            return coordinate
        except Exception as ex:
            logging.info(f"Imagem não foi encontrada. Erro: {ex}")

    @staticmethod
    def click_on_screen(coordenate_to_click: int):
        pyautogui.click(coordenate_to_click)

    @staticmethod
    def write(text: str):
        pyautogui.typewrite(text)
