print("Welcome Head Tail Game.")
print("What you want to choice Head or Tail for head write h for tail write tail.")
import random

a = ['h', 't']
b = random.choice(a)
c = input("Write Here:")
if c == b:
    print("You win.")
    bat_ball = input("Bat or Ball:")
    if bat_ball == 'bat':
        d = 0
        bat_run = 0
        while 6 > d:
            bat = int(input("Bat here:"))
            if bat > 6:
                print("Input your nuber in 6 ")
            import random

            e = [1, 2, 3, 4, 5, 6]
            f = random.choice(e)
            if f == bat:
                print("out")
                print(bat_run)
                e = 0
                com_run = 0
                while e > 6:

                    a4 = [1, 2, 3, 4, 5, 6, ]
                    a5 = random.choice(a4)
                    a6 = int(input('ball here:'))
                    if a5 == a6:
                        print("computer out")
                        print(com_run)
                    else:
                        com_run = com_run + a5

                    print("compuet take ", a5)
                    print("total run is", com_run)
                    e = e + 1
                    if e == 6:
                        d = 0
                        bat_run = 0
                        while 6 > d:
                            bat = int(input("Bat here:"))
                            if bat > 6:
                                print("Input your nuber in 6 ")
                            import random

                            e = [1, 2, 3, 4, 5, 6]
                            f = random.choice(e)
                            if f == bat:
                                print("out")


            else:
                bat_run = bat_run + bat
                d = d + 1
                print(bat_run)

            else:
            bat_run = bat_run + bat
        d = d + 1
        print("total run is:", bat_run)
        print("Computer give", f)
    if d == 6:
        d = 0
        bat_run = 0
        while 6 > d:
            bat = int(input("Bat here:"))
            if bat > 6:
                print("Input your nuber in 6 ")
            import random

            e = [1, 2, 3, 4, 5, 6]
            f = random.choice(e)
            if f == bat:
                print("out")
                break

            else:
                bat_run = bat_run + bat
            d = d + 1
            print(bat_run)




else:
    print("You lost")
import random

a1 = ['bat', 'ball']
a2 = random.choice(a1)
print("computer want to ", a2)
if a2 == 'ball':
    d = 0
    bat_run = 0
    while 6 > d:
        bat = int(input("Bat here:"))
        if bat > 6:
            print("Input your nuber in 6 ")
        import random

        e = [1, 2, 3, 4, 5, 6]
        f = random.choice(e)
        if f == bat:
            print("out")
            break

        else:
            bat_run = bat_run + bat
        d = d + 1
        print(bat_run)

if a2 == 'bat':
    e = 0
    com_run = 0
    while e > 6:

        a4 = [1, 2, 3, 4, 5, 6, ]
        a5 = random.choice(a4)
        a6 = int(input('ball here:'))
        if a5 == a6:
            print("computer out")
            print(com_run)
        else:
            com_run = com_run + a5

        print("compuet take ", a5)
        print("total run is", com_run)
        e = e + 1
        if e == 6:
            d = 0
            bat_run = 0
            while 6 > d:
                bat = int(input("Bat here:"))
                if bat > 6:
                    print("Input your nuber in 6 ")
                import random

                e = [1, 2, 3, 4, 5, 6]
                f = random.choice(e)
                if f == bat:
                    print("out")
                    break

                else:
                    bat_run = bat_run + bat
                d = d + 1
                print(bat_run)







