from tkinter import *
from utils.utils import *
from connection.database_connection import create_connection


# Function That Creates Log In Screen
def create_login_window():
    # Creating Window for the Login Screen
    login_window = Tk()
    # Defining Screen Title
    login_window.title('Login')
    # Defining Background Screen Color
    login_window.configure(bg='#2B2B2B')

    # Defining Width And Height Of The Window:
    login_window_width = 400
    login_window_height = 225
    # Obtaining Computer Screen Size:
    computer_width = login_window.winfo_screenwidth()
    computer_height = login_window.winfo_screenheight()
    # Calculating Coordinates To Position The Interface In The Center Of The Computer Screen:
    login_window_position_x = (computer_width // 2) - (login_window_width // 2)
    login_window_position_y = (computer_height // 2) - (login_window_height // 2)
    # Positioning Interface In The Center Of The Computer Screen:
    login_window.geometry(f'{login_window_width}x{login_window_height}+{login_window_position_x}+'
                          f'{login_window_position_y}')

    # Creating Screen Labels
    # Title Label
    title_label = Label(login_window, text='Login Screen', font='Poppins 16', fg='#BBBBBB', bg='#2B2B2B')
    title_label.grid(row=0, column=0, columnspan=4, pady=10)

    # Username Label
    username_label = Label(login_window, text='Username:', font='Poppins 12 bold', fg='#BBBBBB', bg='#2B2B2B')
    username_label.grid(row=1, column=1, stick='we', padx=(20, 0), pady=10)

    # Password Label
    password_label = Label(login_window, text='Password:', font='Poppins 12 bold', fg='#BBBBBB', bg='#2B2B2B')
    password_label.grid(row=2, column=1, stick='we', padx=(20, 0), pady=10)

    # Defining Images Icon For The Register Product (32px)
    user_icon = PhotoImage(file='../images/user_icon.png')
    password_icon = PhotoImage(file='../images/password_icon.png')

    # Putting The Images In The Interface
    # Product Icon
    product_icon_label = Label(login_window, image=user_icon, bg='#2B2B2B')
    product_icon_label.photo = user_icon
    product_icon_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky='w')
    # Price Icon
    price_icon_label = Label(login_window, image=password_icon, bg='#2B2B2B')
    price_icon_label.photo = password_icon
    price_icon_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky='w')

    # Creating Screen Entries
    # Username Entry
    username_entry = Entry(login_window, font='Poppins 12')
    username_entry.grid(row=1, column=3, padx=(15, 25), sticky='e')

    # Password Entry
    password_entry = Entry(login_window, font='Poppins 12', show='•')
    password_entry.grid(row=2, column=3, padx=(15, 25), sticky='e')

    # Creating Screen Buttons
    # Exit Button
    exit_button = Button(login_window, bg='#3C3F41', text='Exit', font='Poppins 12 bold', fg='#BBBBBB',
                         width=15, command=login_window.destroy)
    exit_button.grid(row=4, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    # Continue Button
    continue_button = Button(login_window, bg='#3C3F41', text='Continue', font='Poppins 12 bold', fg='#BBBBBB',
                             width=15, command=lambda: verify_credentials(login_window, username_entry.get(),
                                                                          password_entry.get()))
    continue_button.grid(row=4, column=2, columnspan=4, padx=(0, 25), pady=10, sticky='e')

    # Starting Screen
    login_window.mainloop()


# Function That Verifies If User's Credentials Are Correct
def verify_credentials(login_window, username, password):
    # Getting Database Connection
    with create_connection() as connection:
        # Creating a Cursor To Make Query
        with connection.cursor() as cursor:
            # Executing Query From The Cursor
            cursor.execute(f'''SELECT * 
                               FROM User
                               WHERE name = '{username}'        
                               AND password = '{password}' ''')
            # Storing Query Return
            user = cursor.fetchone()
            # Conferring If The Credentials Inserted Are Registered
            if user:
                # Destroying Login Window
                login_window.destroy()
                create_main_window()
                # Database Connection And Cursor Safely Closed
            else:
                # Creating A Warning In The Login Window Of Wrong Credentials
                warning_label = Label(login_window, text='Username Or Password Is Incorrect', font='Poppins 12 bold',
                                      fg='#A94228', bg='#2B2B2B')
                warning_label.grid(row=3, column=0, columnspan=4, pady=0, sticky='we')
                # Database Connection And Cursor Safely Closed


# Function That Creates Product Register Screen
def create_main_window():
    # Creating Window For The Main Screen
    main_window = Tk()
    # Defining Screen Title
    main_window.title('Main Menu')
    # Defining Background Screen Color
    main_window.configure(bg='#2B2B2B')
    # Defining Fullness For The Screen
    ##################main_window.attributes('-fullscreen', True)

    # Configuring The Screen To Contain A Menu Bar
    menu_bar = Menu(main_window)
    main_window.configure(menu=menu_bar)

    # Creating A Menu Named 'Files'
    menu_file = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Files', menu=menu_file)

    # Implementing The Menu With The Register Functionality
    menu_file.add_command(label='Register', command=lambda: register_products(main_window))

    # Implementing The Menu With The Exit Functionality
    menu_file.add_command(label='Exit', command=main_window.destroy)

    # Starting Screen
    main_window.mainloop()


# Function To Register New Products In The Database
def product_data_register(product_register_window, product_name, product_price, product_description):
    # Getting Database Connection
    with create_connection() as connection:
        # Creating a Cursor To Make Query
        with connection.cursor() as cursor:
            # Creating A Data Treatment
            if product_name == '' or product_price == '':
                if product_name == '':
                    # Creating A Warning In The Product Register Window Of Empty Name Field
                    warning_label = Label(product_register_window, text='Please Insert Product Name!',
                                          font='Poppins 12 bold', fg='#A94228', bg='#2B2B2B')
                    warning_label.grid(row=4, column=0, columnspan=4, pady=0, sticky='we')
                else:
                    # Creating A Warning In The Product Register Window Of Empty Price Field
                    warning_label = Label(product_register_window, text='Please Insert Product Price!',
                                          font='Poppins 12 bold', fg='#A94228', bg='#2B2B2B')
                    warning_label.grid(row=4, column=0, columnspan=4, pady=0, sticky='we')
            else:
                # Capitalizing Product Name
                product_name = product_name.capitalize()
                # Transforming Data Price To Float Type
                product_price = float(product_price)

                # Executing Query From The Cursor
                cursor.execute(f'''SELECT * 
                                   FROM Product
                                   WHERE name = '{product_name}' ''')
                # Storing Query Return
                product = cursor.fetchone()
                if product:
                    # Creating A Warning In The Product Register Window Of Duplicated Data
                    warning_label = Label(product_register_window, text='This Data Is Already Registered',
                                          font='Poppins 12 bold', fg='#A94228', bg='#2B2B2B')
                    warning_label.grid(row=4, column=0, columnspan=4, pady=0, sticky='we')
                    # Database Connection And Cursor Safely Closed
                else:
                    print(product_price)
                    print(product_name)
                    # Creating A Warning In The Product Register Window Of Successfully Register
                    cursor.execute(f'''INSERT INTO Product(Name, Description, Price)
                                       VALUES ('{product_name}', '{product_description}', {product_price})''')
                    connection.commit()
                    warning_label = Label(product_register_window, text='Data Successfully Registered',
                                          font='Poppins 12 bold', fg='#697E47', bg='#2B2B2B')
                    warning_label.grid(row=4, column=0, columnspan=4, pady=0, sticky='we')
                    # Closing The Cursor And The Connection With The Database


def register_products(main_window):
    # Creating Window For The Main Screen That Overlaps Main Window
    product_register_window = Toplevel(main_window)
    # Defining Screen Title
    product_register_window.title('Register Products')
    # Defining Background Screen Color
    product_register_window.configure(bg='#2B2B2B')

    # Defining Width And Height Of The Window:
    product_register_window_width = 400
    product_register_window_height = 275
    # Obtaining Computer Screen Size:
    computer_width = product_register_window.winfo_screenwidth()
    computer_height = product_register_window.winfo_screenheight()
    # Calculating Coordinates To Position The Interface In The Center Of The Computer Screen:
    product_register_window_position_x = (computer_width // 2) - (product_register_window_width // 2)
    product_register_window_position_y = (computer_height // 2) - (product_register_window_height // 2)
    # Positioning Interface In The Center Of The Computer Screen:
    product_register_window.geometry(f'{product_register_window_width}x{product_register_window_height}+'
                                     f'{product_register_window_position_x}+{product_register_window_position_y}')

    # Creating Screen Labels
    # Title Label
    title_label = Label(product_register_window, text='Product Register', font='Poppins 16', fg='#BBBBBB', bg='#2B2B2B')
    title_label.grid(row=0, column=0, columnspan=5, pady=10, sticky='we')
    # Product Name Label
    product_name_label = Label(product_register_window, text='Name:', font='Poppins 12 bold', fg='#BBBBBB',
                               bg='#2B2B2B')
    product_name_label.grid(row=1, column=1, stick='we', pady=10)

    # Product Price Label
    product_price_label = Label(product_register_window, text='Price: ', font='Poppins 12 bold', fg='#BBBBBB',
                                bg='#2B2B2B')
    product_price_label.grid(row=2, column=1, stick='we', pady=10)

    # Product Description Label
    product_description_label = Label(product_register_window, text='Description:', font='Poppins 12 bold',
                                      fg='#BBBBBB', bg='#2B2B2B')
    product_description_label.grid(row=3, column=1, stick='we', pady=10)

    # Defining Images Icon For The Register Product (32px)
    product_icon = PhotoImage(file='../images/product_icon.png')
    description_icon = PhotoImage(file='../images/description_icon.png')
    price_icon = PhotoImage(file='../images/price_icon.png')

    # Putting The Images In The Interface
    # Product Icon
    product_icon_label = Label(product_register_window, image=product_icon, bg='#2B2B2B')
    product_icon_label.photo = product_icon
    product_icon_label.grid(row=1, column=0, padx=(20, 5), pady=10, sticky='w')
    # Price Icon
    price_icon_label = Label(product_register_window, image=price_icon, bg='#2B2B2B')
    price_icon_label.photo = price_icon
    price_icon_label.grid(row=2, column=0, padx=(20, 5), pady=10, sticky='w')
    # Description Icon
    description_icon_label = Label(product_register_window, image=description_icon, bg='#2B2B2B')
    description_icon.photo = description_icon
    description_icon_label.grid(row=3, column=0, padx=(20, 5), pady=10, sticky='w')

    # Creating Screen Entries
    # Product Name Entry
    product_name_entry = Entry(product_register_window, font='Poppins 12')
    product_name_entry.grid(row=1, column=2, padx=(15, 25), sticky='e')

    # Product Price Entry
    product_price_entry = Entry(product_register_window, font='Poppins 12')
    product_price_entry.grid(row=2, column=2, padx=(15, 25), sticky='e')

    # Product Description Entry
    product_description_entry = Entry(product_register_window, font='Poppins 12')
    product_description_entry.grid(row=3, column=2, padx=(15, 25), sticky='e')

    # Creating Screen Buttons
    # Exit Button
    exit_button = Button(product_register_window, bg='#3C3F41', text='Exit', font='Poppins 12 bold', fg='#BBBBBB',
                         width=15, command=product_register_window.destroy)
    exit_button.grid(row=5, column=0, columnspan=2, padx=(20, 0), pady=10, sticky='w')
    # Continue Button
    continue_button = Button(product_register_window, bg='#3C3F41', text='Continue', font='Poppins 12 bold',
                             fg='#BBBBBB', width=15,
                             command=lambda: product_data_register(product_register_window,
                                                                   product_name_entry.get(),
                                                                   product_price_entry.get(),
                                                                   product_description_entry.get())
                             )
    continue_button.grid(row=5, column=2, columnspan=4, padx=(0, 25), pady=10, sticky='e')
