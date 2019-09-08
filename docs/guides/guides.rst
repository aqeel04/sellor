Orders
======

Sellor gives a possibility to manage orders from dashboard. It can be done in dashboard ``Orders`` tab.


Draft orders
------------

To create draft order, first you must go to dashboard ``Orders`` tab and choose circular **+** button visible above the list of existing orders.

Those orders can be fully edited until confirmed by clicking `Create order`. You can modify ordered items, customer (also just set an email), billing and shipping address, shipping method and discount. Any voucher you apply will cause automatic order recalculation to fit actual state of an order every time it changes.

Confirming an order by clicking `Create order` will change status to unfulfilled and disable most of the edit actions. You can optionally notify customer - if attached any - about that order by sending email.


Marking orders as paid
----------------------

You can manually mark orders as paid if needed in order details page. This option is visible only for unpaid orders as an action in `Payments` card.

.. warning::

  You won't be able to refund a payment handled manually. This is due to lack of enough data required to handle transaction.


Navigation
==========

Sellor gives a possibility to configure storefront navigation. It can be done in dashboard ``Navigation`` tab.

You can add up to 3 levels of menu items inside every menu you create. Each menu item can point to an internal page with Category, Collection, Page or an external website by passing an extra URL.


Managing menu items
-------------------

To manage menu items, first you must go to dashboard ``Navigation`` tab and choose menu to edit. If you want to manage nested menu items, you can navigate through listed menu items up and down.

To add new menu item, choose ``Add`` button visible above the list of menu items. Then fill up the form and click ``Create``.

To edit menu item, choose ``Edit`` button visible next to a menu item on the list or ``Edit menu item`` button below menu item details, if you're inside menu item details view. Make any changes and click ``Update``.

To remove a menu item, choose ``Remove`` button visible next to a menu item on the list or ``Remove menu item`` button below menu item details, if you're inside menu item details view. This action will remove all descendant items and can't be undone.

The menu items display on the storefront in the order that they are listed in menu items list. You can reorder them by handling an icon on the left to the menu items and dragging them to another position.


Managing menus
--------------

Dashboard gives you a possibility to add new menus.

There can be two active menus at once (one for the navbar, the other one for the footer, they can be the same).

Currently assigned menus can be changed via dashboard's ``Navigation`` panel.

Menu is rendered as a vertical list by default. You can change it by passing an extra ``horizontal=True`` argument. Horizontal menus with nested items appear as a dropdown menu on desktops.


Payments
========

Integrating a new Payment Gateway into Sellor
---------------------------------------------

We are using a universal flow, that each gateway should fulfill, there are
several methods that should be implemented.

Your changes should live under the
``sellor.payment.gateways.<gateway name>`` module.


1. get_client_token(connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A client token is a signed data blob that includes configuration and
authorization information required by the payment gateway.

These should not be reused; a new client token should be generated for
each payment request.

Example
"""""""

.. code-block:: python

    def get_client_token(connection_params: Dict) -> str:
        gateway = get_payment_gateway(**connection_params)
        client_token = gateway.client_token.generate()
        return client_token


2. authorize(payment_information, connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A process of reserving the amount of money against the customer's funding
source. Money does not change hands until the authorization is captured.

Example
"""""""

.. code-block:: python

    def authorize(
            payment_information: Dict,
            connection_params: Dict) -> Dict:

        # Handle connecting to the gateway and sending the auth request here
        response = gateway.authorize(token=payment_information['token'])

        # Return a correct response format so Sellor can process it,
        # the response must be json serializable
        return {
            'is_success': response.is_success,
            'transaction_id': response.transaction.id,
            'kind': 'auth',
            'amount': response.amount,
            'currency': response.currency,
            'error': get_error(response),
            'raw_response': get_payment_gateway_response(response),
        }


3. refund(payment_information, connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Full or partial return of captured funds to the customer.

Example
"""""""

.. code-block:: python

    def refund(
            payment_information: Dict,
            **connection_params: Dict) -> Dict:

        # Handle connecting to the gateway and sending the refund request here
        response = gateway.refund(token=payment_information['token'])

        # Return a correct response format so Sellor can process it,
        # the response must be json serializable
        return {
            'is_success': response.is_success,
            'transaction_id': response.transaction.id,
            'kind': 'refund',
            'amount': response.amount,
            'currency': response.currency,
            'error': get_error(response),
            'raw_response': get_payment_gateway_response(response),
        }


4. capture(payment_information, connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A transfer of the money that was reserved during the authorization stage.

Example
"""""""

.. code-block:: python

    def capture(
            payment_information: Dict,
            connection_params: Dict) -> Dict:

        # Handle connecting to the gateway and sending the capture request here
        response = gateway.capture(token=payment_information['token'])

        # Return a correct response format so Sellor can process it,
        # the response must be json serializable
        return {
            'is_success': response.is_success,
            'transaction_id': response.transaction.id,
            'kind': 'refund',
            'amount': response.amount,
            'currency': response.currency,
            'error': get_error(response),
            'raw_response': get_payment_gateway_response(response),
        }


5. void(payment_information, connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A cancellation of a pending authorization or capture.

Example
"""""""

.. code-block:: python

    def void(
            payment_information: Dict,
            connection_params: Dict) -> Dict:

        # Handle connecting to the gateway and sending the void request here
        response = gateway.void(token=payment_information['token'])

        # Return a correct response format so Sellor can process it,
        # the response must be json serializable
        return {
            'is_success': response.is_success,
            'transaction_id': response.transaction.id,
            'kind': 'refund',
            'amount': response.amount,
            'currency': response.currency,
            'error': get_error(response),
            'raw_response': get_payment_gateway_response(response),
        }


6. charge(payment_information, connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authorization and capture in a single step.

Example
"""""""

.. code-block:: python

    def charge(
            payment_information: Dict,
            connection_params: Dict) -> Dict:

        # Handle connecting to the gateway and sending the charge request here
        response = gateway.charge(
            token=payment_information['token'],
            amount=payment_information['amount'])

        # Return a correct response format so Sellor can process it,
        # the response must be json serializable
        return {
            'is_success': response.is_success,
            'transaction_id': response.transaction.id,
            'kind': 'refund',
            'amount': response.amount,
            'currency': response.currency,
            'error': get_error(response),
            'raw_response': get_payment_gateway_response(response),
        }


7. process_payment(payment_information, connection_params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used for the checkout process, it should perform all the necessary
steps to process a payment. It should use already defined functions,
like authorize and capture.

Example
"""""""

.. code-block:: python

    def process_payment(
            payment_information: Dict,
            connection_params: Dict) -> Dict:

        # Authorize, update the token, then capture
        authorize_response = authorize(
            payment_information, connection_params)
        payment_information['token'] = authorize_response['transaction_id']

        capture_response = capture(
            payment_information, connection_params)

        # Return a list of responses, each response must be json serializable
        return [authorize_response, capture_response]

Example
"""""""

.. code-block:: python

    payment_information = {
        'token': 'token-used-for-transaction',  # provided by gateway
        'amount': Decimal('174.32'),  # amount to be authorized/captured/charged/refunded
        'currency': 'USD',  # ISO 4217 currency code
        'billing': {  # billing information
            'first_name': 'Joe',
            'last_name': 'Doe',
            'company_name': 'JoeDoe Inc.',
            'street_address_1': '3417 Bridge Street',
            'street_address_2': '',
            'city': 'Pryor',
            'city_area': '',
            'postal_code': '74361',
            'country': 'US',
            'country_area': 'OK',
            'phone': '+19188249023'},
        'shipping': {  # shipping information
            'first_name': 'Dollie',
            'last_name': 'Sullivan',
            'company_name': '',
            'street_address_1': '2003 Progress Way',
            'street_address_2': '',
            'city': 'Waterloo',
            'city_area': '',
            'postal_code': '50797',
            'country': 'US',
            'country_area': 'IA',
            'phone': '+19188249023'},
        'order': 117,  # order id
        'customer_ip_address': '10.0.0.1',  # ip address of the customer
        'customer_email': 'joedoe@example.com',  # email of the customer
    }


Gateway Response Fields
"""""""""""""""""""""""

.. table:: Gateway response fields

   +----------------+-------------+--------------------------------------------------------------------------+
   | name           | type        | description                                                              |
   +----------------+-------------+--------------------------------------------------------------------------+
   | transaction_id | ``str``     | Transaction ID as returned by the gateway.                               |
   +----------------+-------------+--------------------------------------------------------------------------+
   | kind           | ``str``     | Transaction kind, one of: auth, capture, charge, refund, void.           |
   +----------------+-------------+--------------------------------------------------------------------------+
   | is_success     | ``bool``    | Status whether the transaction was successful or not.                    |
   +----------------+-------------+--------------------------------------------------------------------------+
   | amount         | ``Decimal`` | Amount that the gateway actually charged or authorized.                  |
   +----------------+-------------+--------------------------------------------------------------------------+
   | currency       | ``str``     | Currency in which the gateway charged, needs to be an ISO 4217 code.     |
   +----------------+-------------+--------------------------------------------------------------------------+ 
   | error          | ``str``     | An error message if one occured. Should be ``None`` if no error occured. |
   +----------------+-------------+--------------------------------------------------------------------------+

Additional fields can be sent for logging/debug purposes. The only requirement is that they're serializable by
``DjangoJSONEncoder``. They will be saved in ``gateway_response`` field on Transaction model.


Example
=======

.. code-block: python

    response = {
        'transaction_id': 'token-from-gateway',
        'kind': 'auth',
        'is_success': True,
        'amount': Decimal(14.50),
        'currency': 'USD',
        'error': None,
        'extra_field': 'additional information',
        'raw_response': raw_gateway_response_as_dict}
