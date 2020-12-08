import xlwings as xw
from faker import Faker

fake = Faker(locale='zh_CN')

app = xw.App(visible=True, add_book=False)
file = app.books.add()
sheet1 = file.sheets[0]
for num in range(1, 100000):
    sheet1.range('A%d' % num).value = num
    sheet1.range('C%d' % num).value = fake.name()
    sheet1.range('D%d' % num).value = fake.phone_number()
    sheet1.range('E%d' % num).value = fake.phone_number()
    sheet1.range('F%d' % num).value = fake.address()
    sheet1.range('E%d' % num).value = fake.company()

file.save('d://faker2.xlsx')
print("End")
