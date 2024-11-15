def physics_operation_menu():

        print('\nPhysics Operation Menu:')
        print('a. Calculate the area of a rectangle')
        print('b. Calculate the perimeter of a square')
        print('c. Calculate the force applied on a body')
        print('d. Calculate the potential energy on a body')
        print('e. Calculate the surface tension a body')
        print('f. Quit')

option = "a"

while option != "f":
    physics_operation_menu()
    option = input('Choose an option (a-f): ')
    if option == 'a':

        print('Calculating the area of a rectangle')
        breath = int(input('Enter Breath of the rectangle: '))
        length = int(input('Enter length of the rectangle: '))
        area = breath * length
        print('The area of the rectangle is:', area)


    elif option == 'b':
        print('Calculating the perimeter of a square')
        breath_or_length = int(input('Enter breath or length of the square: '))
        perimeter = 4 * breath_or_length
        print('The perimeter of the square is: ', perimeter)

    elif option == 'c':
        print('Calculating the force on a body')
        mass = int(input('Enter mass of the body: '))
        acceleration = int(input('Enter acceleration of the body: '))
        force = mass * acceleration
        print('The force applied on the body is: ', force)

    elif option == 'd':
        print('Calculating the area of a rectangle')
        mass = int(input('Enter mass of the body: '))
        height = int(input('Enter height of the body: '))
        potential_energy = mass * height * 9.8
        print('The potential energy of the body is: ', potential_energy)

    elif option == 'e':
        print('Calculating the surface tension')
        force = int(input('Enter force on the body: '))
        length = int(input('Enter length of the body: '))
        surface_tension = force * length
        print('The surface tension on the body is:', surface_tension)

    elif option == 'f':
        print('THANK YOU AND GOODBYE')


    else:
        print('Invalid Option, please pick an option again')




