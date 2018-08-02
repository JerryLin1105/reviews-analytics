data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for k in data:
	sum_len = sum_len + len(k)
print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆留言長度小於100')
print(new[15])
