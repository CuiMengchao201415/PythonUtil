# coding: utf-8


# description: 一个守护进程的简单包装类, 具备常用的start|stop|restart|status功能, 使用方便
#             需要改造为守护进程的程序只需要重写基类的run函数就可以了
# date: 2015-10-29
# usage: 启动: python daemon_class.py start
#       关闭: python daemon_class.py stop
#       状态: python daemon_class.py status
#       重启: python daemon_class.py restart
#       查看: ps -axj | grep daemon_class


import os
import sys
import time
import atexit
import signal


class Daemon:
    '''
    a generic daemon class.
    usage: subclass the CDaemon class and override the run() method
    stderr  表示错误日志文件绝对路径, 收集启动过程中的错误日志
    verbose 表示将启动运行过程中的异常错误信息打印到终端,便于调试,建议非调试模式下关闭, 默认为1, 表示开启
    save_path 表示守护进程pid文件的绝对路径
    '''

    def __init__(self, pidfile='/tmp/daemon.pid', stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        if os.path.exists(self.pidfile):
            raise RuntimeError('Already running.')

        # First fork (detaches from parent)
        try:
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            raise RuntimeError('fork #1 faild: {0} ({1})\n'.format(e.errno, e.strerror))

        os.chdir('/')
        os.setsid()
        os.umask(0o22)

        # Second fork (relinquish session leadership)
        try:
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            raise RuntimeError('fork #2 faild: {0} ({1})\n'.format(e.errno, e.strerror))

        # Flush I/O buffers
        sys.stdout.flush()
        sys.stderr.flush()

        # Replace file descriptors for stdin, stdout, and stderr
        with open(self.stdin, 'rb', 0) as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
        with open(self.stdout, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
        with open(self.stderr, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stderr.fileno())

        # Write the PID file
        with open(self.pidfile, 'w') as f:
            print(os.getpid(), file=f)

        # Arrange to have the PID file removed on exit/signal
        atexit.register(lambda: os.remove(self.pidfile))

        signal.signal(signal.SIGTERM, self.__sigterm_handler)

    # Signal handler for termination (required)
    @staticmethod
    def __sigterm_handler(signo, frame):
        raise SystemExit(1)

    def start(self):
        try:
            self.daemonize()
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)

        self.run()

    def stop(self):
        try:
            if os.path.exists(self.pidfile):
                with open(self.pidfile) as f:
                    os.kill(int(f.read()), signal.SIGTERM)
            else:
                print('Not running.', file=sys.stderr)
                raise SystemExit(1)
        except OSError as e:
            if 'No such process' in str(e) and os.path.exists(self.pidfile):
                os.remove(self.pidfile)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        pass