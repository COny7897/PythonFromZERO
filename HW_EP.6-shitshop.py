product = {
    'สินค้า' : ['ขนม','น้ำ','ลูกอม','ไอติม'],
    'ราคา' : [10,15,5,10]
}
welcome = str(input('ต้องการซื้อสินค้าใช้หรือไม่ [y/N] :'))
if welcome == 'y':
    print('ร้านเราขาย')
    for i in product['สินค้า']:
        print(i)

    order = str(input('--------------------\nรับอะไรดีครับ : '))
    while order not in product['สินค้า']:
        print('ขออภัยคุณลูกค้า \nร้านของเราไม่ได้ขาย {} \nกรุณาสั่งใหม่อีกครั้ง'.format(order))
        order = str(input('สั่งใหม่ : '))
    quantity = int(input('จำนวน : '))

    price = int(product['สินค้า'].index(order))
    total_price = product['ราคา'][price] * quantity
    print('--------------------\n จำนวนเงินที่ลูกค้าต้องจ่าย {} บาท \n--------------------'.format(total_price))

    money = int(input('จำนวนเงินที่ลูกค้าจ่าย : '))
    while (total_price > money):
        print('กรุณาจ่ายเงินเพิ่มอีก {} บาท'.format(total_price - money))
        new_money = int(input('จำนวนเงินที่ลูกค้าจ่ายเพิ่ม : '))
        money = money + new_money
    if (total_price < money):
        print('เงินทอน {} บาท \nขอบคุณที่ใช้บริการ :D'.format(money - total_price))
    elif (total_price == money):
        print('--------------------\n ขอบคุณที่ใช้บริการครับ :D')
else:
    print('กรุณาออกจากร้านด้วยครับ')



