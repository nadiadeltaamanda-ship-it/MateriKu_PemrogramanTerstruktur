import os
import shutil

from structures import Materi

FOLDER_PROYEK = os.path.dirname(os.path.abspath(__file__))
FILE_DATA = os.path.join(FOLDER_PROYEK, "data", "materi.txt")
FOLDER_MATERI = os.path.join(FOLDER_PROYEK, "materi")


def siapkan_folder():
    os.makedirs(os.path.dirname(FILE_DATA), exist_ok=True)
    os.makedirs(FOLDER_MATERI, exist_ok=True)
    try:
        with open(FILE_DATA, "x", encoding="utf-8"):
            pass
    except FileExistsError:
        pass  

def muat_materi():
    daftar = []
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            for baris in file:
                if baris.strip() == "":
                    continue  
                try:
                    daftar.append(Materi.dari_baris(baris))
                except ValueError:
                    pass  
    except FileNotFoundError:
        pass  
    return daftar

def simpan_materi(daftar):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        for materi in daftar:
            file.write(materi.ke_baris() + "\n")

def tambah_baris(materi):
    with open(FILE_DATA, "a", encoding="utf-8") as file:
        file.write(materi.ke_baris() + "\n")

def daftar_mata_kuliah():
    hasil = []
    for nama in os.listdir(FOLDER_MATERI):
        if os.path.isdir(os.path.join(FOLDER_MATERI, nama)):
            hasil.append(nama)
    return sorted(hasil)

def buat_folder_mk(nama):
    os.makedirs(os.path.join(FOLDER_MATERI, nama))

def salin_file(sumber, mata_kuliah):
    folder_tujuan = os.path.join(FOLDER_MATERI, mata_kuliah)
    nama_file = os.path.basename(sumber)
    tujuan = os.path.join(folder_tujuan, nama_file)
    nomor = 1
    while os.path.exists(tujuan): 
        nama, ekstensi = os.path.splitext(nama_file)
        tujuan = os.path.join(folder_tujuan, f"{nama}_{nomor}{ekstensi}")
        nomor += 1
    shutil.copy2(sumber, tujuan)
    return os.path.relpath(tujuan, FOLDER_PROYEK).replace("\\", "/")
