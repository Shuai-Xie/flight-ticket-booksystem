# income List 的 数据类型
class IncomeMetric:
    metric = '00'  # 时间段度量标准
    flight_sum = 0
    income = 0

    def __init__(self, metric, flight_sum, income):
        self.metric = metric
        self.flight_sum = flight_sum
        self.income = income


# 订单信息
class Order:
    passenger_name = ''
    flight_name = ''
    flight_route = ''
    flight_ltime = ''
    flight_price = ''

    def __init__(self, pname, fname, froute, fltime, fprice):
        self.passenger_name = pname
        self.flight_name = fname
        self.flight_route = froute
        self.flight_ltime = fltime
        self.flight_price = fprice
