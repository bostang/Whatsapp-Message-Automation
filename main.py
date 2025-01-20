import pyautogui
import time
from configuration import *
import csv

def load_targets(file_path):
    """Membaca file target.csv dan mengembalikan dictionary target peserta."""
    target_peserta = {}
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Pastikan baris tidak kosong
                nomor = int(row[0])  # Kolom pertama sebagai kunci
                target_peserta[nomor] = {
                    "nama": row[1],
                    "gender": row[2],
                    "angkatan": row[3],
                    "nomor_telepon": row[4]
                }
    return target_peserta

def escape():
    pyautogui.press('esc')
    time.sleep(sleep_interval)
    pyautogui.press('esc')

def clear_prompt():
    pyautogui.hotkey('ctrl', 'a') # select all
    pyautogui.press('backspace')


def moving(phone_number):

    # Pindah ke tombol New Chat
    pyautogui.moveTo(new_chat_xy[0], new_chat_xy[1]) # Move the mouse to XY coordinates.
    pyautogui.click()          # Click the mouse.

    time.sleep(1) # delay 1 detik (responsiveness)

    # Pindah ke tombol number pad
    pyautogui.moveTo(number_pad_xy[0],number_pad_xy[1])
    pyautogui.click()          # Click the mouse.

    time.sleep(1) # delay 1 detik (responsiveness)

    # Tekan close country pada number pad (untuk manual ketik +62, berlaku untuk selain +62)
    pyautogui.moveTo(close_number_pad_country_xy[0],close_number_pad_country_xy[1])
    pyautogui.click()          # Click the mouse.

    clear_prompt() # mengosongkan prompt nomor telepon (apabila sebelumnya error)

    # mengetik Nomor telepon (mencari)
    pyautogui.write(phone_number, interval=0)  # type with quarter-second pause in between each key

    time.sleep(5) # delay 5 detik (menunggu sampai phone number found)

    # Tekan tombol chat
    pyautogui.moveTo(chat_xy[0],chat_xy[1])
    pyautogui.click()          # Click the mouse.

    time.sleep(0.5) # delay 1/2 detik (responsiveness)

    # Tekan close country pada number pad (untuk manual ketik +62, berlaku untuk selain +62)
    pyautogui.moveTo(chat_prompt_xy[0],chat_prompt_xy[1])
    pyautogui.click()          # Click the mouse.

    time.sleep(0.5) # delay 1/2 detik (responsiveness)

def chat(nama,gender,angkatan):
    if gender == "Male":
        Salutation = "Pak"
        Salutation_lengkap = "Bapak"
    elif gender == "Female":
        Salutation = "Bu"
        Salutation_lengkap = "Ibu"

    # Sekuens chat
    pyautogui.write(f'Halo selamat {suasana_waktu}, {Salutation}.. apakah benar ini dengan {Salutation_lengkap} {nama} dari IAE angkatan {angkatan}, ya?',interval=typing_delay)
    pyautogui.press('enter')   
    time.sleep(sleep_interval)

    pyautogui.write(f'Jika benar, saya minta izin menganggu waktunya sebentar, {Salutation}.',interval=typing_delay)
    pyautogui.press('enter')   
    time.sleep(sleep_interval)

    pyautogui.write(f'Perkenalkan saya *{nama_penanya}* ({nim_penanya}) - T. {jurusan_penanya} ITB ak. 20{angkatan_penanya} sebagai bagian dari panitia salah satu acara Ikatan Alumni Elektro (IAE) ITB, namanya *OlympIAE 2025*, {Salutation}.',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

    pyautogui.write(f'Singkatnya, OlympIAE ini adalah perlombaan olahraga virtual yang bertujuan untuk mengajak anggota IAE untuk mulai membangun pola hidup sehat berolahraga yang dikemas dengan cara yang menarik, {Salutation}.',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

    pyautogui.write(f'linktr.ee/OlympIAE',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

    pyautogui.write(f'Izin.. Saya di sini bermaksud untuk mengajak {Salutation_lengkap} untuk mendaftar peserta dalam acara ini, {Salutation}.',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

    pyautogui.write(f'karena partisipasi dari {Salutation_lengkap} sungguh sangat berarti bagi kami, {Salutation}.',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

    pyautogui.write(f'Kalau {Salutation_lengkap} tertarik atau sekiranya ingin tahu lebih banyak, saya di sini siap menjelaskan lebih lanjut, {Salutation}.',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

    pyautogui.write(f'Terimakasih untuk perhatiannya, selamat kembali beraktivitas, {Salutation}',interval=typing_delay)
    pyautogui.press('enter')
    time.sleep(sleep_interval)

def main():
    # DEBUG
    # currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    # print(currentMouseX, currentMouseY)

    # Membaca file csv dan menyimpan ke array
    file_path = 'target.csv'
    try:
        target_peserta = load_targets(file_path)
        
        # Ganti tab (VSCode -> WA)
        pyautogui.hotkey('alt', 'tab')

        # mengirim pesan untuk setiap target peserta
        # start = 3
        # ending = 22
        start = 23
        ending = 50
        for k in range(start,ending+1):
            # moving(phone_number="+6289651524904")
            escape()
            moving(phone_number=target_peserta[k]["nomor_telepon"])
            time.sleep(sleep_interval) # beri delay (untuk kestabilan)
            chat(nama=target_peserta[k]["nama"],gender=target_peserta[k]["gender"],angkatan=target_peserta[k]["angkatan"])

    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan. Pastikan file tersedia di direktori yang sama dengan program ini.")


if __name__ == "__main__":
    main()