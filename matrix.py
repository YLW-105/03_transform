"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    translate = new_matrix()
    ident(translate)
    translate[3][0] = x
    translate[3][1] = y
    translate[3][2] = z
    return translate

def make_scale( x, y, z ):
    scale = new_matrix()
    ident(scale)
    scale[0][0] = x
    scale[1][1] = y
    scale[2][2] = z
    return scale

def make_rotX( theta ):
    theta = math.radians(theta)
    rotX = new_matrix()
    ident(rotX)
    cos = math.cos(theta)
    sin = math.sin(theta)
    rotX[1][1] = cos
    rotX[2][1] = -sin
    rotX[1][2] = sin
    rotX[2][2] = cos
    return rotX

def make_rotY( theta ):
    theta = math.radians(theta)
    rotY = new_matrix()
    ident(rotY)
    cos = math.cos(theta)
    sin = math.sin(theta)
    rotY[0][0] = cos
    rotY[2][0] = sin
    rotY[0][2] = -sin
    rotY[2][2] = cos
    return rotY

def make_rotZ( theta ):
    theta = math.radians(theta)
    rotZ = new_matrix()
    ident(rotZ)
    cos = math.cos(theta)
    sin = math.sin(theta)
    rotZ[0][0] = cos
    rotZ[1][0] = -sin
    rotZ[0][1] = sin
    rotZ[1][1] = cos
    return rotZ

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
