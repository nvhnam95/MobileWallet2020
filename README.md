# MobileWallet2020
Thunes's test.

__Overview__
Application that alows user:
- Accesses the service through an HTTP based API, with authentication.
- Creates account, login into system.
- Gets the account's information. (username, balance...)
- Sends money to other accounts.
- Views the transaction history.
- Admin user can view, edit, delete created resources.
- Data are store on SQLite database for mobility.
- There are another feature that would interest the user: saving money:     <br>
-- Simulate deposit money to account.    <br>
-- Create a saving account.    <br>
-- On saving account, user periodically gets the interest base on saving type.    <br>
-- When customer closes the saving account, the original balance and the interest will be added into main account.    <br>

API documentation:
https://documenter.getpostman.com/view/5409175/SzzhddtL
---------------
Running the application:
- Prequisite: python >= 3.5
+ Clone the source code.
+ cd to MobileWallet2020/main
+ Install python dependencies: pip install -r requirements.txt
+ Migrate the database:        <br>
python manage.py makemigrations MobileWallet2020        <br>
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
+ Browse localhost
+ Click on Register, enter username and password.
+ Click on register again to create another user.
+ Login with the first user.
+ After login, customer can see their balance, saving accout information, transaction history...
+ Click on Deposit, then deposit an amount of money.
+ Click on tranfer money to tranfer money to another user.
+ Click on "Create a new saving account?" to create a new saving account, choose every_minute to let the interest raise faster.
+ Click on "Delete a saving account and get the interest." to delete a saving account, the money on that account and interst will be added to main balance.
+ Refresh page will log the user out.
 
---------------
Running with docker:     <br>
docker build -t mobilewallet .      <br>
docker run -it -p 80:8080 --name=my_container mobilewallet python main/manage.py runserver 0.0.0.0:8080

To remove container, run:
docker container rm my_container
