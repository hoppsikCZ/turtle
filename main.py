import turtle_functions as tf
import turtle as t

t.setup(800, 600)

keep_going = True
while keep_going:
    t.reset()
    choice = t.numinput("Vyber možnost", "1 - Náhodné čáry\n2 - Čtvercová spirála\n3 - Klikání\n4 - D", 1, 1, 4)
    if choice == 1:
        tf.random_lines()
    elif choice == 2:
        tf.square_spiral()
    elif choice == 3:
        tf.random_spirals()
    elif choice == 4:
        print("D")
    else:
        print("Neplatná možnost")

    exit_choice = t.textinput("Chceš pokračovat?", "(ano/ne)")
    if exit_choice.lower() == "ne" or exit_choice.lower() == "n":
        keep_going = False
