# qu-backend
queueyeue :)


## Dataporten setup for testing

1. If you don't have one already, create a superuser with `python manage.py createsuperuser`.

2. From the django admin panel ([http://localhost:8000/admin](http://localhost:8000/admin)), go into `Sites` and change the site with ID 1 to domain `localhost` and name `Localhost`.

3. Log in to the [Dataporten Dashboard](https://dashboard.dataporten.no) and register a new application for login. Name and description can be whatever, redirect url should be `http://localhost:8000/accounts/dataporten/login/callback/`.

4. Accept the EULA and create the application.

5. In `Basic info`, make sure `Client type` is set to `confidential` and that user interaction is required.

6. Open `Permissions` from the left hand menu, make sure to accept these five scopes: `email`, `groups`, `profile`, `userid`, `userid_feide`.

7. In the django admin panel, create a new `Social application` with provider `Dataporten` and a descriptive name. Client ID and Secret can be found in `OAuth Details` in the left hand menu of the Dataporten Dashboard of your app.

That's it! You can now use Feide login by going to [http://localhost:8000/accounts/login](http://localhost:8000/accounts/login). In the left hand menu of the Dataporten Dashbord of your app, you can also find `Test users`, which you can use to test the integration without using your own Feide account.
