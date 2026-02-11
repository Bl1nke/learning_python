while True:
    user_points_input = input("Enter your input:  ")
    try:
        int_user_points = int(user_points_input)
        if int_user_points >= 90 and int_user_points <= 100:
            print("Your mark is: A")
        elif int_user_points >= 80 and int_user_points <= 89:    
            print("Your mark is: B")
        elif int_user_points >= 70 and int_user_points <= 79:    
            print("Your mark is: C")
        elif int_user_points >= 60 and int_user_points <= 69:    
            print("Your mark is: D")
        elif int_user_points < 60 and int_user_points >= 0:    
            print("Your mark is: F")
        else:
            print("You can't have this number of points")   
            continue


        break

    except ValueError:
        print("Your Enter is wrong")