'''
- Hãy định nghĩa class SinhVien với các thuộc tính : Họ tên , mã sinh viên , điểm học phần, điểm quá trình
và các phương thức khởi tạo, tính điểm trung bình, hiển thị thông tin
Trong đó : điểm trung bình = điểm quá trình*0.3 + điểm học phần*0.7
- Định nghĩa class LopHoc với các thuộc tính danh sách sinh viên, sĩ số lớp, tên lớp
và phương thức khởi tạo
'''
import json
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

class LopHoc(object):
    def __init__(self, ten_lop):
        self.ten_lop = ten_lop
        self.list_sv = []

    def append_sv(self, SinhVien):
        self.list_sv.append(SinhVien)

    def siso(self):
        return len(self.list_sv)

    def show_danh_sach_lop(self):
        for x in self.list_sv:
            print('Tên : '+ x.hoten + ' ; MSV : ' + x.msv)

    def search(self, para):
        for x in self.list_sv:
            if (x.msv == para) or (x.hoten == para):
                return('Tên : '+ x.hoten + ' ; MSV : ' + x.msv)
                pass
        else:
            return("No match!")

    def remove(self, para):
        for x in self.list_sv:
            if (x.msv == para) or (x.hoten == para):
                self.list_sv.remove(x)

    def import_to_file(self):
        file_op = open('/home/cuongnq/code/bai_tap_oop/bai_1/data.json', 'w')
        for x in self.list_sv:
            file_op.write(x.hoten + ',' + x.msv + ',' + x.dqt + ',' + x.dhp + '\n') 
        file_op.close()

    # def export_to_file(self):
    #     file_op = open('/home/cuongnq/code/bai_tap_oop/bai_1/data', 'r')
    #     start = 1
    #     x = file_op.readline()
    #     while True:
    #         x.split('--')
    #         sinh_vien_{}.format(start)
            


            
        


        


        


sinh_vien_A = SinhVien('Ngo Quoc Cuong', 'B15DCVT049', '6', '8')
sinh_vien_B = SinhVien('Dinh Cong Hung', 'B15DCVT050', '6', '8')
sinh_vien_C = SinhVien('Nguyen Van Tuyen', 'B15DCVT051', '6', '8')

lop_hoc_A = LopHoc('VT1')
lop_hoc_A.append_sv(sinh_vien_A)
lop_hoc_A.append_sv(sinh_vien_B)
lop_hoc_A.append_sv(sinh_vien_C)

lop_hoc_A.show_danh_sach_lop()
print(lop_hoc_A.list_sv)
lop_hoc_A.import_to_file()
# # print(lop_hoc_A.search("B15DCVT051"))

# # print(lop_hoc_A.show_danh_sach_lop())

