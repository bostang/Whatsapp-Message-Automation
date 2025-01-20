# config.py
from datetime import datetime

def get_greeting():
    """Menentukan sapaan berdasarkan waktu sekarang."""
    current_hour = datetime.now().hour

    if 0 <= current_hour < 11:
        return "pagi"
    elif 11 <= current_hour < 16:
        return "siang"
    elif 16 <= current_hour < 18:
        return "sore"
    else:
        return "malam"

# Latar Waktu
suasana_waktu = get_greeting()

# Identitas Penanya
nama_penanya = "Bostang Palaguna"           # CONFIGURABLE
nim_penanya = "13220055"                      # CONFIGURABLE
angkatan_penanya = nim_penanya[3:5]

jurusan_penanya = ""
if nim_penanya[:3] == "132":
    jurusan_penanya = "Elektro"
elif nim_penanya[:3] == "180":
    jurusan_penanya = "Tenaga Listrik"
elif nim_penanya[:3] == "181":
    jurusan_penanya = "Telekomunikasi"
elif nim_penanya[:3] == "183":
    jurusan_penanya = "Biomedis"

# catatan : WA dalam full tab
# Koordinat tombol-tombol
new_chat_xy = [356,67]
number_pad_xy = [624,171]
close_number_pad_country_xy = [619,214]
chat_xy = [497,322]
chat_prompt_xy = [633,1373]

typing_delay = 0.02 #sekon
sleep_interval = 1 #sekon