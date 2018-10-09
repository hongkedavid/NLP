# Ref: https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History
# All commit info
git log --all > $file

# Last 10 commits
git log -10

# Get details of certain commit
git log -p $commit_id

# Ref: https://git-scm.com/docs/pretty-formats
git log --pretty=oneline
git log --pretty=format:"%H - %s - %b"

git log --pretty="%h - %s" --author='$author' --since="2008-10-01" --before="2008-11-01" --no-merges -- t/
