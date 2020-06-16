# MobileWallet2020
Thunes's test.

__Overview__
Application that allow user:
- User access the service through an HTTP based API, with authentication
- Create account, login into system.
- Get the account's information. (username, balance...)
- Send money to other accounts.
- View the transaction history.
- Admin user can view, edit, delete created resources.
- Data are store on SQLite database for mobility.
- There are another feature that would interest the user: saving money:
-- Simulate deposit money to account.
-- Create a saving account.
-- On saving account, user periodically gets the interest base on saving type.
-- When customer closes the saving account, the original balance and the interest will be added into main account.

API documentation:
https://documenter.getpostman.com/view/5409175/SzzhddtL
---------------
Running the application:
- Prequisite: python >= 3.5
+ Clone the source code.
+ cd to MobileWallet2020/main
+ Install python dependencies: pip install -r requirements.txt
+ Migrate the database: 
python manage.py makemigrations MobileWallet2020
python manage.py migrate

+ Run tests:
+ python manage.py test
+ 
+ Create admin user:
python manage.py createsuperuser

+ Run the server on port 80 (orther ports are just fine):
python manage.py runserver 0.0.0.0:80
+ Open browser, navigate to localhost

---------------
Using the admin page:
+ Navigate to: localhost/admin
+ Login with the credentials created above.
+ From the admin site, admin user can audit the data and the usage of services.
--------------

Using the webapp:
+ Browse localhost:8080
+ Click on Register, enter username and password.
+ Click on register again to create another user.
+ Login with the first user.
+ After login, customer can see their balance, saving accout information, transaction history...
+ Click on Deposit, then deposit an amount of money.
+ Click on tranfer money to tranfer money to another user.
+ Click on "Create a new saving account?" to create a new saving account, choose every_minute to let the interest raise faster.
+ Click on "Delete a saving account and get the interest." to delete a saving account, the money on that account and interst will be added to main balance.
+ Refresh page will log the user out.
 
