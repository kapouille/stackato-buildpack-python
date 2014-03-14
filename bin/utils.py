from subprocess import check_call


def print_indent(*lines):
    for line in lines:
        print "       {}".format(line)


def print_step(*lines):
    print "-----> {}".format(lines[0])
    print_indent(*(lines[1:]))


def print_warning(*lines):
    print " !     {}".format(lines[0])
    print_indent(*(lines[1:]))


class Stream(object):
    def __init__(self, display_fun):
        self._display_fun = display_fun

    def write(self, what):
        self._display_fun(*what.split("\n"))


def run(exe, *args, **kwargs):
    command = [exe]
    command.extend([arg.split() for arg in args])
    for option, value in kwargs.items():
        command.append("--" + option.replace("_", "-"))
        command.append(value)

    return check_call(command,
                      shell=True,
                      stdout=Stream(print_indent),
                      stderr=Stream(print_warning))
