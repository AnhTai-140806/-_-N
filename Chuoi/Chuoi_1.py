## Hiện thông tin chuỗi
s1="""Đặng Trương Anh Tài
Đại Học Kinh tế_Luật"""
s2="18 tuổi\nQuê: Trà Vinh"
s3='Thích: du lịch'
print(s1)
print(s2)
print(s3)
print(type(s1))
print()

## Cộng chuỗi
s4="Tui tên là: "
s5="Anh Tài"
s6=s4+s5
s7=s4 + "\n" + s5
print(s6)
print(s7)
print()

## Nhân chuỗi
s8="Cố gắng lên nào!\n"
s9=s8*5
print(s9)

## Kiểm tra có nằm trong chuỗi
s10="Tui thích đi chơi"
s11="thích"
s12=s11 in s10
print(s12)
print()

## Lấy ra trong chuỗi
s13=s10[0]
s14=s10[-1]
s15=s10[len(s10)-1]
s16=s10[4:9]
s17=s10[4:len(s10)]
s18=s10[4:None]
print(s13)
print(s14)
print(s15)
print(s16)
print(s17)
print(s18)
print()
slogan = "No Pain No Gain!"
print(slogan[3:7])
print(slogan[:7])
print(slogan[None:7])
print(slogan[3:])
print(slogan[3:None])
print(slogan[-5:])
print(slogan[:-9])
