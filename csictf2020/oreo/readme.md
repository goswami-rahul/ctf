# Oreo

The cookies have a `flavour` parameter set to `c3RyYXdiZXJyeQ==`, which when decoded from base64, is `strawberry`.  
We need to set flavour to `chocolate`, so just send request with changed cookie, with `flavour` set to `base64('chocolate')`.

Flag

```txt
csictf{1ick_twi5t_dunk}
```
