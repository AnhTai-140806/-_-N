## Viết hoa chữ cái đầu tiên
welcome = "welcome to UEL"
print(welcome.capitalize())
## Hoa thành thường và ngược lại
welcome = "Welcome to UEL"
print(welcome.swapcase())
## Tất cả viết hoa
welcome = "Welcome to UEL"
print(welcome.upper())
## Tất cả viết thường
welcome = "Welcome to UEL"
print(welcome.lower())
## Viết hoa kí tự dầu tiên mỗi từ
welcome = "Welcome to UEL"
print(welcome.title())
print()

## Căn lề
welcome = "UEL"
print(welcome.center(10))
print(welcome.center(10, "*"))
welcome = "UEL"
print(welcome.rjust(10))
print(welcome.rjust(10, "*"))
welcome = "UEL"
print(welcome.ljust(10))
print(welcome.ljust(10, "*"))
print()

## Xóa khoảng trắng thừa: strip, lstrip, rstrip
welcome = "  Welcome to UEL  "
print(welcome.strip())
welcome = "  Welcome to UEL  "
print(welcome.rstrip())
welcome = "  Welcome to UEL  "
print(welcome.lstrip())

## Độ dài chuỗi (tính từ 1)
welcome = "Welcome to UEL!"
print(len(welcome))
print()

## startswith, endswith
welcome = "Welcome to UEL!"
print(welcome.startswith("We"))
print(welcome.startswith("We", 3))
print(welcome.startswith("We", 2, 9))
print(welcome.endswith("!"))
print(welcome.endswith("L!", -2))
print()

## Tìm chuỗi con
slogan = "No Pain No Gain!"
print(slogan.find("No"))
print(slogan.find("No", 2, 6))
print(slogan.find("No", 2))
print(slogan.rfind("No"))
print(slogan.rfind("No", -9, -2))
print()
slogan = "No Pain No Gain!"
print(slogan.index("No", 2))
print(slogan.rindex("No", 5))
print()

## Đếm chuỗi con: count
slogan = "No Pain No Gain!"
print(slogan.count("No"))
print(slogan.count("No", 3))
print(slogan.count("Success"))
print()

## Tách chuỗi: split
slogan = "No-Pain-No-Gain!"
s = slogan.split('-')
print(s)
for i in s:
    print(i)
print()

## Nối chuỗi: join
slogan = "No-Pain-No-Gain!"
s = slogan.split('-')
print(s)
for i in s:
    print(i, end=' ')
print('\n-------------------')
s1 = ' *** '
print("Joined string: ", s1.join(s))
print()

## Thay thế chuỗi: replace
slogan = "No Pain No Gain!"
print(slogan.replace("No", "0"))
print(slogan.replace("No", "0", 1))
print()

## Chuyển đổi chuỗi: maketrans(), translate()
slogan = "No Pain No Gain!"
inputs = "oa"
outputs = "OA"
trans = slogan.maketrans(inputs, outputs)
print(trans)
print(slogan.translate(trans))
print()

## Các hàm kiểm tra: isalnum(), isalpha(), isdigit(), isnumeric()
print('Coin68'.isalnum())
print('Coin68.com'.isalnum())
print('Binance'.isalpha())
print('67'. isdigit())
print('68.5'.isdigit())
print('68abc'.isdigit())
print("⑩⑬㊿".isdigit())
print('86'.isnumeric())
print("⑩⑬㊿".isnumeric())




















