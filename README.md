# PokemonTCGPrices 
A tool to evaulate a Pokemon TCG collection.

## How to use
Create a text file `<NAME>.txt` and add the identifier for each card you own at a new line. Once the text file is ready, drag it into `PokemonTCGPrices.exe` and it will evaluate the collection.  
The output file will be saved on the Desktop with name `output.txt` and will be opened automatically after a few seconds.

## Input File Examle

## How To Build

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

## Thanks
