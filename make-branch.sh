#!/bin/bash

set -euof pipefail

profilename="$1"
projectname="awesome-for-beginners"
branchname="${2:-main}" 

fullname="${profilename}/${branchname}"

branchname="${fullname}-branch-copy"

git checkout main
git checkout -b "${branchname}"
git remote add "${profilename}" "https://github.com/${profilename}/awesome-for-beginners.git"
git fetch "${profilename}"
git merge --no-gpg "${fullname}" -m "Merge ${fullname} into ${branchname}"
git remote remove "${profilename}"
git fetch --prune
git push --set-upstream origin "${branchname}"
git checkout main
