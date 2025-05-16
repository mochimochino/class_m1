import numpy as np
import matplotlib.pyplot as plt


N = 10000 # 試行回数
win_stick_counts = 0 # 扉を変えずに勝った回数を記録
win_change_counts = 0 # 扉を変えて買った回数を記録
win_stick_history = []
win_change_history = []
trials_history = []

for i in range(N):
    trials_history.append(i)
    m = np.random.randint(0, 3) # 当たりの番号
    n = np.random.randint(0, 3) # 初めに選ぶ番号

    doors = [0, 1, 2]
    remaining_doors = doors[:] # ドアのリストをコピー

    remaining_doors.remove(n) # 最初に選んだドアを候補から外す


    # ホストが外すドアを選ぶ (ハズレを選ぶ)
    if n == m:
        # 当たりを選んでいた場合、残りのハズレドアからランダムに一つ選ぶ
        host_choice = np.random.choice(remaining_doors)
        #print("あたり",m,"choice",n,remaining_doors,host_choice)
    else:
        # ハズレを選んでいた場合、残りのハズレドアは一つだけなのでそれを選ぶ
        remaining_doors.remove(m)
        host_choice = remaining_doors[0]
        #print("あたり",m,"choice",n,remaining_doors,host_choice)
    doors.remove(host_choice) # ホストが選んだドアを候補から外す
    #print(doors,host_choice)
    #残りドアが二つの状態
    #プレイヤーがドアを変える場合と変えない場合に場合分けする
    #プレイヤーが変える場合の確立
    doors_change = doors[:]
    #print(n,m,doors_change)
    doors_change.remove(n) # プレイヤーが選んだドアを候補から外す
    choice_door_change = doors_change[0] # プレイヤーが変えたドア
    #print(n,choice_door_change)
    if choice_door_change == m:
        win_change_counts += 1
    else:
        win_change_counts += 0
    #print(m,choice_door_change,win_change_counts)

    #プレイヤーが変えない場合の確立
    if n==m:
        win_stick_counts += 1
    else:
        win_stick_counts += 0
    #print(m,n,win_stick_counts)
    win_stick_history.append(win_stick_counts)
    win_change_history.append(win_change_counts)
    #print(win_stick_history,win_change_history)


print("試行回数:",N)
print("ドアを変えずに勝った回数:", win_stick_counts,"確率:",win_stick_counts/N)
print("ドアを変えて勝った回数:" ,win_change_counts, "確率:" ,win_change_counts/N)



plt.plot(trials_history, win_stick_history, label='Stay', color='blue')
plt.plot(trials_history, win_change_history, label='Change', color='red')
plt.xlabel('Trial Number')
plt.ylabel('Win Count')
plt.legend()
plt.xlim(0,N)
plt.ylim(0, N)
plt.title('Monty Hall Problem Simulation')
plt.savefig('monty_hall_simulation.png')
plt.show()
