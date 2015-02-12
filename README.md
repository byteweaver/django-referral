# django-referral

![build status](https://travis-ci.org/byteweaver/django-referral.png)

A small django application for marketing using referral links

## What is this app good for?

Imagine you got a nice website running and you want to make some marketing in order to gain more users.
This can be achieved by spreading links/banners over the internet pointing to your website.
Now in order to find out how your banners performed you need to know how many users registered
after clicking on one of your banners. To tell them apart you add some unique GET parameter to
each link. This app will detect those referral parameters and store for each user what referrer
lead him to your website.

## Key Features

* Manual and automatic referrer generation.
* Referrer organisation in campaigns.
* Automatic associating of referrers with campaigns using patterns.
* Referrers will be cached in sessions, so when a user first browses your site and does not
  immediately register the referrer will be cached and assigned when the user finally decides
  to register. That way you can link to any site and not necessarily a register page.
* Very easy integration.
* Completely configurable to your needs.
* django 1.7 migrations + legacy south support
* No dependencies
* 100% Test coverage
* Supports django 1.4 - 1.7
* supports python 2 + 3

## Download

### using pip

	pip install django-referral
	
### github

	https://github.com/byteweaver/django-referral
	
## Integration

### 1. Add referral to your INSTALLED_APPS

	INSTALLED_APPS = (
		...
		'referral',
		...
	)

### 2. Add ReferrerMiddleware to your MIDDLEWARE_CLASSES

Since django-referral uses django's session middleware make sure you add it after SessionMiddleware

	MIDDLEWARE_CLASSES = (
		...
		'django.contrib.sessions.middleware.SessionMiddleware',
		'referral.middleware.ReferrerMiddleware',
		...
	)

### 3. Trigger the referrer association after user creation

	from referral.models import UserReferrer
	...
	def my_user_creation_view(request):
		...
		UserReferrer.objects.apply_referrer(user, request)

## Settings

###REFERRAL_GET_PARAMETER

The name of the GET parameter used.

	Default: "ref"

###REFERRAL_SESSION_KEY

The name of the session key that will hold the detected referrer

	Default: "referrer"

###REFERRAL_AUTO_CREATE

Defines whether unknown referrers shall be autocreated

	Default: True

###REFERRAL_AUTO_ASSOCIATE
Defines whether referrers should be associated to campaigns automatically using patterns

	Default: True

###REFERRAL_CASE_SENSITIVE
Defines whether or referrer names are case-sensitive or not.

  Default: False

## Testing

Just run the makefile to set up a virtual environment for testing

	make

For simple test

	make test

For coverage report

	make coverage

For full test in all supported environment (requires tox)

	tox

## Changelog
### V1.0.0
* add django 1.7 support
* add pyton3 support
* additional test cases
* code cleanup
* some pep8 fixes
