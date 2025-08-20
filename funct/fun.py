import webbrowser
import pyautogui
import wave
import pyaudio
# from funct.fun_add import location, diagnostic, music, battery
# from funct.gpt import gpt_qwen
from fuzzywuzzy import fuzz

p = pyaudio.PyAudio()


def command_function(text):
    HOTWORDS = ['открой', 'открыть', 'запусти', 'выполни', 'приложение', 'запусти приложение', 'открой вкладку',
                'уменьши', 'увеличи', 'увеличь', 'уменьшь' 'сделай', 'произведи',
                'сверни', 'отмена', 'отменить', 'отмени', 'воспроизведи', 'проиграй', 'воспроизвести музыку', ]
    response_text = ['скажи', 'покажи', 'найди', 'запроси', 'покажи информацию', 'покажи результат', 'покажи ответ']
    puth = ['"C:\\', '"F:\\', '"E:\\', '"D:\\', '"G:\\']
    web = {
        'https://youtube.com/': ['ютуб', 'youtube'],
        'https://www.google.com/': ['гугл', 'google'],
        'https://vk.com/': ['vk', 'вк'],
        'https://music.mts.ru/': ['музыка', 'мтс музыка', 'мтс'],
        'https://translate.yandex.ru/?from=tableau_yabro': ['переводчик', 'яндекс переводчик'],
        'https://translate.google.com/': ['google переводчик', 'google translate', 'гугл переводчик', 'translate'],
        'https://yandex.ru/pogoda': ['яндекс погода', 'погода'],
        'https://github.com/': ['github', 'GitHub'],
        'https://yandex.ru/maps/': ['яндекс карты', 'карты'],
        'https://dzen.ru/': ['яндекс', 'дзен'],
        'https://stepik.org/': ['степик', 'stepik', ],
        '"C:\\Program Files (x86)\\Microsoft Office\\Office16\\WINWORD.EXE"': ['ворд', 'word', 'вард'],
        '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"': ['хором', 'chrome', 'храм', 'гугл хром',
                                                                         'хром'],
        '"C:\\Program Files (x86)\\Microsoft Office\\Office16\\POWERPNT.EXE"': ['поверпоинт', 'powerpoint'],
        '"cmd.exe"': ['цмд', 'cmd'],
        '"C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.EXE"': ['эксель', 'excel'],
        '"C:\\Program Files\\Firefox Developer Edition\\firefox.exe"': ['фар фокс', 'firefox', 'фаер фокс'],
        '"C:\\Program Files\\Unity Hub\\Unity Hub.exe"': ['юнити', 'unity'],
        'shutdown': ['выключение', 'компьютер', 'выключение системы'],
        'shutdown_programm': ['выход', 'завершить работу', 'завершить', 'завершение работы', 'программу'],
        'location': ['местоположение', 'локация', 'координаты', 'устройства', 'местоположения', 'телефона', 'ноутбука'],
        'diagnostic': ['диагностику', 'проверку', 'системы'],
        'shatdown_comp': ['перезагрузку', 'перезагрузка', 'системы'],
        'C:\\Program Files\\JetBrains\\RustRover 2024.3.7\\bin\\rustrover64.exe': ['rust rover', 'rust', 'раст'],
        'C:\\Program Files\\GIGA IDE\\GIGA IDE Community Edition 2024.1.1\\bin\\idea64.exe': ['python', 'ide',
                                                                                              'пайтон'],
        'Music': ['музыку', 'песни'],
        'battery': ['аккумулятор', 'аккумулятора', 'проверка', 'проверку', 'батарейки'],
        '"F:\\Games\\GTA San Andreas\\gta_sa.exe"': ['gta san andreas'],
        '"F:\\Games\\Grand Theft Auto V\\GTA5.exe"': ['gta v', 'gta'],
        '"F:\\Games\\.minecraft\\TLauncher.exe"': ['майнкрафт', 'minecraft', ],
        '"F:\\Games\\SnowRunner\\en_us\\Sources\\Bin\\SnowRunner.exe"': ['showrunner'],
        '"E:\\Castle Crashers\\castle.exe"': ['кастл', 'castle crashers'],
        ('alt', 'shift'): ['смена языка', 'смени язык', 'смену языа'],
        ('volumedown'): ['уменьши звук', 'уменьши громкость', 'уменьши', 'уменьшь громкость'],
        ('volumeup'): ['увеличь звук', 'увеличи громкость', 'увеличь', 'увеличь громкость', 'увеличить громкость', ],
        ('f11'): ['полноэкраннный режим', 'режим', 'полноэкраннный'],
        ('f5'): ['обновление окна', 'обновление страницы'],
        ('win', 'L'): ['блокировку', 'блокировку экрана'],
        ('win', 'i'): ['настроек', 'настроки'],
        ('win', 'd'): ['свертывание', 'сверни', 'разверни'],
        ('alt', 'f4'): ['закрытие окна', 'закрытие', 'закрой'],
        ('win', 'e'): ['проводника', 'проводник'],
        ('ctrl', 'space'): ['останови', 'остановку', 'остановку музыку', 'остановку песни',
                            'останови музыку', 'останови песни', 'продолжи', 'продолжи музыку', 'продолжи песни',
                            'продолжение', 'продолжение музыки', 'продолжение песни', 'паузу', 'паузу музыки',
                            'паузу песни', ],
        ('ctrl', 'b'): ['повтор', 'повторение', 'повторение музыки', 'повторение песни', 'прошлую', 'прошлую музыку',
                        'прошлую песню', ],
        ('ctrl', 'f'): ['следующую', 'следующую музыку', 'следующую песню'],
        ('ctrl', 'm'): ['свёртывание медиаплеера', 'свёртывание плеера', 'развёртывание медиаплеера',
                        'развёртывание плеера'],
        ('ctrl', 'c'): ['копирование', 'скопировать', 'скопируй', 'копируй'],
        ('ctrl', 'v'): ['вставку', 'вставить', 'вставь'],
        ('ctrl', 'z'): ['отмена', 'отмену'],
        ('ctrl', 'x'): ['вырезание', 'вырезать', 'вырезь'],
        ('ctrl', 's'): ['сохранение', 'сохранить', 'сохрани'],
        ('k'): ['останови видео', 'остаовку видео', 'продолжи видео', 'продолжение видео', 'напаузу видео'],
        ('f'): ['во весь экран', 'во весь экран видео', 'выход из видео'],
    }

    if any(hotword in text for hotword in HOTWORDS):
        for key, value in web.items():
            if any(com in text for com in value):
                if 'https://' in key or 'http://' in key:
                    try:
                        perform_audio('Запрос выполнен сэр')
                        print(f'[Jarvis]: Starting web: {value[1]}')
                        webbrowser.open_new(key)

                    except webbrowser.Error as weberr:
                        # logger2.error(f'Ошибка управления браузером - {weberr}')
                        perform_audio('Мы работаем над проектом сэр 2')
                elif any(puth_app in key for puth_app in puth):
                    try:
                        import subprocess
                        subprocess.Popen(key)
                        print(f'Starting app {value[1]}')
                        perform_audio('Запрос выполнен сэр')
                    except FileNotFoundError:
                        # logger2.error(f'Программа {value} не найдена.')
                        perform_audio('Мы работаем над проектом сэр 2')
                    except Exception:
                        # logger2.error(f'Произошла ошибка при запуске программы: {value}')
                        perform_audio('Мы работаем над проектом сэр 2')
                elif str(type(key)) == "<class 'tuple'>":
                    if len(key) == 2:
                        perform_audio('Запрос выполнен сэр')
                        pyautogui.hotkey(key[0], key[1])
                        # logger2.debug(f'Нажатие сочетания клавиш {key}')
                    else:
                        perform_audio('Запрос выполнен сэр')
                        pyautogui.keyDown(key[0])
                        pyautogui.keyUp(key[0])
                        # logger2.debug(f'Нажатие клавиши {key}')
    else:
        # gpt_qwen(text)
        pass



def perform_audio(text: str):
    # Открываем файл для чтения
    with wave.open(f'Jarvis Sound Pack/{text}.wav', 'rb') as wav_file:
        # Получаем параметры файла
        params = wav_file.getparams()
        print(params)

        # Читаем данные из файла
        frames = wav_file.readframes(params.nframes)

    # Открываем поток для воспроизведения звука
    stream = p.open(format=p.get_format_from_width(params.sampwidth),
                    channels=params.nchannels,
                    rate=params.framerate,
                    output=True)

    # Воспроизводим звук
    stream.write(frames)
