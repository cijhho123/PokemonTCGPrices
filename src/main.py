import time
import sys
import argparse
import heapq
import os
import time
import traceback
from pathlib import Path


from pokemontcgsdk import Card

TOP_CARDS_COUNTER = 50


logo_ascii_art = r"""
  _____      _                                _______ _____ _____   _____      _               
 |  __ \    | |                              |__   __/ ____/ ____| |  __ \    (_)              
 | |__) |__ | | _____ _ __ ___   ___  _ __      | | | |   | |  __  | |__) | __ _  ___ ___  ___ 
 |  ___/ _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \     | | | |   | | |_ | |  ___/ '__| |/ __/ _ \/ __|
 | |  | (_) |   <  __/ | | | | | (_) | | | |    | | | |___| |__| | | |   | |  | | (_|  __/\__ \
 |_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|    |_|  \_____\_____| |_|   |_|  |_|\___\___||___/
    """


def print_welcome_screen():
    welcome_string = r"""
    Welcome to the PokemonTCGPrices.
    This tool uses the pokemontcg.io API to evaulate a collection of Pokemon TCG cards provided as a text file, for more info please refer to the README.md
    """

    print(logo_ascii_art + "\n" + welcome_string)

def parse_cl_arguments():
    parser = argparse.ArgumentParser( prog='PokemonTCGPrices',
                    description='A tool to evaluate Pokemon TCG collection',
                    epilog='created by cijhho123')
    
    parser.add_argument("file", nargs="?", help="The text file containing the card codes", type=str)
    parser.add_argument("-v", "--verbose", action="store_false", help="display info on each card checked while the program runs")

    args = parser.parse_args()

    print("info:\n" + str(vars(args)) + "\n\n")

    # input file
    if args.file is None and len(sys.argv) > 1:
        args.file = sys.argv[1]

    if args.file is None:
        print("Need to drag the text file containing the card codes into the script! the program will exit in 10 seconds.")
        time.sleep(10)
        sys.exit()

    return args

def add_card_to_top_cards_list(topCards, card):
    heapq.heappush(topCards, (card["market"], card))
    if len(topCards) > TOP_CARDS_COUNTER:
        heapq.heappop(topCards)

def add_card_value_to_collection(values, card):
    values[0] += card["low"]
    values[1] += card["market"]
    values[2] += card["high"]

def process_card(cardCode):
    if len(cardCode) == 0:
        cardDict = {"name": "empty", "code": cardCode, "low": float(0), "market": float(0), "high": float(0)}
        return cardDict

    try:
        card = Card.find(cardCode)
        low = market = high = 0

        if card.tcgplayer is not None:
            prices = card.tcgplayer.prices
            #different rarities can share the same code, taking the best rarity of each card
            rarities = ["1stEditionHolofoil", "holofoil", "1stEditionNormal", "reverseHolofoil", "normal"] 
            for rarity in rarities:
                rarity_price = getattr(prices, rarity, None)  
                if rarity_price is not None:
                    low = rarity_price.low
                    market = rarity_price.market
                    high = rarity_price.high
                    break

        elif card.cardmarket is not None:
            prices = card.cardmarket.prices
            low = prices["averageSellPrice"]
            market = prices["averageSellPrice"]
            high = prices["averageSellPrice"]

        cardDict = {"name": card.name, "code": cardCode, "low": float(low), "market": float(market), "high": float(high)}
        return cardDict
    except:
        cardDict = {"name": "ERROR", "code": cardCode, "low": float(0), "market": float(0), "high": float(0)}
        return cardDict

def export_data(values, topCards, problematicCards):
    filePath = os.path.join(os.path.expanduser("~/Desktop"), "output.txt")
    uniquePath = uniquify(filePath)

    topCardsSorted = sorted(topCards)
    topCardsSorted.reverse()
    try:
        outputFile = open(uniquePath, "x")
        outputFile.write("Collection value:")
        outputFile.write(f"\rLower bound for collection: {values[0]}")
        outputFile.write(f"\rMarket Value for collection: {values[1]}")
        outputFile.write(f"\rUpper bound for collection: {values[2]}" + "\n\n")

        outputFile.write(f"Top {TOP_CARDS_COUNTER} most expensive cards:\n")
        for cardIndex, card in enumerate(topCardsSorted):
            outputFile.write(f"#{cardIndex + 1} - {card[1]['name']}, price: {card[1]['market']}\n")

        if len(problematicCards) > 0:
            outputFile.write("\n\nList of problematic codes which were not enter the summuation:\n")
            for card in problematicCards:
                outputFile.write(f"{card["code"]}\n")
        
        print(f"\n\ncreated a summary text file on path {uniquePath}")
        time.sleep(5)
        os.startfile(uniquePath)

    except Exception as e:
            print("Error writing output file, please contact cijhho123 with a screenshot and input file")
            print(str(e))
            print(traceback.format_exc())
        


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path

def main():
    print_welcome_screen()
    args = parse_cl_arguments()
    
    if Path(args.file).suffix != '.txt':
        print("The provided file must be a text file with extension .txt the program will exit in 10 seconds")
        time.sleep(10)
        sys.exit()

    values = [0.0, 0.0, 0.0]  # lowest prices, market value, highest prices
    topCards = []
    problematicCards = []
    
    try:
        file = open(args.file, "r")

        for rawCardCode in file:
            cardCode =  ''.join(rawCardCode.split())  
            cardDict = process_card(cardCode)      

            if cardDict["name"] == "empty":
                continue

            if cardDict["market"] == 0:
                problematicCards.append(cardDict)
            else:
                add_card_value_to_collection(values, cardDict)
                add_card_to_top_cards_list(topCards, cardDict)

                if args.verbose:
                    print(str(cardDict))

        file.close()
        export_data(values, topCards, problematicCards)

    except Exception as e:
        print(str(e))
        print(traceback.format_exc())

        time.sleep(10)
        exit(1)
    


    time.sleep(10)

if __name__ == "__main__":
    main()