win_no = 56
user_input = int(input("Guess the no between 1 to 100 \n"))
if user_input == win_no:
    {
        print("YOU WIN!!")
    }
else: #Nested 'IF_ELSE'
    if user_input < win_no:
        {
            print("TOO LOW")
        }    
    else:
        {
            print("TOO HIGH")
        }    