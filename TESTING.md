## [Testing](#testing)
  * [Code validation](#code-validation)
  * [Testing User stories](#testing-user-stories)
  * [Responsiveness and Compatibility](#responsiveness-and-compatibility)
  * [Testing performance](#testing-performance)
  * [Testing accessibility](#testing-accessibility)
  * [known bugs](#known-bugs)
### [Code Validation](#code-validation)

## HTML5
All tests passed

## CSS3
All tests passed

## JavaScript
All tests passed

## Python
All tests passed

*Please Note - Warnings and errors were given on most pages due to template logic being used in this project. Certain Python files also failed PEP8 checks due to base code set by Django.*
# [Testing User stories](#testing-user-stories)
### First Time Users
Understand the purpose of the site

Users are shown a hero image which promote the sale of gifts on the home page
There is also an about section in the blog section which gives an account of what the site is about and how it started.
Being able to easily sign up for an account

A user can quickly and easily sign in/create an account.
I have tested this feature and found it to be working.
### Returning Users
Will have the ability to securely and swiftly log into their account

All accounts, log in and set up is done by Django and is extremely secure
Log in process is very quick, and allows a user to save their log in details for next time
Profile page contains past orders and order confirmations
I have tested this feature and found it to be working.

When a user is logged in, if they navigate to the profile page they will be given their Order History
Here users can see their default address and change it if needs be, they can also view their previous orders in a list. They can click on each individual order for more comprehensive details of the order.
When a user urchases a product it will be saved to their profile
I have tested this feature and found it to be working.

All users, regardless of logged in status, will be able to purchase products through the site
If a user is logged in when they process an order, it will be displayed on their profile order history
All users will receive an order confirmation email directly to their email inbox

I have tested this feature and found it to be working.
Leave reviews of products

Logged in users are able to leave product reviews
On the product details page, reviews are displayed below the main product information display
User reviews are displayed at the top, and the review form is below them
### Known Bugs()
  remove button not working in the shopping bag page.

  * page would not render as I had not included 'django.template.context_processors.media' in settings.py so my product which at the time lacked an image caused the page to throw an error.

  * server would not load and threw this error 
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/template/engine.py", line 52, in __init__
    self.builtins = self.default_builtins + builtins
    self.builtins = self.default_builtins + builtins
TypeError: can only concatenate list (not "set") to list
TypeError: can only concatenate list (not "set") to list

After searching through files I found that in the settings.py file I had added that in templates I had added 'builtins' and its contents using curly brackets instead of square brackets. This resolved the above issue but threw another error.
django.template.library.InvalidTemplateLibrary: Invalid template library specified. ImportError raised when trying to load 'crispy_forms.templatetags.crispy_forms_fields': No module named 'crispy_forms.templatetags.crispy_forms_fields' - I realised I had a spelling error and removed the stray 's' from fields. The server then operated as expected.

* AttributeError: 'Settings' object has no attribute 'STRIPE_PUBLIC_KEY' when I saved the stripe_public_key to my variables in my workspace I had a typo.
* I had forgotten to pip3 install stripe

* remove button wasnt working because I hadnt added a reverse url to the view to go back to the updated shopping bag.

* stript form for payment not loading correctly.

* secret_key!!

* stripe wasnt working because I had a typo in pid. ()[0] the square bracket was outside the bracket.
when stripe was working a new error came up. this error showed that the checkout orderline wasnt functioning correctly because the site was looking for a product.size element and on my site i dont have product.sizes as it is irrelevant for my beauty product site.

the date wasnt showing on the confirmation email as i had it down as {order.order_date} instead of {order.date}

* add product page didnt open. I used diffchecker.com to check the difference between my code and the video source code. I found a spelling error. A screenshot of this image is included.
[Responsiveness and Compatibility](#responsiveness-and-compatibility)