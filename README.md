---

# What

Quick 'n shitty script to ~~abuse~~ use the scryfall api for obtaining rough pricing on cards in your wishlist.

# How

1. Have a newline-delimited list of cards in some file, say `wishlist.txt`
2.  ```
    python3 pricer.py wishlist.txt [-c usd|usd_foil|eur|tix] [-s name|price] [-v [-v ...]]
    ```

# Why

Stop asking so many questions.

# Example

Using the `example.txt` list of cards, sorting by price, you would get something like the following:

```
(venv🐍 ) ~/git/github/mtg_wishlist_pricer 🌈  🐴  🌯  python pricer.py example.txt -s price
You can find the following cards for as low as the following prices in usd...
Name                          |     Price|Running Total
Squee's Embrace               |      0.14|         0.14
Extract From Darkness         |      0.14|         0.28
Disciple of Deceit            |      0.15|         0.43
Orochi Eggwatcher             |       0.2|         0.63
Trace of Abundance            |      0.22|         0.85
Shifting Shadow               |      0.26|         1.11
Spawnwrithe                   |      0.28|         1.39
Doomgape                      |      0.28|         1.67
Font of Agonies               |       0.3|         1.97
Infernal Genesis              |      0.32|         2.29
Culling Scales                |      0.33|         2.62
Tangleroot                    |      0.33|         2.95
Gabriel Angelfire             |      0.36|         3.31
Aether Rift                   |      0.38|         3.69
Death's Presence              |      0.42|         4.11
Shisato, Whispering Hunter    |      0.43|         4.54
Profane Command               |      0.44|         4.98
Shard Convergence             |      0.53|         5.51
Grenzo, Dungeon Warden        |      0.68|         6.19
Rakdos, the Showstopper       |       0.7|         6.89
Jhoira of the Ghitu           |      0.83|         7.72
Kaseto, Orochi Archmage       |      0.94|         8.66
  1 ---
Sasaya, Orochi Ascendant      |      1.09|         9.75
Scrap Trawler                 |      1.35|        11.10
Crackleburr                   |      1.39|        12.49
Thistledown Liege             |      1.39|        13.88
Order of Whiteclay            |      1.58|        15.46
Wirewood Channeler            |      1.61|        17.07
Glen Elendra Liege            |      1.62|        18.69
Illusionist’s Gambit          |      1.79|        20.48
Minion Reflector              |      2.35|        22.83
Awakening Zone                |      2.57|        25.40
Shizuko, Caller of Autumn     |      2.59|        27.99
Knowledge Pool                |      2.72|        30.71
Sakiko, Mother of Summer      |      2.93|        33.64
Gilder Bairn                  |      2.95|        36.59
O-Kagachi, Vengeful Kami      |      2.97|        39.56
Awakening                     |       3.4|        42.96
Cryptbreaker                  |       3.5|        46.46
Rishkar's Expertise           |      3.82|        50.28
Overbeing of Myth             |      3.84|        54.12
Skirge Familiar               |      3.91|        58.03
Ashenmoor Liege               |      4.13|        62.16
Liege of the Tangle           |      4.25|        66.41
Vindictive Lich               |      4.32|        70.73
Seraph of the Scales          |      4.42|        75.15
Knacksaw Clique               |      4.47|        79.62
Metalluc Mimic                |      6.09|        85.71
Austere Command               |      6.22|        91.93
Door of Destinies             |      6.45|        98.38
  1 venv/
Nemesis of Reason             |      6.57|       104.95
Patron of the Orochi          |      6.97|       111.92
Mayael’s Aria                 |      7.33|       119.25
Kaervek the Merciless         |      7.39|       126.64
Enlightened Tutor             |      7.65|       134.29
Tireless Tracker              |      7.92|       142.21
Kindred Summons               |      8.25|       150.46
Traverse the Outlands         |     10.67|       161.13
Heroic Intervention           |     10.75|       171.88
Deathbringer Liege            |     10.99|       182.87
Diabolic Intent               |     11.78|       194.65
Razaketh, the Foulblooded     |     12.65|       207.30
True-Name Nemesis             |     14.14|       221.44
Dragon Broodmother            |     14.89|       236.33
Mirari's Wake                 |     15.47|       251.80
Reaper King                   |     15.99|       267.79
Herald's Horn                 |      16.2|       283.99
training grounds              |     19.11|       303.10
Polluted Bonds                |     20.81|       323.91
Queen Marchesa                |     21.84|       345.75
Sylvan Library                |     36.82|       382.57
=========================================
Grand total:                  |    382.57
```
