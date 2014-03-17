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
    command = '{} {}'.format(
        exe,
        ' '.join(args)
    )

    print_step("Running " + command)

    process = Popen(command,
                    shell=True,
                    stdout=PIPE,
                    stderr=PIPE,
                    **kwargs)

    out, err = process.communicate()
    if out:
        print_indent(*out.split("\n"))
    if err:
        print_warning(*err.split("\n"))

    return process.returncode

