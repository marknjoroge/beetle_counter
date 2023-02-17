import random

def game():
    MAX_BODY = 1
    MAX_HEAD = 1
    MAX_ANTENNA = 2
    MAX_EYES = 2
    MAX_MOUTH = 1
    MAX_LEGS = 6

    ALL_PARTS_COUNT = MAX_BODY + MAX_HEAD + MAX_ANTENNA + MAX_EYES + MAX_MOUTH + MAX_LEGS

    body_count = 0
    head_count = 0
    antenna_count = 0
    eye_count = 0
    mouth_count = 0
    leg_count = 0

    beetle_complete = False
    collected_parts = 0

    print(
        """
        Welcome to beetle fantasy. 

        You are required to collect all the body parts 
        of a beetle to win the game.

        RULES
        _____

        i.   The game is played by rolling a dice. 
        ii.  Each face of the dice is associated with a beetle body part.
             1. Body             4. Eye
             2. Head             5. Mouth
             3. Antenna          6. Leg
        111. There maximum count associated with a body part is:
             Body       1        Eyes       2
             Head       1        Mouth      1
             Antennae   2        Legs       6
        iv.  You can not collect any other parts without having a body first.
        v.   You can not collect an antenna, eye, or mouth without having a head first.
        vi.  You can quit the game any time by pressing `q`.

        You may begin.
        """)

    while not (beetle_complete):
        user_input = input("Roll dice by pressing `ENTER` key. press `q` to quit.")
        if user_input == "q":
            break

        value = random.randint(1, 6)
        print("dice rolling...\n", value)

        if body_count < MAX_BODY:
            if value == 1:
                body_count += 1
                print("+1 body! (" + str(body_count) + "/" + str(MAX_BODY) + " bodies collected)")
            else:
                print("You can not collect any other parts without having a body first.")

        elif value == 6:
            if leg_count < MAX_LEGS:
                leg_count += 1
                print("+1 leg! (" + str(leg_count) + "/" + str(MAX_LEGS) + " legs collected)")
            else:
                print("No room for more legs.")

        elif head_count < MAX_HEAD:
            if value == 2:
                head_count += 1
                print("+1 head! (" + str(head_count) + "/" + str(MAX_HEAD) + " heads collected)")
            else:
                print("You can not collect an antenna, eye, or mouth without having a head first.")

        else:
            if value == 1:
                print("No room for more bodies")

            elif value == 2:
                print("No room for more heads")

            elif value == 3:
                if antenna_count < MAX_ANTENNA:
                    antenna_count += 1
                    print("+1 antenna! (" + str(antenna_count) + "/" + str(MAX_ANTENNA) + " antennae collected)")
                else:
                    print("No room for more antennae.")

            elif value == 4:
                if eye_count < MAX_EYES:
                    eye_count += 1
                    print("+1 eye! (" + str(eye_count) + "/" + str(MAX_EYES) + " eyes collected)")
                else:
                    print("No room for more eyes.")

            elif value == 5:
                if mouth_count < MAX_MOUTH:
                    mouth_count = 1
                    print("+1 mouth! (" + str(mouth_count) + "/" + str(MAX_MOUTH) + " mouths collected)")
                else:
                    print("No room for more mouth.")

        collected_parts = body_count + head_count + antenna_count + eye_count + mouth_count + leg_count
        print(str(collected_parts) + " parts collected. " + str(ALL_PARTS_COUNT - collected_parts) + " parts to go.\n\n")

        if body_count == MAX_BODY and head_count == MAX_HEAD and antenna_count == MAX_ANTENNA and eye_count == MAX_EYES and mouth_count == MAX_MOUTH and leg_count == MAX_LEGS:
            beetle_complete = True
            print("Congratulations, you have collected all body parts of the beetle!")

game()