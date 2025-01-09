###PERFORMING A SPARSE CHECKOUT

```bash
git sparse-checkout set $CHECKOUT_DIRECTORY_PATH
```

Enables sparse checkout feature in git
Tells git we only want to checkout specific parts of the repository
$CHECKOUT_DIRECTORY_PATH might be something like kubernetes/dev/service1
Only this directory and its contents will be checked out, saving disk space
Everything else in the repository will be ignored

```bash

git fetch --depth=1 origin $CHECKOUT_BRANCH
```

Fetches the latest commit from the specified branch
--depth=1 means we only get the most recent commit (shallow clone)
origin is the remote we added earlier
$CHECKOUT_BRANCH might be "main" or "master" or any other branch name

```bash
git checkout FETCH_HEAD
```

Switches to the commit we just fetched
FETCH_HEAD refers to the latest fetched commit
This gives us the working directory with only the files we specified in sparse-checkout
