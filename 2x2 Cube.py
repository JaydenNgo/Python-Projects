import sys
import array
"3,674,160"
# Set new limit to 5000
sys.setrecursionlimit(50000000) 


class Cube:
    def __init__(self):
        self.u_color = "White"
        self.d_color = "Yellow"
        self.l_color = "Red"
        self.r_color = "Orange"
        self.f_color = "Blue"
        self.b_color = "Green"

        self.u = [self.u_color[0] for i in range(4)]
        self.d = [self.d_color[0] for i in range(4)]
        self.l = [self.l_color[0] for i in range(4)]
        self.r = [self.r_color[0] for i in range(4)]
        self.f = [self.f_color[0] for i in range(4)]
        self.b = [self.b_color[0] for i in range(4)]

        self.all = [self.u, self.l, self.f, self.r, self.b, self.d]

    def print_cube(self):
        for side in self.all:
            for index, square in enumerate(side,1):
                print(square, end = " ")
                if not index%2:
                    print()
            print()

    def print_cube_fancy(self):
        for index, square in enumerate(self.u,1):
            if index%2 == 1:
                print("     ", end = " ")
            print(square, end = " ")
            if not index%2:
                print()
        print()
        
        for i in range(2):
            for side in (self.l, self.f, self.r, self.b):
                for j in range(2*i,2*(i+1)):
                    print(side[j], end = " ")
                print(end = " "*2)
            print()
        print()

        for index, square in enumerate(self.d,1):
            if index%2 == 1:
                print("     ", end = " ")
            print(square, end = " ")
            if not index%2:
                print()
        print("\n\n")

    def rotate_face(self, face, direction = "clock", times=1):
        '''
        0 1
        2 3
        '''

        f = face
        if direction == "clock":
            for i in range(times):
                f[0],f[1],f[3],f[2] = f[2],f[0],f[1],f[3]
        elif direction == "counter":
            for i in range(times):
                f[0],f[1],f[3],f[2] = f[1],f[3],f[2],f[0]
        else:
            print("error in rotate_face")

    def rotate_cube(self, note):
        #print(note)
        if note == "X":
            self.rotate_face(self.l, "counter",1)
            self.rotate_face(self.r, "clock",1)
            
            self.rotate_face(self.u, "clock", 2)
            self.rotate_face(self.b, "clock", 2)
            self.f, self.u, self.b, self.d =  self.d, self.f, self.u, self.b

        elif note == "X'":
            self.rotate_face(self.l, "clock",1)
            self.rotate_face(self.r, "counter",1)

            self.rotate_face(self.d, "clock", 2)
            self.rotate_face(self.b, "clock", 2)

            self.f, self.u, self.b, self.d =  self.u, self.b, self.d, self.f

        elif note == "Y":
            self.rotate_face(self.u, "clock",1)
            self.rotate_face(self.d, "counter",1)

            self.l, self.b, self.r, self.f = self.f, self.l, self.b, self.r

        elif note == "Y'":
            self.rotate_face(self.u, "counter",1)
            self.rotate_face(self.d, "clock",1)

            self.l, self.b, self.r, self.f = self.b, self.r, self.f, self.l

        else:
            print("Error in rotate_cube")
        #self.print_cube_fancy()

    #Slice moves?
    #Hard code?
    def turn(s, note):
        times = 1
        if note[-1].isdigit():
            note, times = note[0], 2
        for i in range(times):
            if note == "U":
                s.l[:2], s.f[:2], s.r[:2], s.b[:2] = s.f[:2], s.r[:2], s.b[:2], s.l[:2]
                s.rotate_face(s.u,"clock",1)
            elif note == "U'":
                s.l[:2], s.f[:2], s.r[:2], s.b[:2] = s.b[:2], s.l[:2], s.f[:2], s.r[:2]
                s.rotate_face(s.u,"counter",1)
            elif note == "F":
                s.rotate_cube("X")
                s.turn("U")
                s.rotate_cube("X'")
            elif note == "F'":
                s.rotate_cube("X")
                s.turn("U'")
                s.rotate_cube("X'")
            elif note == "D":
                s.rotate_cube("X");s.rotate_cube("X")
                s.turn("U")
                s.rotate_cube("X'");s.rotate_cube("X'")
            elif note == "D'":
                s.rotate_cube("X");s.rotate_cube("X")
                s.turn("U'")
                s.rotate_cube("X'");s.rotate_cube("X'")
            elif note == "B":
                s.rotate_cube("X'")
                s.turn("U")
                s.rotate_cube("X")
            elif note == "B'":
                s.rotate_cube("X'")
                s.turn("U'")
                s.rotate_cube("X")
            elif note == "L":
                s.rotate_cube("Y'")
                s.turn("F")
                s.rotate_cube("Y")
            elif note == "L'":
                s.rotate_cube("Y'")
                s.turn("F'")
                s.rotate_cube("Y")
            elif note == "R":
                s.rotate_cube("Y")
                s.turn("F")
                s.rotate_cube("Y'")
            elif note == "R'":
                s.rotate_cube("Y")
                s.turn("F'")
                s.rotate_cube("Y'")
            else:
                print(f"Error in turn(), note = {note}")
        s.all = [s.u, s.l, s.f, s.r, s.b, s.d]
        

    def clone(self):
        new = Cube()
        new.u = [i for i in self.u]
        new.d = [i for i in self.d]
        new.l = [i for i in self.l]
        new.r = [i for i in self.r]
        new.f = [i for i in self.f]
        new.b = [i for i in self.b]
        new.all = [i for i in self.all]
        new.all = [new.u, new.l, new.f, new.r, new.b, new.d]
        return new
    
    def hashed(self):
        return tuple(tuple(row) for row in self.all)

    
total = 0
def search(cube):
    for index, alg in enumerate(possible_moves):
        global total
        clone = cube.clone()
        clone.turn(alg)
        if clone.hashed() in combinations:
            continue
        if not len(combinations) % 10_000:
            print(f"{total:,}, {len(combinations)}")
        combinations.add(clone.hashed())
        total += 1
        search(clone)
        
possible_moves = ["U","D","F","B","L","R"]
reverse = [i+"'" for i in possible_moves]
doubles = [i+"2" for i in possible_moves]
possible_moves = possible_moves + reverse + doubles
print(possible_moves)

T_perm = ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"]

alg1 = ["U2", "F2", "U2", "F2", "U2", "F2"]
alg2 = ["F2", "U2", "F2", "U2", "F2", "U2"]

combinations = set()

cube = Cube()
cube.print_cube_fancy()
print("Start")
search(cube)
print("End")

#cube1 = Cube()
#cube2 = Cube()
#cube1.print_cube_fancy()
#cube2.print_cube_fancy()
'''
for move in alg1:
    cube1.turn(move)
for move in alg2:
    cube2.turn(move)
print(f"Equivalent: {cube1 == cube2}")


cube1.print_cube_fancy()
cube2.print_cube_fancy()
'''
a = (('W', 'R', 'G', 'O'), ('G', 'Y', 'R', 'O'), ('R', 'B', 'G', 'B'), ('Y', 'W', 'W', 'B'), ('G', 'O', 'Y', 'B'), ('Y', 'O', 'W', 'R'))
for i in combinations:
    print(i)
    

print(len(combinations))
print(a in combinations)

print("Done")


