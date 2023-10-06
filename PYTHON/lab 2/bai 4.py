class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)

    @staticmethod
    # Dùng @staticmethod để self không được truyền mặc định vào tham số của hàm
    def __TimUCLN(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def RutGon(self):
        ucln = self.__TimUCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        '''Cộng 2 phân số ps1 + ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        '''Trừ 2 phân số ps1 - ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __mul__(self, other):
        '''Nhân 2 phân số ps1 * ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.RutGon()
        return kq

    def __truediv__(self, other):
        '''Chia 2 phân số ps1 / ps2'''
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.RutGon()
        return kq

ps1 = PhanSo(5, 7)
ps2 = PhanSo(4, 6)
ps3 = PhanSo(-2, 3)
ps4 = PhanSo(-5, 8)
ps5 = PhanSo(6, 8)


class DanhSachPhanSo():
    def __init__(self):
        self.dsps = []

    def ThemPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps)

    def DemPhanSoAm(self):
        Dem = 0
        for ps in self.dsps:
            if ps.tu < 0 or ps.mau < 0:
                Dem += 1
        return Dem
    
    def PsDuongMin(self):
        Min = PhanSo()
        for ps in self.dsps:
            if (ps.tu / ps.mau) < (Min.tu / ps.mau):
                Min = ps
        return Min
    
    def TimPsX(self, x : PhanSo):
        for i in range(len(self.dsps)):
            if self.dsps[i].tu == x.tu and self.dsps[i].mau == x.mau:
                return i
            
    def TongPsAm(self):
        Tong = PhanSo(0, 0)
        for ps in self.dsps:
            if ps.tu < 0 or ps.mau < 0:
                Tong.tu += ps.tu
                Tong.mau += ps.mau
        return Tong
    
    def XoaPsX(self, x : PhanSo):
        for i in range(len(self.dsps)):
            if self.dsps[i].tu == x.tu and self.dsps[i].mau == x.mau:
                del self.dsps[i]
                return True
        return False
            
    def XoaPsTuX(self, x : PhanSo):
        for i in range(len(self.dsps)):
            if self.dsps[i].tu == x.tu:
                del self.dsps[i]
                return True
        return False
            
    def XapXepTangMau(self):
        tg = PhanSo()
        for i in range(len(self.dsps)):
            for j in range(i, len(self.dsps)):
                if self.dsps[i].mau > self.dsps[j].mau:
                    self.dsps[i], self.dsps[j] = self.dsps[j], self.dsps[i]

    def XapXepGiamMau(self):
        tg = PhanSo()
        for i in range(len(self.dsps)):
            for j in range(i, len(self.dsps)):
                if self.dsps[i].mau < self.dsps[j].mau:
                    self.dsps[i], self.dsps[j] = self.dsps[j], self.dsps[i]

    def XapXepTangTu(self):
        tg = PhanSo()
        for i in range(len(self.dsps)):
            for j in range(i, len(self.dsps)):
                if self.dsps[i].tu > self.dsps[j].tu:
                    self.dsps[i], self.dsps[j] = self.dsps[j], self.dsps[i]

    def XapXepGiamTu(self):
        tg = PhanSo()
        for i in range(len(self.dsps)):
            for j in range(i, len(self.dsps)):
                if self.dsps[i].tu < self.dsps[j].tu:
                    self.dsps[i], self.dsps[j] = self.dsps[j], self.dsps[i]


dsps = DanhSachPhanSo()
dsps.ThemPhanSo(ps1)
dsps.ThemPhanSo(ps2)
dsps.ThemPhanSo(ps3)
dsps.ThemPhanSo(ps4)
dsps.ThemPhanSo(ps5)
dsps.xuat()
print("--------------------------------------------------------------")

#Đếm số phân số âm trong mảng
Cau1 = dsps.DemPhanSoAm()
print(f"Có tất cả {Cau1} số phân số âm trong mảng")

#Tìm phân số dương nhỏ nhất
Cau2 = dsps.PsDuongMin()
print(f"Phân số dương nhỏ nhất trong mảng trên là: {Cau2}")

#Tìm vị trí của phân số x trong mảng
x = PhanSo(4, 6)
#x.tu = input("Nhap tu cho x: ")
#x.mau = input("Nhap mau cho x: ")
Cau3 = dsps.TimPsX(x)
print(f"Vị trí của x = {x} trong mảng là: {Cau3}")

#Tổng tất cả các phân số âm trong mảng
Cau4 = dsps.TongPsAm()
print(f"Tổng tất cả các phân số âm trong mảng la: {Cau4}")

#Xóa phân số x trong mảng
y = PhanSo(6, 8)
#y.tu = input("Nhap tu cho y: ")
#y.mau = input("Nhap mau cho y: ")
dsps.XoaPsX(y)
print(f"Đã xóa phân số {y} ra khỏi mảng")
dsps.xuat()
print("--------------------------------------------------------------")

#Xóa tất cả phân số có tử là x
z = PhanSo(5, 8)
#z.tu = input("Nhap tu cho z: ")
#z.mau = input("Nhap mau cho z: ")
dsps.XoaPsTuX(z)
print(f"Đã xóa phân số có tu = {z.tu} ra khỏi mảng")
dsps.xuat()
print("--------------------------------------------------------------")

#Sắp xếp phân số theo chiều tăng, giảm; tăng theo mẫu, tử, giảm theo mẫu tử.
#Tăng theo mẫu 
dsps.XapXepTangMau()
print("Danh sách mảng được xắp xếp tăng theo mẫu là: ")
dsps.xuat()

#Giảm theo mẫu
dsps.XapXepGiamMau()
print("Danh sách mảng được xắp xếp giảm theo mẫu là: ")
dsps.xuat()

#Tăng theo tử
dsps.XapXepTangTu()
print("Danh sách mảng được xắp xếp tăng theo tử là: ")
dsps.xuat()

#Giảm theo tử
dsps.XapXepGiamTu()
print("Danh sách mảng được xắp xếp giảm theo tử là: ")
dsps.xuat()