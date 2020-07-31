# -*- coding:utf-8 -*-
import sys

import dns.resolver



f = open('domain_list.txt', encoding='utf-8')
domain_list = []
for each_line in f:
    domain_list.append(each_line)
print(domain_list)

dns_record = dict.fromkeys(domain_list)
print(dns_record)
print(len(dns_record))

result = dns.resolver.resolve('www.baidu.com', 'CNAME')
# for i in result.response.answer:
#     for j in i.items:
#         print(j.address)
print(result)
print(type(result))



