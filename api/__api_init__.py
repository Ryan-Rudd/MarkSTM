from api.routes.backtest import BacktestAPI
from api.routes.evaluate import EvaluationAPI
from api.routes.metrics import MetricsAPI
from api.routes.predict import predictAPI
from api.routes.profit import profitAPI
from api.routes.roi import roiAPI

class API:
    def Backtest(ticker):
        BacktestAPI.backtest(ticker)
    def Evaluate():
        EvaluationAPI.evaluate()
    def Metrics():
        MetricsAPI.metrics()
    def Predict(label, **features):
        predictAPI.predict(label, features)
    def Profit():
        profitAPI.profit()
    def ROI():
        roiAPI.()