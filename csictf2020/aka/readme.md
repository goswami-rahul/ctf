# AKA

We are given shell, and some file reading commands (e.g. `cat`, `less`) are blocked.  
I used `base64` to get the flag.  

```sh
base64 flag.txt | base64 -d
```

Alternatively, simply we can spawn a new shell

```sh
/bin/sh
```

Flag

```txt
csictf{1_4m_cl4rk3_k3nt}
```
