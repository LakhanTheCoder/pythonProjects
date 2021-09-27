'''Suppostoe we want to move n discs from A to C, means frm = A, aux = B, to = C
    So the program will move n-1 discs from A to B using C as auxliary and Will move the last disc to the C disc and
    then moving n-1 discs from B to C using A as auxliary.
    Follow the comments in the code to follow
'''
def towerOfHanoi(n, frm = 'A', aux = 'B',to = 'C'):
    # If there are only one disc to move move that disc from frm to to.
    if n == 1:
        print("Move from ",frm," to", to);
    else:
        #move n-1 dics from 'frm' to 'aux 'piller using 'to' as auxiliary piller
        towerOfHanoi(n-1,frm,to,aux);
        # moving last disc from 'frm' to 'to' piller
        print("Move from ",frm," to", to);
        # move n-1 dics from 'aux' to 'to 'piller using 'frm' as auxiliary piller
        towerOfHanoi(n-1,aux,frm,to);

print("Give n as input")
n = int(input());
print("Give frm, aux, to piller values")
frm, aux, to = input().strip().split()
print(frm,aux,to)
# Calling recursion function for Tower of Hanoi
towerOfHanoi(n,frm,aux,to);