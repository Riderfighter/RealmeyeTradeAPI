# What is Realmeye?

[Realmeye Trading](https://www.realmeye.com/current-offers)

> Rankings, statistics, in-game trading, player and guild profiles, and more for Realm of the Mad God - the free online MMO RPG game..

----

## What is RealmeyeTradeAPI?

> An unofficial python module that facilitates the automatic creation of trades on [Realmeye](https://www.realmeye.com/) using unofficial methods of interacting with the page.

----

### Example Usage

    from realmeye import Trading
 
    trade = Trading() #Initiates the class.

    trade.login('USERNAME','PASSWORD') #Logs onto realmeye.

    trade.setupOffers(1, [2613, 2793], [1, 1], [2593], [1], False) #Sets up a trade using the item information.

    trade.updateOffers() #sends the trade to realmeye.

    trade.logout() # Logs out.

----

#### Changelog

* 22-Oct-2018 fixed usage of the data parameter with requests.
* 22-Oct-2018 added detailed readme.

----

#### Requirements

* [requests](https://github.com/requests/requests)
