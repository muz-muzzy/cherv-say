import sys
from cherv.cherv import cherv_say
import json
import os
import requests

class SilentWriter:
    def write(self, text):
        pass

    def flush(self):
        pass

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_stdout

with SilentWriter():
    import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def check_settings_file_exists() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = 'settings.json'
    path_to_settings = os.path.join(current_dir, filename)
    if os.path.isfile(path_to_settings):
        pass
    else:
        dictionary = {
            "skin": 0
        }
        with open(path_to_settings, 'w') as f:
            json.dump(obj=dictionary, fp=f)
    return path_to_settings


def main():
    json_path = check_settings_file_exists()

    settings = json.load(open(json_path, 'r'))
    SKIN = settings["skin"]
    skins = {0: "Белый", 1: "Чёрный", 2: "Котик", 3: "Сквидвард"}
    if (len(sys.argv) >= 2):
        if (sys.argv[1] == "--help"):
            print(
                """Использование: cherv [сообщение]
                Список доступных команд:
                --help    Справка по использованию
                --skin    Выбрать облик червя
                """)
            return

        elif (sys.argv[1] == "--skin"):
            print("Введите номер облика, чтобы использовать его.")
            print("Доступные облики червя:\n")
            for k, v in skins.items():
                print(f"{k} - {v}")
            num = int(input("-> "))
            if num not in skins.keys():
                print("Неверное значение.\n")
                return
            SKIN = num
            settings["skin"] = num
            phrase = ""
            if (SKIN == 0): phrase = "Я дефолтный червяк!"
            elif (SKIN == 1): phrase = "Я чёрный червяк!🥷"
            elif (SKIN == 2): phrase = "Мяу :3"
            elif (SKIN == 3): phrase = "Um what the sigma"
            cherv_say(phrase, skin=SKIN)
            json.dump(obj=settings, fp=open(json_path, 'w'))
            return

        elif (sys.argv[1] == "--sound"):
            url = "https://github.com/muz-muzzy/cherv-say/raw/main/cherv.mp3"
            save_directory = os.path.dirname(os.path.abspath(__file__))
            save_path = os.path.join(save_directory, "cherv.mp3")
            download_file(url, save_path)
            cherv_say(skin=SKIN)
            play_mp3(save_path)
            return

        cherv_say(" ".join(sys.argv[1:]), skin=SKIN)

    if len(sys.argv) < 2:
        cherv_say(skin=SKIN)

if __name__ == "__main__":
    main()