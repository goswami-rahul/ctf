# Penguins

<https://ctftime.org/writeup/22266>

We have a zip archive `2020-06-29-173949.zip`. On extracting, the tree looks like

```term
0:24 ctf/rgbCTF2020/penguins git:(master) tree -a -L 2 2020-06-29-173949
2020-06-29-173949
└── git
    ├── 1yeet
    ├── 2yeet
    ├── 3penguin
    ├── flag
    └── .git

2 directories, 4 files

```

Its a git repository. The flag is probably hidden in some previous commits.  
We can see all history using

```sh
git reflog
```

We see

```term
27440c5 (HEAD -> master) HEAD@{0}: checkout: moving from fascinating to master
800bcb9 HEAD@{1}: commit: some things are not needed
57adae7 HEAD@{2}: commit: relevant file
fb70ca3 HEAD@{3}: commit: probably not relevant
5dcac0e HEAD@{4}: commit: another perhaps relevant file
cfd97cd HEAD@{5}: commit: add content to irrelevant file
d14fcbf HEAD@{6}: commit: an irrelevant file
b474ae1 HEAD@{7}: checkout: moving from b474ae165218fec38ac9fb8d64f452c1270e68ea to fascinating
b474ae1 HEAD@{8}: checkout: moving from master to b474ae1
27440c5 (HEAD -> master) HEAD@{9}: commit (merge): Merge branch 'feature1'
102b03d HEAD@{10}: commit: some more changes
b474ae1 HEAD@{11}: commit: some new info
8ee6237 HEAD@{12}: commit: added an interesting file
1117a33 HEAD@{13}: checkout: moving from feature1 to master
7d6997a (feature1) HEAD@{14}: commit: cooler bird
955eeb7 HEAD@{15}: commit: add content
1117a33 HEAD@{16}: checkout: moving from master to feature1
1117a33 HEAD@{17}: commit: birds are cool
9dcf170 HEAD@{18}: commit (initial): first commit
```

Let's checkout at commit `57adae7`, before the deletion.  

```sh
git checkout 57adae7
ls
```

We see some new files

```term
1yeet  2yeet  3parakeet  flag  irrelevant_file  perhaps_relevant  perhaps_relevant_v2  relevant
```

`perhaps_relevant_v2` contains a string which looks like a base64 string  
`YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9`

If we decode it, we get the flag

```sh
base64 -d < perhaps_relevant_v2
```

```term
as yoda once told me "reward you i must"
and then he gave me this ----
rgbctf{d4ngl1ng_c0mm17s_4r3_uNf0r7un473}%
```
