# import re
# fh = open("regex_sum_105819.txt")
# total = 0
# for line in fh:
# 	line = line.strip()
# 	if not len(re.findall('[0-9]+', line)) > 0: continue
# 	for num in re.findall('[0-9]+', line): total = total + int(num)
# print(total)

import re
total = 0
for num in re.findall('[0-9]+', open("regex_sum_105910.txt").read()):total = total + int(num)
print(total)

# import re
# print(sum([ int(i) for i in re.findall('[0-9]+', open("regex_sum_105819.txt").read())]))