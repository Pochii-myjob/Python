import utils
import random

print('【AI】これからじゃんけんをはじめます！')
player_name = input('あなたのお名前を教えて！：')
print('あなたは何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('【AI】0~2の数字で入力してくださいね♪:'))

if utils.validate(player_hand):
    computer_hand = random.randint(0,2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, 'コンピューター')
    
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
    
    while result == '🌟勝ち🌟' :
        print('-------もう１回遊べるドン！-------')
        
        print('【AI】これからじゃんけんをはじめます！')
        print('あなたは何を出しますか？（0: グー, 1: チョキ, 2: パー）')
        player_hand = int(input('【AI】0~2の数字で入力してくださいね♪:'))

        if utils.validate(player_hand):
            computer_hand = random.randint(0,2)
            
            utils.print_hand(player_hand, player_name)

            utils.print_hand(computer_hand, 'コンピューター')
    
            result = utils.judge(player_hand, computer_hand)
            print('結果は' + result + 'でした')

    else:
        print('また遊んでね～')
        print('------------THE END------------')


else:
    print('※最初からやり直してください※')