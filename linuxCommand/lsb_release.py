# -*- coding:utf-8 -*-
# author: dzhhey

info = """No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
"""


def parse(args_=None):
    try:
        if len(args_) == 1:
            if args_[0] == "-a":
                with open("buffer", "w") as f:
                    f.write(info)
        else:
            with open("buffer", "w") as f:
                f.write("No LSB modules are available.")
    except Exception:
        with open("buffer", "w") as f:
            f.write("No LSB modules are available.")
