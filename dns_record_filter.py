# -*- coding:utf-8 -*-
import datetime
import sys
import dns.resolver
import push_hosts_update


def host_record_update():

    with open('domain_list.txt', encoding='utf-8') as f:
        domain_list = []
        for each_line in f:
            p = each_line.rfind('com')
            each_line = each_line[:p+3]
            # print(each_line)
            domain_list.append(each_line)

    dns_record = dict.fromkeys(domain_list)
    dc_dns = ['10.1.120.241', '10.1.124.241']
    # print(dns_record)

    for a in dns_record:
        dc_resolver = dns.resolver.Resolver()
        dc_resolver.nameservers = dc_dns
        result = dc_resolver.resolve(a)
        for i in result.response.answer:
            for j in i.items:
                # print(j)
                add = str(j)
                dns_record[a] = add
                # print(add)

    # print(dns_record)
    hosts_text = []
    update_time = datetime.datetime.now()

    for each in dns_record:
        host_line = '{}\t{}\n'.format(dns_record[each], each)
        # print(host_line)
        hosts_text.append(host_line)

    if sys.platform == 'win32':
        file_path = r'E:\py_project\hosts\hosts.txt'
    else:
        file_path = '/opt/hosts/hosts.txt'

    try:
        with open(file_path, 'w') as host_file:     # 替换hosts文件存放的实际路径
            hosts_text.insert(0, '# {}\n'.format(update_time))  # 行首插入时间戳
            host_file.writelines(hosts_text)
            host_file.close()

    except OSError as reason:
        print('写入文件报错：%s' % reason)


# push update to git
if __name__ == '__main__':
    host_record_update()
    push_hosts_update.push_hosts()
