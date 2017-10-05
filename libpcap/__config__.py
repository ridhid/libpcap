# Copyright (c) 2016-2017, Adam Karpierz
# Licensed under the BSD license
# https://opensource.org/licenses/BSD-3-Clause

from __future__ import absolute_import


def make_config(cfg_name):

    import sys
    import os.path as osp
    from runpy import run_path

    fglobals = sys._getframe(1).f_globals
    fglobals.pop("make_config", None)
    print(fglobals)
    cfg_path = osp.join(osp.dirname(fglobals["__file__"]), cfg_name)
    if osp.isfile(cfg_path):
        fglobals.update({k: v for k, v in run_path(cfg_path).items()
                         if not k.startswith("__")})
    print(fglobals)


make_config("libpcap.cfg")
