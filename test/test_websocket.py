import time
from unittest import TestCase

import zb
from zb.errors import ZbApiException
from zb.model.subscribe_envet import *


class TestSubscriptionClient(TestCase):
    api = zb.MarketClient(url='ws://ttfutures.zb.com/ws/public/v1',
                          connection_delay_failure=5)

    def test_whole_depth_event(self):
        def callback(event: DepthEvent):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_whole_depth_event(symbol='btc_usdt', callback=callback, scale=0.01, error_handler=error_handler)
        time.sleep(60)

    def test_depth_event(self):
        def callback(event: DepthEvent):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_depth_event(symbol='btc_usdt', callback=callback, error_handler=error_handler)
        time.sleep(60)

    def test_subscribe_kline_event(self):
        def callback(event: KlineEvent):
            print(">>  " + str(event))

        self.api.subscribe_kline_event(symbol='btc_usdt', interval=Interval.MIN_15, callback=callback)

        time.sleep(50)

    def test_subscribe_trade_event(self):
        def callback(event: TradeEvent):
            print(">>  " + str(event))

        self.api.subscribe_trade_event(symbol='btc_usdt', callback=callback)
        time.sleep(60)

    def test_subscribe_ticker_event(self):
        def callback(event: TickerEvent):
            print(">>  " + str(event))

        self.api.subscribe_ticker_event(symbol='btc_usdt', callback=callback)
        time.sleep(60)

    def test_all_subscribe_ticker_event(self):
        def callback(event: TickerEvent):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_all_ticker_event(callback=callback, error_handler=error_handler)
        time.sleep(60)

    def test_mark_price_event(self):
        def callback(event: Event):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_mark_price_event(symbol='btc_usdt', callback=callback, error_handler=error_handler)
        time.sleep(120)

    def test_subscribe_all_mark_price_event(self):
        def callback(event: Event):
            print(">>  ", str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_all_mark_price_event(callback=callback, error_handler=error_handler)
        time.sleep(120)

    def test_subscribe_mark_kline_event(self):
        def callback(event: Event):
            print(">>  ", str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_mark_kline_event(symbol='btc_usdt', callback=callback, error_handler=error_handler)
        time.sleep(120)

    def test_subscribe_fund_rate_event(self):
        def callback(event: Event):
            print(">>  ", event.channel, str(event.data))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_fund_rate_event(symbol='btc_usdt', callback=callback, error_handler=error_handler)
        time.sleep(120)

    def test_subscribe_spot_price_event(self):
        def callback(event: Event):
            print(">>  ", event.channel, str(event.data))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_spot_price_event(symbol='all', callback=callback, error_handler=error_handler)
        time.sleep(120)

    def test_unsubscribe_event(self):
        def callback(event: Event):
            print(">>  " + str(event))

        conn_id = self.api.subscribe_spot_price_event(symbol='all', callback=callback)

        time.sleep(5)
        print(">>>> unsubscribe event")
        self.api.unsubscribe_event(conn_id=conn_id, channel='All.bidsSpotPrice')
        print(self.api.connections)

        time.sleep(10)


class TestWsAccountClient(TestCase):
    api = zb.WsAccountClient(api_key='8da1a454-2f07-48e7-b268-72582fb72794',
                             secret_key='d67355ca-3e20-41fc-8e14-bfdf506f72fc',
                             url='ws://ttfutures.zb.com/ws/private/api/v2', )

    def test_login(self):
        def callback(event: DepthEvent):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.login()
        time.sleep(2)
        print(">>>> start")
        self.api.subscribe_fund_change('btc', None)
        time.sleep(60)

    def test_get_balance(self):
        def callback(event: Event):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.get_balance(currency='btc', callback=callback, error_handler=error_handler)
        self.api.get_bill(currency='btc', callback=callback, error_handler=error_handler)
        time.sleep(60)

    def test_get_bill(self):
        def callback(event: Event):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.get_bill(currency='eth',
                          start_time=1629450718756,
                          callback=callback,
                          error_handler=error_handler)
        time.sleep(60)

    def test_subscribe_asset_change(self):
        def callback(event: Event):
            print(">>  " + str(event))

        def error_handler(error: ZbApiException):
            print("error", error)

        self.api.subscribe_asset_change(
            callback=callback,
            error_handler=error_handler)
        time.sleep(6)
        self.api.unsubscribe(self.api.CH_FundAssetChange)

        time.sleep(60)

    def test_get_asset_info(self):
        def callback(event: Event):
            print(">>  " + str(event))

        self.api.login()

        print(">>>> start")
        self.api.get_asset_info(callback=callback)
        time.sleep(60)