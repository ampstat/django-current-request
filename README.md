Django Current Request [![Build Status](https://travis-ci.org/futurice/django-current-request.svg?branch=master)](https://travis-ci.org/futurice/django-current-request)
======================

For that time you need the [HttpRequest](https://docs.djangoproject.com/en/1.9/ref/request-response/#django.http.HttpRequest), you got it.

Usage
-----

Add `djangocurrentrequest.middleware.RequestMiddleware` to `INSTALLED_APPS`.

Call `get_current_request()` to obtain the current HttpRequest object.


