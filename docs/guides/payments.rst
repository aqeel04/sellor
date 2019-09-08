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
