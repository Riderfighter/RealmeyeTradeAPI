from json import dumps

import requests


class Trading():
    """An unoffical api to access realmeye trading
    
    :usage:
    from realmeye import Trading 
    test = Trading()

    test.login('USERNAME','PASSWORD')
    test.setupOffers(1, [2613, 2793], [1, 1], [2593], [1], False)
    test.updateOffers()
    test.logout()
    
    """
    def __init__(self):
        self.s = requests.Session()
        self.sessionId = None
        self.player = None
        self.offers = []

    def login(self, username: str, password: str, bindip='f'):
        """login to realmeye with your account info.

        :parm username: your exact username as a string.
        :parm password: your exact password as  a string.
        :parm bindip: binds the account to your ip 't' = true or 'f' = false, default = 'f'.
        :returns: the data sent back from the realmeye server, OK or ERROR.

        """
        self.player = username

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip, deflate"}
        data = {"password": password,"username": username, "bindToIp": bindip}

        r = self.s.post('https://www.realmeye.com/login',headers=headers,data=data)
        self.sessionId = r.headers['Set-Cookie'].replace(
            'session=', '').replace('; secure', '')
        z = r.text

        cookies = {"session": self.sessionId}
        r = self.s.post('https://www.realmeye.com/log-in', headers=headers,
                        cookies=cookies, data={"redirect":"https://www.realmeye.com/","username": username, "password": password})
        return z

    def logout(self):
        """logouts of realmeye

        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip, deflate"}
        data = {"session": self.sessionId}
        cookies = {"session": self.sessionId}
        self.s.post('https://www.realmeye.com/logout',data=data,headers=headers,cookies=cookies)

    def setupOffers(self, tradeQuantity: int, sellingItems: list, sellingQuantities: list, buyingItems: list, buyingQuantities: list, suspended: bool):
        """creates the offer json :ok_hand:

        :parm tradeQuantity: takes an int that tells how many times you want to do this trade.
        :parm sellingItems: takes a list of item id with their respective integar values.
        :parm sellingQuantities: takes a list of how many of each item you want in their respective order with their respective integar values.
        :parm buyingItems: takes a list of item id with their respective integar values.
        :parm buyingQuantities: takes a list of how many of each item you want in their respective order with their respective integar values.
        :parm suspended: takes a bool that lets realmeye know if the trade is disabled.
        :returns: the json data still as a dict

        """
        json_data = {
            "quantity":tradeQuantity,
            "sellingItems":sellingItems,
            "sellingQuantities":sellingQuantities,
            "buyingItems":buyingItems,
            "buyingQuantities":buyingQuantities,
            "suspended":suspended
        }
        self.offers.append(json_data)
        return json_data
    

    def updateOffers(self):
        """sends the offer json to the server

        """
        data = {"player": self.player, "trades": dumps(self.offers).replace(' ', ''), "session": self.sessionId}
        cookies = {"session": self.sessionId}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip, deflate"}

        return self.s.post('https://www.realmeye.com/save-player-offers-service',data=data,cookies=cookies,headers=headers).json()
