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
