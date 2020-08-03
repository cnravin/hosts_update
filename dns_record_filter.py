# -*- coding:utf-8 -*-
import sys

import dns.resolver


with open('domain_list.txt', encoding='utf-8') as f:
    domain_list = []
    for each_line in f:
        p = each_line.rfind('com')
        each_line = each_line[:p+3]
        # print(each_line)
        domain_list.append(each_line)

dns_record = dict.fromkeys(domain_list)
# print(dns_record)

for a in dns_record:

    result = dns.resolver.resolve(a)
    for i in result.response.answer:
        for j in i.items:
            # print(j)
            add = str(j)
            dns_record[a] = add

# print(dns_record)
hosts_text = []
for each in dns_record:
    host_line = '{}\t{}\n'.format(dns_record[each],each)
    # print(host_line)
    hosts_text.append(host_line)

try:
    with open('D:\\hosts','w') as hostfile: # 替换hosts文件存放的实际路径
        hostfile.writelines(hosts_text)
        hostfile.close()

except OSError as reason:
    print('写入文件报错：%s' % reason)





