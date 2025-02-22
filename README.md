# PokemonTCGPrices 
A tool to evaulate a Pokemon TCG collection.

## How to use
Create a text file `<NAME>.txt` and add the identifier for each card you own at a new line. Once the text file is ready, drag it into `PokemonTCGPrices.exe` and it will evaluate the collection.  
The output file will be saved on the Desktop with name `output.txt` and will be opened automatically after a few seconds.

## Input File Examle
The Text file should contain a single card identifier in a new line.
```
SV1-15  
SM12-123  
XY10-78  
BW8-45  
HGSS3-10  
DP4-88  
EX6-17  
SW3-64  
SWSH8-25  
DP1-12  
```

## How To Build
### Requirements
- Python3
- Pip
- Pyinstaller

### To build the project from source:
1. Clone the repo
2. CD into the project root folder
3. Install dependencies with `pip install -r requirements.txt`
4. Bundle the application into a single .exe file with `pyinstaller .\main.py --onefile --icon=assets\icon.ico`

## How To Identify A Pokemon Card
Each Pokémon card has a **Collector Number** and a **Set Symbol**, which uniquely identify the card.  

### 1. Collector Number
- Found at the **bottom left or bottom right** of the card.
- Appears in the format: **X/Y** (or just **X** in some cases).
  - **X** = the card’s position in the set.
  - **Y** = the total number of cards in the set.
  - Sometimes cards will have numbers higher than the maximum. These are called "Secret Rare" cards and they are some of the most valuable Pokemon cards.
- **Example:** `36/114`  
![collector number example](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibsGl05PG7TyTbU7eYIjcHh_IvMmngNsHccqrHB75cV-7HxFGmF-nHK311qiGIn_a7yv2zhJEtwuufS8bYrcDuhxviKqdcjL1ROVXvMQ3gIZwXCgSCkuA_VqY4lKIFwa8NtWIh2BC5/s0/pokemon-card-number.jpg)


### 2. Set Symbol (Set Code)
- Several times a year, new Pokemon cards are released in different sets. Names like Vivid Voltage, Team Rocket, Sun & Moon, etc.
- Each set has a unique logo printed on the card and a unique list of cards. To determine the set, you locate the logo on the card. It's right above the lower border of the card.
- Then look up the logo in a list of Pokemon set symbols [here](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_Trading_Card_Game_expansions).
- The only set that does not have a logo is the [Pokemon Base Set](https://bulbapedia.bulbagarden.net/wiki/Base_Set_(TCG)). It is the first set of Pokemon cards and the most valuable. If you don't see a logo on your card, that's a good thing.
- **Example:**  
 ![set logo example](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMfRhkIF1JUH8QaYVvn5ulJpU1egc1gk0k8a1OUa-NAdO8ekeuPibgwJCSYmCCZ0_L_6HeswUsmsvO8AttZwyfxHX98rWiur__vXKHMkGUEmtt0VALW8O4LmpPh9tfpTQ0ZGfpeW19/s0/pokemon-card-set-symbol.jpg)  
Locating this logo in the [website](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_Trading_Card_Game_expansions), and finding it belong to the set **XY—Steam Siege** with code **STS**

### 3. Full Card Identifier (Set Code + Collector Number)
To uniquely identify a Pokémon card, use:

```
Set Code - Collector Number
```

### **Examples:**
- `XY3-6` → Card #6 from the XY Furious Fists set.
- `SM1-45` → Card #45 from the Sun & Moon Base Set.


### Price Range
The tool provide 3 estimates for the collection.  
- **Lower** is the lower bound based on the chepest sales of the cards.
- **Marked Value** is the price that best represents the current value of the cards.
- **High** is the upper bound based on the most expensive sales of the cards.

## Thanks
Thanks to [Pokémon TCG API](https://docs.pokemontcg.io/).  
PriceCharting.com for their [article](https://blog.pricecharting.com/2021/01/how-to-tell-what-pokemon-card-you-have.html#fast) on how to identify a card.

