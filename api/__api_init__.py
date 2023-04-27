try:
    from api.routes.backtest import BacktestAPI
    from api.routes.evaluate import EvaluationAPI
    from api.routes.metrics import MetricsAPI
    from api.routes.predict import predictAPI
    from api.routes.profit import profitAPI
    from api.routes.roi import roiAPI
    from api.routes.sharpe_ratio import sharpeRatioAPI
    from api.routes.status import statusAPI
    from api.routes.stop import stopAPI
    from api.routes.train import trainAPI
except ImportError as e:
    ImportError("API Route Import: /api/__api_init__.py: ", e)

class API:
    def Backtest(ticker):
        return BacktestAPI.backtest(ticker)
    def Evaluate():
        return EvaluationAPI.evaluate()
    def Metrics():
        return MetricsAPI.metrics()
    def Predict(label, **features):
        return predictAPI.predict(label, features)
    def Profit():
        return profitAPI.profit()
    def ROI(investment, net):
        return roiAPI.roi(investment, net)
    def SHARPE_RATION():
        return sharpeRatioAPI.sharpe_ratio()
    def Status():
        return statusAPI.status()
    def Stop():
        return stopAPI.stop()
    def Train(**features):
        return trainAPI.train(features)
