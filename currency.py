from flask import flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes



class Currency():

    def __init__(self):
        self.cr = CurrencyRates()
        self.codes = CurrencyCodes()
        self.curr_codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF']

        self.results = {'frm': '', 'to': '', 'amount': ''}


        def check_valid_code(self, frm, to, amount):

            result = self.results
            if frm in self.curr_codes:
                results['frm'] = 'ok'

            else: 
                results['frm'] = 'no'
            if to in self.curr_codes:
                results['to'] = 'ok'
            else: 
                results['to'] = 'no'
            if amount == '':
                results['amount'] = 'no'

            else: 
                results['amount'] = 'ok'
            return self.handle_results(results, frm, to, amount)
        



        def handle_results(self, results, frm, to, amount):
            if 'no' in results.value():
                return self.give_error(results, frm, to)
            else: 
                return self.conversion(frm, to, amount)
            


            def give_error(self, results: frm, to, amount):
                if results['frm'] == 'no':
                    flash(f'Not a valid code: {frm}')
                if results['to'] == 'no':
                    flash(f'Not a valid code: {to}')
                if results['amount'] == 'no':
                    flash('Not a valid amount.')
                return 'error'
                




            def conversion(self, frm, to, amount):
                x = self.codes.get_symbol(to)
                conv = self.cr.convert(frm, to, float(amount))
                conv = round(conv, 2)
                conv = (f'{x}{conv}')
                return conv