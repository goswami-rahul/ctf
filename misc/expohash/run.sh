mkfifo p1
mkfifo p2
./a.out < p1 > p2 &
nc 2020.redpwnc.tf 31458 > p1 < p2 &
