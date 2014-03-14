from subprocess import Popen, PIPE


def print_indent(*lines):
    for line in lines:
        print "       {}".format(line)


def print_step(*lines):
    print "-----> {}".format(lines[0])
    print_indent(*(lines[1:]))


def print_warning(*lines):
    print " !     {}".format(lines[0])
    print_indent(*(lines[1:]))


def run(exe, *args, **kwargs):
    command = [exe]
    for arg in args:
        command.extend(arg.split())
    for option, value in kwargs.items():
        command.append("--" + option.replace("_", "-"))
        command.append(value)

    print_step("Running {}".format(command))

    process = Popen(command,
                    shell=True,
                    stdout=PIPE,
                    stderr=PIPE)

    while True:
        out, err = process.communicate()
        if out:
            print_indent(*out.split("\n"))
        if err:
            print_warning(*err.split("\n"))

        if process.returncode:
            return process.returncode

