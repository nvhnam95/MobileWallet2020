# MobileWallet2020
Thunes's test.

Overview:
Application that allow user:
- Create account, login.
- Get the account information. (username, balance...)
- Send money to another account.

Additional feature:
- Simulate deposit to account.
- Create, delete saving account.
- On saving account, use periodically get the interest base on saving type.
- When customer close the saving account, the original balance and the interest will add into main account. (Haven't had on webapp).

API documentation:
https://documenter.getpostman.com/view/5409175/SzzhddtL

---------------

Running the application:

- Prequisite: python >= 3.5.
+ Clone the source code.
+ cd to MobileWallet2020/main
+ Install python dependencies: pip install -r requirements.txt
+ Migrate the database: 
python manage.py makemigrations MobileWallet2020
python manage.py migrate

+ Create admin user:
python manage.py createsuperuser

+ Run the server on port 80:
python manage.py runserver 0.0.0.0:80

+ Run web app to test the APIs:
cd to: MobileWallet2020\main\web\dist
Run: python simple_serve.py

+ Open browser, navigate to localhost:8080

---------------
Using the admin page:
+ Navigate to: localhost/admin
+ Login with the credentials created above.
+ From the admin site, admin user can audit the data and the usage of services.

Using the webapp:
+ Browse localhost:8080
+ Click on Register, enter username and password.
+ Click on register again to create another user.
+ Login with the first user.
+ After login, customer can see their balance, saving accout information, transaction history...
+ Click on Deposit, then deposit an amount of money.
+ Click on tranfer money to tranfer money to another user.
+ Click on "Create a new one?" to create a new saving account, choose every_minute to let the interest raise faster.
+ Click on "Delete some" to delete a saving account, the money on that account and interst will be added to main balance.
+ Refresh page will log the user out.
 
