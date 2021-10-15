#!/usr/bin/env python

import os
from subprocess import check_call


def str2bool(val):
    if isinstance(val, str):
        return val in ["true", "True", "1"]
    return bool(val)


def input2environ(input):
    return f"INPUT_{input.upper()}"


def get(input):
    return os.environ.get(input2environ(input))


def get_bool(input):
    return str2bool(get(input))


if get_bool("gen-addons-readme"):
    cmd = ["python", "-m", "tools.gen_addon_readme"]
    args = [
        "--addons-dir", get("addons-dir"),
        "--org-name", get("organization"),
        "--repo-name", get("repository"),
        "--branch", get("branch"),
        "--commit" if get_bool("commit") else "--no-commit",
        "--gen-html" if get_bool("gen-html") else "--no-gen-html",
    ]
    check_call(cmd + args)


if get_bool("gen-addons-icon"):
    cmd = ["python", "-m", "tools.gen_addon_icon"]
    args = [
        "--addons-dir", get("addons-dir"),
        "--commit" if get_bool("commit") else "--no-commit",
    ]
    if get("src-path"):
        args += ["--src-path", get("src-path")]
    check_call(cmd + args)


if get_bool("gen-addons-table"):
    bin_path = "/venv/bin/oca-gen-addons-table"
    cmd = ["python", "-m", "tools.gen_addons_table"]
    args = [
        "--addons-dir", get("addons-dir"),
        "--readme-path", get("readme-path"),
        "--commit" if get_bool("commit") else "--no-commit",
    ]
    check_call(cmd + args)
