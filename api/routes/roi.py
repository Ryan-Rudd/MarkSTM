class roiAPI:
    def roi(input_amount, output_amount, fee=7):
        profit = (output_amount - input_amount)
        FEE_TOTAL = float(round((fee*0.07)*100,1))
        TOTAL = profit-FEE_TOTAL
        ROI = TOTAL / input_amount* 100
        return round(ROI, 1)