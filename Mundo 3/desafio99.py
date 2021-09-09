def maior(* n):
    count = 0;
    m = 0;
    for c in n:
        count += 1;
        if count == 0:
            m = c
        elif c > m:
            m = c;
    print(f'Entre os {count} números, o maior foi o número {m}')
maior(2,7,8,6,110,4,5,10,15,25)