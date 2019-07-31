#!/usr/bin/env python
""" Try to get prices for your wishlist from scryfall
"""

import time
import logging
import argparse
import pprint
import requests

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)

API = 'https://api.scryfall.com'
NAMED = '/cards/named'
USD = 'usd'
USD_FOIL = 'usd_foil'

def set_price(card, actual_card, currency=USD):
    """ Set the price on the card from the actual_card... maybe

        :param card: Dictionary representing the final card to print out
        :param actual_card: An individual card printing response from scryfall
        :param currency: Which currency to evaluate prices
        :return: None
    """

    price = None
    if currency == USD:
        for curr in [USD, USD_FOIL]:
            try:
                price = float(actual_card['prices'][curr])
                LOGGER.debug('Found price for actual_card "%s" in currency "%s": %s', actual_card['name'], curr, price)
                break
            except TypeError:
                pass
        if price is None:
            # either no price in this currency or price is None
            LOGGER.debug('Cound not find price for actual_card "%s" in currency "%s", setting to None',
                         actual_card['name'],
                         currency)
    try:
        if card['price'] is None:
            # take the new price no matter what
            card['price'] = price
        else:
            card['price'] = min(card['price'], price)
            LOGGER.debug('Setting price for card "%s" in currency "%s" to minimum:  %s',
                         card['name'],
                         currency,
                         card['price'])
    except KeyError:
        # no card price yet, set initial value
        LOGGER.debug('Setting initial price for card "%s" in currency "%s" to:  %s',
                     card['name'],
                     currency,
                     price)
        card['price'] = price
    except TypeError:
        # Can't compare to None, keep value
        LOGGER.debug('Maintaining price for card "%s" in currency "%s" to:  %s',
                     card['name'],
                     currency,
                     card['price'])

def main(args):
    """ Main entry point
    """

    with open(args.wishlist) as wishes:
        items = wishes.read().strip().split('\n')
    LOGGER.debug("Got wishlist contents:\n%s", pprint.pformat(items))

    cards = []
    for item in items:
        card = {'name': item}
        payload = {'fuzzy': item}
        card_response = requests.get(f"{API}{NAMED}", payload)
        LOGGER.debug("Fuzzy name response:\n%s", pprint.pformat(card_response.json()))
        time.sleep(.1)
        prints = card_response.json()['prints_search_uri']
        prints_response = requests.get(prints)
        LOGGER.debug("Prints response:\n%s", pprint.pformat(prints_response.json()))
        time.sleep(.1)
        for printed in prints_response.json()['data']:
            actual_card = requests.get(printed['uri'])
            time.sleep(.1)
            LOGGER.debug("Specific print response:\n%s", pprint.pformat(actual_card.json()))
            set_price(card, actual_card.json(), args.currency)
        time.sleep(.1)
        cards.append(card)
    name, price = 'Name', 'Price'
    LOGGER.debug("Final cards list:\n%s", pprint.pformat(cards))
    print(f'You can find the following cards for as low as the following prices in {args.currency}...')
    print(f"{name:<30}|{price:<10}")
    for card in cards:
        print(f"{card['name']:<30}|{card['price']:>10}")
    print('='*41)
    print(f"Grand total: {'':<17}|{sum([i['price'] for i in cards])}")



if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('wishlist',
                        help='Path to wishlist file')
    PARSER.add_argument('-c', '--currency',
                        help="Which currency's price to present; default 'usd'",
                        choices=['usd', 'eur', 'usd_foil'],
                        default='usd')
    PARSER.add_argument('-v', '--verbose',
                        help='Verbosity',
                        action='count',
                        default=1)
    PARSER.set_defaults(func=main)
    ARGS = PARSER.parse_args()
    LEVELS = [logging.WARNING, logging.INFO, logging.DEBUG]
    LEVEL = LEVELS[min(len(LEVELS)-1, ARGS.verbose)]
    LOGGER.setLevel(LEVEL)
    ARGS.func(ARGS)
