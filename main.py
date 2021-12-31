import turtle

my_pen = turtle.Turtle()
tut = turtle.Screen() 
tut.bgcolor("black") 
tut.title("Miller Indices Representer") 
my_pen.speed(3)

def cube():
    my_pen.color("white")

    for i in range(4):
        my_pen.pendown()
        my_pen.forward(100)
        my_pen.left(90)

    my_pen.home()
    my_pen.penup()
    my_pen.goto(50, -50)
    my_pen.pendown()

    for i in range(4):
        my_pen.pendown()
        my_pen.forward(100)
        my_pen.left(90)

    my_pen.goto(0, 0)
    my_pen.goto(0, 100)
    my_pen.goto(50, 50)
    my_pen.goto(150, 50)
    my_pen.goto(100, 100)
    my_pen.goto(100, 0)
    my_pen.goto(150, -50)



def Positive_Axis():

    # X-axis
    my_pen.color("green", "green")
    my_pen.penup()
    my_pen.goto(100, 0)
    my_pen.pendown()
    my_pen.goto(180, 0)
    my_pen.begin_fill()
    my_pen.goto(170, 7)
    my_pen.goto(170, -7)
    my_pen.goto(180, 0)
    my_pen.end_fill()
    my_pen.write("x-axis", False, font=("Arial", 15, "bold"))
    my_pen.penup()

    # Y-axis
    my_pen.goto(0, 100)
    my_pen.pendown()
    my_pen.goto(0, 170)
    my_pen.begin_fill()
    my_pen.goto(-7, 160)
    my_pen.goto(7, 160)
    my_pen.goto(0, 170)
    my_pen.end_fill()
    my_pen.write("y-axis", False, font=("Arial", 15, "bold"))
    my_pen.penup()

    # Z-axis 
    my_pen.goto(50, -50)
    my_pen.pendown()
    my_pen.goto(85, -85)
    my_pen.begin_fill()
    my_pen.goto(72, -80)
    my_pen.goto(87, -80)
    my_pen.goto(85, -85)
    my_pen.end_fill()
    my_pen.penup()
    my_pen.goto(90, -80)
    my_pen.write("z-axis", True, font=("Arial", 15, "bold"))

    # origin
    my_pen.penup()
    my_pen.goto(-5, -10)
    my_pen.write("O", align="right", font=("Arial", 15, "bold"))
    

def Plot(x, y, z, negative):

    miller_indices = [x, y, z]
    
    if miller_indices.count(0) == 0:        # (111) & (-1-1-1)

        if negative == True:           
            
            # X-axis
            my_pen.color("green", "green")
            my_pen.penup()
            my_pen.goto(50, 50)
            my_pen.pendown()
            my_pen.goto(-25, 50)
            my_pen.begin_fill()
            my_pen.goto(-25,55)
            my_pen.goto(-30,50)
            my_pen.goto(-25,45)
            my_pen.end_fill()
            my_pen.penup()
            my_pen.goto(-70,50)
            my_pen.write("x̄ axis", True, align="left", font=("Arial", 15, "bold"))
            # Y-axis
            my_pen.penup()
            my_pen.goto(150, -50)
            my_pen.pendown()
            my_pen.goto(150, -100)
            my_pen.begin_fill()
            my_pen.goto(145,-100)
            my_pen.goto(150,-105)
            my_pen.goto(155,-100)
            my_pen.end_fill()
            my_pen.write("ȳ-axis", False, font=("Arial", 15, "bold"))
            # Z-axis
            my_pen.penup()
            my_pen.goto(100, 100)
            my_pen.pendown()
            my_pen.goto(65, 135)
            my_pen.begin_fill()
            my_pen.goto(58,135)
            my_pen.goto(62,142)
            my_pen.goto(72,137)
            my_pen.end_fill()
            my_pen.write("z̄-axis", False, font=("Arial", 15, "bold"))
            
            #showing origin
            my_pen.penup()
            my_pen.goto(150, 50)
            my_pen.write("O", False, font=("Arial", 15, "bold"))

            my_pen.color("blue")
            my_pen.penup()
            my_pen.goto(150-(100/x), 50)         # >> x
            my_pen.pendown()
            my_pen.goto(150, 50-(100/y))         # >> y
            my_pen.goto(150-(50/z), 50+(50/z))        # >> z
            my_pen.goto(150-(100/x), 50)

            
        else:

            Positive_Axis()

            my_pen.color("blue")
            my_pen.penup()
            my_pen.goto(100/x, 0)         # >> x
            my_pen.pendown()
            my_pen.goto(0, 100/y)         # >> y
            my_pen.goto(50/z, -50/z)        # >> z
            my_pen.goto(100/x, 0)

    elif miller_indices.count(0) == 1:

        if miller_indices.index(0) == 1:        #(101) & (-10-1)
            
            if negative == True:                

                my_pen.color("green", "green")
                my_pen.penup()
                my_pen.goto(50, -50)
                my_pen.pendown()
                my_pen.goto(-15, -50)
                my_pen.begin_fill()
                my_pen.goto(-15,-43)
                my_pen.goto(-22,-50)
                my_pen.goto(-15,-57)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(-30,-40)
                my_pen.write("x̄-axis", align="left",font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(150, 50)
                my_pen.pendown()
                my_pen.goto(150, 110)
                my_pen.begin_fill()
                my_pen.goto(143,110)
                my_pen.goto(150,117)
                my_pen.goto(157,110)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(170,120)
                my_pen.write("y-axis", False, font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(100, 0)
                my_pen.pendown()
                my_pen.goto(65, 35)
                my_pen.begin_fill()
                my_pen.goto(72,35)
                my_pen.goto(61,42)
                my_pen.goto(58,31)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(10,40)
                my_pen.write("z̄-axis", False, font=("Arial", 10, "bold"))


                # Drawing origin
                my_pen.penup()
                my_pen.goto(155, -50)
                my_pen.write("O", False, font=("Arial", 15, "bold"))
    

                my_pen.color("orange")          
                my_pen.penup()
                my_pen.goto(150-(50/z), 50+(50/z))
                my_pen.pendown()
                my_pen.goto(150-(100/x), 50)
                my_pen.goto(150-(100/x), -50)
                my_pen.goto(150-(50/z), -(50-(50/z)))
                my_pen.goto(150-(50/z), 50+(50/z))
                
            else:
                
                Positive_Axis()
                my_pen.color("orange")          
                my_pen.penup()
                my_pen.goto(100/x, 0)
                my_pen.pendown()
                my_pen.goto(50/z, -50/z)
                my_pen.goto(50/z, 100-(50/z))
                my_pen.goto(100/x, 100)
                my_pen.goto(100/x, 0)

        elif miller_indices.index(0) == 0:          # (011) & (0-1-1)
            
            if negative == True:
                
                my_pen.color("green", "green")                           # (011)
                my_pen.penup()
                my_pen.goto(150, 50)
                my_pen.pendown()
                my_pen.goto(185, 50)
                my_pen.begin_fill()
                my_pen.goto(185,57)
                my_pen.goto(192,50)
                my_pen.goto(185,43)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(210,70)
                my_pen.write("x-axis", False, align="right", font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(50, -50)
                my_pen.pendown()
                my_pen.goto(50,-85)
                my_pen.begin_fill()
                my_pen.goto(57,-85)
                my_pen.goto(50,-92)
                my_pen.goto(43,-85)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(65,-95)
                my_pen.write("ȳ-axis", False, font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(0, 100)
                my_pen.pendown()
                my_pen.goto(-35, 135)
                my_pen.begin_fill()
                my_pen.goto(-42,135)
                my_pen.goto(-35,142)
                my_pen.goto(-25,135)
                my_pen.end_fill()
                my_pen.write("z̄-axis", False, font=("Arial", 15, "bold"))


                my_pen.penup()
                my_pen.goto(50, 50)
                my_pen.write("O", False, font=("Arial", 15, "bold"))

                my_pen.color("orange")
                my_pen.penup()
                my_pen.goto(50-(50/z), 50+(50/z))
                my_pen.pendown()
                my_pen.goto(150-(50/z), 50+(50/z))
                my_pen.goto(100+(50/y), -50/y)
                my_pen.goto(50/y, -50/y)
                my_pen.goto(50-(50/z), 50+(50/z))

            else:

                Positive_Axis()
                my_pen.color("orange")
                my_pen.penup()
                my_pen.goto(0, 100/y)
                my_pen.pendown()
                my_pen.goto(100, 100/y)
                my_pen.goto(100+(50/z), -50/z)
                my_pen.goto(50/z, -50/z)
                my_pen.goto(0, 100/y)

        else:                                       # (110) & (-1-10)
            
            if negative == True:
                
                
                my_pen.color("green", "green")
                my_pen.penup()
                my_pen.goto(0, 100)
                my_pen.pendown()
                my_pen.goto(-35, 100)
                my_pen.begin_fill()
                my_pen.goto(-35,107)
                my_pen.goto(-42,100)
                my_pen.goto(-35,93)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(-35,110)
                my_pen.write("x̄ axis", False, align="right", font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(100, 0)
                my_pen.pendown()
                my_pen.goto(100, -70)
                my_pen.begin_fill()
                my_pen.goto(93,-70)
                my_pen.goto(100,-77)
                my_pen.goto(107,-70)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(110,-90)
                my_pen.write("ȳ-axis", False, font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(150, 50)
                my_pen.pendown()
                my_pen.goto(185, 15)
                my_pen.begin_fill()
                my_pen.goto(192,19)
                my_pen.goto(189,8)
                my_pen.goto(178,11)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(200,15)
                my_pen.write("z-axis", False, font=("Arial", 15, "bold"))
                

                my_pen.penup()
                my_pen.goto(100, 100)
                my_pen.write("O", False, font=("Arial", 15, "bold"))


                my_pen.color("orange")
                my_pen.penup()
                my_pen.goto(100-(100/x), 100)
                my_pen.pendown()
                my_pen.goto(150-(100/x), 50)
                my_pen.goto(150, 50-(100/y))
                my_pen.goto(100, 100-(100/y))
                my_pen.goto(100-(100/x), 100)

            else:

                Positive_Axis()
                my_pen.color("orange")
                my_pen.penup()
                my_pen.goto(0, 100/y)
                my_pen.pendown()
                my_pen.goto(50, (100/y)-50)
                my_pen.goto((100/x)+50, -50)
                my_pen.goto(100/x, 0)
                my_pen.goto(0, 100/y)

    else:

        if miller_indices[0] != 0:      #(100) & (-100)

            if negative == True:        
                
                # X-axis
                my_pen.color("green", "green")
                my_pen.penup()
                my_pen.goto(0, 0)
                my_pen.pendown()
                my_pen.goto(-40, 0)
                my_pen.begin_fill()
                my_pen.goto(-30, 7)
                my_pen.goto(-30, -7)
                my_pen.goto(-40, 0)
                my_pen.end_fill()
                my_pen.write("x̄-axis", align="right", font=("Arial", 15, "bold"))
                my_pen.penup()

                # Y-axis
                my_pen.goto(100, 100)
                my_pen.pendown()
                my_pen.goto(100, 170)
                my_pen.begin_fill()
                my_pen.goto(93, 160)
                my_pen.goto(107, 160)
                my_pen.goto(100, 170)
                my_pen.end_fill()
                my_pen.write("y-axis", False, font=("Arial", 15, "bold"))
                my_pen.penup()

                # Z-axis 
                my_pen.goto(150, -50)
                my_pen.pendown()
                my_pen.goto(190, -90)
                my_pen.begin_fill()
                my_pen.goto(180, -90)
                my_pen.goto(190, -80)
                my_pen.goto(190, -90)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(200, -90)
                my_pen.write("z-axis",align="left", font=("Arial", 15, "bold"))

                my_pen.penup()
                my_pen.goto(105, 0)
                my_pen.write("O", False, font=("Arial", 15, "bold"))

                my_pen.color("red")
                my_pen.penup()
                my_pen.goto(100-(100/x), 0)
                my_pen.pendown()
                my_pen.goto(100-(100/x), 100)
                my_pen.goto(150-(100/x), 50)
                my_pen.goto(150-(100/x), -50)
                my_pen.goto(100-(100/x), 0)

            else:

                Positive_Axis()
                my_pen.color("red")
                my_pen.penup()
                my_pen.goto(100/x, 0)
                my_pen.pendown()
                my_pen.goto(100/x, 100)
                my_pen.goto(50+(100/x), 50)
                my_pen.goto(50+(100/x), -50)
                my_pen.goto(100/x, 0)

        elif miller_indices[1] != 0:          # (010) & (0-10)
            
            if negative == True:        
                
                # X-axis
                my_pen.color("green", "green")
                my_pen.penup()
                my_pen.goto(100, 100)
                my_pen.pendown()
                my_pen.goto(130, 100)
                my_pen.begin_fill()
                my_pen.goto(120, 107)
                my_pen.goto(120, 93)
                my_pen.goto(130, 100)
                my_pen.end_fill()
                my_pen.write("x-axis", font=("Arial", 15, "bold"))
                my_pen.penup()

                # Y-axis
                my_pen.goto(0, 0)
                my_pen.pendown()
                my_pen.goto(0, -30)
                my_pen.begin_fill()
                my_pen.goto(-7, -20)
                my_pen.goto(7, -20)
                my_pen.goto(0, -30)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(0, -40)
                my_pen.write("ȳ-axis", align="right", font=("Arial", 15, "bold"))
                my_pen.penup()

                # Z-axis 
                my_pen.goto(50, 50)
                my_pen.pendown()
                my_pen.goto(70, 35)
                my_pen.begin_fill()
                my_pen.goto(63, 35)
                my_pen.goto(70, 43)
                my_pen.goto(70, 35)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.goto(80, 20)
                my_pen.write("z-axis", True, font=("Arial", 15, "bold"))
                my_pen.penup()

                my_pen.penup()
                my_pen.goto(-5, 100)
                my_pen.write("O", align="right", font=("Arial", 15, "bold"))

                my_pen.color("red")
                my_pen.penup()
                my_pen.goto(0, 100-(100/y))
                my_pen.pendown()
                my_pen.goto(100, 100-(100/y))
                my_pen.goto(150, 50-(100/y))
                my_pen.goto(50, 50-(100/y))
                my_pen.goto(0, 100-(100/y))

            else:
            
                Positive_Axis()
                my_pen.color("red")
                my_pen.penup()
                my_pen.goto(0, 100/y)
                my_pen.pendown()
                my_pen.goto(100, 100/y)
                my_pen.goto(150, (100/y)-50)
                my_pen.goto(50, (100/y)-50)
                my_pen.goto(0, 100/y)

        else:                                       # (001) & (00-1)
            
            if negative==True:

                # X-axis
                my_pen.color("green", "green")
                my_pen.penup()
                my_pen.goto(150, -50)
                my_pen.pendown()
                my_pen.goto(180, -50)
                my_pen.begin_fill()
                my_pen.goto(170, -43)
                my_pen.goto(170, -57)
                my_pen.goto(180, -50)
                my_pen.end_fill()
                my_pen.write("x-axis", align="left", font=("Arial", 15, "bold"))
                my_pen.penup()

                #Y-axis
                my_pen.goto(50, 50)
                my_pen.pendown()
                my_pen.goto(50, 130)
                my_pen.begin_fill()
                my_pen.goto(43, 120)
                my_pen.goto(57, 120)
                my_pen.goto(50, 130)
                my_pen.end_fill()
                my_pen.write("y-axis", False, font=("Arial", 15, "bold"))
                my_pen.penup()

                # Z-axis 
                my_pen.goto(0, 0)
                my_pen.pendown()
                my_pen.goto(-25, 25)
                my_pen.begin_fill()
                my_pen.goto(-25, 15)
                my_pen.goto(-15, 25)
                my_pen.goto(-25, 25)
                my_pen.end_fill()
                my_pen.penup()
                my_pen.write("z̄-axis", align="right", font=("Arial", 15, "bold"))

                #showing origin
                my_pen.penup()
                my_pen.goto(50, -60)
                my_pen.write("O", align="right", font=("Arial", 15, "bold"))

                my_pen.color("red")
                my_pen.penup()
                my_pen.goto(50-(50/z), -50+(50/z))
                my_pen.pendown()
                my_pen.goto(150-(50/z), -50+(50/z))
                my_pen.goto(150-(50/z), 50+(50/z))
                my_pen.goto(50-(50/z), 50+(50/z))
                my_pen.goto(50-(50/z), -50+(50/z))

            else:

                Positive_Axis()
                my_pen.color("red")
                my_pen.penup()
                my_pen.goto(50/z, -50/z)
                my_pen.pendown()
                my_pen.goto(100+(50/z), -50/z)
                my_pen.goto(100+(50/z), 100-(50/z))
                my_pen.goto(50/z, 100-(50/z))
                my_pen.goto(50/z, -50/z)

    my_pen.hideturtle()



def clear():
    my_pen.clear()
    my_pen.penup()
    my_pen.home()




# while True:

#     try:

#         x = int(input("Provide the x intercept: "))
#         y = int(input("Provide the y intercept: "))
#         z = int(input("Provide the z intercept: "))
#         print("\n")
#     except:
#         print("The input was invalid so Good Bye :)")
#         break

#     negative = True
    

#     if abs(x)==x:
#         if abs(y)==y:
#             if abs(z)==z:
#                 negative = False

#     clear()
#     cube()
#     # Positive_Axis()
#     Plot(abs(x), abs(y), abs(z))