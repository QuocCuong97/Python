'''
Hãy định nghĩa class SinhVien với các thuộc tính : Họ tên , mã sinh viên , điểm học phần, điểm quá trình
và các phương thức khởi tạo, tính điểm trung bình, hiển thị thông tin
Trong đó : điểm trung bình = điểm quá trình*0.3 + điểm học phần*0.7
'''
from decimal import *
getcontext().prec = 3

class SinhVien(object):

    def __init__(self, para_hoten, para_msv, para_dqt, para_dhp):
        self.hoten = para_hoten
        self.msv = para_msv
        self.dqt = para_dqt
        self.dhp = para_dhp

    def tinh_diem_trung_binh(self):
        return Decimal(self.dqt) * Decimal(0.3) + Decimal(self.dhp) * Decimal(0.7)

sinh_vien_A = SinhVien('Ngo Quoc Cuong', 'B15DCVT049', '6', '8')
print(sinh_vien_A.tinh_diem_trung_binh())
