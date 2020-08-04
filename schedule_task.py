# -*- coding:utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
import dns_record_filter
import push_hosts_update
import mov_hosts_file


def main():
    dns_record_filter.host_record_update()
    push_hosts_update.push_hosts()
    mov_hosts_file.mov_file()


sched = BlockingScheduler()
sched.add_job(main, 'cron', day_of_week='mon-sun', hour=0, minute=30)
sched.start()
