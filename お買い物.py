money = 1000
items = {'チョコレート': 100, 'クッキー': 200, 'ケーキ': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('いらっしゃいませ！こちらはお菓子コーナーです！')
    print('【info】所持金は' + str(money) + '円です。' + item_name + 'は1個' + str(items[item_name]) + '円です。' )
    
    
    input_count = input('購入する' + item_name + 'の個数を:の後ろに半角で入力してください：')
    print('【店員A】' +  item_name + 'を' + input_count + '個かごにいれました！')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('お会計は' + str(total_price) + '円でございます。')
    
    if money >= total_price:
        print('【info】' +item_name + 'を' + input_count + '個買いました。')
        money -= total_price
        print('残り' + str(money) + '円です。')

  
        if money == 0 :
          print('【店員A】またお越しくださいませ～')
          break
        
    else:   
        print('【店員A】残念ながらお金が足りません…')
        print('あなたは残念そうに'+ item_name + 'を棚に戻しました.')
        print('【Game Over!!】')
        break

