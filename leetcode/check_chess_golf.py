# https://www.codewars.com/kata/5e320fe3358578001e04ad55/train/python
is_check=lambda C:[R:=range(8),any(C[i][j]=="♔"*(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+(X*I==1)*"♟"+("♝♛"if I*J else"♜♛")*(not X*Y*(X!=Y)and all(C[i+o*(2*(I<Y)-(Y>0))][j+o*(2*(J<X)-(X>0))]==' 'for o in range(1,min(X,Y) if X*Y else X+Y))))for x in R for y in R for i in R for j in R)][1]



# is_check=lambda C:[R:=range(8),any(C[i][j]=="♔"*(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟") and (X*Y*(X!=Y) or all(C[i+o*(2*(I!=Y)-(I!=0))][j+o*(2*(J!=X)-(J!=0))]==' 'for o in range(1,max(X,Y))))for x in R for y in R for i in R for j in R)][1]
# is_check=lambda C:[R:=range(8),any(C[i][j]=="♔"*(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟") and (X*Y*(X!=Y) or all(C[i+o*(2*(I!=Y)-(I!=0))][j+o*(2*(J!=X)-(J!=0))]==' 'for o in range(1,max(X,Y))))for x in R for y in R for i in R for j in R)][1]


# [R:=range(8),any(R)][1]
# (R:=range(8))and any(R)
    
# for q,Q in zip(range(i,8,d),range(j,8,D)) for d in [0,1] for D in [-1,0,1]
# ''.join([C[i+s*d][j+s*D]for s in R if i+s*d in R and j+s*D in R]) for d in [-1,0,1] for D in [-1,0,1]
# ''.join([c for s in R if (i+s*d in R)*(j+s*D in R)*(c:=C[i+s*d][j+s*D])]) for d in [-1,0,1] for D in [-1,0,1]
# ''.join([c for s in R if i+s*d in R and j+s*D in R and c:=C[i+s*d][j+s*D]]) for d in [-1,0,1] for D in [-1,0,1]
# ''.join([c for s in R if i+s*d in R and j+s*D in R and c:=C[i+s*d][j+s*D]]) for d in [-1,0,1] for D in [-1,0,1]
# ''.join([c for s in R if (i+s*d in R)*(j+s*D in R)*(c:=C[i+s*d][j+s*D])!=' ']) for d in [-1,0,1] for D in [-1,0,1]

# [1]in("♝♛"if d*D else"♜♛")
# pawn if 


is_check=lambda C:[R:=range(8),any(
    C[i][j]=="♔"*(C[x][y]in(
        (X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+ \
        (X*I==1)*"♟"+ \
        ("♝♛"if I*J else"♜♛")*(not X*Y*(X!=Y)and
        ("♝♛"*I*J+"♜♛"*not I*J)
            all(C[i+o*(2*(I!=Y)-(I!=0))][j+o*(2*(J!=X)-(J!=0))]==' 'for o in range(1,max(X,Y))))
            all(C[i+o*(2*(I!=Y)-(I!=0))][j+o*(2*(J!=X)-(J!=0))]==' 'for o,O in zip(range(i,x,2*(I<Y)-1),) range(1,max(X,Y))))
    )for x in R for y in R for i in R for j in R)][1]

R=range(8)
L=reversed(R)

list(zip(*grid[::-1]))
+("♝♛"if I*J else"♜♛")*(not X*Y*(X!=Y)and all(C[i+o*(2*(I<Y)-(Y>0))][j+o*(2*(J<X)-(X>0))]==' 'for o in range(1,min(X,Y) if X*Y else X+Y))))
any('♔'+' '*o+c in''.join(x)for x,c in[['♝♛',C[i]],['♜♛',[C[i+j][j]for j in range(8-i)]]]for o in R for i in R)for C in [C:=list(zip(*grid[::-1])C[]]
any('♔'+' '*o+c in''.join(x)for x,c in[['♝♛',C[i]],['♜♛',[C[i+j][j]for j in range(8-i)]]]for o in R for i in R)for C in [C:=list(zip(*grid[::-1])C[]]
is_check=lambda C:[R:=range(8),any(C[i][j]=="♔"*(C[x][y]in((X:=abs(j-y))+abs(I:=i-x))==3)*"♞"+(X*I==1)*"♟"for x in R for y in R for i in R for j in R)][1]
is_check=lambda C:[R:=range(8),any(C[i][j]=="♔"*(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+(X*I==1)*"♟"+("♝♛"if I*J else"♜♛")*(not X*Y*(X!=Y)and all(C[i+o*(2*(I<Y)-(Y>0))][j+o*(2*(J<X)-(X>0))]==' 'for o in range(1,min(X,Y) if X*Y else X+Y))))for x in R for y in R for i in R for j in R)][1]
C[i+j][j]
C[i+j][8-j]
C[j][i+j]
C[8-j][i+j]
for C in [C,zip(C)]

C[i+j][j]
for i in R:
    C[i]
    ''.join([C[i+j][j] for j in range(8-i)])
    ''.join([C[i+j][j] for j in range(8-i)])

    
                                zip('♝♛','♜♛'
                                    '♛'+c for c in'♝♜'
    for x in C[i],[C[i+j][j] for j in range(8-i)]
    
    for j in R:
#         [j] for j in R
    
        C[j][i]
    for j in R:
        C[i][j]
    for j in l
    for j in M:
        
rotate 90
# x  y
# y -x
#-x -y
#-y  x
# 
for R

#             all(C[i+o*f][j+o*g]==' 'for o in Rrange(1,max(X,Y))))
#             all(C[i+o*f][j+o*g]in'♔♝♛'for o in Rrange(1,max(X,Y))))
#             all(C[q][Q]in('♝♛'if s*S else'♜♛')for q,Q in zip(range(i+s,m,s),range(j+S,M,S)))for m,s in [(, in Rrange(1,max(X,Y))))

# # is_check=lambda C:[R:=range(8),any(C[i][j]=="♔"*(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟")for x in R for y in R for i in R for j in R)][1]
# # "♝♛"*(X==Y)if I*J else"♜♛"
# # X*Y*(X!=Y) or all(C[i+o*(2*(I!=Y)-(I!=0))][j+o*(2*(J!=X)-(J!=0))]==' 'for o in range(1,max(X,Y)))
# # is_check=lambda C:[R:=range(8),any(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟"for x in R for y in R for i in R for j in R if C[i][j]=="♔")][1]
# # is_check=lambda C:(R:=range(8))and any(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟"for x in R for y in R for i in R for j in R if C[i][j]=="♔")

# # is_check=lambda C:[from itertools import product as p,any(C[x][y]in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟"for x,y,i,j in p(range(8),repeat=4) if C[i][j]=="♔")][1]



# # is_check=lambda C:[R:=range(8),[any(C[x][y] in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟"for x in R for y in R)for i in R for j in R if C[i][j]=="♔"][0]][1]
# # is_check=lambda C: [(R:=range(8)),[any([(c:=C[x][y])in
# # (("♝♛"*((X:=abs(J))==(Y:=abs(I))))if (I:=i-x)*(J:=j-y) else"♜♛")
# # or X<2and I==1and"♟"==c or  for x in R for y in R])for i in R for j in R if C[i][j] == "♔"][0]][1]
# # (c:=C[x][y])=="♞"or(X<2)*I==1and c==or C[x][y] in((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+((X<2)*I==1)*"♟"
# # def is_check(C):
# #     (R:=range(8))
# #     for i in R:
# #         for j in R:
# #             if C[i][j] == "♔":
# #                 for x in R:
# #                     for y in R:
# # #                         (c:=C[x][y])
# # #                         (I:=i-x)
# # #                         (J:=j-y)
# # #                         (X:=abs(J))
# # #                         if X==Y or X*Y==0:
# # #                             o*((J!=0)-2*(J!=X))
# # #                             o*(J!=0)-2*o*(J!=X)
                            
# #                         s = ((X:=abs(J:=j-y))+(Y:=abs(I:=i-x))==3 and X*Y)*"♞"+("♝♛"*(X==Y)if I*J else"♜♛")+(X*I==1)*"♟"
# # #                         print(i,j,x,y, "_", ((I!=0)-2*(I!=Y)),((J!=0)-2*(J!=X)))
# # #                         print(not(X*Y*(X!=Y)), X, Y, I, J)
# #                         t = X*Y*(X!=Y) or all(C[i+o*(2*(I!=Y)-(I!=0))][j+o*(2*(J!=X)-(J!=0))]==' 'for o in range(1,max(X,Y)))
# # #                         t = X*Y*(X!=Y) or all(C[i+o*(h:=lambda I,Y:2*(I!=Y)-(I!=0))(I,Y)][j+o*h(J,X)]==' 'for o in range(1,max(X,Y)))
# # #                         print(t, not(X*Y*(X!=Y)), X, Y)
# # #                         t = (X*Y+(X!=Y)) and all(C[i+o*((I!=0)-2*(I!=Y))][j+o*((J!=0)-2*(J!=X))]==' 'for o in range(X if X else Y)
# #                         if C[x][y] in s and t:
# #                             print(i,j,x,y,C[x][y],s)
# #                             return True
# #     return False

                        
# # #                         if c in(("♝♛"*(X==Y))if I*J else"♜♛") or X*I==1and"♟"==c or abs(I)+X==3and"♞"==c:
# # #                             print(i,j,x,y,c)
# # #                             return True
# # #     return False
# # # #                 any([
# # # #          in ])
                
# # # #      [any([
# # # #          (c:=C[x][y])in("♝♛"if(I:=i-x)*(J:=j-y)else"♜♛")or (X:=abs(J))<2and I==1and"♟"==c or abs(I)+X==3and"♞"==c for x in R for y in R])
# # # #     ki, kj= [(i,j) for i in range(8) for j in range(8) if C[i][j] == "♔"][0]
# # # #     print(ki, kj)
# # # #     ds = {(x,y):"♜♛"if x==0 or y==0else"♝♛"for x in[-1,0,1]for y in[-1,0,1]}
# # # #      0<=(u:=U+i*x)<8and 0<=(v:=V+i*y)<8and(C[u][v]in s + C[u][v]!=' ') for i in range(1,8)] for (x,y),s in{(x,y):"♜♛"if x==0 or y==0else"♝♛"for x in[-1,0,1]for y in[-1,0,1]}
# # # #     

# # # # def is_check(C):
# # # # #     ki, kj= [any([(c:=C[x][y])in("♝♛"if(I:=i-x)*(J:=j-y)else"♜♛")or (X:=abs(J))<2and I==1and"♟"==c or abs(I)+X==3and"♞"==c for x in R for y in R])for i in (R:=range(8)) for j in R if C[i][j] == "♔"][0]
# # # #     U,V = ki, kj
# # # #     print(ki, kj)
# # # #     ds = {(x,y):"♜♛"if x==0 or y==0else"♝♛"for x in[-1,0,1]for y in[-1,0,1]}
# # # #     if any([(l:=[c for i in range(1,8) if 0<=(u:=U+i*x)<8and 0<=(v:=V+i*y)<8and(c:=C[u][v])!=' '])and l[0]in s for x,y,s in [(x,y,"♜♛"if x==0 or y==0else"♝♛")for x in[-1,0,1]for y in[-1,0,1]]]):
# # # #         return True
# # # #     for (x,y),s in ds.items():
# # # #         for i in range(1,8):
# # # #             u,v=ki+i*x,kj+i*y
# # # #             if 0<=u<8and 0<=v<8:
# # # #                 if x==-1 and y!=0 and i==1 and C[u][v]=="♟": return True
# # # # #                 if C[u][v]in s: return True
# # # #                 if C[u][v]!=' ': break
# # # #     for a in [1,2]:
# # # #         b = 3-a
# # # #         for c in [-a,a]:
# # # #             for d in [-b,b]:
# # # #                 u,v=ki+c,kj+d
# # # #                 if 0<=u<8and 0<=v<8 and C[u][v]=="♞": return True
# # # #     return False


def king_is_in_check(C : list[list[str]]) -> bool:
    ki, kj= [(i,j) for i in range(8) for j in range(8) if C[i][j] == "♔"][0]
    print(ki, kj)
    ds = {(x,y):"♜♛"if x==0 or y==0else"♝♛"for x in[-1,0,1]for y in[-1,0,1]}
    for (x,y),s in ds.items():
        for i in range(1,8):
            u,v=ki+i*x,kj+i*y
            if 0<=u<8and 0<=v<8:
                if x==-1 and y!=0 and i==1 and C[u][v]=="♟": return True
                if C[u][v]in s: return True
                if C[u][v]!=' ': break
    for a in [1,2]:
        b = 3-a
        for c in [-a,a]:
            for d in [-b,b]:
                u,v=ki+c,kj+d
                if 0<=u<8and 0<=v<8 and C[u][v]=="♞": return True
    return False