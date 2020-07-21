undefined8 main(void)

{
  undefined *puVar1;
  int iVar2;
  int bal2;
  int bal1;
  char *inp;
  
  inp = (char *)malloc(0x400);
  fgets(inp,0x400,stdin);
  setbuf(stdout,(char *)0x0);
  while (puVar1 = sa, *inp != '\0') {
    switch(*inp) {
    case '!':
      tmp = sa;
      sa = sb;
      sb = sc;
      sc = puVar1;
      break;
    case '$':
      sa = sa + 1;
      *sa = 1;
      break;
    case '+':
      sa[-1] = *sa + sa[-1];
      sa = sa + -1;
      break;
    case ',':
      iVar2 = getchar();
      *sa = (char)iVar2;
      break;
    case '-':
      sa[-1] = sa[-1] - *sa;
      sa = sa + -1;
      break;
    case '.':
      puVar1 = str + 1;
      *str = *sa;
      str = puVar1;
      break;
    case '[':
      if (*sa == '\0') {
        bal1 = 1;
        while (bal1 != 0) {
          inp = inp + 1;
          if (*inp == '[') {
            bal1 = bal1 + 1;
          }
          else {
            if (*inp == ']') {
              bal1 = bal1 + -1;
            }
          }
        }
      }
      break;
    case ']':
      if (*sa != '\0') {
        bal2 = 1;
        while (bal2 != 0) {
          inp = inp + -1;
          if (*inp == '[') {
            bal2 = bal2 + -1;
          }
          else {
            if (*inp == ']') {
              bal2 = bal2 + 1;
            }
          }
        }
      }
    }
    inp = inp + 1;
  }
  str = STR;
  iVar2 = strcmp(STR,"HELLO\n");
  if (iVar2 == 0) {
    puts(str);
    system("cat flag.txt");
  }
  else {
    puts("Failed.");
  }
  return 0;
}