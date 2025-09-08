#!/usr/bin/env bash
# Merge branches into main in the recommended order
# Usage: save as merge-ordered.sh, chmod +x merge-ordered.sh, then ./merge-ordered.sh

set -euo pipefail

# Ensure we're in a git repo and clean
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "Not a git repo"; exit 1; }
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Working tree not clean. Commit/stash changes first."
  exit 1
fi

# Remotes and target branch
REMOTE="origin"
TARGET="main"

# Order matters:
BRANCHES=(
  "chore/split-curricula-folders"
  "feat/progression-based-curriculum"
  "cursor/develop-progressive-music-curriculum-for-children-bb33"
  "cursor/develop-progressive-mechanics-curriculum-a900"
)

echo "Fetching all…"
git fetch --all --prune

echo "Checking out ${TARGET} and updating…"
git checkout "${TARGET}"
git pull --ff-only "${REMOTE}" "${TARGET}"

for B in "${BRANCHES[@]}"; do
  echo
  echo "=== Merging ${B} into ${TARGET} ==="
  # Ensure we have the remote branch ref
  git fetch "${REMOTE}" "${B}"

  # Make sure main is up to date before each merge
  git checkout "${TARGET}"
  git pull --ff-only "${REMOTE}" "${TARGET}"

  # Merge remote-tracking branch to avoid creating a local branch
  set +e
  git merge --no-ff --no-edit "${REMOTE}/${B}"
  MERGE_STATUS=$?
  set -e

  if [[ ${MERGE_STATUS} -ne 0 ]]; then
    echo
    echo "Conflict while merging ${B}."
    echo "Resolve conflicts, then run:"
    echo "  git add -A && git commit --no-edit"
    echo "  git push ${REMOTE} ${TARGET}"
    echo "Then re-run this script to continue with remaining branches."
    exit ${MERGE_STATUS}
  fi

  echo "Pushing ${TARGET}…"
  git push "${REMOTE}" "${TARGET}"
done

echo
echo "All merges completed successfully."

