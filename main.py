import time
print('███╗░░██╗██╗░█████╗░██╗░░██╗░██████╗░███████╗███╗░░██╗\n████╗░██║██║██╔══██╗██║░██╔╝██╔════╝░██╔════╝████╗░██║\n██╔██╗██║██║██║░░╚═╝█████═╝░██║░░██╗░█████╗░░██╔██╗██║\n██║╚████║██║██║░░██╗██╔═██╗░██║░░╚██╗██╔══╝░░██║╚████║\n██║░╚███║██║╚█████╔╝██║░╚██╗╚██████╔╝███████╗██║░╚███║\n╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝')
inputnick = input('Nickname(Example: TestNick): ')
inputrange = int(input('Count: '))
rangeinput = inputrange + 1
f = open('nick.txt', 'w')
for i in range(rangeinput):
    f.write(f"{inputnick}_{i}\n")
print(f'Thanks! Count of nicknames {i} \nNickname: {inputnick}')
time.sleep(5)
exit()
