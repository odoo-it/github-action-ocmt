#!/usr/bin/env python

import os
from subprocess import check_call

check_call([
    "oca-gen-addon-readme",
    "--addons-dir", os.environ["INPUT_ADDONS_DIR"],
    "--org-name", os.environ["INPUT_ORG_NAME"],
    "--repo-name", os.environ["INPUT_REPO_NAME"],
    "--branch", os.environ["INPUT_BRANCH_NAME"],
    "--commit",
])

check_call([
    "oca-gen-addon-icon",
    "--addons-dir", os.environ["INPUT_ADDONS_DIR"],
    "--commit",
])

check_call([
    "oca-gen-addons-table",
    "--commit",
])
