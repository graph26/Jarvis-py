# import os
# import psutil
# from funct.fun import *
# from datetime import datetime
# import folium
#
#
# def location(text: str):
#     import ipinfo
#     ip = {
#         '192.168.31.35': ['ноутбук', 'ноут', 'Lenovo'],
#         '85.140.162.187': ['Xiaomi', 'телефон', 'note', '11', 'графит'],
#         '192.168.137.41': ['смартфон', 'Xiaomi', 'plus', '5'],
#     }
#     access_token = '97e42b7bf0c9bf'
#     handler = ipinfo.getHandler(access_token)
#     for ip, value in ip.items():
#         if text.lower() in value:
#             ip_address = ip
#     details = handler.getDetails(ip_address)
#
#     map = folium.Map(location=[60.01, 100.00], zoom_start=8)
#
#     folium.Marker(location=[details.loc.split(',')[0], details.loc.split(',')[1]], popup=f"Устройство - {ip_address}",
#                   icon=folium.Icon(color='green')).add_to(map)
#
#     map.save("location/map.html")
#
#     now = datetime.now()
#     time_now = now.strftime("%H:%M:%S")
#     date_now = now.strftime("%Y-%m-%d")
#     with open('location/location.txt', 'r') as f:
#         f.write(f'Устройство - {ip_address}\n')
#         f.write(f'Находится - {details.city}, {details.region}, {details.country_name}\n')
#         f.write(f'Координаты - {details.loc}\n')
#         f.write(f'Время запроса - {time_now}\n')
#         f.write(f'Дата запроса - {date_now}\n')
#         f.write('--------------------------------------------------------\n')
#
#
#
# def diagnostic():
#     cpu_percent = psutil.cpu_percent(interval=1)  #Получение информации о процессоре
#     battery = psutil.sensors_battery()
#     percent = battery.percent # процент
#     power = battery.power_plugged # Подключено ли к зарядке
#     for proc in psutil.process_iter(['pid', 'name', 'username']): # Получение данных о процессах
#         proc_info = proc.info
#     disk = psutil.disk_usage('/') # Получение информации о диске
#     total_disk = f"Total disk space: {disk.total / (1024 ** 3):.2f} GB"
#     used_disk = f"Used disk space: {disk.used / (1024 ** 3):.2f} GB"
#     free_disk = f"Free disk space: {disk.free / (1024 ** 3):.2f} GB"
#     disk_usage = f"Disk usage: {disk.percent}%"
#     memory = psutil.virtual_memory() # Получение информации о памяти
#     total_memory = f"Total memory: {memory.total / (1024 ** 3):.2f} GB"
#     avaible_memory = f"Available memory: {memory.available / (1024 ** 3):.2f} GB"
#     used_memory = f"Used memory: {memory.used / (1024 ** 3):.2f} GB"
#     memory_usage = f"Memory usage: {memory.percent}%"
#
#     now = datetime.now()
#     time_now = now.strftime("%H:%M:%S")
#     date_now = now.strftime("%Y-%m-%d")
#     with open("Systemd/diagnostic.txt", "w") as f:
#         f.write(f"Current time: {time_now}\n")
#         f.write(f"Current date: {date_now}\n")
#         f.write(f"CPU Usage: {cpu_percent}%\n")
#         f.write(f"Battery Percentage: {percent}%\n")
#         f.write(f"Total Memory: {total_memory}\n")
#         f.write(f"Available Memory: {avaible_memory}\n")
#         f.write(f"Used Memory: {used_memory}\n")
#         f.write(f"Memory Usage: {memory_usage}\n")
#         f.write(f"Total Disk Space: {total_disk}\n")
#         f.write(f"Used Disk Space: {used_disk}\n")
#         f.write(f"Free Disk Space: {free_disk}\n")
#         f.write(f"Disk Usage: {disk_usage}\n")
#         f.write(f"Power Status: {power}\n")
#         if power:
#             f.write("Battery is plugged in.\n")
#         else:
#             f.write("Battery is not plugged in.\n")
#         f.write("CPU Processes:\n")
#         for proc in psutil.process_iter(['pid', 'name', 'username']):
#             proc_info = proc.info
#             f.write(f"PID: {proc_info['pid']}, Name: {proc_info['name']}, User: {proc_info['username']}\n")
#         f.write('----------------------------------------------------------------------------------------\n')
#
#
#
# def music():
#     avtors = {
#         'Agata_Kristi_' : 'Агата Кристи',
#         'aktor_2_': 'Фактор 2',
#         'Kino_': 'Кино',
#         'KnyaZz_': 'Князь',
#         'Korol_i_SHut_': 'Король и Шут',
#         'Nautilus_Pompilius_': 'Nautilus Pompilius',
#         'Splin_': 'Сплин',
#         'Subbota_': 'Subbota',
#         'Xassa_': 'Xassa',
#     }
#     List_music = [files for root, directories, files in os.walk(r"F:\Музыка")]
#     print(List_music)
#     for i in range(len(List_music)):
#         print(List_music[0][i])
#         music_name = [i for i in List_music[0][i].split('-')]
#         for key, value in avtors.items():
#             if key == music_name[0]:
#                 music_name[0] = value
#
#         # playsound.playsound(f"F:\\Музыка\\{List_music[0][i]}")
#
#
# def battery():
#     def get_battery_status():
#         battery = psutil.sensors_battery()
#         if battery is None:
#             return None
#         return {
#             "percent": battery.percent,
#             "plugged": battery.power_plugged,
#             "secsleft": battery.secsleft
#         }
#
#     def format_time(seconds):
#         if seconds == psutil.POWER_TIME_UNLIMITED:
#             return "∞"
#         elif seconds == psutil.POWER_TIME_UNKNOWN:
#             return "??"
#         else:
#             h = seconds // 3600
#             m = (seconds % 3600) // 60
#             return f"{h} ч {m} мин"
#
#     status = get_battery_status()
#     if not status:
#         logger2.info("[bold red]Батарея не найдена.[/bold red]")
#
#     percent = status["percent"]
#     plugged = status["plugged"]
#     time_left = format_time(status["secsleft"])
#     state = "🔌 На зарядке" if plugged else "🔋 На батарее"

