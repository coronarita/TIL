# 대소문자 개수 나눠서
f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()

n_of_yesterday = yesterday_lyric.count("Yesterday")
print("Number of a word 'Yesterday'", n_of_yesterday)
n_of_yesterday = yesterday_lyric.count("yesterday")
print("Number of a word 'yesterday'", n_of_yesterday)