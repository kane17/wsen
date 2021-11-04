Simpsons = {'Abraham', 'Mona', 'Clancy', 'Jackie', 'Herb', 'Homer',
            'Marge', 'Patty', 'Selma', 'Bart', 'Lisa', 'Maggie', 'Ling'}

MarriedTo = {('Abraham', 'Mona'), ('Mona', 'Abraham'), ('Clancy', 'Jackie'), ('Jackie', 'Clancy'), ('Homer', 'Marge'),
             ('Marge', 'Homer')}

ChildOf = {('Herb', 'Abraham'), ('Homer', 'Abraham'), ('Homer', 'Mona'), ('Marge', 'Clancy'),
           ('Marge', 'Jackie'), ('Patty', 'Clancy'), ('Patty', 'Jackie'), ('Selma', 'Clancy'),
           ('Selma', 'Jackie'), ('Bart', 'Homer'), ('Bart', 'Marge'), ('Lisa', 'Homer'),
           ('Lisa', 'Marge'), ('Maggie', 'Homer'), ('Maggie', 'Marge'), ('Ling', 'Selma')}

SimpsonsKart = set()
for a in Simpsons:
    for b in Simpsons:
        SimpsonsKart.add((a, b))

# for i in SimpsonsKart:
#     print(i)
#
# print(ChildOf.issubset(SimpsonsKart))
# print(SimpsonsKart)

T = {(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
     (0, 8), (0, 9), (1, 0), (1, 2), (1, 6), (1, 7), (2, 0),
     (2, 1), (2, 3), (2, 8), (3, 0), (3, 2), (3, 4), (3, 8),
     (4, 0), (4, 3), (4, 5), (4, 9), (5, 0), (5, 4), (5, 6),
     (5, 9), (6, 0), (6, 1), (6, 5), (6, 7), (7, 0), (7, 1),
     (7, 6), (7, 8), (7, 9), (7, 10), (8, 0), (8, 2), (8, 3),
     (8, 7), (8, 9), (8, 10), (9, 0), (9, 4), (9, 5), (9, 7),
     (9, 8), (9, 10), (10, 7), (10, 8), (10, 9)}
S = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
     (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
     (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
     (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
     (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
     (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
     (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
     (7, 7), (7, 8), (7, 9), (8, 7), (8, 8), (8, 9), (9, 7),
     (9, 8), (9, 9), (10, 10)}
L = {(0, 7), (0, 8), (0, 9), (0, 10), (1, 7), (1, 8), (1, 9),
     (1, 10), (2, 7), (2, 8), (2, 9), (2, 10), (3, 7), (3, 8),
     (3, 9), (3, 10), (4, 7), (4, 8), (4, 9), (4, 10), (5, 7),
     (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10),
     (7, 10), (8, 10), (9, 10)}
B = {(0, 7), (1, 7), (6, 7), (0, 8), (2, 8), (3, 8), (0, 9),
     (4, 9), (5, 9), (7, 10), (8, 10), (9, 10)}

#print(B.issubset(L))

White = {2,5,7}
Orange = {1,6}
Black = {3,4,9}
Green = {8,10}
Blue = {0}

# result = True
# for x in range(11):
#     result = result and x in Blue
# print(result)


result2 = True
for x in range(11):
    if x in White:
        result1 = False
for y in range(11):
    result1 = result1 or (y in Orange and (x,y)
                          in T)
for x in range(11):
    if x in Orange:
        result2 = False
for y in range(11):
    result2 = result1 or (y in White and (x,y)
                          in T)

result2 = result2 and result1
print(result2)