# config file for Backtest
data_path = '../../../../export/scratch/for_yifan/research/'

start_date = '20170103'          # min date is 20170103
end_date = '20200821'            # max date is 20200821

# strategy param
capital = 100000000              # total capital
times = ['open', 'close']        # available time to trade

longshort = {
        'bond':[1],              # long only
        'stock':[1, -1]          # long & short
}

fee_rate = {
        'bond':0.0001,           # 0.01% transaction cost (buy/sell)
        'stock':0.0001,          # 0.01% transaction cost (buy/sell)
        'lending': 0.1,          # stock annual lending cost
        'selling': 0.001,        # 0.1% stock selling tax
}

cbond_min_share = 10             # minimum trading volume of convertible bond
stock_min_share = 100            # minimum trading volume of stock

valid_both = True                # required 'valid' status for both convertible bond and stock if trade any of them

# analysis param
annual_date = 250                # annual trading day　　　　 
riskfree_rate = 0.04             # annual risk-free rate

# 359 available tickers
cbond_tickers = [
               '110033.SH', '128011.SZ', '110031.SH', '113010.SH', '127003.SZ',
               '128009.SZ', '110034.SH', '128013.SZ', '123001.SZ', '128012.SZ',
               '110030.SH', '110032.SH', '113009.SH', '113011.SH', '113012.SH',
               '113008.SH', '128014.SZ', '127004.SZ', '128015.SZ', '113013.SH',
               '128016.SZ', '113014.SH', '113015.SH', '113016.SH', '113502.SH',
               '128017.SZ', '110038.SH', '128019.SZ', '128018.SZ', '110039.SH',
               '110040.SH', '128020.SZ', '123002.SZ', '128023.SZ', '128021.SZ',
               '128022.SZ', '128025.SZ', '113503.SH', '128026.SZ', '110041.SH',
               '128024.SZ', '113017.SH', '110042.SH', '128029.SZ', '123003.SZ',
               '128028.SZ', '128027.SZ', '128032.SZ', '123004.SZ', '123007.SZ',
               '128033.SZ', '128030.SZ', '123006.SZ', '123005.SZ', '113018.SH',
               '128034.SZ', '128035.SZ', '123009.SZ', '128036.SZ', '127005.SZ',
               '110043.SH', '123008.SZ', '113019.SH', '113504.SH', '113505.SH',
               '128038.SZ', '128037.SZ', '113507.SH', '127006.SZ', '113506.SH',
               '113508.SH', '113509.SH', '128039.SZ', '113511.SH', '113510.SH',
               '128040.SZ', '110044.SH', '113512.SH', '113513.SH', '110045.SH',
               '127007.SZ', '113514.SH', '123010.SZ', '123011.SZ', '128041.SZ',
               '113516.SH', '123013.SZ', '123014.SZ', '113517.SH', '128043.SZ',
               '113515.SH', '123012.SZ', '128042.SZ', '128044.SZ', '123015.SZ',
               '128045.SZ', '113518.SH', '128046.SZ', '113520.SH', '128048.SZ',
               '113519.SH', '123016.SZ', '113521.SH', '128047.SZ', '110047.SH',
               '113522.SH', '113020.SH', '110046.SH', '128049.SZ', '123017.SZ',
               '127008.SZ', '113523.SH', '128050.SZ', '110048.SH', '113524.SH',
               '128051.SZ', '113525.SH', '110049.SH', '110050.SH', '128052.SZ',
               '123018.SZ', '113526.SH', '127010.SZ', '113527.SH', '127009.SZ',
               '128053.SZ', '128054.SZ', '113021.SH', '113528.SH', '128056.SZ',
               '110051.SH', '123019.SZ', '123021.SZ', '113022.SH', '123020.SZ',
               '110052.SH', '128059.SZ', '128057.SZ', '113529.SH', '128055.SZ',
               '110053.SH', '127011.SZ', '110055.SH', '128058.SZ', '110054.SH',
               '123022.SZ', '128060.SZ', '110056.SH', '123023.SZ', '123024.SZ',
               '113530.SH', '123025.SZ', '113531.SH', '128062.SZ', '128061.SZ',
               '113532.SH', '113533.SH', '128063.SZ', '113024.SH', '110057.SH',
               '113534.SH', '127012.SZ', '113025.SH', '128064.SZ', '110058.SH',
               '113026.SH', '128065.SZ', '128066.SZ', '127013.SZ', '128067.SZ',
               '113535.SH', '113536.SH', '128068.SZ', '123026.SZ', '123027.SZ',
               '113537.SH', '113028.SH', '113027.SH', '128069.SZ', '123028.SZ',
               '113538.SH', '128070.SZ', '113539.SH', '113540.SH', '113541.SH',
               '113542.SH', '113543.SH', '123029.SZ', '128073.SZ', '123030.SZ',
               '128071.SZ', '128072.SZ', '123031.SZ', '113544.SH', '128074.SZ',
               '128075.SZ', '123032.SZ', '128077.SZ', '113545.SH', '128076.SZ',
               '128078.SZ', '110059.SH', '128079.SZ', '113546.SH', '127014.SZ',
               '113548.SH', '113547.SH', '123033.SZ', '110060.SH', '123034.SZ',
               '110061.SH', '123035.SZ', '128080.SZ', '113549.SH', '113551.SH',
               '113550.SH', '128081.SZ', '113552.SH', '110062.SH', '128083.SZ',
               '110063.SH', '128082.SZ', '113029.SH', '113553.SH', '128085.SZ',
               '113556.SH', '113559.SH', '123036.SZ', '128084.SZ', '113554.SH',
               '128086.SZ', '113557.SH', '110065.SH', '113555.SH', '113558.SH',
               '110064.SH', '128087.SZ', '128088.SZ', '128091.SZ', '113030.SH',
               '128093.SZ', '128089.SZ', '123037.SZ', '128092.SZ', '123038.SZ',
               '128090.SZ', '123039.SZ', '123040.SZ', '127015.SZ', '113562.SH',
               '113561.SH', '123041.SZ', '123042.SZ', '113031.SH', '128094.SZ',
               '113563.SH', '128095.SZ', '128096.SZ', '113565.SH', '113564.SH',
               '128097.SZ', '113032.SH', '128098.SZ', '110066.SH', '123043.SZ',
               '113566.SH', '113571.SH', '113568.SH', '113567.SH', '113569.SH',
               '113570.SH', '110067.SH', '128100.SZ', '113572.SH', '128099.SZ',
               '123045.SZ', '128101.SZ', '123044.SZ', '110068.SH', '128102.SZ',
               '123046.SZ', '123047.SZ', '113033.SH', '128103.SZ', '113574.SH',
               '128104.SZ', '113575.SH', '113034.SH', '110069.SH', '113576.SH',
               '128106.SZ', '123048.SZ', '123049.SZ', '113577.SH', '110070.SH',
               '128105.SZ', '127016.SZ', '123050.SZ', '113578.SH', '113581.SH',
               '113580.SH', '113579.SH', '113573.SH', '128107.SZ', '113035.SH',
               '128108.SZ', '113583.SH', '113582.SH', '128109.SZ', '113584.SH',
               '123051.SZ', '123053.SZ', '127017.SZ', '123052.SZ', '123054.SZ',
               '128111.SZ', '113586.SH', '113585.SH', '128110.SZ', '128112.SZ',
               '123055.SZ', '113588.SH', '113587.SH', '128114.SZ', '128113.SZ',
               '128115.SZ', '113589.SH', '128117.SZ', '113591.SH', '123056.SZ',
               '128116.SZ', '123057.SZ', '113590.SH', '110071.SH', '113592.SH',
               '127018.SZ', '128118.SZ', '113036.SH', '128121.SZ', '128119.SZ',
               '123058.SZ', '113593.SH', '127019.SZ', '123059.SZ', '127020.SZ',
               '123060.SZ', '128120.SZ', '113037.SH', '128122.SZ', '123062.SZ',
               '123061.SZ', '113595.SH', '128123.SZ', '113596.SH', '128124.SZ',
               '110073.SH', '123063.SZ', '113597.SH', '128125.SZ']




