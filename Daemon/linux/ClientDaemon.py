import os
import sys
import time

from Daemon import Daemon


class ClientDaemon(Daemon):
    def __init__(self, name, save_path, stdin=os.devnull, stdout=os.devnull, stderr=os.devnull, home_dir='.', umask=22,
                 verbose=1):
        Daemon.__init__(self, save_path, stdin, stdout, stderr, home_dir, umask, verbose)
        self.name = name  # 派生守护进程类的名称

    def run(self, output_fn, **kwargs):
        fd = open(output_fn, 'w')
        while True:
            line = time.ctime() + '\n'
            fd.write(line)
            fd.flush()
            time.sleep(1)
        fd.close()


if __name__ == '__main__':
    help_msg = 'Usage: python %s <start|stop|restart|status>' % sys.argv[0]
    if len(sys.argv) != 2:
        print(help_msg)
        sys.exit(1)
    p_name = 'clientd'  # 守护进程名称
    pid_file = '/tmp/daemon.pid'  # 守护进程pid文件的绝对路径
    log_fn = '/tmp/daemon.log'  # 守护进程日志文件的绝对路径
    err_fn = '/tmp/daemon.err.log'  # 守护进程启动过程中的错误日志,内部出错能从这里看到
    cD = ClientDaemon(p_name, pid_file, stderr=err_fn, verbose=1)

    if sys.argv[1] == 'start':
        cD.start(log_fn)
    elif sys.argv[1] == 'stop':
        cD.stop()
    elif sys.argv[1] == 'restart':
        cD.restart(log_fn)
    elif sys.argv[1] == 'status':
        alive = cD.is_running()
        if alive:
            print('process [%s] is running ......' % cD.get_pid())

        else:
            print('daemon process [%s] stopped' % cD.name)
    else:
        print('invalid argument!')
        print(help_msg)
