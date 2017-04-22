# Currency converter

This is command line currency converter, capable to convert given amount of many to more than 100 world currencies by actual rates.

### Instalation

Run `curr_converter` with python3. Libraries `requests` and `grequests` need to be installed.

```
# install packages
pip3 install requests
pip3 install grequests

# run program
python3 ./curr_converter [arguments]
```

### Usage
```
curr_converter [-h] -a AMOUNT -i I_CURR [-o O_CURR]

arguments:
  -h, --help        show this help message and exit
  -a AMOUNT, --amount AMOUNT
                Amount in given currency, that will be converted.
  -i I_CURR, --input_currency I_CURR
                Input currency: 3-letter shortcut or currency symbol.
  -o O_CURR, --output_currency O_CURR
                Output currency: 3-letter shortcut or currency symbol.
                If not listed, all currencies will be listed.
```

# Example
```
python3 ./curr_converter.py -i £ -a 1 -o CZK
{
    "input": {
        "amount": "1.00",
        "currency": "GBP"
    },
    "output": {
        "CZK": "32.19"
    }
}
```

## Notes

Application uses http://rate-exchange-1.appspot.com/ API for currency conversion by actual rate and https://gist.github.com/Fluidbyte/2973986 for currencies symbols and codes info.

In order to find api supporting as many foreign currencies as possible, selected API doesn't support listing all rates by single request - that's why listing all currencies rates requires sending request for each one and this command can be a bit slower.
