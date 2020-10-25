def eliminate_non_celebrities(matrix):
    """Take an n x n matrix that has m[i][j] = True iff i knows j and return
    person who is maybe a celebrity."""
    possible_celeb = 0
    n = len(matrix)
    for p in range(1, n):
        if (matrix[possible_celeb][p]
            or not matrix[p][possible_celeb]):
            possible_celeb = p
    return possible_celeb
 
 
def check_if_celebrity(possible_celeb, matrix):
    """Take an n x n matrix that has m[i][j] = True iff i knows j and return
    True if possible_celeb is a celebrity."""
    for i in range(n):
        if matrix[possible_celeb][i] is True:
            return False
 
    for i in range(n):
        if matrix[i][possible_celeb] is False:
            if i != possible_celeb:
                return False
 
    return True
 
 
n = int(input('Number of people: '))
 
# create n x n matrix initialized to False that has m[i][j] = True iff i knows j
m = [[False]*n for _ in range(n)]
 
for i in range(n):
    people = input('Enter list of people known to {}: '.format(i)).split()
    for p in people:
        p = int(p)
        m[i][p] = True
 
possible_celeb = eliminate_non_celebrities(m)
 
if check_if_celebrity(possible_celeb, m):
    print('{} is the celebrity.'.format(possible_celeb))
else:
    print('There is no celebrity.')
