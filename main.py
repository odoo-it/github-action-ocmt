#!/usr/bin/env python

import os
from subprocess import check_call


def str2bool(val):
    if isinstance(val, bool):
        return val
    elif isinstance(val, str):
        return val in ["true", "True", "1"]
    else:
        return bool(val)


def input2environ(input):
    return f"INPUT_{input.upper()}"


def get(input):
    return os.environ.get(input2environ(input))


def get_bool(input):
    return str2bool(get(input))


if get_bool("gen-addons-readme"):
    bin_path = "/app/bin/oca-gen-addon-readme"
    args = [
        "--addons-dir", get("addons-dir"),
        "--org-name", get("organization"),
        "--repo-name", get("repository"),
        "--branch", get("branch"),
        "--commit" if get_bool("commit") else "--no-commit",
        "--gen-html" if get_bool("gen-html") else "--no-gen-html",
    ]
    check_call([bin_path] + args)


if get_bool("gen-addons-icon"):
    bin_path = "/app/bin/oca-gen-addon-icon"
    args = [
        "--addons-dir", get("addons-dir"),
        "--commit" if get_bool("commit") else "--no-commit",
    ]
    if get("src-path"):
        args += ["--src-path", get("src-path")]
    check_call([bin_path] + args)


if get_bool("gen-addons-table"):
    bin_path = "/app/bin/oca-gen-addons-table"
    args = [
        "--addons-dir", get("addons-dir"),
        "--readme-path", get("readme-path"),
        "--commit" if get_bool("commit") else "--no-commit",
    ]
    check_call([bin_path] + args)
