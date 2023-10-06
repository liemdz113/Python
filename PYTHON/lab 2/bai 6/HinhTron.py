import math
from HinhHoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, enum: int, bankinh: float) -> None:
        super().__init__(enum, bankinh)
        self._enum = enum
        self.__banKinh = bankinh

    def HinhTron(self, enum: int, banKinh: float):
        pass

    def TinhDienTich(self) -> float:
        return pow(self.__banKinh) * math.pi

    def xuat(self):
        print(f"{self._enum}, Ban Kinh: {self.__banKinh}, Dien TichHT: {self.tinhDienTich()}")