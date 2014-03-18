from os import environ
from subprocess import Popen, PIPE
from threading import Thread
import sys

_DEBUG = 'BUILDPACK_DEBUG' in environ

class StreamLogger:

    def _reader(self):
        for line in self._stream:
            self._formatter(line.strip())

    def __init__(self, stream, formatter):
        self._stream = stream
        self._formatter = formatter
        self._thread = Thread(target=self._reader)
        self._thread.start()

    def join(self):
        self._thread.join()


def print_indent(*lines):
    for line in lines:
        print "       {}".format(line)
    sys.stdout.flush()


def print_step(*lines):
    print "-----> {}".format(lines[0])
    print_indent(*(lines[1:]))


def print_warning(*lines):
    for line in lines:
        print " !     {}".format(line)


def print_debug(*lines):
    if _DEBUG:
        for line in lines:
            print " *     {}".format(line)


def run(exe, *args, **kwargs):
    command = '{} {}'.format(
        exe,
        ' '.join(args)
    )

    print_debug("Running " + command)

    process = Popen(command,
                    shell=True,
                    stdout=PIPE,
                    stderr=PIPE,
                    **kwargs)

    loggers = [
        StreamLogger(process.stdout, print_indent),
        StreamLogger(process.stderr, print_warning),
    ]

    process.wait()
    for logger in loggers:
        logger.join()

    return process.returncode

