def scrape_shortstocks(table_data):
    for data in table_data:
        #get symbol
        symbol_name = data.td.a.text
        #get company name
        company_name = data.find('td', class_ = 'data-col1 Ta(start) Pstart(10px) Pend(6px)').text
        # #get last price
        last_price = data.find('td', class_ = 'data-col2 Ta(end) Pstart(10px) Pend(6px) Fw(b)').text
        # #get percent change
        percent_change = data.find('td', class_ = 'data-col4 Ta(end) Pstart(10px) Pend(6px)').text
        # #get volume
        volume_today = data.find('td', class_ = 'data-col6 Ta(end) Pstart(10px) Pend(6px)').text
        # #get marketcap
        market_cap = data.find('td', class_ = 'data-col8 Ta(end) Pstart(10px) Pend(6px)').text

        print(f'Symbol Name: {symbol_name}')
        print(f'Company Name: {company_name}')
        print(f'Last Price: {last_price}')
        print(f'Percent Change Today: {percent_change}')
        print(f'Volume: {volume_today}')
        print(f'Market Cap: {market_cap}')
        print('____________________%_____________________')