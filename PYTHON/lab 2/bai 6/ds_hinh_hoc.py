from enum import Enum
import math

from HinhHoc import HinhHoc
from HinhChuNhat import HinhChuNhat
from HinhTron import HinhTron
from HinhVuong import HinhVuong

class DanhSachHH:
    def __init__(self):
        self.dshh = []

    def themHH(self, hh: HinhHoc):
        self.dshh.append(hh)

    def xuat(self):
        for hh in self.dshh:
            print(hh)

    def TimHinhCoDienTichLonNhat(self):
        for i in self.dshh:
            max = self.dshh[0]
            if self.dshh[i].TinhDienTich() > max:
                max = self.dshh[i]
        return max
    
    def TimHinhCoDienTichNhoNhat(self):
        for i in self.dshh:
            min = self.dshh[0]
            if self.dshh[i].TinhDienTich() < min:
                min = self.dshh[i]
        return min
    
    def TimHinhTronNhoNhat(self):
        for i in self.dshh:
            if self.dshh[i].enum == 1:
                min = self.dshh[i]
                if self.dshhh[i].enum == 1 and self.dshhh[i].TinhDienTich() < min:
                    min = self.dshh[i]
        return min
    
    def SapGiamTheoDienTich(self):
        for i in range(len(self.dshh)):
            for j in range(i, len(self.dshh)):
                if self.dshh[i].TinhDienTich() < self.dshh[j].TinhDienTich():
                    self.dshh[i], self.dshh[j] = self.dshh[j], self.dshh[i]

    def DemSLHinhTron(self):
        dem = 0
        for i in self.dshh:
            if self.dshh[i].enum == 1:
                dem += 1
        return dem 
    
    def DemSLHinhChuNhat(self):
        dem = 0
        for i in self.dshh:
            if self.dshh[i].enum == 2:
                dem += 1
        return dem
    
    def DemSLHinhVuong(self):
        dem = 0
        for i in self.dshh:
            if self.dshh[i].enum == 3:
                dem += 1
        return dem 
    
    def TinhTongDienTich(self):
        sum = 0
        for i in self.dshh:
            sum += self.dshh[i].TinhDienTich()
        return sum 
    
    def TimHinhLonNhat(self, loai: int):
        for i in self.dshh:
            max = self.dshh[0]
            if self.dshhh[i].enum == loai and self.dshhh[i].TinhDienTich() > max:
                max = self.dshh[i]
        return max
    
    def TimVTHCoDienTichX(self, x: float):
        for i in self.dshh:
            if self.dshhh[i].TinhDienTich() == x:
                return i
            return -1
            
    def XoaHinhTaiVT(self, j : int):
        for i in self.dshh:
            if i == j:
                del self.dshh[i]
                return True
        return False
    
    def TimHinhTheoDTich(self, x: float):
        for i in self.dshh:
            if self.dshhh[i].TinhDienTich() == x:
                return self.dshh[i]
            return -1
            
    def XoaHinhTheoLoai(self, loai: int):
        for i in self.dshh:
            if self.dshhh[i].enum == loai:
                del self.dshh[i]
                return True
            return False
    
    def XuatHinhTheoChieuTang(self, loai: int):
        for i in range(len(self.dshh)):
            for j in range(i, len(self.dshh)):
                if self.dshh[i].TinhDienTich() > self.dshh[j].TinhDienTich():
                    self.dshh[i], self.dshh[j] = self.dshh[j], self.dshh[i]
        for i in self.dshh:
            if self.dshh[i].enum == loai:
                print(self.dshh[i])

    def XuatHinhTheoChieuGiam(self, loai: int):
        for i in range(len(self.dshh)):
            for j in range(i, len(self.dshh)):
                if self.dshh[i].TinhDienTich() < self.dshh[j].TinhDienTich():
                    self.dshh[i], self.dshh[j] = self.dshh[j], self.dshh[i]
        for i in self.dshh:
            if self.dshh[i].enum == loai:
                print(self.dshh[i])  


            



    
    
                

        
            

