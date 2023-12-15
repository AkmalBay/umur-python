import getpass
import time
import datetime as dt
import os

def finish_animation():
    text = "PROGRAM SELESAI, SEMOGA HARIMU MENYENANGKAN:)"
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.1)  # Sesuaikan kecepatan animasi dengan keinginan Anda
    print("\n")

def authenticate():
    stored_password = "ApabaeKena157"
    entered_password = getpass.getpass("Masukan password: ")

    if entered_password == stored_password:
        print("Password benar. Akses diberikan.")
        return True
    return entered_password == stored_password

def loading_animation():
    print("Menjalankan skrip", end="", flush=True)
    for _ in range(5):  # Ganti angka ini dengan jumlah titik (atau animasi lain) yang diinginkan
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

# Minta pengguna untuk mengotentikasi sampai berhasil
while not authenticate():
    print("Password salah GOBLOK!!!. Silahkan coba lagi, kalau tidak tau TANYA!!!")

# Jika otentikasi berhasil, lanjutkan dengan menjalankan skrip
loading_animation()
def animate_text(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def animate_plus_signs(num_signs, delay=0.1):
    for _ in range(num_signs):
        print("+", end="", flush=True)
        time.sleep(delay)
    print()

# Menentukan teks
text1 = "┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ┌┬┐┌─┐┌┐┌┌─┐┬ ┬┬┌┬┐┬ ┬┌┐┌┌─┐  ┬ ┬┌┬┐┬ ┬┬─┐"
text2 = "├─┘├┬┘│ ││ ┬├┬┘├─┤│││  │││├┤ ││││ ┬├─┤│ │ │ │││││ ┬  │ │││││ │├┬┘"
text3 = "┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  ┴ ┴└─┘┘└┘└─┘┴ ┴┴ ┴ └─┘┘└┘└─┘  └─┘┴ ┴└─┘┴└─"

# Menambahkan animasi pada setiap teks
animate_plus_signs(75)
animate_text("=" * 5 + text1 + "=" * 5)
animate_text("=" * 5 + text2 + "=" * 5)
animate_text("=" * 5 + text3 + "=" * 5)

def animate_below_text(text, delay=0.1):
    animate_text(text, delay)
animate_below_text("+"*31 + " BY MR.53C4X " + 31*"+")
print("\n" * 1)

print("Silahkan masukan tanggal, bulan, dan tahun anda lahir.\n")

while True:
    try:
        tanggal = int(input("Tanggal\t: "))
        bulan = int(input("Bulan\t: "))
        tahun = int(input("Tahun\t: "))
    except ValueError:
        print("Masukan angka GOBLOK!, bukan huruf.")
        continue  # Mulai kembali iterasi loop jika terjadi kesalahan

    try:
        tanggal_lahir = dt.date(tahun, bulan, tanggal)
    except ValueError:
        print("Tanggal, Bulan, atau Tahun tidak valid.")
        continue  # Mulai kembali iterasi loop jika terjadi kesalahan

    hari_ini = dt.date.today()
    umur_hari = hari_ini - tanggal_lahir
    umur_tahun = umur_hari.days // 365
    umur_bulan_sisa = (umur_hari.days % 365) //30

    print(f"\nAnda saat ini berusia {umur_tahun} tahun, {umur_bulan_sisa} bulan \n")

    is_done = input("masih mau ngecek lagi ngga brooo?? (y/n) ")

    if is_done.lower() == "n":
        finish_animation()  # Menjalankan animasi "PROGRAM SELESAI"
        break
    elif is_done.lower() != "y":
        print("Input tidak valid. Keluar dari program.")
        finish_animation()
        break



