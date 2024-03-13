# from configparser import ConfigParser

# config = ConfigParser()
# config.read('adb.conf')

# # 读取整个conf文件的内容
# for line in config['Rule']:
#     # print(line)
#     print(line.split(',')[0])
    # print(section)
#     options = config.options(section)
#     print(options)
    # for option in options:
    #     value = config.get(section, option)
        # print(value)
        # print(f"{section} - {option} : {value}")
        
import re
all_rule = set()
pattern = re.compile(".*Reject", re.IGNORECASE)

with open('adb.conf', 'r') as a1, \
    open('antiands.conf','r') as a2, \
    open('outputs.conf', 'w') as out:
    
    cnt_1 = 0
    for line in a1:
        line = line.strip()
        if pattern.match(line):
            all_rule.add(line)
            cnt_1 += 1
    
    cnt_2 = 0
    for line in a2:
        line = line.strip()
        if pattern.match(line):
            all_rule.add(line)
            cnt_2 += 1
    
    l = list(all_rule)
    
    l.sort()
    cnt_3 = 0
    for i in l:
        print(i, file=out, end='\n')
        cnt_3 += 1
        
    print(cnt_1, cnt_2, cnt_3)
    print(cnt_1 + cnt_2)