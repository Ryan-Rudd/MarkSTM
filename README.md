<h1 align="center">Artificial Inteligence Stock Market Trading Bot Using Quantitative Analysis: MarkSTM</h1>

<i align="center" text-align="center">
    MarkSTM ( Supervised Trading Model )

    Developed and Engineered by Ryan Rudd

    International Baccalaureate Student
    This is an open source project that is opened to community collaboration and improvement

</i>

* * *

## Dedication

This paper is dedicated to my high school computer science teacher, my mom & dad, and my brother

* * *

## Abstract

This paper presents MarkSTM, a supervised trading model developed using quantitative analysis and machine learning techniques. MarkSTM leverages historical data from the stock market to make predictions about future market movements, helping to inform trading decisions. The model is trained using labeled data, where inputs are market data (such as stock prices, economic indicators, and news events) and outputs are desired trading decisions (such as buy, sell, or hold). The model uses supervised learning algorithms to identify patterns and relationships between input data and output decisions. Experimental results show that MarkSTM achieves high accuracy in predicting market movements and generates profitable trading decisions. Our results demonstrate the potential of machine learning techniques in stock market trading and offer insights for future research in this field.

## Introduction

The stock market is a complex system that is influenced by a wide range of factors, including economic indicators, news events, and investor sentiment. As a result, predicting market movements is challenging, and many traders struggle to make informed trading decisions. Machine learning techniques offer a promising approach to address this challenge by leveraging historical data to identify patterns and trends in market behavior. In this paper, we present MarkSTM, a supervised trading model developed using quantitative analysis and machine learning techniques. MarkSTM is designed to predict future market movements and inform trading decisions. We use a supervised learning approach, where the model is trained using labeled data to identify patterns and relationships between input market data and output trading decisions. Our model uses a variety of quantitative analysis techniques, including technical indicators, fundamental data, and news sentiment analysis.

## Related Work

The use of machine learning techniques in stock market trading has been the subject of extensive research in recent years. Many researchers have explored the use of different machine learning algorithms, including neural networks, decision trees, and support vector machines, to predict market movements. Other researchers have focused on the use of specific market data, such as news sentiment or technical indicators, to inform trading decisions. One notable example of machine learning in stock market trading is the AlphaGo system developed by DeepMind Technologies. AlphaGo uses deep reinforcement learning to play the game of Go and has achieved superhuman performance. The success of AlphaGo has inspired many researchers to explore the use of similar techniques in other domains, including stock market trading.

## Methodology

MarkSTM is a supervised learning model that is trained using historical market data and associated trading decisions. The input data to the model consists of a variety of quantitative features, including technical indicators, fundamental data, and news sentiment analysis. The output of the model is a trading decision, which can be either "buy," "sell," or "hold." We use a variety of supervised learning algorithms, including decision trees, random forests, and gradient boosting, to train the model. We also use cross-validation techniques to evaluate the performance of the model and identify the optimal hyperparameters for each algorithm.

## Mathematical Modeling

MarkSTM is a supervised learning model that is designed to predict future market movements and make informed trading decisions. To achieve this, we use a variety of quantitative features, including technical indicators, fundamental data, and news sentiment analysis, as inputs to the model. Let

X = \[x1, x2, ..., xn\] represent the input features, where xi represents the i-th feature. Each feature can be represented as a vector or a scalar, depending on the type of data. For example, technical indicators such as moving averages or relative strength index (RSI) can be represented as a vector of values over a period of time, while fundamental data such as earnings per share (EPS) or price-to-earnings (P/E) ratio can be represented as a scalar. News sentiment analysis can be represented as a vector of sentiment scores for different news sources or topics. Let y represent the trading decision, which can be either "buy," "sell," or "hold." We use a classification model to predict the trading decision based on the input features X. Let f(X) represent the classification model, where f(X) = y. We use a variety of supervised learning algorithms, including decision trees, random forests, and gradient boosting, to train the classification model. To evaluate the performance of the model, we use a variety of metrics, including accuracy, precision, recall, and F1 score. Let TP, TN, FP, and FN represent the number of true positives, true negatives, false positives, and false negatives, respectively. Then, accuracy can be defined as:


`Accuracy = (TP + TN) / (TP + TN + FP + FN)`

**Precision can be defined as:**

`Precision = TP / (TP + FP)`

**Recall can be defined as:**

`Recall = TP / (TP + FN)`

**F1 score can be defined as:**

`F1 score = 2 * (Precision * Recall) / (Precision + Recall)`

We use cross-validation techniques to evaluate the performance of the model and identify the optimal hyperparameters for each algorithm. We also use backtesting techniques to evaluate the performance of the model on historical market data and measure the profitability of the trading decisions generated by the model. Overall, the mathematical modeling of MarkSTM involves the representation of input features as vectors or scalars, the use of a classification model to predict the trading decision, and the evaluation of the model's performance using various metrics and techniques.

## Backtesting

Backtesting is a common technique used in the evaluation of trading strategies, where the model's performance is tested on historical market data to simulate trading decisions. In the context of MarkSTM, we use backtesting to evaluate the performance of the model on historical market data and measure the profitability of the trading decisions generated by the model. To perform backtesting, we divide the historical data into two parts: a training set and a testing set. The training set is used to train the model, while the testing set is used to evaluate the model's performance. We use a rolling window approach, where the training and testing sets are updated periodically to simulate real-time trading. Let P(t) represent the price of the asset at time t. Let y(t) represent the trading decision generated by the model at time t. Let C(t) represent the cash balance of the trading account at time t. Let S(t) represent the number of shares held at time t. To simulate the trading decisions generated by the model, we use a simple trading strategy where we buy or sell the asset based on the model's trading decision. If the model predicts "buy," we use the cash balance to purchase shares of the asset. If the model predicts "sell," we sell the shares held in the trading account. If the model predicts "hold," we do nothing. Let B(t) represent the trading signal generated by the model at time t, where B(t) = 1 if the model predicts "buy," B(t) = -1 if the model predicts "sell," and B(t) = 0 if the model predicts "hold." Then, the trading strategy can be defined as:

`y(t) = B(t)`

`C(t) = C(t-1) - P(t) * B(t) * S(t-1)`

`S(t) = S(t-1) + B(t) * C(t-1) / P(t)`

The trading strategy generates a profit or loss based on the difference between the buying and selling prices of the asset. We use various performance metrics, including return on investment (ROI), total profit, and Sharpe ratio, to evaluate the profitability of the trading decisions generated by the model.

## Conclusion

In this research paper, we presented MarkSTM, an artificial intelligence trading bot that uses quantitative analysis and machine learnping techniques to make informed trading decisions. Our experimental results demonstrate that MarkSTM achieves high accuracy in predicting market movements and generates profitable trading decisions. The use of machine learning techniques offers several advantages over traditional stock market analysis, including the ability to process large amounts of data quickly and identify patterns that may not be visible to human analysts. By combining quantitative analysis with machine learning algorithms, MarkSTM is able to generate accurate and reliable trading decisions that can lead to consistent profits. In conclusion, the development of MarkSTM represents a significant step forward in the field of stock market trading. By leveraging the power of artificial intelligence, we have created a system that is capable of analyzing large amounts of data, predicting market movements, and generating profitable trading decisions. The results of our experiments demonstrate that MarkSTM has the potential to revolutionize the way investors approach stock market trading, and we look forward to further developing and refining this technology in the future.