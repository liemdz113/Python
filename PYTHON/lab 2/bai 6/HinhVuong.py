from HinhHoc import HinhHoc

class HinhVuong(HinhHoc):
    def __init__(self, enum: int, canh: float):
        super().__init__(enum, canh)
        self._enum = enum
        self._canh = canh

    def HinhVuong(self, canh: float):
        pass

    def TinhDienTich(self) -> float:
        return self._canh * self._canh

    def xuat(self):
        print(f"{self._enum}, canh: {self._canh} dien tich HV: {self.TinhDienTich()}")