ALOUGES Damien

Cryptocurrency Master is a chatbot that help people in cryptocurrency trading
at start I named it Bitcoin_nanalyst but I changed hes name because he can process other crypto currencies than the bitcoin

The chatbot functionnalities are :
    - it can give info on many pairs of currencies but need to get the api format of all pairs : 
                - Bitcoin / euro  => XXBTZEUR
                - Bitcoin / USD   => XBTZUSD
                - Bitcoin cash / euro => BCHEUR
                - Bitcoin cash / USD => BCHUSD
                - Bitcoin cash /Bitcoin => BCHXBT
                - Ethereum / euro => XETHZEUR
                - Ethereum / USD => XETHZUSD
                - Ethereum / Bitcoin => XETHXXBT
    - to give latest open, close, high and low price and vwap(volume weighted average price) of a pair of currencies
    - it respond politely to greetings and farewells
    - it can give you the vwap of a pair of yesterday, last week, last 2 weeks
    - and it can give a sort-term and a long-term vwap prediction of a pair


Here is an exemple of a conversation with the bot for every functionnalities : 
    
"hi"
Crypto-currency Master: hello !              at : 2020-04-05 19:54:23

"can you give me the open price of XXBTZEUR ?"
Crypto-currency Master: the price of the open trade of XXBTZEUR is 6300.1              at : 2020-04-05 19:56:36

"give me vwap of BCHEUR of the last two weeks"
Crypto-currency Master: The vwap of the pair BCHEUR the last 2 weeks is 206.4              at : 2020-04-05 20:00:08

"get me the vwap of BCHXBT of yesterday"
Crypto-currency Master: The vwap of the pair BCHXBT the last day is 0.03435              at : 2020-04-05 20:03:11

"give me a long term prediction of the price of BCHEUR"
Crypto-currency Master: with my great calculation I can say that next week the price of BCHEUR will be 225.25 and change by 3.57%              at : 2020-04-05 20:03:48

"give me a short-term prediction of XETHZEUR price"
Crypto-currency Master: with my great calculation I can say that tomorrow the price of XETHZEUR will be 133.98 and change by 0.89%              at : 2020-04-05 20:05:08

"How to heal from COVID-19 ?"
Crypto-currency Master: I don't understand what you ask              at : 2020-04-05 20:06:27

"Goodbye !"
Crypto-currency Master: Bye! take care.              at : 2020-04-05 20:09:06





The chatbot is really slow to respond because of the structure of it and the API, I really didn't make a well optimized structure and at every call the api make the bot wait for 5 seconds before give it the data.

the javascript script call the python script for every queries to do it in a better way I should have make them run  in the same time and make  them communicate.

It is a web application, I had in mind to put it on the web but I didn't had the time to deploy it.

To run it you just have to do a $npm install and  then a $npm start and the app will start on localhost:3000

You can send him  a message by pressing enter or clicking on the send button.