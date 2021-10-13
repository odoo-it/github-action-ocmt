#!/bin/bash
ls /app
oca-gen-addon-readme --addons-dir=$INPUT_ADDONS_DIR --org-name=$INPUT_ORG_NAME --repo-name=$INPUT_REPO_NAME --branch=$INPUT_BRANCH_NAME --commit
oca-gen-addon-icon --addons-dir=$INPUT_ADDONS_DIR --commit
oca-gen-addons-table --commit
