Handling Money Amounts
======================

Sellor uses the `Prices <https://github.com/mirumee/prices/>`_ and `django-prices <https://github.com/mirumee/django-prices/>`_ libraries to store, calculate and display amounts of money, prices and ranges of those and `django-prices-vatlayer <https://github.com/mirumee/django-prices-vatlayer>`_ to handle money ammounts. Money amounts are stored on model using `MoneyField` that provides its own safechecks on currency and precision of stored amount.


Default currency
----------------

All prices are entered and stored in a single default currency controlled by the :ref:`DEFAULT_CURRENCY <settings_configuration>` settings key. Sellor can display prices in a user's local currency (see :ref:`openexchangerates`) but all purchases are charged in the default currency.

.. warning::

  The currency is not stored in the database. Changing the default currency in a production environment will not recalculate any existing orders. All numbers will remain the same and will be incorrectly displayed as the new currency.


Money
-----

In Sellor's codebase, money amounts exist as `Money` instance.

`Money` is a type representing amount of money in specific currency: 100 USD is represented by `Money(100, 'USD')`.
This type doesn't hold any additional information useful for commerce but, unlike `Decimal`, it implements safeguards and checks for calculations and comparisons of monetary values.

Money amounts are stored on model using `MoneyField` that provides its own safechecks on currency and precision of stored amount.

If you ever need to get to the `Decimal` of your `Money` object, you'll find it on the `amount` property.

Products and shipping methods prices are stored using `MoneyField`. All prices displayed in dashboard, excluding orders, are as they have been entered in the forms. You can decide if those prices are treated as gross or net in dashboard.

Prices displayed in orders are gross or net depending on setting how prices are displayed for customers, both in storefront and dashboard. This way staff users will always see the same state of an order as the customer.


MoneyRange
----------

Sometimes a product may be available under more than single price due to its variants defining custom prices different from the base price.

For such situations `Product` defines additional `get_price_range` method that return `MoneyRange` object defining minimum and maximum prices on its `start` and `stop` attributes.
This object is then used by the UI to differentiate between displaying price as "10 USD" or "from 10 USD" in case of products where prices differ between variants.


Product Structure
=================

Before filling your shop with products we need to introduce 3 product concepts - *product types*, *products*, *product variants*.


Overview
--------

Consider a book store. One of your *products* is a book titled "Introduction to Sellor".

The book is available in hard and soft cover, so there would be 2 *product variants*.

Type of cover is the only attribute which creates separate variants in our store, so we use *product type* named "Book" with variants enabled and a "Cover type" *variant attribute*.


Product Variants
----------------

Variants are the most important objects in your shop. All cart and stock operations use variants. Even if a product doesn't have multiple variants, the store will create one under the hood.


Products
--------

Describes common details of a few *product variants*. When the shop displays the category view, items on the list are distinct *products*. If the variant has no overridden property (example: price), the default value is taken from the *product*.

- ``publication_date``
    Until this date the product is not listed in storefront and is unavailable for users.

- ``is_featured``
    Featured products are displayed on the front page.


Product Types
---------------

Think about types as templates for your products. Multiple *products* can use the same product type.

- ``product_attributes``
    Attributes shared among all *product variants*. Example: publisher; all book variants are published by same company.

- ``variant_attributes``
    It's what distinguishes different *variants*. Example: cover type; your book can be in hard or soft cover.

- ``is_shipping_required``
    Indicates whether purchases need to be delivered. Example: digital products; you won't use DHL to ship an MP3 file.

- ``has_variants``
    Turn this off if your *product* does not have multiple variants or if you want to create separate *products* for every one of them.

    This option mainly simplifies product management in the dashboard. There is always at least one *variant* created under the hood.


.. warning:: Changing a product type affects all products of this type.

.. warning:: You can't remove a product type if there are products of that type.


Attributes
----------

*Attributes* can help you better describe your products. Also, the can be used to filter items in category views.

The attribute values display in the storefront in the order that they are listed in the list in attribute details view. You can reorder them by handling an icon on the left to the values and dragging them to another position.

There are 2 types of *attributes* - choice type and text type. If you don't provide choice values, then attribute is text type.

Examples
~~~~~~~~

* *Choice type*: Colors of a t-shirt (for example 'Red', 'Green', 'Blue')
* *Text type*: Number of pages in a book


Example: Coffee
~~~~~~~~~~~~~~~

Your shop sells Coffee from around the world. Customer can order 1kg, 500g and 250g packages. Orders are shipped by couriers. 

.. table:: Coffee - Attributes

   =================  ===========
   Attribute          Values
   =================  ===========
   Country of origin  * Brazil
                      * Vietnam
                      * Colombia
                      * Indonesia
   Package size       * 1kg
                      * 500g
                      * 250g
   =================  ===========

.. table:: Coffee - Product type

   ======  ===================  =========  ==================  =========
   Name    Product attributes   Variants?  Variant attributes  Shipping?
   ======  ===================  =========  ==================  =========
   Coffee  * Country of origin  Yes        * Package size      Yes
   ======  ===================  =========  ==================  =========

.. table:: Coffee - Product

   ============  ================  =================  =================================
   Product type  Name              Country of origin  Description
   ============  ================  =================  =================================
   Coffee        Best Java Coffee  Indonesia          Best coffee found on Java island!
   ============  ================  =================  =================================

.. table:: Coffee - Variants
   :widths: 30 30 40 

   ====  ============  ==============
   SKU   Package size  Price override
   ====  ============  ==============
   J001  1kg           $20
   J002  500g          $12
   J003  250g          $7
   ====  ============  ==============


Example: Online game items
~~~~~~~~~~~~~~~~~~~~~~~~~~

You have great selection of online games items. Each item is unique, important details are included in description. Bought items are shipped directly to buyer account.

.. table:: Online Game Items - Attributes

   ==========  ================
   Attribute   Values
   ==========  ================
   Game        * Kings Online
               * War MMO
               * Target Shooter
   Max attack  ---
   ==========  ================

.. table:: Online Game Items - Product type

   =========  ==================  =========  ==================  =========
   Name       Product attributes  Variants?  Variant attributes  Shipping?
   =========  ==================  =========  ==================  =========
   Game item  * Game              No         ---                 No
              * Max attack
   =========  ==================  =========  ==================  =========

.. table:: Online Game Items - Products

   ============  ================  =======  ==============  ==========  =================================
   Product type  Name              Price    Game            Max attack  Description
   ============  ================  =======  ==============  ==========  =================================
   Game item     Magic Fire Sword  $199     Kings Online    8000        Unique sword for any fighter.
   Game item     Rapid Pistol      $2500    Target Shooter  250         Fastest pistol in the whole game.
   ============  ================  =======  ==============  ==========  =================================


Thumbnails
==========

Sellor uses `VersatileImageField <https://github.com/respondcreate/django-versatileimagefield>`_ replacement for Django's ImageField.
For performance reasons, in non-debug mode thumbnails are pregenerated by the worker's task, fired after saving the instance.
Accessing missing image will result in 404 error.

In debug mode thumbnails are generated on demand.


Generating Products Thumbnails Manually
---------------------------------------

Create missing thumbnails for all ProductImage instances.

.. code-block:: console

 $ python manage.py create_thumbnails


Deleting Images
---------------

Image renditions are not deleted automatically with the Image instance, so is the main image.
More on deleting images can be found in `VersatileImageField documentation <https://django-versatileimagefield.readthedocs.io/en/latest/deleting_created_images.html>`_


Stock Management
================

Each product variant has a stock keeping unit (SKU).

Each variant holds information about *quantity* at hand, quantity *allocated* for already placed orders and quantity *available*.

**Example:** There are five boxes of shoes. Three of them have already been sold to customers but were not yet dispatched for shipment. The stock records **quantity** is **5**, **quantity allocated** is **3** and **quantity available** is **2**.

Each variant also has a *cost price* (the price that your store had to pay to obtain it).


Product Availability
--------------------

A variant is *in stock* if it has unallocated quantity.

The highest quantity that can be ordered is the available quantity in product variant.


Allocating Stock for New Orders
-------------------------------

Once an order is placed, quantity needed to fulfil each order line is immediately marked as *allocated*.

**Example:** A customer places an order for another box of shoes. The stock records **quantity** is **5**, **quantity allocated** is now **4** and **quantity available** becomes **1**.


Decreasing Stock After Shipment
-------------------------------

Once order lines are marked as shipped, each corresponding stock record will have both its quantity at hand and quantity allocated decreased by the number of items shipped.

**Example:** Two boxes of shoes from warehouse A are shipped to a customer. The stock records **quantity** is now **3**, **quantity allocated** becomes **2** and **quantity available** stays at **1**.


Order Management
================

Orders are created after customers complete the checkout process. The `Order` object itself contains only general information about the customer's order.


Fulfillment
-----------

The fulfillment represents a group of shipped items with corresponding tracking number. Fulfillments are created by a shop operator to mark selected products in an order as fulfilled.

There are two possible fulfillment statuses:

- ``NEW``
    The default status of newly created fulfillments.

- ``CANCELED``
    The fulfillment canceled by a shop operator. This action is irreversible.


Order statuses
--------------

There are four possible order statuses, based on statuses of its fulfillments:

- ``UNFULFILLED``
    There are no fulfillments related to an order or each one is canceled. An action by a shop operator is required to continue order processing.

- ``PARTIALLY FULFILLED``
    There are some fulfillments with ``FULFILLED`` status related to an order. An action by a shop operator is required to continue order processing.

- ``FULFILLED``
    Each order line is fulfilled in existing fulfillments. Order doesn't require further actions by a shop operator.

- ``CANCELED``
    Order has been canceled. Every fulfillment (if there is any) has ``CANCELED`` status. Order doesn't require further actions by a shop operator.

There is also ``DRAFT`` status, used for orders newly created from dashboard and not yet published.


Events
======

.. note::
    Events are autogenerated and will be triggered
    when certain actions are completed, such us creating the order,
    cancelling fulfillment or completing a payment.


Order Events
------------

.. table:: Order Events
   :widths: 25 25 50

   +---------------------------+---------------------------+---------------------------------------------------------------+
   | Code                      | GraphQL API value         | Description                                                   |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``placed``                | ``PLACED``                | An order was placed by the customer.                          |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``draft_placed``          | ``FROM_DRAFT``            | An order was created from draft by the staff user.            |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``oversold_items``        | ``OVERSOLD_ITEMS``        | An order was created from draft.                              |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``canceled``              | ``CANCELED``              | The order was cancelled.                                      |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``order_paid``            | ``ORDER_PAID``            | The order was fully paid by the customer.                     |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``marked_as_paid``        | ``MARKED_AS_PAID``        | The order was manually marked as fully paid by the staff user.|
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``updated``               | ``UPDATED``               | The order was updated.                                        |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``email_sent``            | ``EMAIL_SENT``            | An email was sent to the customer.                            |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``captured``              | ``CAPTURED``              | The payment was captured.                                     |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``refunded``              | ``REFUNDED``              | The payment was refunded.                                     |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``voided``                | ``VOIDED``                | The payment was voided.                                       |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``fulfill_canceled``      | ``FULFILL_CANCELED``      | Fulfillment for one or more of the items was canceled.        |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``restock_items``         | ``RESTOCK_ITEMS``         | One or more of the order's items have been resocked           |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``fulfill_items``         | ``FULFILL_ITEMS``         | One or more of the order's items have been fulfilled.         |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``note_added``            | ``NOTE_ADDED``            | A note was added to the order by the staff.                   |
   +---------------------------+---------------------------+---------------------------------------------------------------+
   | ``other``                 | ``OTHER``                 | Status used during reimporting of the legacy events.          |
   +---------------------------+---------------------------+---------------------------------------------------------------+
