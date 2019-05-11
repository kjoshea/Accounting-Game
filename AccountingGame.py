# INITIALIZE INCOME STATEMENT AS A DICTIONARY

income_statement = {'Sales': 0, 'COGS': None, 'Gross Profit': None, 'SG&A': 0, 'Depreciation': 0,
                    'Pre-Tax Earnings': None, 'Income Taxes': None, 'Earnings': None}

# SET LINE ITEMS TO FORMULAS FROM TOP TO BOTTOM AS THEY APPEAR ON INCOME STATEMENT

income_statement['COGS'] = income_statement['Sales'] * .60
income_statement['Gross Profit'] = income_statement['Sales'] - income_statement['COGS']
income_statement['Pre-Tax Earnings'] = income_statement['Gross Profit'] - income_statement['SG&A'] - \
                                       income_statement['Depreciation']
income_statement['Income Taxes'] = income_statement['Pre-Tax Earnings'] * .20
income_statement['Earnings'] = income_statement['Pre-Tax Earnings'] - income_statement['Income Taxes']


