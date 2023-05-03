# CSCE-410-Project

## Algorithm Notes 
```python
print(index.db) => {'db': {'./test.txt': {'id': './test.txt', 'text': 'Bee Movie Script - ... Special thanks to SergeiK.'}}}
print(index.index) => {'Bee': [{'doc_id': './test.txt', 'frequency': 16}], 'Movie': [{'doc_id': './test.txt', 'frequency': 4}], ... }
```  

## Comparosin

### Small Corpus
#### Files/Folders
(venv) (base) nkolbas@cse-witty-18 CSCE-410-Project % ls -R compare_corpus_original 
Thriller        small

compare_corpus_original/Thriller:
Dark Games_1234927.txt

compare_corpus_original/small:
test.txt        test2.txt

#### Run
------ STARTING ------
------ BEGINNING COMPARISON ------
Cleaning the comparison directory
Comparing initial build times...
Building index for old approach
Building index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file deletion
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Removing stale indexes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file modification
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file creation
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Searching for old approach
Searching for new approach
Searching for old approach in sub dir
Searching for new approach in sub dir
-------- Building index --------
Old index build finished in 0.0078 seconds
New index build finished in 1.0166 seconds
Old index rebuild after delete finished in 0.0072 seconds
New index rebuild after delete finished in 0.0035 seconds
Old index rebuild after modification finished in 0.0070 seconds
New index rebuild after modification finished in 0.0044 seconds
Old index rebuild after addition finished in 0.0069 seconds
New index rebuild after addition finished in 0.0042 seconds
-------- Index storage usage --------
The amount of storage used initially for old approach was 107743 bytes
The amount of storage used after building index for old approach was 107778 bytes
The amount of storage increase used by old approach was 1.0003x
The amount of storage used initially for new approach was 107743 bytes
The amount of storage used after building index for new approach was 779653 bytes
The amount of storage increase used by new approach was 7.2362x
-------- Index searching --------
Old search index finished in 0.0002 seconds
New search index finished in 0.0001 seconds
Old search index subdir finished in 0.0002 seconds
New search index subdir finished in 0.0001 seconds
╒════════════════════════════╤═════════════════════╤═══════════════════╤══════════════════════════════════════════════════════════════════════════════════════════╕
│ Category                   │ Traditional Index   │ Lic-T             │ Description                                                                              │
╞════════════════════════════╪═════════════════════╪═══════════════════╪══════════════════════════════════════════════════════════════════════════════════════════╡
│ Index Build                │ 0.0078 seconds      │ 1.0166 seconds    │ The time it takes to build the initial index                                             │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild Delete       │ 0.0072 seconds      │ 0.0035 seconds    │ The time it takes to rebuild the index after a file has been deleted                     │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild Modification │ 0.0070 seconds      │ 0.0044 seconds    │ The time it takes to rebuild the index after a file has been modified                    │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild New          │ 0.0069 seconds      │ 0.0042 seconds    │ The time it takes to rebuild the index after a new file has been added                   │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage Initially          │ 107743.0000 bytes   │ 107743.0000 bytes │ The amount of storage used initially by the directory being indexed (should be the same) │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage After Build        │ 107778.0000 bytes   │ 779653.0000 bytes │ The amount of storage used by the directory being indexed after indexed                  │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage Increase           │ 1.0003x             │ 7.2362x           │ The multiple of the initial storage to the new storage usage                             │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Full Search                │ 0.0002 seconds      │ 0.0001 seconds    │ The amount of time it takes to search the whole index                                    │
├────────────────────────────┼─────────────────────┼───────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Subdir Search              │ 0.0002 seconds      │ 0.0001 seconds    │ The amount of time it takes to search only a certain sub folder                          │
╘════════════════════════════╧═════════════════════╧═══════════════════╧══════════════════════════════════════════════════════════════════════════════════════════╛

### Medium Corpus
#### Files/Folders
(venv) (base) nkolbas@cse-witty-18 CSCE-410-Project % ls -R compare_corpus_original
Thriller        small

compare_corpus_original/Thriller:
Dark Games_1234927.txt                                  Mr Mark Fenton_1282592.txt                              The Roommate_1265990.txt
Hider in the House_0097503.txt                          Possessions_0227291.txt                                 The Utah Murder Project_0831374.txt
His Secret Past_5865046.txt                             Red Eye_0421239.txt                                     The Witching Hour_1634140.txt
Jorge Alberto vs The Neoliberal Demons_4203196.txt      The Boy Next Door_3181822.txt

compare_corpus_original/small:
test.txt        test2.txt

#### Run
------ STARTING ------
------ BEGINNING COMPARISON ------
Cleaning the comparison directory
Comparing initial build times...
Building index for old approach
Building index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file deletion
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Removing stale indexes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file modification
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file creation
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Searching for old approach
Searching for new approach
Searching for old approach in sub dir
Searching for new approach in sub dir
-------- Building index --------
Old index build finished in 0.1908 seconds
New index build finished in 12.8205 seconds
Old index rebuild after delete finished in 0.1414 seconds
New index rebuild after delete finished in 0.0455 seconds
Old index rebuild after modification finished in 0.1427 seconds
New index rebuild after modification finished in 0.0672 seconds
Old index rebuild after addition finished in 0.1528 seconds
New index rebuild after addition finished in 0.0365 seconds
-------- Index storage usage --------
The amount of storage used initially for old approach was 1598695 bytes
The amount of storage used after building index for old approach was 1598730 bytes
The amount of storage increase used by old approach was 1.0000x
The amount of storage used initially for new approach was 1598695 bytes
The amount of storage used after building index for new approach was 12003610 bytes
The amount of storage increase used by new approach was 7.5084x
-------- Index searching --------
Old search index finished in 0.0024 seconds
New search index finished in 0.0002 seconds
Old search index subdir finished in 0.0025 seconds
New search index subdir finished in 0.0002 seconds
╒════════════════════════════╤═════════════════════╤═════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════╕
│ Category                   │ Traditional Index   │ Lic-T               │ Description                                                                              │
╞════════════════════════════╪═════════════════════╪═════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════╡
│ Index Build                │ 0.1908 seconds      │ 12.8205 seconds     │ The time it takes to build the initial index                                             │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild Delete       │ 0.1414 seconds      │ 0.0455 seconds      │ The time it takes to rebuild the index after a file has been deleted                     │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild Modification │ 0.1427 seconds      │ 0.0672 seconds      │ The time it takes to rebuild the index after a file has been modified                    │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild New          │ 0.1528 seconds      │ 0.0365 seconds      │ The time it takes to rebuild the index after a new file has been added                   │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage Initially          │ 1598695.0000 bytes  │ 1598695.0000 bytes  │ The amount of storage used initially by the directory being indexed (should be the same) │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage After Build        │ 1598730.0000 bytes  │ 12003610.0000 bytes │ The amount of storage used by the directory being indexed after indexed                  │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage Increase           │ 1.0000x             │ 7.5084x             │ The multiple of the initial storage to the new storage usage                             │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Full Search                │ 0.0024 seconds      │ 0.0002 seconds      │ The amount of time it takes to search the whole index                                    │
├────────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Subdir Search              │ 0.0025 seconds      │ 0.0002 seconds      │ The amount of time it takes to search only a certain sub folder                          │
╘════════════════════════════╧═════════════════════╧═════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════╛

### Large Corpus
#### Files/Folders
3200 Files
(venv) (base) nkolbas@cse-witty-18 CSCE-410-Project % ls -R compare_corpus_original
1
101 Days of 101 Dalmatians_0249328.txt
Action
After Hours Revisits Rock Stars Lamb Entrees and Late Night_5070224.txt
Animation
Cider House Rules_4865798.txt
Comedy
Crime
Documentary
Drama
Family
Fantasy
Gentleman in Mufti_0258525.txt
History
Horror
Hudson Halls_0283738.txt
Music
Musical
Mystery
News
Ni os Espectaculares_2585466.txt
Reality-TV
Reunion_0483314.txt
Romance
Sci-Fi
Short
Slay the Dreamer IMDb_11144100.txt
Sneakers_1256467.txt
Star Wars Ep 1 The Phantom Menace w Ryan Paul from Cold Callers Comedy Podcast_12764338.txt
Talk-Show
The Flintstones_5161338.txt
The Italian Job_0290675.txt
Thriller
War
Western
small
test.txt

compare_corpus_original/1:
test2.txt

compare_corpus_original/Action:
Adventure
American Shaolin_0101327.txt
Animation
Armstrong_4451006.txt
Comedy
Crime
Drama
Family
Fantasy
Nan quan wang_0110625.txt
Sci-Fi
Thriller
Western

compare_corpus_original/Action/Adventure:
Batman Begins_0372784.txt
Batman Forever_0112462.txt
Batman_0096895.txt
Collateral Damage_0699285.txt
Comedy
Drama
Fantasy
First Blood_0083944.txt
History
Indiana Jones and the Kingdom of the Crystal Skull_0367882.txt
Indiana Jones and the Last Crusade_0097576.txt
Indiana Jones and the Temple of Doom_0087469.txt
Mystery
Raiders of the Lost Ark_0082971.txt
Romance
Sci-Fi
The Dark Knight Rises_1345836.txt
Thriller
Western

compare_corpus_original/Action/Adventure/Comedy:
Crime
Family
Fantasy
Fifty Fifty_0106902.txt
Knight and Day_1013743.txt
Romance
Sci-Fi
The Interview_2788710.txt
The Man from U N C L E_1638355.txt
The Spy Who Dumped Me_6663582.txt
Thriller
Wild Hogs_0486946.txt

compare_corpus_original/Action/Adventure/Comedy/Crime:
Austin Powers The Spy Who Shagged Me_0145660.txt
Thriller

compare_corpus_original/Action/Adventure/Comedy/Crime/Thriller:
Charlie s Angels_0160127.txt

compare_corpus_original/Action/Adventure/Comedy/Family:
Romance
Sci-Fi
The Suite Life on Deck_1181917.txt

compare_corpus_original/Action/Adventure/Comedy/Family/Romance:
The Three Musketeers_0108333.txt

compare_corpus_original/Action/Adventure/Comedy/Family/Sci-Fi:
Small Soldiers_0122718.txt
Thunderbirds_0167456.txt

compare_corpus_original/Action/Adventure/Comedy/Fantasy:
Big Trouble in Little China_0090728.txt
Last Action Hero_0107362.txt
Sci-Fi

compare_corpus_original/Action/Adventure/Comedy/Fantasy/Sci-Fi:
Thor Ragnarok_3501632.txt
Thriller

compare_corpus_original/Action/Adventure/Comedy/Fantasy/Sci-Fi/Thriller:
Innerspace_0093260.txt

compare_corpus_original/Action/Adventure/Comedy/Romance:
Romancing the Stone_0088011.txt

compare_corpus_original/Action/Adventure/Comedy/Sci-Fi:
Deadpool_1431045.txt
Guardians of the Galaxy Vol 2_3896198.txt
Men in Black 3_1409024.txt
Men in Black_0119654.txt
Superman III_0086393.txt

compare_corpus_original/Action/Adventure/Comedy/Thriller:
Kingsman The Secret Service_2802144.txt
Western

compare_corpus_original/Action/Adventure/Comedy/Thriller/Western:
Maverick_0110478.txt

compare_corpus_original/Action/Adventure/Drama:
All Is Lost_2017038.txt
Fantasy
Gladiator_0172495.txt
Noah_1959490.txt
Romance
Sci-Fi
Seven Samurai_0047478.txt
Thriller
War
Western

compare_corpus_original/Action/Adventure/Drama/Fantasy:
Beowulf Grendel_0402057.txt
Crouching Tiger Hidden Dragon Sword of Destiny_2652118.txt
Romance
Snow White and the Huntsman_1735898.txt
The Lord of the Rings The Fellowship of the Ring_0120737.txt
The Lord of the Rings The Return of the King_0167260.txt
The Lord of the Rings The Two Towers_0167261.txt

compare_corpus_original/Action/Adventure/Drama/Fantasy/Romance:
Game of Thrones_0944947.txt
Willow_0096446.txt

compare_corpus_original/Action/Adventure/Drama/Romance:
King Kong_0360717.txt
Robin Hood Prince of Thieves_0102798.txt
The Aeronauts_6141246.txt
War
Western

compare_corpus_original/Action/Adventure/Drama/Romance/War:
The Four Feathers_0240510.txt
The Last of the Mohicans_0104691.txt

compare_corpus_original/Action/Adventure/Drama/Romance/Western:
Roughshod_0041827.txt

compare_corpus_original/Action/Adventure/Drama/Sci-Fi:
Avengers Endgame_4154796.txt
Battlestar Galactica_0407362.txt
Cloak Dagger_5614844.txt
NightMan_0128886.txt
Okja_3967856.txt
Superman_0078346.txt
The Postman_0119925.txt
Thriller

compare_corpus_original/Action/Adventure/Drama/Sci-Fi/Thriller:
Star Trek First Contact_0117731.txt
War for the Planet of the Apes_3450958.txt
WarGames_0086567.txt

compare_corpus_original/Action/Adventure/Drama/Thriller:
Robin Hood_4532826.txt
Sanctum_0881320.txt
The Book of Eli_1037705.txt
The Poseidon Adventure_0069113.txt

compare_corpus_original/Action/Adventure/Drama/War:
Legionnaire_0126388.txt

compare_corpus_original/Action/Adventure/Drama/Western:
Apache Drums_0043291.txt

compare_corpus_original/Action/Adventure/Fantasy:
Clash of the Titans_0800320.txt
Conan the Barbarian_0816462.txt
DragonHeart_0116136.txt
Dragonslayer_0082288.txt
Highlander_0091203.txt
Horror
Pirates of the Caribbean At World s End_0449088.txt
Pirates of the Caribbean Dead Man s Chest_0383574.txt
Pirates of the Caribbean Dead Men Tell No Tales_1790809.txt
Pirates of the Caribbean The Curse of the Black Pearl_0325980.txt
Prince of Persia The Sands of Time_0473075.txt
Sci-Fi
The Mummy_0120616.txt
Thor_0800369.txt
Thriller

compare_corpus_original/Action/Adventure/Fantasy/Horror:
Sci-Fi
Solomon Kane_0970452.txt
Thriller

compare_corpus_original/Action/Adventure/Fantasy/Horror/Sci-Fi:
Blade Trinity_0359013.txt
Hellboy II The Golden Army_0411477.txt

compare_corpus_original/Action/Adventure/Fantasy/Horror/Thriller:
The Mummy Tomb of the Dragon Emperor_0859163.txt

compare_corpus_original/Action/Adventure/Fantasy/Sci-Fi:
Aquaman_1477834.txt
Avatar_0499549.txt
Ender s Game_1731141.txt
Fantastic Four_0120667.txt
Highlander Endgame_0144964.txt
Krull_0085811.txt
Star Wars Episode I The Phantom Menace_0120915.txt
Star Wars Episode II Attack of the Clones_0121765.txt
Star Wars Episode III Revenge of the Sith_0121766.txt
Star Wars Episode IV A New Hope_0076759.txt
Star Wars Episode V The Empire Strikes Back_0080684.txt
Star Wars Episode VI Return of the Jedi_0086190.txt
Superman The Man of Steel_1453257.txt
TRON 2 0_0208650.txt
Thriller
War

compare_corpus_original/Action/Adventure/Fantasy/Sci-Fi/Thriller:
Star Trek V The Final Frontier_0098382.txt

compare_corpus_original/Action/Adventure/Fantasy/Sci-Fi/War:
Wonder Woman_0451279.txt

compare_corpus_original/Action/Adventure/Fantasy/Thriller:
Cirque du Freak The Vampire s Assistant_0450405.txt
Reign of Fire_0253556.txt
The Mummy Returns_0209163.txt
Tomb Raider_1365519.txt

compare_corpus_original/Action/Adventure/History:
The Vikings_0052365.txt

compare_corpus_original/Action/Adventure/Mystery:
Sci-Fi
Sherlock Holmes_0988045.txt
Thriller

compare_corpus_original/Action/Adventure/Mystery/Sci-Fi:
Divergent_1840309.txt
Star Trek The Next Generation_0092455.txt
Thriller

compare_corpus_original/Action/Adventure/Mystery/Sci-Fi/Thriller:
Star Trek Generations_0111280.txt

compare_corpus_original/Action/Adventure/Mystery/Thriller:
National Treasure_0368891.txt

compare_corpus_original/Action/Adventure/Romance:
Tarzan s Secret Treasure_0034266.txt

compare_corpus_original/Action/Adventure/Sci-Fi:
2012_1190080.txt
After Earth_1815862.txt
Batman v Superman Dawn of Justice_2975590.txt
Battlefield Earth_0185183.txt
Beneath the Planet of the Apes_0065462.txt
Black Panther_1825683.txt
Dune_0087182.txt
Edge of Tomorrow_1631867.txt
Escape from New York_0082340.txt
Fantastic Four_1502712.txt
Flash Gordon_0080745.txt
Green Lantern_1133985.txt
Independence Day_0116629.txt
Iron Man_0371746.txt
John Carter_0401729.txt
Jurassic World_0369610.txt
Logan s Run_0074812.txt
Oblivion_1483013.txt
Pacific Rim_1663662.txt
Ready Player One_1677720.txt
Spider Man 2_0316654.txt
Spider Man_0145487.txt
Star Trek II The Wrath of Khan_0084726.txt
Star Trek III The Search for Spock_0088170.txt
Star Trek_0796366.txt
Star Wars Episode VII The Force Awakens_2488496.txt
Stargate_0111282.txt
Superman II_0081573.txt
Superman IV The Quest for Peace_0094074.txt
The Avengers_0848228.txt
The Fifth Element_0119116.txt
The Incredible Hulk_0800080.txt
The Lost World Jurassic Park_0119567.txt
The Predator_3829266.txt
The Time Machine_0268695.txt
Thriller
Transformers_0418279.txt
War
Waterworld_0114898.txt
X Men Origins Wolverine_0458525.txt
X Men_0120903.txt

compare_corpus_original/Action/Adventure/Sci-Fi/Thriller:
Aliens_0090605.txt
Armageddon_0120591.txt
Escape from L A_0116225.txt
G I Joe The Rise of Cobra_1046173.txt
Hardcore Henry_3072482.txt
I Am Number Four_1464540.txt
Inception_1375666.txt
Jurassic Park III_0163025.txt
Jurassic Park_0107290.txt
Mad Max 2 The Road Warrior_0082694.txt
Planet of the Apes_0133152.txt
Predator_0093773.txt
Predators_1424381.txt
Serenity_0379786.txt
Star Trek Insurrection_0120844.txt
Star Trek Nemesis_0253754.txt
Star Trek VI The Undiscovered Country_0102975.txt
Starship Troopers_0120201.txt
Super 8_1650062.txt
The Avengers_0118661.txt
The Hunger Games_1392170.txt
X2 X Men United_0290334.txt

compare_corpus_original/Action/Adventure/Sci-Fi/War:
Timeline_0300556.txt

compare_corpus_original/Action/Adventure/Thriller:
Broken Arrow_0115759.txt
Casino Royale_0381061.txt
Cliffhanger_0106582.txt
Commando_0088944.txt
Death Proof_1028528.txt
Die Hard with a Vengeance_0112864.txt
Executive Decision_0116253.txt
From Russia with Love_0057076.txt
GoldenEye_0113189.txt
Goldfinger_0058150.txt
Mission Impossible II_0120755.txt
Mission Impossible_0117060.txt
Rambo First Blood Part II_0089880.txt
Skyfall_1074638.txt
Skyscraper_5758778.txt
Speed_0111257.txt
The A Team_0429493.txt
The Expendables_1320253.txt
The Hunt for Red October_0099810.txt
The Rock_0117500.txt
The World Is Not Enough_0143145.txt
Tomorrow Never Dies_0120347.txt
You Only Live Twice_0062512.txt
xXx_0295701.txt

compare_corpus_original/Action/Adventure/Western:
The Wild Bunch_0065214.txt

compare_corpus_original/Action/Animation:
The Hundred Year Old Mystery_1229165.txt

compare_corpus_original/Action/Comedy:
American Ultra_3316948.txt
Crime
Drama
Horror
MacGruber_1470023.txt
Romance
Smokey and the Bandit_0076729.txt
Team America World Police_0372588.txt
Thriller

compare_corpus_original/Action/Comedy/Crime:
21 Jump Street_1232829.txt
30 Minutes or Less_1622547.txt
Crime Spree_0310924.txt
Drama
Family
Fantasy
Kick Ass_1250777.txt
Lock Stock and Two Smoking Barrels_0120735.txt
Mystery
Pineapple Express_0910936.txt
The Other Guys_1386588.txt
Thriller
Tower Heist_0471042.txt

compare_corpus_original/Action/Comedy/Crime/Drama:
Chapter Seven Loud Fast and Keep Going_6866356.txt
Thriller

compare_corpus_original/Action/Comedy/Crime/Drama/Thriller:
48 Hrs_0083511.txt
Beverly Hills Cops_11322610.txt
Metro_0119664.txt

compare_corpus_original/Action/Comedy/Crime/Family:
Monsieur Gangster_0057591.txt

compare_corpus_original/Action/Comedy/Crime/Fantasy:
The Mask_0110475.txt

compare_corpus_original/Action/Comedy/Crime/Mystery:
Ryan Hansen Solves Crimes on Television_7068580.txt

compare_corpus_original/Action/Comedy/Crime/Thriller:
Bad Boys for Life_1502397.txt
Beverly Hills Cop_0086960.txt
Free Fire_4158096.txt
Game Night_2704998.txt
Midnight Run_0095631.txt
Mr Mrs Smith_0356910.txt
Ocean s Eight_5164214.txt
RED_1245526.txt
Rush Hour 2_0266915.txt
Rush Hour_0120812.txt
The Last Boy Scout_0102266.txt
The Nice Guys_3799694.txt

compare_corpus_original/Action/Comedy/Drama:
Family
The Family Man_9544034.txt

compare_corpus_original/Action/Comedy/Drama/Family:
The Pacifier_0395699.txt

compare_corpus_original/Action/Comedy/Horror:
Lake Placid_0139414.txt
The Night Watchmen_4102722.txt

compare_corpus_original/Action/Comedy/Romance:
Mr Right_2091935.txt
The Bounty Hunter_1038919.txt

compare_corpus_original/Action/Comedy/Thriller:
Wrongfully Accused_0120901.txt

compare_corpus_original/Action/Crime:
Daredevil_0287978.txt
Drama
Fantasy
Firetrap_0243907.txt
Horror
Looter_0436517.txt
Sci-Fi
Thriller
Walking Tall_0351977.txt

compare_corpus_original/Action/Crime/Drama:
Badlands_0069762.txt
Lord of War_0399295.txt
Only God Forgives_1602613.txt
Sci-Fi
Strangle Hold_0596969.txt
Thriller
Western

compare_corpus_original/Action/Crime/Drama/Sci-Fi:
The Rover_2345737.txt
Thriller

compare_corpus_original/Action/Crime/Drama/Sci-Fi/Thriller:
Strange Days_0114558.txt
Time to Hunt_11777040.txt

compare_corpus_original/Action/Crime/Drama/Thriller:
15 Minutes_0179626.txt
16 Blocks_0450232.txt
Absolute Power_0118548.txt
Antitrust_0218817.txt
Chaos_0402910.txt
Code of Silence_0088936.txt
Cradle 2 the Grave_0306685.txt
Death Sentence_0804461.txt
Eastern Promises_0765443.txt
End of Watch_1855199.txt
Gangs of Wasseypur_1954470.txt
Hard Rain_0120696.txt
Hard to Kill_0099739.txt
Heist_0252503.txt
Hostage_0340163.txt
L on The Professional_0110413.txt
Law Abiding Citizen_1197624.txt
Man on Fire_0328107.txt
Max Payne_0467197.txt
Miami Vice_0430357.txt
New Jack City_0102526.txt
Nick of Time_0113972.txt
Payback_0120784.txt
Street Kings_0421073.txt
Superfights_0114582.txt
The Accountant_2140479.txt
The Brave One_0476964.txt
The Dark Knight_0468569.txt
The Devil s Own_0118972.txt
The French Connection_0067116.txt
The Jackal_0119395.txt
The Killer_0097202.txt
The Punisher_0098141.txt
The Punisher_0330793.txt
Thief_0083190.txt
Twelve_1407084.txt
Western

compare_corpus_original/Action/Crime/Drama/Thriller/Western:
Hell or High Water_2582782.txt

compare_corpus_original/Action/Crime/Drama/Western:
3 10 to Yuma_0381849.txt

compare_corpus_original/Action/Crime/Fantasy:
Batman Returns_0103776.txt
Catwoman_0327554.txt
Thriller

compare_corpus_original/Action/Crime/Fantasy/Thriller:
The Crow City of Angels_0115986.txt

compare_corpus_original/Action/Crime/Horror:
From Dusk Till Dawn_0116367.txt

compare_corpus_original/Action/Crime/Sci-Fi:
Hollow Man_0533545.txt
Thriller

compare_corpus_original/Action/Crime/Sci-Fi/Thriller:
Deja Vu_0453467.txt
Face Off_0119094.txt
Judge Dredd_0113492.txt
RoboCop_0093870.txt
Western

compare_corpus_original/Action/Crime/Sci-Fi/Thriller/Western:
Outland_0082869.txt

compare_corpus_original/Action/Crime/Thriller:
Aaranya Kaandam_1496729.txt
Assassins_0112401.txt
Black Rain_0096933.txt
Con Air_0118880.txt
Crank_0479884.txt
Deep Cover_0104073.txt
El Mariachi_0104815.txt
Frank Miller s Sin City A Dame to Kill For_0458481.txt
Get Carter_0067128.txt
Gone in 60 Seconds_0187078.txt
Hitman_0465494.txt
John Wick_2911666.txt
Kill Bill Vol 1_0266697.txt
Kill Bill Vol 2_0378194.txt
Lethal Weapon 4_0122151.txt
Lethal Weapon_0093409.txt
Machete_0985694.txt
Passenger 57_0105104.txt
Point Break_0102685.txt
RocknRolla_1032755.txt
Romeo Must Die_0165929.txt
Ronin_0122690.txt
Swordfish_0244244.txt
The Assignment_0118647.txt
The Boondock Saints II All Saints Day_1300851.txt
The Boondock Saints_0144117.txt
The Driver_0077474.txt
The Equalizer_0455944.txt
The Fast and the Furious_0232500.txt
The Getaway_0068638.txt
The Mechanic_0472399.txt
The Taking of Pelham One Two Three_0072251.txt
The Warriors_0080120.txt
Ticker_0196158.txt
Wanted_0493464.txt
Whiteout_0365929.txt

compare_corpus_original/Action/Drama:
300_0416449.txt
A Coriolanus rny k ban_2245685.txt
Fantasy
Horror
Roadracers_0111002.txt
Sci-Fi
Sport
The Base_0185908.txt
The Last Samurai_0325710.txt
Thriller
Top Gun_0092099.txt
War
Warriors Two_0078517.txt
Western

compare_corpus_original/Action/Drama/Fantasy:
47 Ronin_1335975.txt
Hancock_0448157.txt
Horror
Romance
Sci-Fi
The Crow_0109506.txt

compare_corpus_original/Action/Drama/Fantasy/Horror:
Sci-Fi
Van Helsing_5197820.txt

compare_corpus_original/Action/Drama/Fantasy/Horror/Sci-Fi:
Perfect Creature_0403407.txt

compare_corpus_original/Action/Drama/Fantasy/Romance:
Buffy the Vampire Slayer_0118276.txt

compare_corpus_original/Action/Drama/Fantasy/Sci-Fi:
Y The Last Man_8042500.txt

compare_corpus_original/Action/Drama/Horror:
Rage of the Werewolf_0191391.txt

compare_corpus_original/Action/Drama/Sci-Fi:
Bloodshot_1634106.txt
Elysium_1535108.txt
Snowpiercer_1706620.txt
Thriller

compare_corpus_original/Action/Drama/Sci-Fi/Thriller:
Chain Reaction_0115857.txt
Equilibrium_0238380.txt
I Robot_0343818.txt
Johnny Mnemonic_0113481.txt
Kin_6017942.txt
Logan_3315342.txt
Looper_1276104.txt
Rise of the Planet of the Apes_1318514.txt
The Omega Man_0067525.txt
Transcendence_2209764.txt
V for Vendetta_0434409.txt

compare_corpus_original/Action/Drama/Sport:
Days of Thunder_0099371.txt
Rocky Balboa_0479143.txt
Warrior_1291584.txt

compare_corpus_original/Action/Drama/Thriller:
Air Force One_0118571.txt
Body of Lies_0758774.txt
Colombiana_1657507.txt
Hanna_0993842.txt
Hold the Dark_5057140.txt
Proof of Life_0228750.txt
Red Sparrow_2873282.txt
The Kingdom_0431197.txt
The Last Castle_0272020.txt
Vantage Point_0443274.txt
War
White House Down_2334879.txt

compare_corpus_original/Action/Drama/Thriller/War:
Eye in the Sky_2057392.txt

compare_corpus_original/Action/Drama/War:
Fury_2713180.txt
G I Jane_0119173.txt
Memphis Belle_0100133.txt
Ran_0089881.txt

compare_corpus_original/Action/Drama/Western:
Django and Sartana Are Coming It s the End_0216546.txt

compare_corpus_original/Action/Family:
Mighty Morphin Power Rangers_0183515.txt

compare_corpus_original/Action/Fantasy:
Big Trouble in Little China_6199850.txt
Horror
Thriller

compare_corpus_original/Action/Fantasy/Horror:
Hellboy_0167190.txt
Legion_1038686.txt
Mystery
Nightbreed_0100260.txt
Thriller

compare_corpus_original/Action/Fantasy/Horror/Mystery:
Constantine_0360486.txt

compare_corpus_original/Action/Fantasy/Horror/Thriller:
End of Days_0146675.txt

compare_corpus_original/Action/Fantasy/Thriller:
Bright_5519340.txt
Drive Angry_1502404.txt
Ghost Rider_0259324.txt

compare_corpus_original/Action/Sci-Fi:
Alien Nation_0094631.txt
Alien vs Predator_9824546.txt
Batman Robin_0118688.txt
Battle Los Angeles_1217613.txt
Battle for the Planet of the Apes_0069768.txt
Conquest of the Planet of the Apes_0068408.txt
Escape from the Planet of the Apes_0067065.txt
Halo_2934286.txt
Short
Spacejacked_0120174.txt
Star Wars The New Droid Army_1505922.txt
Tenet_6723592.txt
Terminator 2 Judgment Day_0103064.txt
Terminator 3 Rise of the Machines_0181852.txt
Terminator Salvation_0438488.txt
The Matrix Reloaded_0234215.txt
The Matrix Revolutions_0242653.txt
The Matrix_0133093.txt
The Terminator_0088247.txt
Thriller

compare_corpus_original/Action/Sci-Fi/Short:
T2 3 D Battle Across Time_0117880.txt

compare_corpus_original/Action/Sci-Fi/Thriller:
Blade Runner_0083658.txt
Darkman_0099365.txt
Demolition Man_0106697.txt
District 9_1136608.txt
Gamer_1034032.txt
Godzilla_0120685.txt
Lucy_2872732.txt
Next_0435705.txt
Repo Men_1053424.txt
Skyline_1564585.txt
Surrogates_0986263.txt
The Island_0399201.txt
The Running Man_0093894.txt
The War of the Worlds_0046534.txt
Total Recall_0100802.txt
Upgrade_6499752.txt
Western

compare_corpus_original/Action/Sci-Fi/Thriller/Western:
Cowboys Aliens_0409847.txt

compare_corpus_original/Action/Thriller:
Arctic Blue_0106303.txt
Atomic Blonde_2406566.txt
Die Hard 2_0099423.txt
Die Hard_0095016.txt
Duel_0067023.txt
Enemy of the State_0120660.txt
Live Free or Die Hard_0337978.txt
Ninja Assassin_1186367.txt
Olympus Has Fallen_2302755.txt
Safe House_1599348.txt
Salt_0944835.txt
Southern Comfort_0083111.txt
Taken_0936501.txt
The Head Hunter_0085841.txt
The Hitcher_0091209.txt
The Siege_0133952.txt
Ultimate Target_0243327.txt
Unknown_1401152.txt

compare_corpus_original/Action/Western:
American Outlaws_0244000.txt

compare_corpus_original/Animation:
Family
History
Indiana Jones_5999108.txt
The Slowest Game_2941508.txt

compare_corpus_original/Animation/Family:
Adaptation_2980718.txt
Fantasy
Mystery

compare_corpus_original/Animation/Family/Fantasy:
Musical
The Red Turtle_3666024.txt

compare_corpus_original/Animation/Family/Fantasy/Musical:
Romance
The Nightmare Before Christmas_0107688.txt

compare_corpus_original/Animation/Family/Fantasy/Musical/Romance:
The Little Mermaid_0097757.txt

compare_corpus_original/Animation/Family/Mystery:
O Brother Where Art Thou_1156696.txt

compare_corpus_original/Animation/History:
The Dark Years_0879974.txt

compare_corpus_original/Comedy:
2 Broke Girls_1845307.txt
30 Rock_0496424.txt
40 Year Old Virgin_0887155.txt
9 to 5_0080319.txt
Ace Ventura Pet Detective_0109040.txt
Airplane_0080339.txt
Al Wazeer Jay_6543896.txt
American Milkshake_2254364.txt
American Werewolf in London_1789110.txt
Anchorman The Legend of Ron Burgundy_0357413.txt
Authors Anonymous_2114461.txt
Barely Legal_0302297.txt
Blockers_2531344.txt
Booksmart_1489887.txt
Caf Majestic_0257298.txt
Cedar Rapids_1477837.txt
Clerks_0109445.txt
Complete Guide to Guys_0407680.txt
Crime
Dangerous Liasons_0582886.txt
Dave_8531222.txt
Dazed and Confused_0106677.txt
Dead Dogs Wag No Tails_0732564.txt
Death at a Funeral_1321509.txt
Downton Abby Miller_2996668.txt
Dr Strangelove or How I Learned to Stop Worrying and Love the Bomb_0057012.txt
Drama
Dumb and Dumber_0109686.txt
Dumb and Dumberer When Harry Met Lloyd_0329028.txt
Edward Eddie the Eagle Edwards_5328298.txt
Everybody Comes to Nick s_1218598.txt
Family
Fantasy
Ferris Bueller s Day Off_0091042.txt
Fighting Belle_5662022.txt
Fixed_4777004.txt
Fortuosity_0502412.txt
Four Rooms_0113101.txt
From Here to Infirmity_0606185.txt
Halloween IV The Return of Michael Myers Hot Mustard Water_13376032.txt
Horror
Hot romance_6048960.txt
How to Ruin Your Favorite Sitcoms with Simple Math_6870282.txt
I Hope They Serve Beer in Hell_1220628.txt
In the Loop_1226774.txt
Indiana Jones and the Monkey King Finale_12407576.txt
Insidious_7176504.txt
Jay and Silent Bob Strike Back_0261392.txt
Kill Bill Volumen 1_7316868.txt
License to Drive_0095519.txt
Lost in America_0089504.txt
Man Overboard_1186829.txt
Mean Girls_0377092.txt
Millionaire Slumdog_1400356.txt
Mon Love Sib Meun_4876734.txt
Music
Musical
My Best Friend s Birthday_0359715.txt
Mystery
Napoleon Dynamite_0374900.txt
National Lampoon s Christmas Vacation_0097958.txt
Neither Seen Nor Recognized_0051989.txt
Next Friday_0195945.txt
Nightmare on Elm Street and 2012_1934056.txt
Office Space_0151804.txt
Parks and Recreation_1266020.txt
Quiz Show Winner_4335006.txt
Romance
Romy and Michele s High School Reunion_0120032.txt
Same Time Next Year_6797728.txt
Scary Movie_0175142.txt
Sci-Fi
Second Chance_1324069.txt
Short
Someone to Watch Over Me_1464643.txt
Spare Me_1078001.txt
Sport
Superbad_0829482.txt
Talk-Show
The Blast from the Past_0581053.txt
The Boss_2702724.txt
The Brady Bunch Movie_0112572.txt
The Devil by the Tail_0064232.txt
The First Separation_0793669.txt
The Great Outdoors_0095253.txt
The Hangover_1119646.txt
The Hebrew Hammer_0317640.txt
The Jerk_0079367.txt
The Lake House_0538279.txt
The Reader_9885352.txt
The Rise and Rise of Michael Rimmer_0066302.txt
The Surfer King_0418206.txt
The Toy_0084809.txt
This Is the End_1245492.txt
Thriller
Up All Night_1843323.txt
Veep_1759761.txt
Waking Up the Town_0016497.txt
War
Western
What About Bob_0103241.txt
What to Expect When You re Expecting_10064788.txt
Where Is Everybody 101_5719890.txt
Who s Your Daddy_0287138.txt
Why Him_4501244.txt
Year One_1045778.txt
You ll Never Walk Alone in This Town Again_0639513.txt
Young Frankenstein_0072431.txt

compare_corpus_original/Comedy/Crime:
A Fish Called Wanda_0095159.txt
Analyze That_0289848.txt
Analyze This_0122933.txt
Chernobyl_11966300.txt
Drama
Fun with Dick and Jane_0076059.txt
Get Shorty_5761496.txt
Go_0139239.txt
Heathers_0097493.txt
Horrible Bosses 2_2170439.txt
Horrible Bosses_1499658.txt
Malibu s Most Wanted_0328099.txt
My Cousin Vinny_0104952.txt
Mystery
Naked Gun 33 1 3 The Final Insult_0110622.txt
Raising Arizona_0093822.txt
Romance
Sci-Fi
Seven Psychopaths_1931533.txt
Short
Snatch_0208092.txt
Sport
The Distinguished Gentleman_0104114.txt
The Ladykillers_0048281.txt
The Naked Gun 2 The Smell of Fear_0102510.txt
The Sting II_0086370.txt
Thriller

compare_corpus_original/Comedy/Crime/Drama:
American Psycho_0144084.txt
Bad Santa_0307987.txt
Bottle Rocket_0115734.txt
Detective_0089066.txt
Four Lions_1341167.txt
Harlem Nights_0097481.txt
Hesher_1403177.txt
Hustlers_5503686.txt
Life_0123964.txt
Made_0227005.txt
Mini s First Time_0425253.txt
Mystery
Observe and Report_1197628.txt
Paper Moon_0070510.txt
Romance
The Big White_0402850.txt
The Confessions of Felix Krull_0083383.txt
The Foundation_0495031.txt
The Sting_0070735.txt
Three Billboards Outside Ebbing Missouri_5027774.txt
Thriller
Who Framed the Good Cop_7211154.txt

compare_corpus_original/Comedy/Crime/Drama/Mystery:
Body of Proof_1587669.txt
Romance
Thriller

compare_corpus_original/Comedy/Crime/Drama/Mystery/Romance:
Bones_0460627.txt
Inherent Vice_1791528.txt

compare_corpus_original/Comedy/Crime/Drama/Mystery/Thriller:
A Simple Favor_7040874.txt
Knives Out_8946378.txt

compare_corpus_original/Comedy/Crime/Drama/Romance:
Fallen Angels_0112913.txt
Focus_2381941.txt
Little Athens_0417907.txt
Nurse Betty_0171580.txt
Thriller

compare_corpus_original/Comedy/Crime/Drama/Romance/Thriller:
Out of Sight_0120780.txt
The Big Easy_0092654.txt

compare_corpus_original/Comedy/Crime/Drama/Thriller:
Burn After Reading_0887883.txt
Death to Smoochy_0266452.txt
Hackers_0113243.txt
I Don t Feel at Home in This World Anymore_5710514.txt
In Bruges_0780536.txt
Matchstick Men_0325805.txt
The King of Comedy_0085794.txt
The Player_0105151.txt
Wild at Heart_0100935.txt

compare_corpus_original/Comedy/Crime/Mystery:
Fletch_0089155.txt
Surveillance_0261336.txt
The Thin Man_0025878.txt
Thriller

compare_corpus_original/Comedy/Crime/Mystery/Thriller:
Clue_0088930.txt
The Golden Eye_0040394.txt

compare_corpus_original/Comedy/Crime/Romance:
Extract_1225822.txt
Intolerable Cruelty_0138524.txt
Thriller
Trouble in Paradise_0023622.txt

compare_corpus_original/Comedy/Crime/Romance/Thriller:
Date Night_1279935.txt

compare_corpus_original/Comedy/Crime/Sci-Fi:
Strange Brew_0086373.txt

compare_corpus_original/Comedy/Crime/Short:
The Favour_10714870.txt

compare_corpus_original/Comedy/Crime/Sport:
The Big Lebowski_0118715.txt

compare_corpus_original/Comedy/Crime/Thriller:
Arsenic and Old Lace_0036613.txt
Birthday Girl_0188453.txt
Cecil B Demented_0173716.txt
Fatal Instinct_0106873.txt
Serial Mom_0111127.txt
The Guard_1540133.txt
The Ladykillers_0335245.txt
Very Bad Things_0124198.txt

compare_corpus_original/Comedy/Drama:
20th Century Women_4385888.txt
28 Days_0191754.txt
3 Idiots_1187043.txt
A Monkey in Winter_0056636.txt
A Serious Man_1019452.txt
About Schmidt_0257360.txt
American Graffiti_0069704.txt
Another Year_1431181.txt
Bad Words_2170299.txt
Barbershop_0303714.txt
Barney s Version_1423894.txt
Being Human_0106379.txt
Being There_0078841.txt
Birdman or The Unexpected Virtue of Ignorance_2562232.txt
Boys on the Side_0112571.txt
Brigsby Bear_5805752.txt
Butter_1349451.txt
Calvary_2234003.txt
City Island_1174730.txt
Dead Poets Society_0097165.txt
Diner_0083833.txt
Dirty Girl_1107319.txt
Do the Right Thing_0097216.txt
Downhill_4558376.txt
Edtv_0131369.txt
Eighth Grade_7014006.txt
Family
Fantasy
Fast Times at Ridgemont High_0083929.txt
Fortune Cookie_0210688.txt
Friday_0113118.txt
Funny People_1201167.txt
Ghost World_0162346.txt
Grandma_4270516.txt
Hannah and Her Sisters_0091167.txt
Happiness_0147612.txt
Happy Birthday Wanda June_0067180.txt
Henry Fool_0122529.txt
History
Horror
Human Nature_0219822.txt
I ll Do Anything_0110097.txt
Ingrid Goes West_5962210.txt
Juno_0467406.txt
Lady Bird_4925292.txt
Little Miss Sunshine_0449059.txt
Living in Oblivion_0113677.txt
Lost in Translation_0335266.txt
Margot at the Wedding_0757361.txt
Me and Earl and the Dying Girl_2582496.txt
Melvin and Howard_0081150.txt
Mid90s_5613484.txt
Mississippi Grind_2349144.txt
Mistress America_2872462.txt
Mr Smith Goes to Washington_0031679.txt
Mumford_0140397.txt
Music
Mystery
Newton_6484982.txt
Paradise_1262990.txt
Please Give_0878835.txt
Postcards from the Edge_0100395.txt
Quartet_1441951.txt
Ready to Wear_0110907.txt
Red White Black and Blue_0707959.txt
Romance
Sci-Fi
Shameless_1586680.txt
Shampoo_0073692.txt
Short
Smoke_0114478.txt
Sport
St Vincent_2170593.txt
State and Main_0120202.txt
Stepmom_0120686.txt
Stranger Than Paradise_0088184.txt
Swingers_0117802.txt
Terms of Endearment_0086425.txt
Thank You for Smoking_0427944.txt
The Angriest Man in Brooklyn_1294970.txt
The Breakfast Club_0088847.txt
The Descendants_1033575.txt
The Devil Wears Prada_0458352.txt
The Edge of Seventeen_1878870.txt
The Farewell_8637428.txt
The Four Seasons_0082405.txt
The Meyerowitz Stories_5536736.txt
The Royal Tenenbaums_0265666.txt
The Savages_0775529.txt
The Squid and the Whale_0367089.txt
The Way Way Back_1727388.txt
Thriller
Tin Men_0094155.txt
Toni Erdmann_4048272.txt
Wadjda_2258858.txt
War
Withnail I_0094336.txt
Wonder Boys_0185014.txt
Young Adult_1625346.txt

compare_corpus_original/Comedy/Drama/Family:
Between Love and Friendship_5445434.txt
Diary of a Wimpy Kid_1196141.txt
Huge_1591511.txt
Marley Me_0822832.txt
Piano Piano Kid_0105137.txt
Romance
Secondhand Lions_0327137.txt
Sport
Three Men and a Baby_0094137.txt
We Bought a Zoo_1389137.txt

compare_corpus_original/Comedy/Drama/Family/Romance:
And Away We Go_1003594.txt
Good Boy_5358714.txt
My Girl 2_0110613.txt
My Girl_0102492.txt

compare_corpus_original/Comedy/Drama/Family/Sport:
The Sandlot_0108037.txt

compare_corpus_original/Comedy/Drama/Fantasy:
Being John Malkovich_0120601.txt
Harvey_0042546.txt
Pleasantville_0120789.txt
Romance
Shortcut to Happiness_0263265.txt
The Devil and Daniel Webster_0033532.txt
The Fisher King_0101889.txt
The Hudsucker Proxy_0110074.txt

compare_corpus_original/Comedy/Drama/Fantasy/Romance:
Big_0094737.txt
Click_0389860.txt
Peggy Sue Got Married_0091738.txt
Practical Magic_0120791.txt
Ruby Sparks_1839492.txt
Sci-Fi
Scrooged_0096061.txt
Sport
Stranger Than Fiction_0420223.txt
The Secret Life of Walter Mitty_0359950.txt

compare_corpus_original/Comedy/Drama/Fantasy/Romance/Sci-Fi:
About Time_2194499.txt

compare_corpus_original/Comedy/Drama/Fantasy/Romance/Sport:
17 Again_0974661.txt

compare_corpus_original/Comedy/Drama/History:
Romance
The Death of Stalin_4686844.txt

compare_corpus_original/Comedy/Drama/History/Romance:
Shakespeare in Love_0138097.txt

compare_corpus_original/Comedy/Drama/Horror:
Tusk_3099498.txt

compare_corpus_original/Comedy/Drama/Music:
Bamboozled_0215545.txt
Beaches_0094715.txt
Brad s Status_5884230.txt
Inside Llewyn Davis_2042568.txt
Mystery
Nashville_0073440.txt
Pump Up the Volume_0100436.txt
Romance

compare_corpus_original/Comedy/Drama/Music/Mystery:
Hail Caesar_0475290.txt

compare_corpus_original/Comedy/Drama/Music/Romance:
Breakin_0086998.txt
Sing Street_3544112.txt
The Fabulous Baker Boys_0097322.txt
The Thing Called Love_0108327.txt

compare_corpus_original/Comedy/Drama/Mystery:
Gosford Park_0280707.txt
Six Degrees of Separation_0108149.txt
The Hospital_0067217.txt
Tully_5610554.txt
While We re Young_1791682.txt

compare_corpus_original/Comedy/Drama/Romance:
10 Things I Hate About You_0147800.txt
500 Days of Summer_1022603.txt
A Good Year_0401445.txt
Alfie_0375173.txt
As Good as It Gets_0119822.txt
Beautiful Girls_0115639.txt
Beginners_1532503.txt
Benny Joon_0106387.txt
Breakfast at Tiffany s_0054698.txt
Bridget Jones s Baby_1473832.txt
Broadcast News_0092699.txt
Burning Annie_0307879.txt
Car Wash_0074281.txt
Celeste Jesse Forever_1405365.txt
Chasing Amy_0118842.txt
Class_0085346.txt
Crazy Rich Asians_3104988.txt
Crazy Stupid Love_1570728.txt
Crazylove_0416658.txt
Damsels in Distress_1667307.txt
Easy A_1282140.txt
Elizabethtown_0368709.txt
Emma_0116191.txt
Enough Said_2390361.txt
Flipped_0817177.txt
Forgetting Sarah Marshall_0800039.txt
Four Weddings and a Funeral_0109831.txt
Frances Ha_2347569.txt
Garden State_0333766.txt
God s Country Off Route 9_1470596.txt
Happy Go Lucky_1045670.txt
Harold and Maude_0067185.txt
He s Just Not That Into You_1001508.txt
Hero_0104412.txt
His Girl Friday_0032599.txt
Hope and Glory_0093209.txt
How Do You Know_1341188.txt
I Think I Love My Wife_0770772.txt
I ll See You in My Dreams_3236120.txt
In Good Company_0385267.txt
Infinitely Polar Bear_1969062.txt
It s Complicated_1230414.txt
It s Kind of a Funny Story_0804497.txt
Larry Crowne_1583420.txt
Lars and the Real Girl_0805564.txt
Learning to Drive_3062976.txt
Little Children_0404203.txt
Love Actually_0314331.txt
Luke and Brie Are on a First Date_1106815.txt
Made for Each Other_0031602.txt
Maggie s Plan_3471098.txt
Marriage Story_7653254.txt
Meet John Doe_0033891.txt
Moonrise Kingdom_1748122.txt
Moonstruck_0093565.txt
Mr Deeds Goes to Town_0027996.txt
Mrs Winterbourne_0117104.txt
My Best Friend s Wedding_0119738.txt
Never Been Kissed_0151738.txt
Notting Hill_0125439.txt
Now and Then_0114011.txt
One Fine Day_0117247.txt
One Way Passage_0023305.txt
One Wild Moment_2191765.txt
Pygmalion_0030637.txt
Reality Bites_0110950.txt
Rushmore_0128445.txt
Sabrina_0047437.txt
Safety Not Guaranteed_1862079.txt
Say Anything_0098258.txt
Sci-Fi
Second Act_2126357.txt
Sex and the City_1000774.txt
Silver Linings Playbook_1045658.txt
Skin Deep_0098343.txt
Sleepless in Seattle_0108160.txt
Solitary Man_1294213.txt
Something s Gotta Give_0337741.txt
Spanglish_0371246.txt
Sport
Storytelling_0250081.txt
Submarine_1440292.txt
Tamara Drewe_1486190.txt
The American President_0112346.txt
The Anniversary Party_0254099.txt
The Apartment_0053604.txt
The Artist_1655442.txt
The Battle of Shaker Heights_0357470.txt
The Best Exotic Marigold Hotel_1412386.txt
The Big Sick_5462602.txt
The Bonfire of the Vanities_0099165.txt
The Comedian_1967614.txt
The Diary of a Teenage Girl_3172532.txt
The Girl Next Door_0265208.txt
The Goodbye Girl_0076095.txt
The Graduate_0061722.txt
The Hollars_3714720.txt
The Kids Are All Right_0842926.txt
The Meddler_4501454.txt
The Mirror Has Two Faces_0117057.txt
The Proposal_1041829.txt
The Rules of Attraction_0292644.txt
The Spectacular Now_1714206.txt
The Sweetest Christmas_7030432.txt
The Switch_0889573.txt
The Terminal_0362227.txt
The Watermelon Woman_0118125.txt
Thriller
Tootsie_0084805.txt
Trainwreck_3152624.txt
Two for the Road_0062407.txt
Up in the Air_1193138.txt
Vicky Cristina Barcelona_0497465.txt
War
Western
When Harry Met Sally_0098635.txt
While You Were Sleeping_0114924.txt
Working Girl_0096463.txt
You ve Got Mail_0128853.txt

compare_corpus_original/Comedy/Drama/Romance/Sci-Fi:
Blast from the Past_0124298.txt
Thriller

compare_corpus_original/Comedy/Drama/Romance/Sci-Fi/Thriller:
The Lobster_3464902.txt

compare_corpus_original/Comedy/Drama/Romance/Sport:
Breaking Away_0078902.txt
Jerry Maguire_0116695.txt
The Cutting Edge_0104040.txt
Tin Cup_0117918.txt

compare_corpus_original/Comedy/Drama/Romance/Thriller:
Punch Drunk Love_0272338.txt

compare_corpus_original/Comedy/Drama/Romance/War:
Life Is Beautiful_0118799.txt

compare_corpus_original/Comedy/Drama/Romance/Western:
The Electric Horseman_0079100.txt

compare_corpus_original/Comedy/Drama/Sci-Fi:
Maniac_5580146.txt
S1m0ne_0258153.txt
The Middleman_1122770.txt
The Truman Show_0120382.txt

compare_corpus_original/Comedy/Drama/Short:
Basaan_3386408.txt
Battle of Algiers_8070404.txt

compare_corpus_original/Comedy/Drama/Sport:
Game 6_0425055.txt
Stick It_0430634.txt
Win Win_1606392.txt

compare_corpus_original/Comedy/Drama/Thriller:
Barton Fink_0101410.txt
Parasite_6751668.txt
The Cable Guy_0115798.txt

compare_corpus_original/Comedy/Drama/War:
Forbidden Games_0043686.txt
Jojo Rabbit_2584384.txt
Last Flag Flying_6018306.txt
MASH_0066026.txt
Stalag 17_0046359.txt

compare_corpus_original/Comedy/Family:
A Christmas Story_0085334.txt
A Few Good Men_0849162.txt
Cheaper by the Dozen_0349205.txt
Fantasy
Home Alone_0099785.txt
Romance
Short

compare_corpus_original/Comedy/Family/Fantasy:
Are We Done Yet_0422774.txt
Hocus Pocus_0107120.txt
Musical
The Flintstones_0109813.txt

compare_corpus_original/Comedy/Family/Fantasy/Musical:
Mary Poppins Returns_5028340.txt

compare_corpus_original/Comedy/Family/Romance:
Bringing Up Baby_0029947.txt
Father of the Bride_0101862.txt

compare_corpus_original/Comedy/Family/Short:
The Sandwich Days_1629412.txt

compare_corpus_original/Comedy/Fantasy:
Beetlejuice_0094721.txt
Bruce Almighty_0315327.txt
Christ Complex_2416048.txt
Horror
Liar Liar_0119528.txt
Little Nicky_0185431.txt
Romance
The Addams Family_0101272.txt
The Change Up_1488555.txt

compare_corpus_original/Comedy/Fantasy/Horror:
Army of Darkness_0106308.txt
Gremlins 2 The New Batch_0099700.txt
Gremlins_0087363.txt
My Name Is Bruce_0489235.txt
The Frighteners_0116365.txt
The Witches of Eastwick_0094332.txt
Thriller

compare_corpus_original/Comedy/Fantasy/Horror/Thriller:
An American Werewolf in Paris_0118604.txt
Idle Hands_0138510.txt

compare_corpus_original/Comedy/Fantasy/Romance:
Groundhog Day_0107048.txt
Kate Leopold_0035423.txt
Midnight in Paris_1605783.txt
Mr Destiny_0100201.txt
Slash_4729990.txt
The Invention of Lying_1058017.txt
What Women Want_0207201.txt

compare_corpus_original/Comedy/Horror:
An American Werewolf in London_0082010.txt
Jennifer s Body_1131734.txt
Music
Piranha 3D_0464154.txt
Scary Movie 2_0257106.txt
Sci-Fi
Shaun of the Dead_0365748.txt
Short
Sucker_0178047.txt
Talk-Show
The Babysitter_4225622.txt
The Lost Boys_0093437.txt
Thriller
Tremors_0100814.txt
Waxwork_0096426.txt

compare_corpus_original/Comedy/Horror/Music:
Trick or Treat_0092112.txt

compare_corpus_original/Comedy/Horror/Sci-Fi:
Body Bags_0106449.txt
First Man on Mars_4562262.txt
Killer Klowns from Outer Space_0095444.txt
Slither_0439815.txt

compare_corpus_original/Comedy/Horror/Short:
Blood Drips Heavily on Newsies Square_0478982.txt
Cabin Fever Family Friendly Version_1010382.txt
Jason Vs Freddy_13124010.txt

compare_corpus_original/Comedy/Horror/Talk-Show:
Freddy vs Jason_5843012.txt

compare_corpus_original/Comedy/Horror/Thriller:
A Bucket of Blood_0112594.txt

compare_corpus_original/Comedy/Music:
Detroit Rock City_0165710.txt
Musical
Pitch Perfect 2_2848292.txt
Romance
Short
Talk-Show
The Adventures of Priscilla Queen of the Desert_0109045.txt
The Producers_0063462.txt
This Is Spinal Tap_0088258.txt

compare_corpus_original/Comedy/Music/Musical:
A Hard Day s Night_0058182.txt

compare_corpus_original/Comedy/Music/Romance:
A Night at the Roxbury_0120770.txt
Pitch Perfect_1981677.txt
Some Like It Hot_0053291.txt
The Wedding Singer_0120888.txt

compare_corpus_original/Comedy/Music/Short:
The 6th Sense_2016299.txt

compare_corpus_original/Comedy/Music/Talk-Show:
Airforce One 2 Revenge of President Dracula_1843432.txt
Conan_1637574.txt

compare_corpus_original/Comedy/Musical:
Romance
Shock Treatment_0083067.txt
The Best Little Whorehouse in Texas_0083642.txt
The Cocoanuts_0019777.txt
The Rocky Horror Picture Show_0073629.txt
War

compare_corpus_original/Comedy/Musical/Romance:
April in Paris_0044370.txt
Singin in the Rain_0045152.txt
White Christmas_0047673.txt

compare_corpus_original/Comedy/Musical/War:
Duck Soup_0023969.txt

compare_corpus_original/Comedy/Mystery:
Manhattan Murder Mystery_0107507.txt
Sci-Fi

compare_corpus_original/Comedy/Mystery/Sci-Fi:
Welcome to Upload_9072146.txt

compare_corpus_original/Comedy/Romance:
All About Steve_0881891.txt
Am lie_0211915.txt
Annie Hall_0075686.txt
Arthur_1334512.txt
Bad Teacher_1284575.txt
Bareilly Ki Barfi_6967980.txt
Boy Who Never Slept_1781782.txt
Bridesmaids_1478338.txt
Clueless_0112697.txt
Cougar Town_1441109.txt
Down in the Boondocks_0591691.txt
Friends with Benefits_1632708.txt
Good Luck Chuck_0452625.txt
Hair Show_0382561.txt
Hall Pass_0480687.txt
I Love You Man_1155056.txt
It Happened One Night_0025316.txt
Joe Versus the Volcano_0099892.txt
John Tucker Must Die_0455967.txt
Knocked Up_0478311.txt
Legally Blonde_0250494.txt
Mallrats_0113749.txt
Man Trouble_0104804.txt
Mr Blandings Builds His Dream House_0040613.txt
My Big Fat Greek Wedding 2_3760922.txt
Ninotchka_0031725.txt
No Strings Attached_1411238.txt
Norbit_0477051.txt
Platinum Blonde_0022268.txt
Pretty Woman_0100405.txt
Runaway Bride_0163187.txt
Sci-Fi
Sex Drive_1135985.txt
She s Out of My League_0815236.txt
Short
Sixteen Candles_0088128.txt
Slackers_0240900.txt
So I Married an Axe Murderer_0108174.txt
Sport
The 40 Year Old Virgin_0405422.txt
The Back up Plan_1212436.txt
The Holiday_0457939.txt
The House Bunny_0852713.txt
The Ugly Truth_1142988.txt
The Wedding Date_0372532.txt
There s Something About Mary_0129387.txt
This Is 40_1758830.txt
Thriller
Two and a Half Men_0369179.txt
Valentine s Day_0817230.txt
Wedding Crashers_0396269.txt
Wives and Lovers_0057688.txt
Yes Man_1068680.txt

compare_corpus_original/Comedy/Romance/Sci-Fi:
Real Genius_0089886.txt

compare_corpus_original/Comedy/Romance/Short:
The Things My Father Never Taught Me_2234521.txt

compare_corpus_original/Comedy/Romance/Sport:
Bull Durham_0094812.txt

compare_corpus_original/Comedy/Romance/Thriller:
Drop Dead Gorgeous_0157503.txt

compare_corpus_original/Comedy/Sci-Fi:
Airplane II The Sequel_0083530.txt
Dark Star_0069945.txt
Freaked_0109838.txt
Hot Tub Time Machine_1231587.txt
Space Milkshake_1954843.txt
The World s End_1213663.txt

compare_corpus_original/Comedy/Short:
After School Special_0371514.txt
Bropocalypse Now The Redux_2171807.txt
Crazy Love_0417555.txt
Grapes of Wrath_3764508.txt
Little Black Book_9109336.txt
Now or Never_0012512.txt
Shawshank Redemption_3125798.txt
Southgate to Brighton_7547872.txt
The Good Samaritan_2175086.txt
The X Files Fight the Future Blooper Reel_7083566.txt
Then She Was Gone_1541935.txt
Three Sappy People_0032029.txt
Thriller

compare_corpus_original/Comedy/Short/Thriller:
Identity Theft_1840923.txt

compare_corpus_original/Comedy/Sport:
Balls Out Gary the Tennis Coach_0787470.txt
Caddyshack_0080487.txt
Major League_0097815.txt
Semi Pro_0839980.txt
Talladega Nights The Ballad of Ricky Bobby_0415306.txt

compare_corpus_original/Comedy/Talk-Show:
Abhishek Bachchan Rishi Kapoor and Supriya Pathak_6321142.txt
Black Mirror Review The National Anthem SPOILERS_7938500.txt
Black Mirror Review USS Callister SPOILERS_7818912.txt
Game of Thrones Review The Dragon and the Wolf Season 7 Episode 7_7317326.txt
How to Train Your Dragon The Hidden World Trailer Thoughts_8542038.txt
Paddington 2_7904114.txt
Supergirl Captain America 1990 and Roger Corman s Fantastic Four_4062018.txt
The Grand Tour_5712554.txt
The Iron Throne Game of Thrones AWFUL Final episode_11628564.txt
War for Planet of the Apes 2nd Trailer Reaction_6845022.txt
Wes Cravens New Nightmare_10961244.txt

compare_corpus_original/Comedy/Thriller:
Suburbicon_0491175.txt

compare_corpus_original/Comedy/War:
The Men Who Stare at Goats_1234548.txt

compare_corpus_original/Comedy/Western:
Blazing Saddles_0071230.txt

compare_corpus_original/Crime:
Documentary
Drama
E101 Pilot_10161616.txt
Thriller

compare_corpus_original/Crime/Documentary:
Drama
Unusual Suspects_1546360.txt

compare_corpus_original/Crime/Documentary/Drama:
Cabin in the Woods_11768622.txt

compare_corpus_original/Crime/Drama:
12 Angry Men_0118528.txt
9 millimeter_0118542.txt
American Hustle_1800241.txt
Animal Kingdom_1313092.txt
Boyz n the Hood_0101507.txt
Casino_0112641.txt
Cool Hand Luke_0061512.txt
Drive_0780504.txt
Drugstore Cowboy_0097240.txt
Film-Noir
Frozen River_0978759.txt
Gangs of New York_0217505.txt
Gold_1800302.txt
Hard Eight_0119256.txt
Highway_0165361.txt
History
Homicide The Movie_0226771.txt
In the Bedroom_0247425.txt
Light Sleeper_0102307.txt
Maria Full of Grace_0390221.txt
Mobsters_0102460.txt
Music
Mystery
Once Upon a Time in America_0087843.txt
Outbreak_0525549.txt
Pulp Fiction_0110912.txt
Romance
Scarface_0086250.txt
Sci-Fi
Smoke Gets in Your Eyes_0614236.txt
Sport
Spring Breakers_2101441.txt
Taxi Driver_0075314.txt
The Godfather Coda The Death of Michael Corleone_0099674.txt
The Godfather Part II_0071562.txt
The Godfather_0068646.txt
The Man Who Wasn t There_0243133.txt
Thriller
To Kill a Mockingbird_0056592.txt
True Believer_0098524.txt
Wall Street_0094291.txt
Western

compare_corpus_original/Crime/Drama/Film-Noir:
An Act of Murder_0040072.txt
Thriller

compare_corpus_original/Crime/Drama/Film-Noir/Thriller:
Angels with Dirty Faces_0029870.txt
Killer s Kiss_0048254.txt
The Desperate Hours_0047985.txt
The Night of the Hunter_0048424.txt

compare_corpus_original/Crime/Drama/History:
The Conspirator_0968264.txt
Thriller

compare_corpus_original/Crime/Drama/History/Thriller:
22 July_7280898.txt

compare_corpus_original/Crime/Drama/Music:
Hustle Flow_0410097.txt

compare_corpus_original/Crime/Drama/Mystery:
Before and After_0115645.txt
Evil Under the Sun_0083908.txt
Glengarry Glen Ross_0104348.txt
Grand Hotel_7671068.txt
In the Valley of Elah_0478134.txt
Motherless Brooklyn_0385887.txt
Murderland_1531804.txt
Thriller

compare_corpus_original/Crime/Drama/Mystery/Thriller:
8MM_0134273.txt
Anatomy of a Murder_0052561.txt
Awake_0211933.txt
Bad Times at the El Royale_6628394.txt
Body Double_0086984.txt
Breakdown_0118771.txt
Deception_0800240.txt
Devil in a Blue Dress_0112857.txt
Diamond Dust_4003070.txt
Disturbia_0486822.txt
Dressed to Kill_0080661.txt
Entrapment_0629253.txt
Gone Baby Gone_0452623.txt
In the Heat of the Night_0061811.txt
Inside Man_0454848.txt
Jennifer 8_0104549.txt
Knight Moves_0104627.txt
L A Confidential_0119488.txt
Michael Clayton_0465538.txt
Mystic River_0327056.txt
Prisoners_1392214.txt
Se7en_0114369.txt
Sleuth_0857265.txt
The Black Dahlia_0387877.txt
The Client_0109446.txt
The General s Daughter_0144214.txt
The Girl on the Train_3631112.txt
The Girl with the Dragon Tattoo_1568346.txt
The Last Kiss Goodnight_0700739.txt
The Limey_0165854.txt
The Pelican Brief_0107798.txt
The Salton Sea_0235737.txt
The Watcher_0204626.txt
True Crime_0139668.txt
Under the Silver Lake_5691670.txt
Western
Wild Things Diamonds in the Rough_0448179.txt
Wild Things_0120890.txt
Wind River_5362988.txt
Witness for the Prosecution_0051201.txt
Wonderland_0335563.txt
You Were Never Really Here_5742374.txt
Zodiac_0443706.txt

compare_corpus_original/Crime/Drama/Mystery/Thriller/Western:
Bad Day at Black Rock_0047849.txt
The Hateful Eight_3460252.txt

compare_corpus_original/Crime/Drama/Romance:
An American Tragedy_0021607.txt
Private Lives_12560270.txt
Queen Slim_8722346.txt
Thriller

compare_corpus_original/Crime/Drama/Romance/Thriller:
Body Heat_0082089.txt
Notes on a Scandal_0465551.txt
Rushlights_1536437.txt
The Crying Game_0104036.txt
The Lost Son_0144286.txt
The Public Eye_0105187.txt
The Wild One_0047677.txt
True Romance_0108399.txt
Witness_0090329.txt

compare_corpus_original/Crime/Drama/Sci-Fi:
A Clockwork Orange_0066921.txt

compare_corpus_original/Crime/Drama/Sport:
Hard Times_0073092.txt
Two for the Money_0417217.txt

compare_corpus_original/Crime/Drama/Thriller:
21 Grams_0315733.txt
A Perfect World_0107808.txt
A Simple Plan_0120324.txt
American Bully_1169133.txt
Apt Pupil_0118636.txt
Bad Lieutenant_0103759.txt
Blood Simple_0086979.txt
Blood and Wine_0115710.txt
Blue Ruin_2359024.txt
Boiler Room_0181984.txt
Breaking Bad_0903747.txt
Collateral_0369339.txt
Cop Land_0118887.txt
Enough_0278435.txt
Fargo_2802850.txt
Fracture_0488120.txt
Frailty_0264616.txt
Hannibal_0212985.txt
Heat_0113277.txt
Jackie Brown_0119396.txt
Jade_0113451.txt
Jimmy and Judy_0425151.txt
John Q_0251160.txt
Joker_7286456.txt
Kalifornia_0107302.txt
Last Time Forever_0479942.txt
Love Bones_2419232.txt
Mean Streets_0070379.txt
Miller s Crossing_0100150.txt
Mr Brooks_0780571.txt
No Country for Old Men_0477348.txt
On the Waterfront_0047296.txt
Panic Room_0258000.txt
Playback_1729217.txt
Reasonable Doubt_2304953.txt
Reservation Road_0831884.txt
Road to Perdition_0257044.txt
Rolling Thunder_0076637.txt
Roman J Israel Esq_6000478.txt
Sexy Beast_0203119.txt
The American_1440728.txt
The Departed_0407887.txt
The Gambler_2039393.txt
The Grifters_0099703.txt
The Informers_0865554.txt
The Life of David Gale_0289992.txt
The Lincoln Lawyer_1189340.txt
The Place Beyond the Pines_1817273.txt
The Silence of the Lambs_0102926.txt
The Talented Mr Ripley_0134119.txt
The Town_0840361.txt
Traffic_0181865.txt
Training Day_0139654.txt
U Turn_0120399.txt
Unthinkable_0914863.txt
We Own the Night_0498399.txt
While She Was Out_0887971.txt

compare_corpus_original/Crime/Drama/Western:
The Sisters Brothers_4971344.txt

compare_corpus_original/Crime/Thriller:
Asesinos por naturaleza_0309302.txt
Green Guys_1514045.txt
Killing Zoe_0110265.txt
Mute Witness_0110604.txt
Ocean s Eleven_0240772.txt
Ocean s Twelve_0349903.txt
Phone Booth_0183649.txt
Shallow Grave_0111149.txt
The Box_0928188.txt

compare_corpus_original/Documentary:
1976 l lection du Parti qu b cois_11327984.txt
50 50_4487264.txt
A Child Is Born The Scottish Doctor_0899329.txt
Alien Engineering Part 1_1713914.txt
Beach Theme Railroad Apartment_7239184.txt
Blood Roses and Deadly Diamonds_3908274.txt
Case 39_3022534.txt
City Hall_12094720.txt
Deep Sky Eye_9489732.txt
Drama
Far from the Madding Crowd_5146456.txt
Fast Five_3022828.txt
Fernando Arrabal lit Sa corolle noire ditions A Biren suivi de Ah la belle ann e ditions Ginasservis et Paris_12447550.txt
Get Low_3022266.txt
Grapes of Wrath The Ghost of Modern America_11127676.txt
History
Kim Cattrall Sexual Intelligence_0490603.txt
Last Tangle in Paris_2250606.txt
Moebius Redux A Life in Pictures_1029340.txt
Moneyball_3024352.txt
Monty Roberts A Real Horse Whisperer_1477465.txt
Short
Southern Belle_7100408.txt
Sport
Stuntman_6539830.txt
Talk-Show
The Italians of Egypt_6340290.txt
The Men Who Stare at Goats_1128598.txt
The Theory of Everything God Devils Dimensions Man_5124130.txt
Three Thousand Mile Garden_1426967.txt
Time Machine The True Story of the Screaming Eagles The 101st Airborne_1243956.txt
Wes Craven Nightmare on Elm Street Johny Depp_7095810.txt
Western
Working for the Man_1364020.txt
X Men Origins Wolverine_3012064.txt

compare_corpus_original/Documentary/Drama:
Streetwise_0088196.txt

compare_corpus_original/Documentary/History:
Naked Planet_0441831.txt
Reality-TV
The Reagans_12351448.txt
War

compare_corpus_original/Documentary/History/Reality-TV:
Ghost Adventures_1319900.txt
Pride and Prejudice_1332374.txt

compare_corpus_original/Documentary/History/War:
Crusades_0111931.txt
Spitfire_5913184.txt

compare_corpus_original/Documentary/Short:
2010 The Odyssey Continues_0235153.txt
A Message for Peace Making Hotel Rwanda_0476811.txt
Gran Torino Next Door_1753876.txt
Harry Potter and the Half Blood Prince_1470324.txt
Hellbound Hellraiser II Lost in the Labyrinth_0401463.txt
Lon_7663372.txt
Sunshine Cleaning A Fresh Look at a Dirty Business_1517098.txt
The Best Exotic Marigold Hotel Behind the Story Lights Colours and Smiles_5173200.txt
The Meaning of Monty Python s Meaning of Life_0472471.txt
The Personal Diaries_3328956.txt
V for Vendetta Unmasked_0775408.txt
War

compare_corpus_original/Documentary/Short/War:
Liberty s Triumph_1486791.txt

compare_corpus_original/Documentary/Sport:
Last Chance U_5863126.txt

compare_corpus_original/Documentary/Talk-Show:
Ex Machina_4601270.txt
The Thin Man_0820597.txt

compare_corpus_original/Documentary/Western:
Sitting Bull A Stone in My Heart_1493183.txt

compare_corpus_original/Drama:
25th Hour_0307901.txt
99 Homes_2891174.txt
A Fantastic Woman_5639354.txt
A Hard Days Night_0581729.txt
A Thousand Acres_0120323.txt
About Alex_2667918.txt
After the Wedding_7985692.txt
All About Eve_0042192.txt
All God s Children Can Dance_0847214.txt
American Beauty_0169547.txt
American History X_0120586.txt
American Madness_0022626.txt
An Education_1174732.txt
Away from Her_0491747.txt
Babel_0449467.txt
Bloodwork_0711844.txt
Blue Jasmine_2334873.txt
Bodies Rest Motion_0106447.txt
Boogie Nights_0118749.txt
Boyhood_1065073.txt
Bringing Ashley Home_1765730.txt
Candle to Water_2387411.txt
Capernaum_8267604.txt
Cell The Web Series_1667667.txt
Cherry_9130508.txt
Cinema Paradiso_0095765.txt
City of Joy_0103976.txt
Cortes_3523738.txt
Crash_0115964.txt
Custody_6002232.txt
Driving Miss Daisy_0097239.txt
Easily Broken_0946528.txt
Edward Ford IMDb_3020462.txt
El pianista_0158088.txt
Elizabeth Blue_5881892.txt
Equity_3958780.txt
Family
Fantasy
Fences_2671706.txt
Fight Club_0137523.txt
Film-Noir
Five Easy Pieces_0065724.txt
For Colored Girls_1405500.txt
Four Feathers_0005353.txt
Foxtrot_6896536.txt
Fried Green Tomatoes_0101921.txt
Full Body Massage_0113131.txt
Happy End_5304464.txt
Him Here After_2379480.txt
History
Honey Boy_8151874.txt
Horror
I Smile Back_3640682.txt
I ve Loved You So Long_1068649.txt
If I Had a Hammer_0210742.txt
Julia_0076245.txt
Kids_0113540.txt
Kiss of the Spider Woman_0089424.txt
Kramer vs Kramer_0079417.txt
L oeuvre au noir_0095773.txt
Las calles sin nombre_3174956.txt
Life as a House_0264796.txt
Little Men_4919484.txt
Locke_2692904.txt
Long Way Down_2207528.txt
Loveless_6304162.txt
Magnolia_0175880.txt
Makebelieve_0305793.txt
Manchester by the Sea_4034228.txt
Margaret_0466893.txt
Mary Rose_0417952.txt
Midnight Cowboy_0064665.txt
Miss Sloane_4540710.txt
Moonlight_4975722.txt
Mud_1935179.txt
Mumbai Diaries_1433810.txt
Music
My Own Private Idaho_0102494.txt
Mystery
Network_0074958.txt
Norma Rae_0079638.txt
Novitiate_4513316.txt
On Golden Pond_0082846.txt
One Flew Over the Cuckoo s Nest_0073486.txt
Ordinary People_0081283.txt
Pain and Glory_8291806.txt
Panther_0114084.txt
Pariah_1233334.txt
Paris Texas_0087884.txt
Philadelphia_0107818.txt
Plastic Man_0200365.txt
Precious_0929632.txt
Promised Land_2091473.txt
R D Laing IMDb_4153228.txt
Rabbit Hole_0935075.txt
Rails Ties_0822849.txt
Rambling Rose_0102753.txt
Rebel Without a Cause_0048545.txt
Requiem for a Dream_0180093.txt
Roma_6155172.txt
Romance
Ronnie Rocket IMDb_3076988.txt
Scent of a Woman_0105323.txt
Sci-Fi
Sex Lies and Videotape_0098724.txt
Shoot the Moon_0084675.txt
Short
Sling Blade_0117666.txt
Smashed_2063781.txt
So Pretty_9595506.txt
Sport
Stolen Summer_0286162.txt
Synecdoche New York_0383028.txt
The Artist and the Model_1990217.txt
The Bachelor Party_0050156.txt
The Beaver_1321860.txt
The Believer_0247199.txt
The Blue Hotel_0554018.txt
The Cincinnati Kid_0059037.txt
The Company Men_1172991.txt
The Crowded Room IMDb_0411256.txt
The Day the Clown Cried_0068451.txt
The Deep End of the Ocean_0120646.txt
The Florida Project_5649144.txt
The Hand That Rocks the Cradle_0008041.txt
The Help_1454029.txt
The Ice Storm_0119349.txt
The Kingdom of Heaven IMDb_3762612.txt
The Last Black Man in San Francisco_4353250.txt
The Last Dance_0246748.txt
The Last Flight_0022054.txt
The Last Temptation of Christ_0095497.txt
The Low Life_0110400.txt
The Master_1560747.txt
The Only Living Boy in New York_0460890.txt
The Other Side of the Wind_0069049.txt
The Passion of the Christ_0335345.txt
The Ploughman s Lunch_0086122.txt
The Road_0898367.txt
The Russell Girl_1097649.txt
The Shawshank Redemption_0111161.txt
The Shift_1333015.txt
The Shipping News_0120824.txt
The Silence_4603640.txt
The Sweet Hereafter_0120255.txt
The Swimmer_0063663.txt
The Verdict_0084855.txt
The Visitor_0969307.txt
The West Wing_0200276.txt
The White Angel_1064931.txt
The Wife_3750872.txt
The Woodsman_0361127.txt
There Will Be Blood_0469494.txt
Thirteen Conversations About One Thing_0268690.txt
Three Days to Live_0805337.txt
Thriller
To Sleep with Anger_0100791.txt
Tom Brown s Schooldays_0415322.txt
Trainspotting_0117951.txt
Viridiana_0055601.txt
Wall Street Money Never Sleeps_1027718.txt
War
Way Back Home_2018166.txt
Western
What Price Hollywood_0023686.txt
What They Had_6662736.txt
You Can Count on Me_0203230.txt

compare_corpus_original/Drama/Family:
Fantasy
Romance
Sounder_0069303.txt
Sport
Thriller

compare_corpus_original/Drama/Family/Fantasy:
It s a Wonderful Life_0038650.txt
Sport

compare_corpus_original/Drama/Family/Fantasy/Sport:
Field of Dreams_0097351.txt

compare_corpus_original/Drama/Family/Romance:
Taking Sides_0665723.txt

compare_corpus_original/Drama/Family/Sport:
The Rookie_0265662.txt

compare_corpus_original/Drama/Family/Thriller:
The Paradise Virus_0352696.txt

compare_corpus_original/Drama/Fantasy:
A Christmas Carol_0044008.txt
Enter the Void_1191111.txt
Horror
Mystery
Romance
The Seventh Seal_0050976.txt
The Tree of Life_0478304.txt
War

compare_corpus_original/Drama/Fantasy/Horror:
Ginger Snaps_0210070.txt
I Walked with a Zombie_0036027.txt
Mystery
Queen of the Damned_0238546.txt
The Company of Wolves_0087075.txt
The Magic Toyshop_0097806.txt
Thriller

compare_corpus_original/Drama/Fantasy/Horror/Mystery:
The Gift_0219699.txt
The Lighthouse_7984734.txt
Thriller

compare_corpus_original/Drama/Fantasy/Horror/Mystery/Thriller:
Crimson Peak_2554274.txt
Let Me In_1228987.txt
What Lies Beneath_0161081.txt

compare_corpus_original/Drama/Fantasy/Horror/Thriller:
Doctor Sleep_5606664.txt
The Craft_0115963.txt
The Wolfman_0780653.txt

compare_corpus_original/Drama/Fantasy/Mystery:
Romance
Sam I Am_0539417.txt
Thriller

compare_corpus_original/Drama/Fantasy/Mystery/Romance:
Portrait of Jennie_0040705.txt

compare_corpus_original/Drama/Fantasy/Mystery/Thriller:
The Nines_0810988.txt

compare_corpus_original/Drama/Fantasy/Romance:
Beauty and the Beast_0038348.txt
Edward Scissorhands_0099487.txt
Meet Joe Black_0119643.txt
Sci-Fi
Somewhere in Time_0081534.txt
The Curious Case of Benjamin Button_0421715.txt
The Twilight Saga Eclipse_1325004.txt
The Twilight Saga New Moon_1259571.txt
Thriller

compare_corpus_original/Drama/Fantasy/Romance/Sci-Fi:
Mr Nobody_0485947.txt
The Time Traveler s Wife_0452694.txt

compare_corpus_original/Drama/Fantasy/Romance/Thriller:
Ghost_0099653.txt

compare_corpus_original/Drama/Fantasy/War:
Pan s Labyrinth_0457430.txt

compare_corpus_original/Drama/Film-Noir:
All the King s Men_0041113.txt
Call Northside 777_0040202.txt
Sunset Blvd_0043014.txt
Sweet Smell of Success_0051036.txt
The Lost Weekend_0037884.txt

compare_corpus_original/Drama/History:
Horror
Romance
Salt of the Earth_0047443.txt
The Grapes of Wrath_0032551.txt
Thriller
Troy_0332452.txt
War

compare_corpus_original/Drama/History/Horror:
Beloved_0120603.txt

compare_corpus_original/Drama/History/Romance:
Mandingo_0073349.txt
War

compare_corpus_original/Drama/History/Romance/War:
Gone with the Wind_0031381.txt

compare_corpus_original/Drama/History/Thriller:
Bridge of Spies_3682448.txt
JFK_0102138.txt
Thirteen Days_0146309.txt
War

compare_corpus_original/Drama/History/Thriller/War:
Battleship Potemkin_0015648.txt
Salvador_0091886.txt
Valkyrie_0985699.txt

compare_corpus_original/Drama/History/War:
Black Hawk Down_0265086.txt
Land of Mine_3841424.txt
Macbeth_10095582.txt
The Empty Mirror_0116192.txt

compare_corpus_original/Drama/Horror:
Count Dracula_0065569.txt
Count Dracula_0075882.txt
Freaks_0022913.txt
Horror of Dracula_0051554.txt
Interview with the Vampire The Vampire Chronicles_0110148.txt
Mystery
Romance
Rosemary s Baby_0063522.txt
Sci-Fi
The Babadook_2321549.txt
The Shining_0081505.txt
Thriller

compare_corpus_original/Drama/Horror/Mystery:
Jacob s Ladder_0099871.txt
Mother_5109784.txt
Romance
Sci-Fi
Short
The Seventh Victim_0036341.txt
Thriller

compare_corpus_original/Drama/Horror/Mystery/Romance:
The Birds_0056869.txt

compare_corpus_original/Drama/Horror/Mystery/Sci-Fi:
Brightburn_7752126.txt
Thriller

compare_corpus_original/Drama/Horror/Mystery/Sci-Fi/Thriller:
Nightflyers_6903284.txt
Pi_0138704.txt

compare_corpus_original/Drama/Horror/Mystery/Short:
Duplex_1410017.txt

compare_corpus_original/Drama/Horror/Mystery/Thriller:
Bloody Murder 2 Closing Camp_0303732.txt
Chasing Sleep_0221069.txt
Eli_5294518.txt
Hereditary_7784604.txt
In the Mouth of Madness_0113409.txt
Isle of the Dead_0037820.txt
Lights Out_4786282.txt
Midsommar_8772262.txt
Remember Me_3484180.txt
Summer of 84_5774450.txt
The Haunting in Connecticut_0492044.txt
The Killing of a Sacred Deer_5715874.txt
The Mothman Prophecies_0265349.txt
The Unborn_1139668.txt
Twin Peaks Fire Walk with Me_0105665.txt
War

compare_corpus_original/Drama/Horror/Mystery/Thriller/War:
The Bunker_0252963.txt

compare_corpus_original/Drama/Horror/Romance:
Memento Mori_0266075.txt
Sci-Fi
Thriller

compare_corpus_original/Drama/Horror/Romance/Sci-Fi:
Mary Shelley s Frankenstein_0109836.txt

compare_corpus_original/Drama/Horror/Romance/Thriller:
Spellbinder_0096152.txt

compare_corpus_original/Drama/Horror/Sci-Fi:
A Quiet Place_6644200.txt
Splice_1017460.txt
The Fly_0091064.txt
The Last Man on Earth_0058700.txt
Thriller

compare_corpus_original/Drama/Horror/Sci-Fi/Thriller:
28 Days Later_0289043.txt
Under the Skin_1441395.txt
Victor Frankenstein_1976009.txt

compare_corpus_original/Drama/Horror/Thriller:
American Horror Story_1844624.txt
Bedlam_0038343.txt
Lost Souls_0160484.txt
Martyrs_1663655.txt
Nebraska_1804272.txt
Peeping Tom_0054167.txt
Seven Days to Live_0221928.txt
Take Shelter_1675192.txt
The Tattooist_0817228.txt
Willard_0310357.txt
Wind Chill_0486051.txt

compare_corpus_original/Drama/Music:
8 Mile_0298203.txt
Her Smell_7942742.txt
Mr Holland s Opus_0113862.txt
Music of the Heart_0166943.txt
Musical
Romance
Tender Mercies_0086423.txt
Velvet Goldmine_0120879.txt
Vox Lux_5960374.txt
Whiplash_2582802.txt
Young Soul Rebels_0103312.txt

compare_corpus_original/Drama/Music/Musical:
All That Jazz_0078754.txt
Cabaret_0068327.txt
Romance

compare_corpus_original/Drama/Music/Musical/Romance:
Burlesque_1126591.txt
The Jazz Singer_0018037.txt

compare_corpus_original/Drama/Music/Romance:
A Star Is Born_0075265.txt
Crazy Heart_1263670.txt
Flashdance_0085549.txt
Purple Rain_0087957.txt
The Duchess of Langeais_0781435.txt
The Sun Is also a Star_6423362.txt

compare_corpus_original/Drama/Mystery:
Agnes of God_0088683.txt
Citizen Kane_0033467.txt
L Avventura_0053619.txt
Lone Star_0116905.txt
Romance
Sci-Fi
The Past_2404461.txt
The Rapture_0102757.txt
Thriller
War
Winter s Bone_1399683.txt
Wonderstruck_5208216.txt

compare_corpus_original/Drama/Mystery/Romance:
Julieta_4326444.txt
Sci-Fi
Thriller
War

compare_corpus_original/Drama/Mystery/Romance/Sci-Fi:
Solaris_0307479.txt

compare_corpus_original/Drama/Mystery/Romance/Thriller:
Deceptions_0089008.txt
Labor of Love IMDb_1677731.txt
Rebecca_0032976.txt
Snow Falling on Cedars_0120834.txt
The Constant Gardener_0387131.txt

compare_corpus_original/Drama/Mystery/Romance/War:
Atonement_0783233.txt

compare_corpus_original/Drama/Mystery/Sci-Fi:
I Think We re Alone Now_6169694.txt
K PAX_0272152.txt
Moon_1182345.txt
Thriller
War of the Worlds_9686194.txt
Westworld_0475784.txt
White People_2172095.txt

compare_corpus_original/Drama/Mystery/Sci-Fi/Thriller:
Arrival_2543164.txt
Cube_0123755.txt
Donnie Darko_0246578.txt
Kafka_0102181.txt
S Darko_1231277.txt
Signs_0286106.txt
The Expanse_3230854.txt
The Happening_0949731.txt
The Manchurian Candidate_0368008.txt
The Prestige_0482571.txt
The X Files_0120902.txt
Unbreakable_0217869.txt

compare_corpus_original/Drama/Mystery/Thriller:
A Perfect Getaway_0971209.txt
Affliction_0118564.txt
After Life_0838247.txt
Basic Instinct_0103772.txt
Blue Velvet_0090756.txt
Buried_1462758.txt
Chinatown_0071315.txt
Copycat_0112722.txt
Don t Look Now_0069995.txt
First Reformed_6053438.txt
Flightplan_0408790.txt
Gone Girl_2267998.txt
Insomnia_0278504.txt
Martha Marcy May Marlene_1441326.txt
Mulholland Dr_1619856.txt
Searching_7668870.txt
Secret Window_0363988.txt
Stay_0371257.txt
The Devil s Advocate_0118971.txt
The Firm_0106918.txt
The Sixth Sense_0167404.txt
The Village_0368447.txt
Tinker Tailor Soldier Spy_1340800.txt
We Need to Talk About Kevin_1242460.txt

compare_corpus_original/Drama/Mystery/War:
Apocalypse Now_0078788.txt

compare_corpus_original/Drama/Romance:
A Single Man_1315981.txt
A Tree Grows in Brooklyn_0038190.txt
Amour_1602620.txt
An Officer and a Gentleman_0084434.txt
Angel Eyes_0225071.txt
Anna Karenina_1781769.txt
At First Sight_0132512.txt
Au pan coup_0290137.txt
Autumn in New York_0174480.txt
Before Midnight_2209418.txt
Before Sunrise_0112471.txt
Before Sunset_0381681.txt
Blue Valentine_1120985.txt
Call Me by Your Name_5726616.txt
Carol_2402927.txt
Chocolat_0241303.txt
Cruel Intentions_0139134.txt
Days of Heaven_0077405.txt
Disobedience_6108178.txt
Downton Abbey_1606375.txt
Far from Heaven_0297884.txt
Forrest Gump_0109830.txt
Frankie_8019694.txt
Good Will Hunting_0119217.txt
Grand Hotel_0022958.txt
Great Expectations_0119223.txt
Hook Line and Sinker Part 2_0549217.txt
If Beale Street Could Talk_7125860.txt
Indecent Proposal_0107211.txt
Inventing the Abbotts_0119381.txt
Jack Goes Boating_1278379.txt
Jane Eyre_1229822.txt
Just One Look Part 1_1190257.txt
Kids in the Hall_3360652.txt
Leaving Las Vegas_0113627.txt
Life Itself_5989218.txt
Life on Liberty Street_0399281.txt
Little Women_3281548.txt
Marty_0048356.txt
Memoirs of a Geisha_0397535.txt
Monster s Ball_0285742.txt
Normal Adolescent Behavior_0790721.txt
Nothing But a Man_0058414.txt
Othello_0114057.txt
Petulia_0063426.txt
Phantom Thread_5776858.txt
Poetic Justice_0107840.txt
Pride Prejudice_0414387.txt
Rachel Getting Married_1084950.txt
Remember Me_1403981.txt
Revolutionary Road_0959337.txt
Romeo Juliet_0117509.txt
Rust and Bone_2053425.txt
Sci-Fi
Sense and Sensibility_0114388.txt
Some Kind of Wonderful_0094006.txt
Sport
St Elmo s Fire_0090060.txt
Sweet November_0230838.txt
The Accidental Tourist_0094606.txt
The Bridges of Madison County_0112579.txt
The Cider House Rules_0124315.txt
The Cooler_0318374.txt
The Fault in Our Stars_2582846.txt
The Good Girl_0279113.txt
The Great Gatsby_1343092.txt
The Hours_0274558.txt
The Last Picture Show_0067328.txt
The Perks of Being a Wallflower_1659337.txt
The Reader_0976051.txt
The Scarlet Letter_0114345.txt
Third Person_2343793.txt
Thriller
Titanic_0120338.txt
Under the Greenwood Tree_0465653.txt
Up Close Personal_0118055.txt
War
Water for Elephants_1067583.txt
Western
Women in Love_0066579.txt
You Came Along_0038263.txt

compare_corpus_original/Drama/Romance/Sci-Fi:
Eternal Sunshine of the Spotless Mind_0338013.txt
Her_1798709.txt
Never Let Me Go_1334260.txt
Thriller

compare_corpus_original/Drama/Romance/Sci-Fi/Thriller:
Passengers_1355644.txt

compare_corpus_original/Drama/Romance/Sport:
Love Basketball_0199725.txt
Waves_8652728.txt

compare_corpus_original/Drama/Romance/Thriller:
Broken Embraces_0913425.txt
Labor Day_1967545.txt
Match Point_0416320.txt
Mo gui tian shi_0320109.txt
Obsessed_1198138.txt
The Human Stain_0308383.txt
Three Wishes_0310227.txt
Unfaithful_0250797.txt

compare_corpus_original/Drama/Romance/War:
Casablanca_0034583.txt
Come See the Paradise_0099291.txt
Coming Home_0077362.txt
Dear John_0989757.txt
Doctor Zhivago_0059113.txt
From Here to Eternity_0045793.txt
The English Patient_0116209.txt
The Life and Death of Colonel Blimp_0036112.txt
The Messenger_0790712.txt
The Year of Living Dangerously_0086617.txt

compare_corpus_original/Drama/Romance/Western:
The Horse Whisperer_0119314.txt

compare_corpus_original/Drama/Sci-Fi:
A I Artificial Intelligence_0212720.txt
Brazil_0088846.txt
Close Encounters of the Third Kind_0075860.txt
Downsizing_1389072.txt
Metropolis_0017136.txt
Short
The Day After_0085404.txt
The Day the Earth Stood Still_0043456.txt
Thriller
Upstream Color_2084989.txt
War

compare_corpus_original/Drama/Sci-Fi/Short:
Doing Time_0808884.txt

compare_corpus_original/Drama/Sci-Fi/Thriller:
Chronicle_1706593.txt
Fahrenheit 451_0360556.txt
Gattaca_0119177.txt
Gravity_1454468.txt
Lucy in the Sky_4682804.txt
THX 1138_0066434.txt
The Butterfly Effect_0289879.txt

compare_corpus_original/Drama/Sci-Fi/War:
Things to Come_0028358.txt

compare_corpus_original/Drama/Short:
3000_4759852.txt
53 1_4329278.txt
Fogg s Millions_0221183.txt
Maniacs_4626904.txt
One Saliva Bubble_12999032.txt
Reservoir Dogs Sundance Institute 1991 June Film Lab_6493238.txt
Starcrossed_0420931.txt
The Doors of Perception_4649358.txt
The Restless Spirit_0132471.txt

compare_corpus_original/Drama/Sport:
Any Given Sunday_0146838.txt
Creed II_6343314.txt
Creed_3076658.txt
Million Dollar Baby_0405159.txt
Rocky V_0100507.txt
Rocky_0075148.txt
Sidewalks of New York_0164167.txt
The Hustler_0054997.txt
The Power of One_0105159.txt
The Way Back_8544498.txt
The Wrestler_1125849.txt

compare_corpus_original/Drama/Thriller:
A Death in the Gunj_5918074.txt
A Dry White Season_0097243.txt
A Few Good Men_0104257.txt
A History of Violence_0399146.txt
A Separation_1832382.txt
Anonymous_1521197.txt
Arbitrage_1764183.txt
Black Swan_0947798.txt
Bright Angel_0101510.txt
Bringing Out the Dead_0163988.txt
Cape Fear_0055824.txt
Contagion_1598778.txt
Disclosure_0109635.txt
Fatal Attraction_0093010.txt
Final Analysis_0104265.txt
Flight_1907668.txt
Hard Candy_0424136.txt
Margin Call_1615147.txt
Misery_0100157.txt
Nocturnal Animals_4550098.txt
Norman_4191702.txt
One Eight Seven_0118531.txt
Rendition_0804522.txt
Return to Sender_2948790.txt
Ringer_0117480.txt
Room_3170832.txt
Shadow Dancer_1770734.txt
Single White Female_0105414.txt
Sketch Artist II Hands That See_0114463.txt
Stone_1423995.txt
Suburbia_0086589.txt
Syriana_0365737.txt
The Abduction_0115452.txt
The Debt_1226753.txt
The House Next Door_0286702.txt
The Ides of March_1124035.txt
The Man Who Knew Too Much_0049470.txt
The Parallax View_0071970.txt
The Post_6294822.txt
War
Warning Shot_5113250.txt
Western

compare_corpus_original/Drama/Thriller/War:
The Beguiled_5592248.txt
The Hurt Locker_0887912.txt

compare_corpus_original/Drama/Thriller/Western:
High Noon_0044706.txt

compare_corpus_original/Drama/War:
1917_8579674.txt
84C MoPic_0096744.txt
Beasts of No Nation_1365050.txt
Cross of Iron_0074695.txt
Full Metal Jacket_0093058.txt
Mudbound_2396589.txt
Platoon_0091763.txt
Saving Private Ryan_0120815.txt
Son of Saul_3808342.txt
The Battle of Algiers_0058946.txt
The Deer Hunter_0077416.txt
The Thin Red Line_0058648.txt
The Thin Red Line_0120863.txt
Three Kings_0158436.txt
Under Fire_0086510.txt

compare_corpus_original/Drama/Western:
3 Godfathers_0040064.txt
Django Unchained_1853728.txt
Giant_0049261.txt
McCabe Mrs Miller_0067411.txt
Ride the High Country_0056412.txt
The Rider_6217608.txt
Unforgiven_0105695.txt

compare_corpus_original/Family:
A Snack to Remember_5293758.txt
Bright Birds_6022752.txt
Debt The Good the Bad the Ugly_1755079.txt
Dumb and Dumber_9113296.txt
Game-Show
Musical
Sci-Fi

compare_corpus_original/Family/Game-Show:
Nickelodeon Arcade_0300828.txt

compare_corpus_original/Family/Musical:
Sandman_0176118.txt

compare_corpus_original/Family/Sci-Fi:
E T the Extra Terrestrial_0083866.txt

compare_corpus_original/Fantasy:
Horror
Thriller
Unaired Game of Thrones Prequel Pilot_6857128.txt

compare_corpus_original/Fantasy/Horror:
A Nightmare on Elm Street 3 Dream Warriors_0093629.txt
A Nightmare on Elm Street 3 Freddy s rache_12734734.txt
A Nightmare on Elm Street 5 The Dream Child_0097981.txt
Freddy s Dead The Final Nightmare_0101917.txt
Mystery
Nosferatu_0013442.txt
Orgy of the Dead_0054240.txt
Pet Sematary II_0105128.txt
Thir13en Ghosts_0245674.txt
Thriller
Vampyr_0023649.txt

compare_corpus_original/Fantasy/Horror/Mystery:
1408_0450385.txt
Sleepy Hollow_0162661.txt
Thriller

compare_corpus_original/Fantasy/Horror/Mystery/Thriller:
Suspiria_1034415.txt
Wes Craven s New Nightmare_0111686.txt

compare_corpus_original/Fantasy/Horror/Thriller:
Cat People_0034587.txt
Fright Night_0089175.txt
Jason Goes to Hell The Final Friday_0107254.txt
Pet Sematary_0098084.txt

compare_corpus_original/Fantasy/Thriller:
The Hole_1085779.txt

compare_corpus_original/History:
Rocket Man_9279928.txt

compare_corpus_original/Horror:
13 13 13_2991516.txt
A Nightmare on Elm Street 2 Freddy s Revenge_0089686.txt
A Nightmare on Elm Street 4 The Dream Master_0095742.txt
A Nightmare on Elm Street_0087800.txt
Asylum_0068230.txt
Black Christmas_0454082.txt
Bram Stoker s Dracula_0103874.txt
Carrie_0074285.txt
Curse the Darkness IMDb_2443956.txt
Damien Omen II_0077394.txt
Edges of Darkness_1442498.txt
Every I Know What You Did Last Summer Movie Ranked_13256474.txt
From Dusk Til Dawn_6146998.txt
Gateway IMDb_8765666.txt
Ghost Ship_0288477.txt
Halloween II_0082495.txt
Hellraiser III Hell on Earth_0104409.txt
House of 1000 Corpses_0251736.txt
It_1396484.txt
London After Midnight_0018097.txt
Mystery
Necromancer_0095716.txt
Prince of Darkness_0093777.txt
Sci-Fi
Short
Stigmata_0145531.txt
The Amityville Asylum_2216212.txt
The Bunker_1877788.txt
The Cabin in the Woods_1259521.txt
The Changeling_0080516.txt
The Evil Dead_0083907.txt
The Exorcist_0070047.txt
The Final Terror_0082379.txt
The Howling_0082533.txt
The Human Centipede First Sequence_1467304.txt
The Omen_0075005.txt
The Ouija Experiment_2364842.txt
The Phantom of the Opera_0016220.txt
The Ruins_0963794.txt
The Texas Chain Saw Massacre_0072271.txt
Thriller
Witchery_0096453.txt

compare_corpus_original/Horror/Mystery:
April Fool s Day_0090655.txt
I Know What You Did Last Summer_0119345.txt
I Still Know What You Did Last Summer_0130018.txt
Jeepers Creepers_0263488.txt
Mirrors_0790686.txt
Paranormal Activity_1179904.txt
Ringu_0178868.txt
Saw_0387564.txt
Sci-Fi
Scream 2_0120082.txt
Scream 3_0134084.txt
Scream 4_1262416.txt
Solstice_0473267.txt
Sorority Row_1232783.txt
The Blair Witch Project_0185937.txt
The Fog_0432291.txt
The Grudge_3612126.txt
The Ring_0298130.txt
Thriller

compare_corpus_original/Horror/Mystery/Sci-Fi:
The Thing_0084787.txt
Thriller

compare_corpus_original/Horror/Mystery/Sci-Fi/Thriller:
Disturbing Behavior_0134619.txt
Halloween III Season of the Witch_0085636.txt
The Fourth Kind_1220198.txt
The Relic_0120004.txt

compare_corpus_original/Horror/Mystery/Thriller:
Annabelle_3322940.txt
As Above So Below_2870612.txt
Cherry Falls_0175526.txt
Dead Silence_0455760.txt
Exorcist The Beginning_0204313.txt
Friday the 13th Part 2_0082418.txt
Friday the 13th_0758746.txt
From Hell_0120681.txt
Get Out_5052448.txt
Gothika_0348836.txt
Happy Death Day_5308322.txt
Hellraiser Deader_0337636.txt
Hellraiser Hellseeker_0274546.txt
Insidious Chapter 2_2226417.txt
It Follows_3235888.txt
Lord of Illusions_0113690.txt
Mystery of the Wax Museum_0024368.txt
Orphan_1148204.txt
Pet Sematary_0837563.txt
Psycho_0054215.txt
Slender Man_5690360.txt
Stir of Echoes_0164181.txt
The Conjuring_1457767.txt
The Grudge_0391198.txt
The Midnight Meat Train_0805570.txt
The Nun_5814060.txt
The Others_0230600.txt
The Trace We Leave Behind_4117326.txt
They_0283632.txt
Totem_6791238.txt
Urban Legend_0146336.txt
Us_6857112.txt
Valentine_0242998.txt
Velvet Buzzsaw_7043012.txt
When a Stranger Calls_0080130.txt

compare_corpus_original/Horror/Sci-Fi:
Alien_0078748.txt
Bird Box_2737304.txt
Body Snatchers_0106452.txt
Dr Jekyll and Mr Hyde_0022835.txt
Hellraiser Bloodline_0116514.txt
Invaders from Mars_0091276.txt
Mimic_0119675.txt
Plan 9 from Outer Space_0052077.txt
Rabid_5628902.txt
Shivers_0073705.txt
The Faculty_0133751.txt
The Thing from Another World_0044121.txt
Thriller
Twilight Zone The Movie_0086491.txt

compare_corpus_original/Horror/Sci-Fi/Thriller:
Alien Covenant_2316204.txt
Altered States_0080360.txt
Bats_0200469.txt
Event Horizon_0119081.txt
Land of the Dead_0418819.txt
Screamers_0114367.txt
The Blob_0094761.txt
The Cell_0209958.txt
The Island of Dr Moreau_0116654.txt
The Mist_0884328.txt
The Rage Carrie 2_0144814.txt
eXistenZ_0120907.txt

compare_corpus_original/Horror/Short:
Dead to Me_10160908.txt
Duchess the Xmas Killer_11343194.txt
Maleficent_3264268.txt
Unborn_1230395.txt

compare_corpus_original/Horror/Thriller:
ATM_1603257.txt
Animal Among Us_3612008.txt
Bad Dreams_0094701.txt
Bad Moon_0115610.txt
Candyman_0103919.txt
Children of the Corn_0087050.txt
Dark Asylum_0224626.txt
Day of the Dead_0088993.txt
Drag Me to Hell_1127180.txt
Fear of Clowns_0362636.txt
Final Destination 2_0309593.txt
Final Destination_0195714.txt
Friday the 13th Part III_0083972.txt
Friday the 13th Part VI Jason Lives_0091080.txt
Friday the 13th The Final Chapter_0087298.txt
Frost Portrait of a Vampire_0212277.txt
Halloween 4 The Return of Michael Myers_0095271.txt
Halloween H20 20 Years Later_0120694.txt
Halloween Resurrection_0220506.txt
Halloween The Curse of Michael Myers_0113253.txt
Hellbound Hellraiser II_0095294.txt
Hellraiser_0093177.txt
I Spit on Your Grave_1242432.txt
Malicious_6197494.txt
Night of the Living Dead_0063350.txt
Poltergeist_0084516.txt
Prom Night_0081383.txt
Texas Chainsaw_1572315.txt
The Body Snatcher_0037549.txt
The Crazies_0455407.txt
The Fog_0080749.txt
The Hills Have Eyes_0454841.txt
The Last House on the Left_0844708.txt
The Leopard Man_0036104.txt
The Purge_2184339.txt
The Strangers_0482606.txt
Timber Falls_0857295.txt
Vacancy_0452702.txt
Western

compare_corpus_original/Horror/Thriller/Western:
Dead Birds_0377749.txt
The Burrowers_0445939.txt

compare_corpus_original/Music:
Human Touch Babis Papadopoulos_2606376.txt
In Performance at the White House Thelonious Monk Institute of Jazz_1615849.txt
Mariachi El Bronx_5716702.txt
Prom 39 Bach Orchestral Transcriptions_1713081.txt
Reality-TV
Short
Talk-Show

compare_corpus_original/Music/Reality-TV:
Brightstar Buzz_7682456.txt

compare_corpus_original/Music/Short:
Beck 1000 BPM_8212568.txt
Lady Antebellum Lookin for a Good Time_10871176.txt
Skip Marley Cry to Me_11574380.txt
Sting They Dance Alone Cueca Solo_7573714.txt
The Cure Boys Don t Cry_8085166.txt

compare_corpus_original/Music/Talk-Show:
Mr and Mrs Smith Of Course You Are_0804059.txt

compare_corpus_original/Musical:
Bye Bye Bijou_9242596.txt
Short

compare_corpus_original/Musical/Short:
One Good Turn_0021214.txt

compare_corpus_original/Mystery:
Charlie Chan Carries On_0021733.txt
Charlie Chan s Chance_0022755.txt
Charlie Chan s Greatest Case_0023881.txt
Mind Games_0300500.txt
Thriller

compare_corpus_original/Mystery/Thriller:
Identity_0309698.txt
Lost Highway_0116922.txt
Rear Window_0047396.txt
The Ninth Gate_0142688.txt
Three Days of the Condor_0073802.txt

compare_corpus_original/News:
Hurt Locker Cherie Year One_2135208.txt
Kingsman Theory of Everything Foxcatcher_4682196.txt
OZ the Great and Powerful Snitch Dark Skies_3008428.txt
Primaries the Vice Presidency_3889492.txt
Talk-Show
Toilet Time Youth in Revolt Daybreakers Darksiders Might Magic Clash of Heroes and Twitter_12059586.txt

compare_corpus_original/News/Talk-Show:
Alfred Hitchcock and the Making of Psycho_1362861.txt
Captain Richard Phillips_1631589.txt

compare_corpus_original/Reality-TV:
Excess Baggage_2171882.txt
I ll Stop the World and Melt with You_2213523.txt
Nottingham_0905731.txt
Punch Drunk Love_6002148.txt
Sci-Fi
Shining The Light_9106126.txt
Short Term Pain Long Term Gain_2761612.txt
Sport
Talk-Show
Who s Your Daddy_0446076.txt
Wreck It Ralph_10946860.txt

compare_corpus_original/Reality-TV/Sci-Fi:
2001 A Space Road Odyssey_0288910.txt

compare_corpus_original/Reality-TV/Sport:
Vince The Roommate from Hell_1491722.txt

compare_corpus_original/Reality-TV/Talk-Show:
A Most Violent Year_5169360.txt

compare_corpus_original/Romance:
Branagh Theatre Live Romeo and Juliet_5943392.txt
High Fidelity_0876719.txt
Sci-Fi
Short
Western

compare_corpus_original/Romance/Sci-Fi:
Starman_0088172.txt
Thriller

compare_corpus_original/Romance/Sci-Fi/Thriller:
The Adjustment Bureau_1385826.txt

compare_corpus_original/Romance/Short:
The Phantom Menace_6892482.txt

compare_corpus_original/Romance/Western:
Rio Grande_0042895.txt

compare_corpus_original/Sci-Fi:
Back to the Planet of the Apes_0071184.txt
Encrypt_0338963.txt
Short
Thriller

compare_corpus_original/Sci-Fi/Short:
Robin The Story of Dick Grayson_1705130.txt

compare_corpus_original/Sci-Fi/Thriller:
Hardware_0099740.txt
Limitless_1219289.txt
Sunshine_0448134.txt
The Arrival_0115571.txt
The Atomic Submarine_0052587.txt

compare_corpus_original/Short:
2 Guns a Grenade a Pizza Guy_1871996.txt
An Unconventional Love Story The Making of Last Chance Harvey_2043778.txt
Charlie St Cloud T4 Movie Special_1738344.txt
Five Feet High and Rising_0240507.txt
Groupie_0212976.txt
London Fields Are Blue_0418838.txt
My Mother Dreams the Satan s Disciples in New York_0177023.txt
Non plus ultra_0385126.txt
One Soldier s Story The Journey of American Sniper_4781700.txt
Parallax view_8505542.txt
Room with a View_10404922.txt
Smokin Aces The Big Gun_1148297.txt
Special_0381613.txt
The Numbers_0497647.txt
Thriller
Vikings A Warrior Society Rites of Passage_4620494.txt
XTRMN8mm_5660414.txt

compare_corpus_original/Short/Thriller:
He Dies at the End_1753891.txt

compare_corpus_original/Talk-Show:
29th Street Highlander 2 The Quickening Billy Bathgate Year of the Gun_6099126.txt
Altered Carbon Episode 1 Spoiler Free Review Out of the Past_13255492.txt
American Gods 1x1 REACTION The Bone Orchard_11563674.txt
Baywatch_5797522.txt
Black Sails 1x6 REACTION VI_11027128.txt
Breaking Bad 3x11 REACTION Abiquiu_11724326.txt
Breaking Bad 3x3 REACTION I F T_11713132.txt
Breaking Bad Crafting a TV Pilot_7470416.txt
Brooklyn Nine Nine 1x13 REACTION The Bet_12904524.txt
Challenging Times During Adolescence with Dr Louise Hayes_13493454.txt
Chernobyl 1x2 REACTION Please Remain Calm_11524920.txt
Chernobyl 1x4 REACTION The Happiness of All Mankind_11524932.txt
Doom Patrol 1x1 REACTION Pilot_11528496.txt
Edge of Darkness When in Rome Saint John of Las Vegas Legion Tooth Fairy 44 Inch Chest_1596979.txt
Good Omens 1x1 REACTION In the Beginning_12150620.txt
Goonies 2_10326460.txt
Henry s Crime_2324817.txt
Indiana Jones and the Raiders of the Lost Ark_6358934.txt
Intelligence Pilot Episode Review_12487302.txt
Janice Dickinson_6288616.txt
Maverick Trading Mom The Return of Jafar Widows Peak Even Cowgirls Get the Blues_1949376.txt
Music Lyrics Bridge to Terabithia Breach Black Snake Moan The Lives of Others_7200804.txt
Professional Theatre 2_12821228.txt
Rick and Morty 1x11 REACTION Ricksy Business_12564112.txt
Rick and Morty 1x5 REACTION Meeseeks and Destroy_12564080.txt
Rick and Morty 2x2 REACTION Mortynight Run_12604042.txt
Royal Tenenbaums_12287150.txt
Sleepaway Camp Trilogy Review_4532344.txt
The Boys 1x1 REACTION The Name of the Game_11511586.txt
The Break Up The Omen Peaceful Warrior An Inconvenient Truth Twelve and Holding The Puffy Chair_7217830.txt
The Design of The Good Place Janets_12543550.txt
The Haunting of Hill House 1x1 REACTION Steven Sees a Ghost_11673608.txt
The Lord of the Rings Halloween Autumn Sonata Goin South Dogs The Dragon Lives The Hills Have Eyes_3438082.txt
The Revenant_5506074.txt
The Shipping News_7354772.txt
Tony Collins Sport in Capitalist Society A Short History_13044676.txt
True Detective Seeing Things Episode Review_12658012.txt
True Detective The Long Bright Dark Episode Review_12487418.txt
True Detective The Secret Fate Of All Life Episode Review_12658584.txt
Up Close and Personal_0497080.txt

compare_corpus_original/Thriller:
Dark Games_1234927.txt
Hider in the House_0097503.txt
His Secret Past_5865046.txt
Jorge Alberto vs The Neoliberal Demons_4203196.txt
Mr Mark Fenton_1282592.txt
Possessions_0227291.txt
Red Eye_0421239.txt
The Boy Next Door_3181822.txt
The Roommate_1265990.txt
The Utah Murder Project_0831374.txt
The Witching Hour_1634140.txt
War

compare_corpus_original/Thriller/War:
Saboteur_0035279.txt

compare_corpus_original/War:
To the White Sea IMDb_4969494.txt

compare_corpus_original/Western:
Glory Road_0502360.txt

compare_corpus_original/small:
test.txt
test2.txt

#### Run
------ STARTING ------
------ BEGINNING COMPARISON ------
Cleaning the comparison directory
Comparing initial build times...
Building index for old approach
Building index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file deletion
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Removing stale indexes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file modification
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Rebuilding index for file creation
Rebuilding index for old approach
Rebuilding index for new approach
Checking for changes...
Building index...
100% - Index building for files complete!
Merging indexes...
100% - Merging complete!
Index building complete!
Searching for old approach
Searching for new approach
Searching for old approach in sub dir
Searching for new approach in sub dir
-------- Building index --------
Old index build finished in 286.8267 seconds
New index build finished in 2672.1059 seconds
Old index rebuild after delete finished in 288.2643 seconds
New index rebuild after delete finished in 9.7177 seconds
Old index rebuild after modification finished in 291.8812 seconds
New index rebuild after modification finished in 9.1267 seconds
Old index rebuild after addition finished in 291.4151 seconds
New index rebuild after addition finished in 12.5753 seconds
-------- Index storage usage --------
The amount of storage used initially for old approach was 370727926 bytes
The amount of storage used after building index for old approach was 370727961 bytes
The amount of storage increase used by old approach was 1.0000x
The amount of storage used initially for new approach was 370727926 bytes
The amount of storage used after building index for new approach was 3521055012 bytes
The amount of storage increase used by new approach was 9.4977x
-------- Index searching --------
Old search index finished in 1.0822 seconds
New search index finished in 0.0019 seconds
Old search index subdir finished in 0.6010 seconds
New search index subdir finished in 0.0024 seconds
╒════════════════════════════╤══════════════════════╤═══════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════╕
│ Category                   │ Traditional Index    │ Lic-T                 │ Description                                                                              │
╞════════════════════════════╪══════════════════════╪═══════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════╡
│ Index Build                │ 286.8267 seconds     │ 2672.1059 seconds     │ The time it takes to build the initial index                                             │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild Delete       │ 288.2643 seconds     │ 9.7177 seconds        │ The time it takes to rebuild the index after a file has been deleted                     │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild Modification │ 291.8812 seconds     │ 9.1267 seconds        │ The time it takes to rebuild the index after a file has been modified                    │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Index Rebuild New          │ 291.4151 seconds     │ 12.5753 seconds       │ The time it takes to rebuild the index after a new file has been added                   │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage Initially          │ 370727926.0000 bytes │ 370727926.0000 bytes  │ The amount of storage used initially by the directory being indexed (should be the same) │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage After Build        │ 370727961.0000 bytes │ 3521055012.0000 bytes │ The amount of storage used by the directory being indexed after indexed                  │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Storage Increase           │ 1.0000x              │ 9.4977x               │ The multiple of the initial storage to the new storage usage                             │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Full Search                │ 1.0822 seconds       │ 0.0019 seconds        │ The amount of time it takes to search the whole index                                    │
├────────────────────────────┼──────────────────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ Subdir Search              │ 0.6010 seconds       │ 0.0024 seconds        │ The amount of time it takes to search only a certain sub folder                          │
╘════════════════════════════╧══════════════════════╧═══════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════╛
