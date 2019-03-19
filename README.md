# django-coupons

![build status](https://travis-ci.org/byteweaver/django-coupons.png)

A reuseable Django application for coupon gereration and handling

## Setup instructions

1. Install `django-coupons` via pip:
   ```
   $ pip install django-coupons
   ```

2. Add `'coupons'` to `INSTALLED_APPS` in `settings.py`.

3. Migrate database:

   ```
   $ python manage.py migrate
   ```
   

## Working with coupons

To manage coupons, use the administration interface.

### Manualy adding coupons

To manually add coupons for discounts:

1. Click **Add coupon**
2. Enter the coupon properties:

| Property | Description |
| -------- | ----------- |
| Code | Code used by the customer to apply the coupon. A combination of letters, digits and other characters that make up the code of the coupon. The code serves as a unique identifier for the coupon. <br/><br/>Leave the field empty to [generate random code](#generating-random-coupon-code). |
| Value | Amount/Percent, depending on discount type you choose, that will be taken off the subtotal of any invoices. Entered without a currency unit or a percent sign. |
| Type | <ul><li> **Money based coupon** - This discount type will deduct the specified amount from the total amount on the invoice </li><li>**Percentage discount** - This discount type will deduct the specified percentage amount instead of just an amount from the invoice.</li></ul> |
| User limit | Maximum number of times this coupon can be redeemed, in total, across all users, before it is no longer valid. The system counts redemptions once for each purchase, not for each product affected by the related discount.<br/><br/>Set zero to allow unlimited use of the coupon code. |
| Valid until | Date after which the coupon can no longer be redeemed. <br/><br/> Leave empty for coupons that never expire. |
| Duration | The Duration deals with the recurring functionality of coupons. This specifies how long a coupon can be applied to a subscription after being added. There are 3 types of durations: <ul><li> **forever** - Coupons do not have an expiration time set, and the discount will be applied as long as the subscription is active.</li><li> **once** - coupons can only be used once in a subscription and cannot be used again after being redeemed. Once the discount is applied on the initial charge, the coupon will no longer be applicable.</li><li> **repeating** - coupons will have a fixed time duration. Once this time is over, the coupon can no longer be applied to the subscription.</li></ul> |
| Duration in months | If duration is repeating, the number of months the coupon applies. |
| Coupon users | Bound coupon to a specific user(s) |

3. Click **Save**

#### Supported use cases of coupons

This application supports different kind of coupons in the way how they can be redeemed.
The difference is defined by the number of possible redeems and if they are bound to a specific user (may even be a list of users) or not.

    1) single time (default), coupon can be used one time without being bound to an user.
    2) user limited, coupon can be used one time but only by a specific user.
    3) limit number, coupon can be used a limited number of times, by any user once.
    4) users list, coupon can be used by a defined list of users, each once.
    5) unlimited, coupon can be used unlimited times, but only once by the same user.

### Generating coupons

To have the system generate multiple coupons at once:

1. Click **Generate coupons**
2. Specify the properties of the coupon code generator:

| Property | Description |
| -------- | ----------- |
| Quantity | Specify how many coupon codes the system generates after you click **Generate**. |
| Prefix | The system [generates random coupon codes](#generating-random-coupon-code). The coupon code prefix allows you to enter a prefix to be shared by all codes generated in the current batch operation. If you leave the field empty, the system generates coupon codes without a shared prefix. |

3. Click **Generate**

The system creates the specified number of new coupon codes, optionally with the specified code prefix. 

### Generating random coupon code

If coupon code is not defined it will be generated randomly by the system. Still some rules will be used that can be redefined in settings:

* COUPONS_CODE_LENGTH - Length of coupon code, 15 by default
* COUPONS_CODE_CHARS - Characters used to generate code, combination of ascii letters and digits by default
* COUPONS_SEGMENTED_CODES - Whether code should be splited into segments, False by default
* COUPONS_SEGMENT_LENGTH - Length of code segment, 4 by default
* COUPONS_SEGMENT_SEPARATOR - Separator used to separate code segments, '-' by default
