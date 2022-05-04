def currency_rates(argv):
    program, currency_code, *args = argv
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_code = currency_code.upper()
    dt = datetime.strptime(response.headers['Date'], "%a, %d %B %Y %H:%M:%S %Z").date()

    if content.count(f'>{currency_code}<'):
        position = content.index(f'>{currency_code}<')
        nominal_start_position = position + content[position:].index('<Nominal>')+9
        nominal_finish_position = position + content[position:].index('</Nominal>')
        nominal = float(content[nominal_start_position:nominal_finish_position])
        position += content[position:].index(f'<Value>')+7
        return float(content[position:position+7].replace(',','.')) / nominal, dt
    else:
        return None


if __name__ == '__main__':
    import sys
    from requests import get, utils
    from datetime import datetime
    
    print(*currency_rates(sys.argv), sep=', ')
