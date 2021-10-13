#!/usr/bin/env python

import os
from subprocess import check_call

print(os.environ)

check_call([
    "oca-gen-addon-readme",
    "--addons-dir", os.environ.get("INPUT_ADDONS_DIR", "."),
    "--org-name", os.environ.get("INPUT_ORG_NAME", "odoo-it"),
    "--repo-name", os.environ.get("INPUT_REPO_NAME", "test"),
    "--branch", os.environ.get("INPUT_BRANCH_NAME", "14.0"),
    "--commit",
])

check_call([
    "oca-gen-addon-icon",
    "--addons-dir", os.environ.get("INPUT_ADDONS_DIR", "."),
    "--commit",
])

check_call([
    "oca-gen-addons-table",
    "--commit",
])
