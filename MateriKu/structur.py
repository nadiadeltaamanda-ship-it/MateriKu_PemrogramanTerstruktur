class Materi:

    def __init__(self, mata_kuliah, pertemuan, judul, deskripsi, lokasi):
        self.mata_kuliah = mata_kuliah 
        self.pertemuan = pertemuan      
        self.judul = judul             
        self.deskripsi = deskripsi     
        self.lokasi = lokasi           
        
    def ke_baris(self):
        kolom = [self.mata_kuliah, self.pertemuan, self.judul, self.deskripsi, self.lokasi]
        
        kolom = [str(k).replace("|", "/") for k in kolom]
        return "|".join(kolom)

    @staticmethod
    def dari_baris(baris):
        kolom = baris.strip().split("|")
        if len(kolom) != 5:
            raise ValueError("Jumlah kolom salah")
        return Materi(kolom[0], int(kolom[1]), kolom[2], kolom[3], kolom[4])
