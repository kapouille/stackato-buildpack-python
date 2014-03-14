def print_indent(*lines):
    for line in lines:
        print "       {}".format(line)


def print_step(*lines):
    print "-----> {}".format(lines[0])
    print_indent(*(lines[1:]))


def print_warning(*lines):
    print " !     {}".format(lines[0])
    print_indent(*(lines[1:]))
