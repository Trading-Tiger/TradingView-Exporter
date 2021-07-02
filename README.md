# :rocket: TradingView Exporter :rocket:
![alt text](https://trading-tigers.com/assets/img/TradingTigers-TIGS-.png)
##### Here comes the TradingView Exporter

Trading-Tigers TradingView Export is able to react and execute an Webhook Signal on Binance Futures! High speed!  

### [CHECK MORE MODULES AND INDICATORS](https://Trading-Tigers.com)
### [TradingTigers Token @BSC](https://bscscan.com/token/0x34faa80fec0233e045ed4737cc152a71e490e2e3)
## Your benefits of our software.
#### READY FOR ALL!
Suitable for experienced, advanced and novice traders, perfect for learning.  

#### EARN WHILE YOU SLEEP!
The automated TradingTiger bots work 24/7 so you don't have to.  
#### QUICK AND EASY TO SET UP!
Little to no trading experience or programming knowledge required.  
You can run multiple trading pairs on the same exchange and check for Take Profit and Stop Loss.
#### !!!!PLEASE MAKE SURE TRADING LEVERAGE IS HIGH RISK!!!!!! 

## Preview
comming soon
## Enter our Community
[![Discord Shield](https://discordapp.com/api/guilds/766340441075089418/widget.png?style=banner2)](https://discord.gg/xAGZHAr)  


## Download  
[Find a version for your system at Releases](https://github.com/Trading-Tiger/TradingView-Exporter/releases/)  

## Settings  
#### Main Settings
##### It is recommended to use a server.
##### TradingView Alarm Message Example

```javascript
{
"whitelist" : "3412-Passwd",
"side" : "{{strategy.market_position}}", -> LONG or SHORT
"symbol" : "{{ticker}}", -> WITH PERP!!
"indicator" : "Predictum", -> Only a Name for your Indicator
"comment": "{{strategy.order.comment}}" Comment From your Strategy or just leave it free, if "Ready" or "Get" are in the incoming message, it will not execute anything. 
}
```
## Config
"IP" : "0.0.0.0", -> Server IP. (0.0.0.0 Automatically sets its IP) Find your IP with Ipconfig or ifconfig!  
"PORT" : 80, Port for receiving, 80 is recommended.  
"whitelist" : "3412-Passwd", -> Your security key, only messages with the key will be executed.  
"trade_on_exchange": true, -> Execute Signals ?  
### Api Keys
Never give your API Key authorization to withdrawal, make sure that you enable trading and futures. 
### coins
"coins" : ["BTCUSDT", "XRPUSDT" , "ADAUSDT" ], -> Pairs to Trade on Binance Future.  
You can find a complete COIN list [HERE](https://github.com/Trading-Tiger/Supported_Trading_Pairs/blob/main/Binance_Future_Pairs.json).
### Position calculation
"BalancePercent_per_Order" : 0.5, -> Wallet percentage size of a position.  
"Max_Percent_in_Coin" : 1.5, -> The maximum Wallet percentage size of a position on a trading pair.  
"leverage" : 3,-> Set Your Leverage!  
### Discord  
You want to receive notifications about achieved stop loss, no problem, activate it and add your Discord webhook URL.  
"discord" : true,  
"discord_channel_webhook": "https://discord.com/api/webhooks/795290618/qOc_NnbAB0",  

  
## Optional
Install [Nodejs](https://nodejs.org/en/)  
Open CMD or SHELL with Admin
```javascript
npm install pm2 -g
```
Then you can start your Tiger Tool with:
```javascript
pm2 start <appname> --name "<set_name>"
```
And Monitoring it with:
```javascript
pm2 monit
```
Some more PM2 commands:
```javascript
pm2 status
pm2 restart <APP_Name>
pm2 stop <APP_Name>
pm2 delete <APP_Name>
```
