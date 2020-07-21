# Archenemy

Use steghide to extract hidden zip (use blank passphrase)

```sh
$ steghide extract -sf arched.jpeg
Enter passphrase: 
wrote extracted data to "flag.zip".
```

Then bruteforce its password using `fcrackzip` and `rockyou.txt`

```sh
$ fcrackzip -D -p /opt/rockyou.txt -u -v flag.zip
found file 'meme.jpg', (size cp/uc  27553/ 27752, flags 9, chk 9ed1)


PASSWORD FOUND!!!!: pw == kathmandu
```

