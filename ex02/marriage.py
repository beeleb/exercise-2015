"""
n人ずつの男女各人に異性n人に対してのランダムに順序付けられた選好を与え
それをもとにして男性最良安定マッチングを作るプログラムです

"""

import numpy as np
n = 10 # 男女の人数
m_prefer = np.empty([n,n])
for i in range(n):
    m_prefer[i] = np.arange(n)
    np.random.shuffle(m_prefer[i])

f_prefer = np.empty([n,n])
for i in range(n):
    f_prefer[i] = np.arange(n)
    np.random.shuffle(f_prefer[i])
"""
m_prefer[i][j]はi番目の男性のj番目の女性に対する好みの順位を表しています
f_prefer[i][j]はi番目の女性のj番目の男性に対する好みの順位を表しています

"""
    
m_engage = -np.ones(n) # 男性の婚約状態を表す -1は未婚約、それ以外はその数字の女性と婚約中ということ
f_engage = -np.ones(n) # 女性の婚約状態を表す
proposing = -1 # 婚約申し込みを保存しておく
proposed = -1 #婚約申し込まれを保存しておく

print"Men's preference is below."
print m_prefer # アルゴリズムが正しいか確認するためにとりあえず表示
print"Women's preference is below."
print f_prefer # 数字が小さいほうがより好ましい



while(np.sum(m_engage) != np.sum(range(n))):
    for proposing in range(n):
        if m_engage[proposing] == -1:
            proposed = np.argmin(m_prefer[proposing]) # 最も好みの相手に申し込む
            m_prefer[proposing][proposed] = n # 一度婚約申し込みをした相手には二度申し込まないようにするため
            if f_engage[proposed] == -1:
                f_engage[proposed] = proposing
                m_engage[proposing] = proposed
            else:
                if f_prefer[proposed][proposing] < f_prefer[proposed][f_engage[proposed]]:
                    m_engage[f_engage[proposed]] = -1
                    m_engage[proposing] = proposed
                    f_engage[proposed] = proposing

for i in range(n):
    print("Man " + str(i) + " got married to Woman " + str(int(m_engage[i])))
    
