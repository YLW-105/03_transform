from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, 'r').read()
    file = file.split('\n')
    i = 0

    while i < len(file):
        if file[i] == "line":
            a = file[i+1]
            a = a.split(' ')
            add_edge(points, int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]))
            i = i + 1

        elif file[i] == "ident":
            ident(transform)

        elif file[i] == "scale":
            a = file[i + 1]
            a = a.split(' ')
            s = make_scale(int(a[0]), int(a[1]), int(a[2]))
            matrix_mult(s, transform)
            i = i + 1

        elif file[i] == "move":
            a = file[i + 1]
            a = a.split(' ')
            t = make_translate(int(a[0]), int(a[1]), int(a[2]))
            matrix_mult(t, transform)
            i = i + 1

        elif file[i] == "rotate":
            a = file[i + 1]
            a = a.split(' ')
            angle = float(a[1])
            if a[0] == "x":
                r = make_rotX(angle)
            if a[0] == "y":
                r = make_rotY(angle)
            if a[0] == "z":
                r = make_rotZ(angle)
            matrix_mult(r, transform)
            i = i + 1

        elif file[i] == "apply":
            matrix_mult(transform, points)

        elif file[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        elif file[i] == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            a = file[i + 1]
            a = a.split(' ')
            save_extension(screen, a[0])

        elif file[i] == "quit":
            break

        i = i + 1

    file.close()
