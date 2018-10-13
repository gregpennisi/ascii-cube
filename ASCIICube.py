from Linked_List import Linked_List

Y = Linked_List()
B = Linked_List()
R = Linked_List()
G = Linked_List()
O = Linked_List()
W = Linked_List()

#Yellow 0
#Red 2
#Green 3
#Orange 4
#Blue 1
#White 5

faces = [Y , B , R , G , O , W]
count = 0
r = "reg"
p = "prime"
t = "two"

for item in faces :

    for i in range(8) :

        item.append_element(count)

    count += 1

def right_turn(turn_type, instructions) :

    line_list = Linked_List()

    line_list.append_element(Y.get_element_at(0))
    line_list.append_element(Y.get_element_at(7))
    line_list.append_element(Y.get_element_at(6))

    line_list.append_element(R.get_element_at(0))
    line_list.append_element(R.get_element_at(7))
    line_list.append_element(R.get_element_at(6))

    line_list.append_element(W.get_element_at(0))
    line_list.append_element(W.get_element_at(7))
    line_list.append_element(W.get_element_at(6))

    for i in range(4 , 1 , -1) :
        line_list.append_element(O.get_element_at(i))

    if turn_type == "prime" :

        instructions.append_element("R'")

        for i in range(9) :
            line_list.rotate_left()

    elif turn_type == "reg" :

        instructions.append_element("R")

        for i in range(3) :
            line_list.rotate_left()

    elif turn_type == "two" :

        instructions.append_element("R2")

        for i in range(6) :
            line_list.rotate_left()

    Y.change_val(0 , line_list.get_element_at(0))
    Y.change_val(7 , line_list.get_element_at(1))
    Y.change_val(6 , line_list.get_element_at(2))
    R.change_val(0 , line_list.get_element_at(3))
    R.change_val(7 , line_list.get_element_at(4))
    R.change_val(6 , line_list.get_element_at(5))
    W.change_val(0 , line_list.get_element_at(6))
    W.change_val(7 , line_list.get_element_at(7))
    W.change_val(6 , line_list.get_element_at(8))
    O.change_val(4 , line_list.get_element_at(9))
    O.change_val(3 , line_list.get_element_at(10))
    O.change_val(2 , line_list.get_element_at(11))

    if turn_type == "prime" :

        for i in range(6) :
            G.rotate_left()

    elif turn_type == "reg" :

        for i in range(2) :
            G.rotate_left()

    elif turn_type == "two" :

        for i in range(4) :
            G.rotate_left()

    return instructions

def left_turn(turn_type, instructions) :

    line_list = Linked_List()

    for i in range(4 , 1 , -1) :
        line_list.append_element(Y.get_element_at(i))

    line_list.append_element(O.get_element_at(0))
    line_list.append_element(O.get_element_at(7))
    line_list.append_element(O.get_element_at(6))

    for i in range(4 , 1 , -1) :
        line_list.append_element(W.get_element_at(i))

    for i in range(4 , 1 , -1) :
        line_list.append_element(R.get_element_at(i))

    if turn_type == "prime" :

        instructions.append_element("L'")

        for i in range(9) :
            line_list.rotate_left()

    elif turn_type == "reg" :

        instructions.append_element("L")

        for i in range(3) :
            line_list.rotate_left()

    elif turn_type == "two" :

        instructions.append_element("L2")

        for i in range(6) :
            line_list.rotate_left()

    Y.change_val(4 , line_list.get_element_at(0))
    Y.change_val(3 , line_list.get_element_at(1))
    Y.change_val(2 , line_list.get_element_at(2))
    O.change_val(0 , line_list.get_element_at(3))
    O.change_val(7 , line_list.get_element_at(4))
    O.change_val(6 , line_list.get_element_at(5))
    W.change_val(4 , line_list.get_element_at(6))
    W.change_val(3 , line_list.get_element_at(7))
    W.change_val(2 , line_list.get_element_at(8))
    R.change_val(4 , line_list.get_element_at(9))
    R.change_val(3 , line_list.get_element_at(10))
    R.change_val(2 , line_list.get_element_at(11))

    if turn_type == "prime" :

        for i in range(6) :
            B.rotate_left()

    elif turn_type == "reg" :

        for i in range(2) :
            B.rotate_left()

    elif turn_type == "two" :

        for i in range(4) :
            B.rotate_left()

    return instructions

def up_turn(turn_type, instructions) :

    line_list = Linked_List()

    for i in range(2 , -1 , -1) :
        line_list.append_element(O.get_element_at(i))

    for i in range(2 , -1 , -1) :
        line_list.append_element(B.get_element_at(i))

    for i in range(2 , -1 , -1) :
        line_list.append_element(R.get_element_at(i))

    for i in range(2 , -1 , -1) :
        line_list.append_element(G.get_element_at(i))

    if turn_type == "prime" :

        instructions.append_element("U'")

        for i in range(9) :
            line_list.rotate_left()

    elif turn_type == "reg" :

        instructions.append_element("U")

        for i in range(3) :
            line_list.rotate_left()

    elif turn_type == "two" :

        instructions.append_element("U2")

        for i in range(6) :
            line_list.rotate_left()

    O.change_val(2 , line_list.get_element_at(0))
    O.change_val(1 , line_list.get_element_at(1))
    O.change_val(0 , line_list.get_element_at(2))
    B.change_val(2 , line_list.get_element_at(3))
    B.change_val(1 , line_list.get_element_at(4))
    B.change_val(0 , line_list.get_element_at(5))
    R.change_val(2 , line_list.get_element_at(6))
    R.change_val(1 , line_list.get_element_at(7))
    R.change_val(0 , line_list.get_element_at(8))
    G.change_val(2 , line_list.get_element_at(9))
    G.change_val(1 , line_list.get_element_at(10))
    G.change_val(0 , line_list.get_element_at(11))

    if turn_type == "prime" :

        for i in range(6) :
            Y.rotate_left()

    elif turn_type == "reg" :

        for i in range(2) :
            Y.rotate_left()

    elif turn_type == "two" :

        for i in range(4) :
            Y.rotate_left()

    return instructions

def down_turn(turn_type, instructions) :

    line_list = Linked_List()

    for i in range(6 , 3 , -1) :
        line_list.append_element(R.get_element_at(i))

    for i in range(6 , 3 , -1) :
        line_list.append_element(B.get_element_at(i))

    for i in range(6 , 3 , -1) :
        line_list.append_element(O.get_element_at(i))

    for i in range(6 , 3 , -1) :
        line_list.append_element(G.get_element_at(i))

    if turn_type == "prime" :

        instructions.append_element("D'")

        for i in range(9) :
            line_list.rotate_left()

    elif turn_type == "reg" :

        instructions.append_element("D")

        for i in range(3) :
            line_list.rotate_left()

    elif turn_type == "two" :

        instructions.append_element("D2")

        for i in range(6) :
            line_list.rotate_left()

    R.change_val(6 , line_list.get_element_at(0))
    R.change_val(5 , line_list.get_element_at(1))
    R.change_val(4 , line_list.get_element_at(2))
    B.change_val(6 , line_list.get_element_at(3))
    B.change_val(5 , line_list.get_element_at(4))
    B.change_val(4 , line_list.get_element_at(5))
    O.change_val(6 , line_list.get_element_at(6))
    O.change_val(5 , line_list.get_element_at(7))
    O.change_val(4 , line_list.get_element_at(8))
    G.change_val(6 , line_list.get_element_at(9))
    G.change_val(5 , line_list.get_element_at(10))
    G.change_val(4 , line_list.get_element_at(11))

    if turn_type == "prime" :

        for i in range(6) :
            W.rotate_left()

    elif turn_type == "reg" :

        for i in range(2) :
            W.rotate_left()

    elif turn_type == "two" :

        for i in range(4) :
            W.rotate_left()

    return instructions

def front_turn(turn_type, instructions) :

    line_list = Linked_List()

    for i in range(6 , 3 , -1) :

        line_list.append_element(Y.get_element_at(i))

    line_list.append_element(B.get_element_at(0))
    line_list.append_element(B.get_element_at(7))
    line_list.append_element(B.get_element_at(6))

    for i in range(2 , -1 , -1) :
        line_list.append_element(W.get_element_at(i))

    for i in range(4 , 1 , -1) :
        line_list.append_element(G.get_element_at(i))

    if turn_type == "prime" :

        instructions.append_element("F'")

        for i in range(9) :
            line_list.rotate_left()

    elif turn_type == "reg" :

        instructions.append_element("F")

        for i in range(3) :
            line_list.rotate_left()

    elif turn_type == "two" :

        instructions.append_element("F2")

        for i in range(6) :
            line_list.rotate_left()

    Y.change_val(6 , line_list.get_element_at(0))
    Y.change_val(5 , line_list.get_element_at(1))
    Y.change_val(4 , line_list.get_element_at(2))
    B.change_val(0 , line_list.get_element_at(3))
    B.change_val(7 , line_list.get_element_at(4))
    B.change_val(6 , line_list.get_element_at(5))
    W.change_val(2 , line_list.get_element_at(6))
    W.change_val(1 , line_list.get_element_at(7))
    W.change_val(0 , line_list.get_element_at(8))
    G.change_val(4 , line_list.get_element_at(9))
    G.change_val(3 , line_list.get_element_at(10))
    G.change_val(2 , line_list.get_element_at(11))

    if turn_type == "prime" :

        for i in range(6) :
            R.rotate_left()

    elif turn_type == "reg" :

        for i in range(2) :
            R.rotate_left()

    elif turn_type == "two" :

        for i in range(4) :
            R.rotate_left()

    return instructions

def back_turn(turn_type, instructions) :

    line_list = Linked_List()

    for i in range(2 , -1 , -1) :

        line_list.append_element(Y.get_element_at(i))
    
    line_list.append_element(G.get_element_at(0))
    line_list.append_element(G.get_element_at(7))
    line_list.append_element(G.get_element_at(6))

    for i in range(6 , 3, -1) :
        line_list.append_element(W.get_element_at(i))

    for i in range(4 , 1 , -1) :
        line_list.append_element(B.get_element_at(i))

    if turn_type == "prime" :

        instructions.append_element("B'")

        for i in range(9) :
            line_list.rotate_left()

    elif turn_type == "reg" :

        instructions.append_element("B")

        for i in range(3) :
            line_list.rotate_left()

    elif turn_type == "two" :

        instructions.append_element("B2")

        for i in range(6) :
            line_list.rotate_left()

    Y.change_val(2 , line_list.get_element_at(0))
    Y.change_val(1 , line_list.get_element_at(1))
    Y.change_val(0 , line_list.get_element_at(2))
    G.change_val(0 , line_list.get_element_at(3))
    G.change_val(7 , line_list.get_element_at(4))
    G.change_val(6 , line_list.get_element_at(5))
    W.change_val(6 , line_list.get_element_at(6))
    W.change_val(5 , line_list.get_element_at(7))
    W.change_val(4 , line_list.get_element_at(8))
    B.change_val(4 , line_list.get_element_at(9))
    B.change_val(3 , line_list.get_element_at(10))
    B.change_val(2 , line_list.get_element_at(11))

    if turn_type == "prime" :

        for i in range(6) :
            O.rotate_left()

    elif turn_type == "reg" :

        for i in range(2) :
            O.rotate_left()

    elif turn_type == "two" :

        for i in range(4) :
            O.rotate_left()

    return instructions

def text_conv(val) :

    if val == 0 :
        return "Y"

    elif val == 1 :
        return "B"

    elif val == 2 :
        return "R"

    elif val == 3 :
        return "G"

    elif val == 4 :
        return "O"

    elif val == 5 :
        return "W"

#---------------------------------------------------------------------#

print("\nThis is a low-end, text-based Rubik's cube.\nIf you're reading this, you're probably me.\nIf you're not me, thanks for humoring me by looking at this.\n")
print("\nCurrent orientation:\n")
print("                                               ______________________   _______ _______ _______")
print("                                           ,.''",text_conv(Y.get_element_at(2))," .' ",text_conv(Y.get_element_at(1)),"  .' ",text_conv(Y.get_element_at(0)),"   .| |       |       |       |")
print("                                         .'_____._'_____.'______..'  | |       |       |       |")
print("                                     ,.' ",text_conv(Y.get_element_at(3)),"  .'  Y  .'  ",text_conv(Y.get_element_at(7))," ,' |    | |  ",text_conv(O.get_element_at(2)),"  |  ",text_conv(O.get_element_at(1)),"  |  ",text_conv(O.get_element_at(0)),"  |")
print("                                  ,.'------.'-----.-'-----.,'   | ",text_conv(G.get_element_at(0)),"| |       |       |       |")
print("                                ,'  ",text_conv(Y.get_element_at(4))," .'  ",text_conv(Y.get_element_at(5))," .' ",text_conv(Y.get_element_at(6)),"  ,' |    |    | |_______|_______|_______|")
print("     _______ _______ _______   ._______'_______'______'    | ",text_conv(G.get_element_at(1)),"|  ,'| |       |       |       |")
print("    |       |       |       | |       |       |       | ",text_conv(G.get_element_at(2)),"|   .|'   | |       |       |       |")
print("    |       |       |       | |       |       |       |    |.'  | ",text_conv(G.get_element_at(7)),"| |  ",text_conv(O.get_element_at(3)),"  |   O   |  ",text_conv(O.get_element_at(7)),"  |")
print("    |  ",text_conv(B.get_element_at(2)),"  |  ",text_conv(B.get_element_at(1)),"  |  ",text_conv(B.get_element_at(0)),"  | |  ",text_conv(R.get_element_at(2)),"  |  ",text_conv(R.get_element_at(1)),"  |  ",text_conv(R.get_element_at(0)),"  |   .|    |    | |       |       |       |")
print("    |       |       |       | |       |       |       |.'  |  G |   ,| |-------|-------|-------|")
print("    |-------|-------|-------| |-------|-------|-------|    |    |.'  | |       |       |       |")
print("    |       |       |       | |       |       |       | ",text_conv(G.get_element_at(3)),"|   .|    | |  ",text_conv(O.get_element_at(4)),"  |  ",text_conv(O.get_element_at(5)),"  |  ",text_conv(O.get_element_at(6)),"  |")
print("    |  ",text_conv(B.get_element_at(3)),"  |   B   |  ",text_conv(B.get_element_at(7)),"  | |  ",text_conv(R.get_element_at(3)),"  |   R   |  ",text_conv(R.get_element_at(7)),"  |    |.'  | ",text_conv(G.get_element_at(6)),"| |       |       |       |")
print("    |       |       |       | |       |       |       |   .|    |    | |_______|_______|_______|")
print("    |-------|-------|-------| |-------|-------|-------|.'  | ",text_conv(G.get_element_at(5)),"|   .'")
print("    |       |       |       | |       |       |       |    |    |.'")
print("    |  ",text_conv(B.get_element_at(4)),"  |  ",text_conv(B.get_element_at(5)),"  |  ",text_conv(B.get_element_at(6)),"  | |  ",text_conv(R.get_element_at(4)),"  |  ",text_conv(R.get_element_at(5)),"  |  ",text_conv(R.get_element_at(6)),"  | ",text_conv(G.get_element_at(4)),"|  .'")
print("    |       |       |       | |       |       |       |   ,'")
print("    |_______|_______|_______| |_______|_______|_______|.'  ")
print("                               _______ _______ _______")
print("                              |       |       |       |")
print("                              |       |       |       |")
print("                              |  ",text_conv(W.get_element_at(2)),"  |  ",text_conv(W.get_element_at(1)),"  |  ",text_conv(W.get_element_at(0)),"  |")
print("                              |       |       |       |")
print("                              |_______|_______|_______|")
print("                              |       |       |       |")
print("                              |       |       |       |")
print("                              |  ",text_conv(W.get_element_at(3)),"  |   W   |  ",text_conv(W.get_element_at(7)),"  |")
print("                              |       |       |       |")
print("                              |-------|-------|-------|")
print("                              |       |       |       |")
print("                              |  ",text_conv(W.get_element_at(4)),"  |  ",text_conv(W.get_element_at(5)),"  |  ",text_conv(W.get_element_at(6)),"  |")
print("                              |       |       |       |")
print("                              |_______|_______|_______|")
print("Move key:\n\nUppercase - clockwise\nLowercase - counterclockwise\n(move)2 - double turn\nF/f/f2 - front face\n\
B/b/b2 - back face\nU/u/u2 - up face\nD/d/d2 - down face\nL/l/l2 - left face\nR/r/r2 - right face")
move_cmd = str(input("\nEnter desired move or Q to quit: "))

instructions = Linked_List()

while move_cmd.lower() != "q" :

    if move_cmd == "R" :
        right_turn(r , instructions)
    elif move_cmd == "r" :
        right_turn(p , instructions)
    elif move_cmd == "R2" or move_cmd == "R2" :
        right_turn(t , instructions)

    if move_cmd == "L" :
        left_turn(r , instructions)
    elif move_cmd == "l" :
        left_turn(p , instructions)
    elif move_cmd == "L2" or move_cmd == "l2" :
        left_turn(t , instructions)

    if move_cmd == "F" :
        front_turn(r , instructions)
    elif move_cmd == "f" :
        front_turn(p , instructions)
    elif move_cmd == "f2" or move_cmd == "F2" :
        front_turn(t , instructions)

    if move_cmd == "B" :
        back_turn(r , instructions)
    elif move_cmd == "b" :
        back_turn(p , instructions)
    elif move_cmd == "b2" or move_cmd == "B2" :
        back_turn(t , instructions)

    if move_cmd == "U" :
        up_turn(r , instructions)
    elif move_cmd == "u" :
        up_turn(p , instructions)
    elif move_cmd == "U2" or move_cmd == "u2" :
        up_turn(t , instructions)

    if move_cmd == "D" :
        down_turn(r , instructions)
    elif move_cmd == "d" :
        down_turn(p , instructions)
    elif move_cmd == "d2" or move_cmd == "D2" :
        down_turn(t , instructions)

    print("\nCurrent orientation:\n")
    print("                                               ______________________   _______ _______ _______")
    print("                                           ,.''",text_conv(Y.get_element_at(2))," .' ",text_conv(Y.get_element_at(1)),"  .' ",text_conv(Y.get_element_at(0)),"   .| |       |       |       |")
    print("                                         .'_____._'_____.'______..'  | |       |       |       |")
    print("                                     ,.' ",text_conv(Y.get_element_at(3)),"  .'  Y  .'  ",text_conv(Y.get_element_at(7))," ,' |    | |  ",text_conv(O.get_element_at(2)),"  |  ",text_conv(O.get_element_at(1)),"  |  ",text_conv(O.get_element_at(0)),"  |")
    print("                                  ,.'------.'-----.-'-----.,'   | ",text_conv(G.get_element_at(0)),"| |       |       |       |")
    print("                                ,'  ",text_conv(Y.get_element_at(4))," .'  ",text_conv(Y.get_element_at(5))," .' ",text_conv(Y.get_element_at(6)),"  ,' |    |    | |_______|_______|_______|")
    print("     _______ _______ _______   ._______'_______'______'    | ",text_conv(G.get_element_at(1)),"|  ,'| |       |       |       |")
    print("    |       |       |       | |       |       |       | ",text_conv(G.get_element_at(2)),"|   .|'   | |       |       |       |")
    print("    |       |       |       | |       |       |       |    |.'  | ",text_conv(G.get_element_at(7)),"| |  ",text_conv(O.get_element_at(3)),"  |   O   |  ",text_conv(O.get_element_at(7)),"  |")
    print("    |  ",text_conv(B.get_element_at(2)),"  |  ",text_conv(B.get_element_at(1)),"  |  ",text_conv(B.get_element_at(0)),"  | |  ",text_conv(R.get_element_at(2)),"  |  ",text_conv(R.get_element_at(1)),"  |  ",text_conv(R.get_element_at(0)),"  |   .|    |    | |       |       |       |")
    print("    |       |       |       | |       |       |       |.'  |  G |   ,| |-------|-------|-------|")
    print("    |-------|-------|-------| |-------|-------|-------|    |    |.'  | |       |       |       |")
    print("    |       |       |       | |       |       |       | ",text_conv(G.get_element_at(3)),"|   .|    | |  ",text_conv(O.get_element_at(4)),"  |  ",text_conv(O.get_element_at(5)),"  |  ",text_conv(O.get_element_at(6)),"  |")
    print("    |  ",text_conv(B.get_element_at(3)),"  |   B   |  ",text_conv(B.get_element_at(7)),"  | |  ",text_conv(R.get_element_at(3)),"  |   R   |  ",text_conv(R.get_element_at(7)),"  |    |.'  | ",text_conv(G.get_element_at(6)),"| |       |       |       |")
    print("    |       |       |       | |       |       |       |   .|    |    | |_______|_______|_______|")
    print("    |-------|-------|-------| |-------|-------|-------|.'  | ",text_conv(G.get_element_at(5)),"|   .'")
    print("    |       |       |       | |       |       |       |    |    |.'")
    print("    |  ",text_conv(B.get_element_at(4)),"  |  ",text_conv(B.get_element_at(5)),"  |  ",text_conv(B.get_element_at(6)),"  | |  ",text_conv(R.get_element_at(4)),"  |  ",text_conv(R.get_element_at(5)),"  |  ",text_conv(R.get_element_at(6)),"  | ",text_conv(G.get_element_at(4)),"|  .'")
    print("    |       |       |       | |       |       |       |   ,'")
    print("    |_______|_______|_______| |_______|_______|_______|.'  ")
    print("                               _______ _______ _______")
    print("                              |       |       |       |")
    print("                              |       |       |       |")
    print("                              |  ",text_conv(W.get_element_at(2)),"  |  ",text_conv(W.get_element_at(1)),"  |  ",text_conv(W.get_element_at(0)),"  |")
    print("                              |       |       |       |")
    print("                              |_______|_______|_______|")
    print("                              |       |       |       |")
    print("                              |       |       |       |")
    print("                              |  ",text_conv(W.get_element_at(3)),"  |   W   |  ",text_conv(W.get_element_at(7)),"  |")
    print("                              |       |       |       |")
    print("                              |-------|-------|-------|")
    print("                              |       |       |       |")
    print("                              |  ",text_conv(W.get_element_at(4)),"  |  ",text_conv(W.get_element_at(5)),"  |  ",text_conv(W.get_element_at(6)),"  |")
    print("                              |       |       |       |")
    print("                              |_______|_______|_______|")
    move_cmd = str(input("\n\nEnter desired move or Q to quit: "))

