# Django REST API

This REST API project is a bank account's API based on 'Django REST Framework' where you are able to visualize a list of registered 
bank accounts and perform HTTP methods.

## Used Technologies
<a href="#"><img src="https://img.shields.io/badge/Python-3.9.5-aff.svg?color=068bff"></a>
<a href="#"><img src="https://img.shields.io/badge/Django-3.2.4-aff.svg?color=004008"></a>
<a href="#"><img src="https://img.shields.io/badge/Django REST Framework-3.12.4-aff.svg?color=e91500"></a>

## Usage
Download the repository
```
git clone https://github.com/alanBovadilla97/REST_API_DJANGO.git
```
Run it in the console with the command
```
python manage.py runserver [port]
```
Then open the project in your browser in localhost server with the port previously indicated
```
localhost:[port]
```
The homepage will be open.
![homepage](images/homepage.png)

The, in the navbar you can click the option 'Account List' or type on the browser
```
localhost:[port]/accounts/
```

And you'll be redirected to the page where we can see a list of the registered bank accounts
![homepage](images/accounts.png)

If you want to POST a new account, go to the bottom of the page and input the following fields (All the fields are required):
```
* OwnerName: [String]
* Balance: [Int]
* AccountType: [String]
```
![homepage](images/postAccount.png)

To be able to preview a specific account, enter in your browser the identifier(pk) of that account like this:
```
localhost:[port]/accounts/[pk]
```
![homepage](images/accountDetails.png)

Here you are going to see the specific information for that account. In order to modify the information of this account, go
to the bottom of the page and press 'PUT'
![homepage](images/updateAccount.png)

To open the API's structure press the button 'OPTIONS'
![homepage](images/apiStructure.png)

An finally, to perform the DELETE method, press the 'DELETE' button
![homepage](images/deleteAccount.png)

A confirmation dialog will appear, to finally perform the operation press 'Delete'

## Credits
®2021. Alan Jair Bovadilla Huerta
