# tkinter in object oriented python
import tkinter as tk
from tkinter import ttk # Kind of like CSS for tkinter
# Looks good on windows, but kinda funny on linux (maybe don't use then)

import urllib # standard python library
import json # standard python library
import pandas as pd # sudo -H pip3 install pandas
import numpy as np # already had it (otherwise to find it)

import matplotlib # sudo apt-get install python3-matplotlib
matplotlib.use("TkAgg") # Spin up TK backend for matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
# from matplotlib.figure import Figure # use plt.figure()
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc


# Constants
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
LIGHT_COLOR = "#00A3E0"
DARK_COLOR = "#183A54"
style.use("ggplot")
# Typical matplotlib code
# f = Figure(figsize=(10,6), dpi=100)
f = plt.figure()
# a = f.add_subplot(111)

# Globals - Defaults
# #Exchange
exchange = "BTC-e"
datCounter = 9000 # ms
program_name = "btce"
# #TimeFrame
dataPace = "tick"
# #SampleSize
resampleSize = "15m"
candleWidth = 0.008
# #Indicators
topIndicator = "none"
mainIndicator = "none"
bottomIndicator = "none"
EMAs = []
SMAs = []
# Animation
chartLoad = True
paneCount = 1


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(popup, text="OK", command=popup.destroy)
    b1.pack()
    popup.mainloop()


def tutorial():
    # This is how to create a guided tutorial with different windows
    # I wonder if I could use coroutines here to send messages to the tutorial
    # windows when the desired task is done
    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title("Part 3")
            label = ttk.Label(tut3, text="Part 3", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            b1 = ttk.Button(tut3, text="Done", command=tut3.destroy)
            b1.pack()
            tut3.mainloop()

        tut2.wm_title("Part 2")
        label = ttk.Label(tut2, text="Part 2", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(tut2, text="Next", command=page3)
        b1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="Part 1", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(tut, text="Overview", command=page2)
    b1.pack()
    b2 = ttk.Button(tut, text="Trading", command=lambda: popupmsg("N/A"))
    b2.pack()
    b3 = ttk.Button(tut, text="Indicators", command=lambda: popupmsg("N/A"))
    b3.pack()
    tut.mainloop()


def changeTimeFrame(tf):
    global dataPace
    global datCounter

    if tf == "7d" and resampleSize == "1m":
        popupmsg("Too much data!\nChoose a smaller TimeFrame or higher Interval")
    else:
        dataPace = tf
        datCounter = 9000 # force and update


def changeSampleSize(size, width):
    global resampleSize
    global datCounter
    global candleWidth

    if dataPace == "7d" and size == "1m":
        popupmsg("Too much data!\nChoose a smaller TimeFrame or higher Interval")
    elif dataPace == "tick":
        popupmsg("Currently viewing tick data, not OHLC")
    else:
        resampleSize = size
        candleWidth = width
        datCounter = 9000 # force and update


def changeExchange(disp_name, prog_name):
    global exchange
    global datCounter
    global program_name

    exchange = disp_name
    program_name = prog_name
    datCounter = 9000 # force and update


def addTopIndicator(indicator):
    global topIndicator
    global datCounter

    if dataPace == "tick":
        popupmsg("Currently viewing tick data, indicators not available")

    elif indicator == "none":
        topIndicator = indicator
        datCounter = 9000

    elif indicator == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")

        label = ttk.Label(rsiQ, text="Choose how many periods for each RSI calc")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        # Could be replace with a coroutine
        def callback():
            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(int(periods))

            topIndicator = group
            datCounter = 9000

            print("Set top indicator to", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        rsiQ.mainloop() # in tutorial he uses tk.mainloop() does it matter?

    elif indicator == "macd":
        topIndicator = "macd"
        datCounter = 9000


def addMainIndicator(indicator):
    global mainIndicator
    global datCounter

    if dataPace == "tick":
        popupmsg("Currently viewing tick data, indicators not available")

    elif indicator != "none":
        if mainIndicator == "none":
            if indicator == "sma":
                midQ = tk.Tk()
                midQ.wm_title("Periods?")

                label = ttk.Label(midQ, text="Choose periods for SMA")
                label.pack(side="top", fill="x", pady=10)

                e = ttk.Entry(midQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    mainIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    mainIndicator.append(group)
                    datCounter = 9000

                    print("main indicator set to", mainIndicator)
                    midQ.destroy()

                b = ttk.Button(midQ, text="Submit", width=10, command=callback)
                b.pack()
                midQ.mainloop()

            elif indicator == "ema":
                midQ = tk.Tk()
                midQ.mw_title("Periods?")

                label = ttk.Label(midQ, text="Choose periods for EMA")
                label.pack(side="top", fill="x", pady=10)

                e = ttk.Entry(midQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    mainIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    mainIndicator.append(group)
                    datCounter = 9000

                    print("main indicator set to", mainIndicator)
                    midQ.destroy()

                b = ttk.Button(midQ, text="Submit", width=10, command=callback)
                b.pack()
                midQ.mainloop()

        else: # mainIndicator has values
            if indicator == "sma":
                midQ = tk.Tk()
                midQ.wm_title("Periods?")

                label = ttk.Label(midQ, text="Choose periods for SMA")
                label.pack(side="top", fill="x", pady=10)

                e = ttk.Entry(midQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    mainIndicator.append(group)
                    datCounter = 9000

                    print("main indicator set to", mainIndicator)
                    midQ.destroy()

                b = ttk.Button(midQ, text="Submit", width=10, command=callback)
                b.pack()
                midQ.mainloop()

            elif indicator == "ema":
                midQ = tk.Tk()
                midQ.wm_title("Periods?")

                label = ttk.Label(midQ, text="Choose periods for EMA")
                label.pack(side="top", fill="x", pady=10)

                e = ttk.Entry(midQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    mainIndicator.append(group)
                    datCounter = 9000

                    print("main indicator set to", mainIndicator)
                    midQ.destroy()

                b = ttk.Button(midQ, text="Submit", width=10, command=callback)
                b.pack()
                midQ.mainloop()
    else:
        mainIndicator = "none"


def addBottomIndicator(indicator):
    global bottomIndicator
    global datCounter

    if dataPace == "tick":
        popupmsg("Currently viewing tick data, indicators not available")

    elif indicator == "none":
        bottomIndicator = indicator
        datCounter = 9000

    elif indicator == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")

        label = ttk.Label(rsiQ, text="Choose how many periods for each RSI calc")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        # Could be replace with a coroutine
        def callback():
            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(int(periods))

            bottomIndicator = group
            datCounter = 9000

            print("Set bottom indicator to", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        rsiQ.mainloop() # in tutorial he uses tk.mainloop() does it matter?

    elif indicator == "macd":
        bottomIndicator = "macd"
        datCounter = 9000


def loadChart(run):
    global chartLoad

    if run == "start":
        chartLoad = True
    elif run == "stop":
        chartLoad = False


def animate(i):
    global refreshrate
    global datCounter
    global chartLoad
    global paneCount
    global exchange
    global program_name

    if chartLoad:
        if paneCount == 1:
            if dataPace == "tick":
                try:
                    if exchange == "BTC-e":
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan = 4)
                        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan = 4, sharex = a)

                        dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)
                        data = data["btc_usd"]
                        data = pd.DataFrame(data) # turn into a pandas dataset

                        data["datestamp"] = np.array(data["timestamp"].astype("datetime64[s]"))
                        allDates = data["datestamp"].tolist()

                        # format buys datasets
                        buys = data[(data["type"]=="bid")]
                        buyDates = (buys["datestamp"].tolist())

                        # format sells datasets
                        sells = data[(data["type"]=="ask")]
                        sellsDates = (sells["datestamp"].tolist())

                        volume = data["amount"]

                        a.clear()

                        a.plot_date(buyDates, buys["price"], LIGHT_COLOR, label="buys")
                        a.plot_date(sellsDates, sells["price"], DARK_COLOR, label="sells")

                        a2.fill_between(allDates, 0, volume, facecolor=DARK_COLOR)

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)

                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2,
                                borderaxespad=0)

                        title = "BTC-e BTCUSD Prices\nLast Price:{}".format(data["price"][1999])
                        a.set_title(title)

                        priceData = data["price"].apply(float).tolist()
                    elif exchange == "Bitstamp":
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan = 4)
                        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan = 4, sharex = a)

                        dataLink = 'https://www.bitstamp.net/api/transactions/'
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)
                        data = pd.DataFrame(data) # turn into a pandas dataset

                        data["datestamp"] = np.array(data["date"].apply(int)).astype("datetime64[s]")
                        allDates = data["datestamp"].tolist()

                        volume = data["amount"].apply(float).tolist()

                        a.clear()

                        a.plot_date(allDates, data["price"], LIGHT_COLOR, label="data")
                        a2.fill_between(allDates, 0, volume, facecolor=DARK_COLOR)

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)

                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2,
                                borderaxespad=0)

                        title = "Bitstamp BTCUSD Prices\nLast Price:{}".format(data["price"][0])
                        a.set_title(title)

                        priceData = data["price"].apply(float).tolist()
                    elif exchange == "Bitfinex":
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan = 4)
                        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan = 4, sharex = a)

                        dataLink = 'https://api.bitfinex.com/v1/trades/btcusd?limit=2000'
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)
                        data = pd.DataFrame(data) # turn into a pandas dataset

                        data["datestamp"] = np.array(data["timestamp"].astype("datetime64[s]"))
                        allDates = data["datestamp"].tolist()

                        # format buys datasets
                        buys = data[(data["type"]=="buy")]
                        buyDates = (buys["datestamp"].tolist())

                        # format sells datasets
                        sells = data[(data["type"]=="sell")]
                        sellsDates = (sells["datestamp"].tolist())

                        volume = data["amount"].apply(float).tolist()

                        a.clear()

                        a.plot_date(buyDates, buys["price"], LIGHT_COLOR, label="buys")
                        a.plot_date(sellsDates, sells["price"], DARK_COLOR, label="sells")
                        plt.setp(a.get_xticklabels(), visible=False)

                        a2.fill_between(allDates, 0, volume, facecolor=DARK_COLOR)

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2,
                                borderaxespad=0)

                        title = "Bitfinex BTCUSD Prices\nLast Price:{}".format(data["price"][0])
                        a.set_title(title)

                        priceData = data["price"].apply(float).tolist()
                    elif exchange == "Huobi":
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=6, colspan=4)
                        dataLink = "http://seaofbtc.com/api/basic/price?key=1&tf=1d&exchange=" + program_name
                        data = urllib.request.urlopen(dataLink).read()
                        data = data.decode()
                        data = json.loads(data)

                        dateStamp = np.array(data[0]).astype("datetime64[s]")
                        dateStamp = dateStamp.tolist()

                        df = pd.DataFrame({"DateTime":dateStamp})
                        df["Price"] = data[1]
                        df["Volume"] = data[2]
                        df["Symobl"] = "BTCUSD"
                        df["MPLDate"] = df["DateTime"].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        df = df.set_index("DateTime")

                        a.plot_date(df["MPLDate"][-4500:], df["Price"][-4500:], LIGHT_COLOR, label="Price")

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))

                        title = "Huobi BTCUSD Prices\nLast Price:{}".format(df["Price"][-1])
                        a.set_title(title)

                        priceData = data["price"].apply(float).tolist()
                except Exception as e:
                    print("Failed because of", e)
            else:
                # prevent the plot from redrawing too often
                if datCounter > 12:
                    try:
                        if exchange == "Huobi":
                            if topIndicator != "none":
                                a = plt.subplot2grid((6, 4), (1, 0), rowspan=1, colspan=4)
                                a2 = plt.subplot2grid((6, 4), (0, 0), rowspan=1, colspan=4, sharex=a)
                            else:
                                a = plt.subplot2grid((6, 4), (0, 0), rowspan=1, colspan=4)
                        else: # Not Huobi
                            if topIndicator != "none" and bottomIndicator != "none":
                                # Main Graph
                                a = plt.subplot2grid((6, 4), (1, 0), rowspan=3, colspan=4)
                                # Volume Graph
                                a2 = plt.subplot2grid((6, 4), (4, 0), rowspan=1, colspan=4, sharex=a)
                                # Bottom Indicator
                                a3 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)
                                # Top Indicator
                                a0 = plt.subplot2grid((6, 4), (0, 0), rowspan=1, colspan=4, sharex=a)
                            elif topIndicator != "none":
                                # Main Graph
                                a = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4)
                                # Volume Graph
                                a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)
                                # Top Indicator
                                a0 = plt.subplot2grid((6, 4), (0, 0), rowspan=1, colspan=4, sharex=a)
                            elif bottomIndicator != "none":
                                # Main Graph
                                a = plt.subplot2grid((6, 4), (0, 0), rowspan=4, colspan=4)
                                # Volume Graph
                                a2 = plt.subplot2grid((6, 4), (4, 0), rowspan=1, colspan=4, sharex=a)
                                # Bottom Indicator
                                a3 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)
                            else:
                                # Main Graph
                                a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                                # Volume Graph
                                a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)
                        # Acquire the data from SeaofBTC (Normalized data)
                        data = urllib.request.urlopen("http://seaofbtc.com/api/basic/price?key=1&tf="+dataPace+"&exchange="+program_name).read()
                        data = data.decode()
                        data = json.loads(data)

                        dateStamp = np.array(data[0]).astype("datetime64[s]")
                        dateStamp = dateStamp.tolist()

                        # create pandas data frame
                        df = pd.DataFrame({"DateTime": dateStamp})
                        df["Price"] = data[1]
                        df["Volume"] = data[2]
                        df["Symbol"] = "BTCUSD"
                        df["MPLDate"] = df["DateTime"].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        df = df.set_index("DateTime")

                        #generate OHLC
                        OHLC = df["Price"].resample(resampleSize, how="ohlc")
                        OHLC = OHLC.dropna() # Drop nan's

                        volumeData = df["Volume"].resample(resampleSize, how={"volume":"sum"})

                        OHLC["dateCopy"] = OHLC.index
                        OHLC["MPLDates"] = OHLC["dateCopy"].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        del OHLC["dateCopy"]

                        volumeData["dateCopy"] = volumeData.index
                        volumeData["MPLDates"] = volumeData["dateCopy"].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        del volumeData["dateCopy"]

                        priceData = OHLC["close"].apply(float).tolist()

                        a.clear()

                        # Start plotting
                        if mainIndicator != "none":
                            for eachMA in mainIndicator:
                                if eachMa[0] == "sma":
                                    sma = pd.rolling_mean(OHLC["cloase"], eachMA[1])
                                    label = str(eachMA[1])+" SMA"
                                    a.plot(OHLC["MPLDates"], sma, label=label)
                                if eachMa[0] == "ema":
                                    ewma = pd.stats.moments.ewma
                                    label = str(eachMA[1])+" EMA"
                                    a.plot(OHLC["MPLDates"], ewma(OHLC["close"], eachMA[1]), label=label)

                            a.legend(loc=0)

                        if topIndicator[0] == "rsi":
                            rsiIndicator(priceData, "top")
                        elif topIndicator == "macd":
                            try:
                                computeMACD(priceData, location="top")
                            except Exception as e:
                                print(str(e))

                        if bottomIndicator[0] == "rsi":
                            rsiIndicator(priceData, "bottom")
                        elif bottomIndicator == "macd":
                            try:
                                computeMACD(priceData, location="bottom")
                            except Exception as e:
                                print(str(e))

                        csticks = candlestick_ohlc(a, OHLC[["MPLDates", "open", "high", "low", "close"]].values, width=candleWidth, colorup=LIGHT_COLOR, colordown=DARK_COLOR)
                        a.set_ylabel("Price")
                        if exchange != "Huobi":
                            a2.fill_between(volumeData["MPLDates"], 0, volumeData["volume"], facecolor=DARK_COLOR)
                            a2.set_ylabel("Volume")

                        a.xaxis.set_major_locator(mticker.MaxNLocator(3))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

                        if exchange != "Huobi":
                            plt.setp(a.get_xticklabels(), visible=False)

                        if topIndicator != "none":
                            plt.setp(a0.get_xticklabels(), visible=False)

                        if bottomIndicator != "none":
                            plt.setp(a2.get_xticklabels(), visible=False)

                        x = (len(OHLC["close"])) - 1 # ID of last element
                        if dataPace == "1d":
                            title = exchange + " 1 Day Data with " + resampleSize + " Bars\nLast Price: {}".format(OHLC["close"][x])
                        if dataPace == "3d":
                            title = exchange + " 3 Day Data with " + resampleSize + " Bars\nLast Price: {}".format(OHLC["close"][x])
                        if dataPace == "7d":
                            title = exchange + " 7 Day Data with " + resampleSize + " Bars\nLast Price: {}".format(OHLC["close"][x])

                        if topIndicator != "none":
                            a0.set_title(title)
                        else:
                            a.set_title(title)

                        datCounter = 0
                    except Exception  as e:
                        print("failed because of", e)
                        datCounter = 9000
                else:
                    datCounter += 1

    # #OLD METHOD
    # # Populate data
    # pullData = open("sampleData.txt", "r").read()
    # dataList = pullData.split('\n')
    # xList = []
    # yList = []
    # for line in dataList:
    #     if len(line) > 1:
    #         x, y = line.split(',')
    #         xList.append(int(x))
    #         yList.append(int(y))
    # # draw data to plot
    # a.clear()
    # a.plot(xList, yList)


class SeaofBTCapp(tk.Tk): # Inherits from tk.Tk
    # Class Constructor
    def __init__(self, *args, **kwargs):
        # Initialize Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # style settings
        #tk.Tk.iconbitmap(self,
        # default="C:\\Users\\jdmaxwell\\Documents\\scripts\\test.ico")
        # needs to acutally be .ico
        tk.Tk.wm_title(self, "Sea of BTC client")
        # fill-> fill given space, expand-> spill over to empty space
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create menu bar
        menubar = tk.Menu(container)

        #tearoff=1 lets you make a new window from the menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings",
                            command=lambda: popupmsg("Not supported yet"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="BTC-e",
                            command=lambda: changeExchange("BTC-e", "btce"))
        exchangeChoice.add_command(label="Bitfinex",
                            command=lambda: changeExchange("Bitfinex", "bitfinex"))
        exchangeChoice.add_command(label="Bitstamp",
                            command=lambda: changeExchange("Bitstamp", "bitstamp"))
        exchangeChoice.add_command(label="Huobi",
                            command=lambda: changeExchange("Huobi", "huobi"))
        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        dataTimeFrame = tk.Menu(menubar, tearoff=1)
        dataTimeFrame.add_command(label="Tick",
                                command=lambda: changeTimeFrame('tick'))
        dataTimeFrame.add_command(label="1 Day",
                                command=lambda: changeTimeFrame('1d'))
        dataTimeFrame.add_command(label="3 Day",
                                command=lambda: changeTimeFrame('3d'))
        dataTimeFrame.add_command(label="1 Week",
                                command=lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label="Data Time Frame", menu=dataTimeFrame)

        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label="Tick",
                            command=lambda: changeTimeFrame('tick'))
        OHLCI.add_command(label="1 Min",
                            command=lambda: changeSampleSize('1m', 0.0005))
        OHLCI.add_command(label="5 Min",
                            command=lambda: changeSampleSize('5m', 0.003))
        OHLCI.add_command(label="15 Min",
                            command=lambda: changeSampleSize('15m', 0.008))
        OHLCI.add_command(label="30 Min",
                            command=lambda: changeSampleSize('30m', 0.016))
        OHLCI.add_command(label="1 Hr",
                            command=lambda: changeSampleSize('1h', 0.032))
        OHLCI.add_command(label="3 Hr",
                            command=lambda: changeSampleSize('3h', 0.096))
        menubar.add_cascade(label="OHLC Interval", menu=OHLCI)

        topIndicator = tk.Menu(menubar, tearoff=1)
        topIndicator.add_command(label="None",
                                command=lambda: addTopIndicator("none"))
        topIndicator.add_command(label="RSI",
                                command=lambda: addTopIndicator("rsi"))
        topIndicator.add_command(label="MACD",
                                command=lambda: addTopIndicator("macd"))
        menubar.add_cascade(label="Top Indicator", menu=topIndicator)

        mainIndicator = tk.Menu(menubar, tearoff=1)
        mainIndicator.add_command(label="None",
                                command=lambda: addMainIndicator("none"))
        mainIndicator.add_command(label="SMA",
                                command=lambda: addMainIndicator("sma"))
        mainIndicator.add_command(label="EMA",
                                command=lambda: addMainIndicator("ema"))
        menubar.add_cascade(label="Main(middle) Indicator", menu=mainIndicator)

        bottomIndicator = tk.Menu(menubar, tearoff=1)
        bottomIndicator.add_command(label="None",
                                command=lambda: addBottomIndicator("none"))
        bottomIndicator.add_command(label="RSI",
                                command=lambda: addBottomIndicator("rsi"))
        bottomIndicator.add_command(label="MACD",
                                command=lambda: addBottomIndicator("macd"))
        menubar.add_cascade(label="Bottom Indicator", menu=bottomIndicator)

        tradeButton = tk.Menu(menubar, tearoff=1)
        tradeButton.add_command(label="Manual Trading",
                                command=lambda: popupmsg("NOT LIVE YET."))
        tradeButton.add_command(label="Automatic Trading",
                                command=lambda: popupmsg("NOT LIVE YET."))
        tradeButton.add_separator()
        tradeButton.add_command(label="Quick Buy",
                                command=lambda: popupmsg("NOT LIVE YET."))
        tradeButton.add_command(label="Quick Sell",
                                command=lambda: popupmsg("NOT LIVE YET."))
        tradeButton.add_separator()
        tradeButton.add_command(label="Configure Quick Buy / Sell",
                                command=lambda: popupmsg("NOT LIVE YET."))
        menubar.add_cascade(label="Trading", menu=tradeButton)

        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume",command=lambda: loadChart("start"))
        startStop.add_command(label="Pause",command=lambda: loadChart("stop"))
        menubar.add_cascade(label="Resume/Pause client", menu=startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=tutorial)
        helpmenu.add_command(label="About", command=lambda: popupmsg("ABOUT"))
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)

        # Create a dictionary to hold all frames (views)
        self.frames = { }
        # Add all pages to frames dictionary
        for Page in (StartPage, BTCePage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # display the passed frame
        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise() # Tk method to bring the frame to the front


class StartPage(tk.Frame): # Inherits from tk.Frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="EULA Page...\n...\n...\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(BTCePage))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.pack()


class BTCePage(tk.Frame):
    # Pulling data from btc-e.com/api public API
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # Bring graph to the forground to display it
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Set up the toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        # This line doesn't seem to need to be there, it works without it
        # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# Start running tkinter app
if __name__ == "__main__":
    app = SeaofBTCapp()
    app.geometry("1280x720")
    # Will be threaded eventually
    ani = animation.FuncAnimation(f, animate, interval=2000) # interval is in ms
    app.mainloop()
