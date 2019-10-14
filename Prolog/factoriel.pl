fact(1,1).
fact(N,X):-fact(N-1,Y),X is N*Y.
