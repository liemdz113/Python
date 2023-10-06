from datetime import date

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: date):
        self.__maSo = maSo  # private
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten):
        self.__hoTen = hoten

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

     # tuong tu phuong thuc ghi de toString()
    def __str__(self):
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    # hanh vi doi tuong sinh vien
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")


class DanhSachSV:
    def __init__(self):
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # tim sinh vien theo mssv, neu co tra ve sinh vien
    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    # tim sinh vien theo mssv, neu co tra ve vi tri sv trong ds
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    # tim sinh vien ten "Nam"
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.rsplit(' ', 1)[-1] == ten]
        #rsplit cũng hoàn toàn như phương thức split, có điều là việc tách từ bên phải sang trái

    # tim nhung sinh vien sinh truoc 15/06/2000
    def timSvSinhTruocNgay(self, ngay: date):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]


sv1 = SinhVien(2112997, "Đỗ Thanh Liêm",
               date(2003,12,12))
sv2 = SinhVien(2110000, "Nguyễn Văn A",
               date(2003,7,24))
sv3 = SinhVien(2110001, "Trần thị B",
               date(2003,2,12))
sv4 = SinhVien(2110002, "Nguyễn Thị C",
               date(2003,4,7))

# sv.xuat()
ds = DanhSachSV()
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.xuat()

msTim = int(input("Nhập vào mã số muốn tìm: "))
kq = ds.timSvTheoMssv(msTim)
print("Đã tìm thấy sinh viên có mã số: ", msTim)
for sv in kq:
    sv.xuat()
x = ds.timVTSvTheoMssv(msTim)
print(f"Vị trí của sinh viên trên là {x}")  # vị trí của sinh viên, bắt đầu từ 0

#  xoa sinh vien
msXoa = int(input("Nhập vào mã số muốn xóa: "))
ds.xoaSvTheoMssv(msXoa)
ds.xuat()

# tim ten sinh viên
ten = input("Nhập tên muốn tìm: ")
kq = ds.timSvTheoTen(ten)
print("Đã tìm thấy sinh viên có tên: ", ten)
for sv in kq:
    sv.xuat()

# tim truoc ngay sinh truoc 15/06/2000
ngay = date(2003,6,15)
kqNgay = ds.timSvSinhTruocNgay(ngay)
print("Đã tìm thấy ngày sinh trước 13/06/2003: ")
for sv in kqNgay:
    sv.xuat()