'''
Xây dựng các lớp theo sơ đồ sau :

                            Hình vẽ
                               |
            ___________________|___________________
            |                                     |
        Hai chiều                              Ba chiều
            |                                     |
     _______|________                     ________|________
     |      |       |                     |               |
   Tròn   Vuông   Tam giác               Cầu          Lập phương

Tạo phương thức cho các lớp trên và cho phép in ra được thông tin của các hình
như chu vi , diện tích, thể tích...
'''

class HinhVe(object):
    
    def __init__(self, para_ten):
        self.ten_hinh = para_ten
        
class HaiChieu(HinhVe):
    def __init__(self, para_ten):
        super().__init__(para_ten)
    def tinh_chu_vi(self, para_)
class BaChieu(object):