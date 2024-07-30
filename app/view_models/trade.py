"""
交易数据的视图
"""
__author__ = 'JOJO'


def _map_to_trade(single):
    return dict(
        user_name=single.user.nickname,
        time=single.create_datetime.strftime('%Y-%m-%d'),
        id=single.id
    )


class TradeInfo:
    def __init__(self, trades):
        self.total = 0
        self.trades = []
        # trades是字典
        self._parse(trades)

    def _parse(self, trades):
        self.total = len(trades)
        self.trades = [_map_to_trade(gift) for gift in trades]
