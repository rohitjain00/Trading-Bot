# Trading-Bot
Trading bot for an Internship program

> ## ⚠️ WARNING — Research / Paper-Trading Only
> This bot is an educational prototype. It has **NO stop-loss**, **no position-sizing caps**
> (it always trades a fixed `STOCK_QTY = 10`), and no other risk controls.
> Never point it at real funds without adding proper risk management first.

## Bianance API
[Here](https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md) is the API of Binance as used in the above project.

# Bollinger Bands
A Bollinger bands is a technical analysis tool defined by two bands which are simply the 2 standard deviation +/- of  20-days Simple Moving Average. The factor 2 and the window of 20 days could vary but these are the standard once. The two bands depict the volatility of the market Because standard deviation is a measure of volatility, when the markets become more volatile the bands widen; during less volatile periods, the bands contract. Closer the price moves to the upper band the more likely the price is to drop and vice versa. So we create a buy signal when the price hits the lower band and a sell signal when the price hits the upper band. Although this strategy is not meant to be used alone when trading because it weighs the older price data the same as the most recent. Overall it's not a perfect strategy but has a high probability of success.

Classes Distribution of the project for ease in understanding

![class diagram](https://github.com/rohitjain00/Trading-Bot/blob/master/Trading-botdrawio.png)

[Here](https://github.com/rohitjain00/Trading-Bot/blob/master/BackTesting%20Result.pdf) is how the project looks while running

## Instructions to setup project enviroment

#### Installing Virtual enviroment
`pip install virtualenv`

Test your installation:

`virtualenv --version`

#### Create new virtual enviroment
(Execute all the commands rom the root folder)

`virtualenv venv`

#### Activate virtual enviroment
`source venv/bin/activate`

#### Install requirements
`pip install -r requirements.txt`

## Starting the project

1. In the [Main.py](https://github.com/rohitjain00/Trading-Bot/blob/master/Main.py) adjust the parameters needed to trade.
2. Run the Main.py file.

## Running with Docker

This project is fully Dockerized! To run the application locally without dealing with system dependencies, simply ensure you have Docker and Docker Compose installed and run:

`ash
docker-compose up --build
`
This will automatically build the containers, install all necessary dependencies, and spin up the environment.
