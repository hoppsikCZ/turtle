import turtle_functions as tf
import turtle as t

t.setup(800, 600)

keep_going = True
while keep_going:
    t.reset()
    choice = t.numinput("Vyber možnost",
                        "1 - Náhodné čáry\n2 - Čtvercová spirála\n3 - Náhodné spirály\n4 - Klikání (nelze opustit)", 1,
                        1, 4)
    if choice == 1:
        tf.random_lines()
    elif choice == 2:
        tf.square_spiral()
    elif choice == 3:
        tf.random_spirals()
    elif choice == 4:
        t.onscreenclick(tf.go_to_click)
        t.mainloop()
        break
    else:
        print("Neplatná možnost")

    keep_going = False
    exit_choice = t.textinput("Chceš pokračovat?", "(ano/NE)")
    if exit_choice is not None:
        if exit_choice.lower() == "ano" or exit_choice.lower() == "a":
            keep_going = True
