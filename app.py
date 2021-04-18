from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
		symbol = request.form.get("symbol")
		allotment = int(request.form.get("allotment"))
		final_share_price = float(request.form.get("final_share_price"))
		sell_commission = float(request.form.get("sell_commission"))
		initial_share_price = float(request.form.get("initial_share_price"))
		buy_commission = float(request.form.get("buy_commission"))
		capital_tax_rate = float(request.form.get("capital_tax_rate"))
       
       	#calculation part
		proceeds = allotment * final_share_price
		total_tax = ((final_share_price - initial_share_price)*allotment - (buy_commission+sell_commission))
		tax = (total_tax* capital_tax_rate)/100
		initial_total = allotment * initial_share_price
		cost = initial_total + buy_commission +sell_commission + tax
		net_profit = proceeds - cost
		return_on_investment = (net_profit / cost) * 100
		breakeven = (initial_total + buy_commission + sell_commission )/ allotment

       	#reprocess calculations for printing
		print_proceeds = "$%.2f" % proceeds
		print_cost = "$%.2f" % cost
		print_total = str(allotment) + " x $" + str(initial_share_price) + " = %.2f" % initial_total
		print_gain = str(capital_tax_rate) + "% of $" + "%.2f" % total_tax + " = %.2f" % tax
		print_net_profit = "$" + "%.2f" % net_profit
		print_return_on_investment = "%.2f" % return_on_investment + "%"
		print_breakeven = "$" + "%.2f" % breakeven

		tempData = {'ticketSymbol': symbol, 'allotment': allotment,
                   'final_share_price': final_share_price, 'sell_commission':sell_commission,
                   'initial_share_price':initial_share_price , 'buy_commission':buy_commission,
                   'capital_tax_rate':capital_tax_rate, 'print_proceeds':print_proceeds, 'print_gain':print_gain,
                   'print_cost':print_cost, 'print_total': print_total, 'print_net_profit':print_net_profit,
                   'print_return_on_investment':print_return_on_investment, 'print_breakeven':print_breakeven}
		return render_template('result.html', **tempData)

if __name__ == '__main__':
    app.run(debug=True)

