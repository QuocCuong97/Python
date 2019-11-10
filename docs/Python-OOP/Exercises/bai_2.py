'''
Định nghĩa class LopHoc với các thuộc tính danh sách sinh viên, sĩ số lớp, tên lớp
và phương thức khởi tạo
'''
class LopHoc(object):
    def __init__(self, para_dssv, para_si_so, para_ten_lop):
        self.dssv = para_dssv
        self.si_so = para_si_so
        self.ten_lop = para_ten_lop
    
class SinhVien(object):

    def __init__(self, para_hoten):
        self.hoten = para_hoten

sinh_vien_A = SinhVien('Ngo Quoc Cuong')
sinh_vien_B = SinhVien('Dinh Cong Hung')


