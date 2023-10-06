from HinhHoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, enum: int, ChieuDai: float, ChieuRong: float):
        super().__init__(enum, ChieuDai, ChieuRong)
        self._enum = enum
        self.__chieuDai = ChieuDai
        self.__chieuRong = ChieuRong

    def HinhChuNhat(self, dai: float, rong: float):
        pass

    def TinhDienTich(self) -> float:
        return self.__chieuDai * self.__chieuRong

    def xuat(self):
        print(
            f"{self._enum}, Chieu dai: {self.__chieuDai}, Chieu Rong: {self.__chieuRong}, dien tich HCN: {self.TinhDienTich()}")