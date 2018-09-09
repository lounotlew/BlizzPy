# WoWCharacter - Documentations
> Written by Lewis Kim

### Usage

``WoWCharacter`` is a wrapper for player character data in the WoW Community API.

To initialize an instance of ``WoWCharacter``:

```python
from blizzpy.wow import WoWCharacter

MyCharacter = WoWCharacter(api_key, characterName, realm, locale="en_US", token=None)
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Realms are not case sensitive.

Example:

For a character named "Xfitvegan" in the realm "Proudmoore" of "en_US",

```python
MyCharacter = WoWCharacter(api_key="SOME_API_KEY", characterName="Xfitvegan", realm="proudmoore")
```

Or, for a character named "Shinela" in the realm "Argent Dawn" of "eu_GB",

```python
MyCharacter = WoWCharacter(api_key="SOME_API_KEY", characterName="Shinela", realm="argent-dawn", locale="eu_GB")
```

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving basic character data:_

**1) Raw API character data.**

```python
MyCharacter.get_character_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Selected character's class.**

```python
MyCharacter.get_class()
```

``PARAMS``: None

Returns a ``str`` of the character's class.

Classes: Warrior, Paladin, Hunter, Rogue, Priest, Death Knight, Shaman, Mage, Warlock, Monk, Druid, Demon Hunter.

**3) Selected character's race.**

```python
MyCharacter.get_race()
```

``PARAMS``: None

Returns a ``str`` of the character's race.

Races: Human, Orc, Dwarf, Night Elf, Forsaken/Undead, Tauren, Gnome, Troll, Goblin, Blood Elf, Draenei, Worgen, Pandaren, Nightborne, Highmountain Tauren, Void Elf, Lightforged Draenei, Dark Iron Dwarf, Mag'har Orc.

**4) Selected character's gender.**

```python
MyCharacter.get_gender()
```

``PARAMS``: None

Returns a ``str`` of the character's gender.

Genders: Male, Female.

**5) Selected character's level.**

```python
MyCharacter.get_level()
```

``PARAMS``: None

Returns an ``int`` of the character's current level.

Levels: Integers between 1 and 120.

**6) Selected character's achievement points.**

```python
MyCharacter.get_achievement_points()
```

``PARAMS``: None

Returns an ``int`` of the character's total achievement points.

Achievement Points: Any integer greater than or equal to 0.

**7) Selected character's faction.**

```python
MyCharacter.get_faction()
```

``PARAMS``: None

Returns a ``str`` of the character's faction.

Factions: Alliance, Horde.

#### _Retrieving the character's achievements data:_

**1) Raw API character achievements data.**

```python
MyCharacter.get_achievements_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'achievements'.

See https://dev.battle.net/io-docs for details.

**2) Achievements data as pandas dataframe.**

```python
MyCharacter.get_achievements_df(ascending_time=False)
```

``PARAMS``:
- ``ascending_time``: ``boolean``. Sort the dataframe in ascending time if ``True.``

Returns a ``pandas`` dataframe with 2 columns: ID's of completed achievements, ``achievementsCompleted``, and the timestamps of their completions, ``achievementsCompletedTimestamp``.

**3) Whether or not the character has an achievement completed.**

```python
MyCharacter.has_achievement(achievement_id)
```

``PARAMS``:
- ``achievement_id``: ``int``. ID of the achievement to search.

Returns a ``boolean``. ``True`` if the character has completed the achievement; ``False`` otherwise.

#### _Retrieving the character's appearance data:_

**1) Raw API character appearance data.**

```python
MyCharacter.get_appearance_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'appearance'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's facial features.**

```python
MyCharacter.get_facial_features()
```

``PARAMS``: None

Returns an ``int`` code of the selected character's facial features.

**3) Selected character's skin color.**

```python
MyCharacter.get_skincolor()
```

``PARAMS``: None

Returns an ``int`` code of the selected character's skin color.

**4) Selected character's hairstyle.**

```python
MyCharacter.get_hairstyle()
```

``PARAMS``: None

Returns an ``int`` code of the selected character's hairstyle.

**5) Selected character's hair color.**

```python
MyCharacter.get_hair_color()
```

``PARAMS``: None

Returns an ``int`` code of the selected character's hair color.

#### _Retrieving the character's activity feed data:_

**1) Raw API character feed data.**

```python
MyCharacter.get_feed_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'feed'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving the character's guild data:_

**1) Raw API character guild data.**

```python
MyCharacter.get_guild_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'guild'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's guild's name.**

```python
MyCharacter.get_guild_name()
```

``PARAMS``: None

Returns a ``str`` the selected character's guild's name.

**3) Number of members in the selected character's guild.**

```python
MyCharacter.get_num_guild_members()
```

``PARAMS``: None

Returns an ``int`` of the number of members in the selected character's guild.

**4) Selected character's guild's achievement points.**

```python
MyCharacter.get_guild_achievement_points()
```

``PARAMS``: None

Returns an ``int`` of the selected character's guild's total achievement points.

#### _Retrieving the character's hunter pets data (if the character is a hunter):_

**1) Raw API character hunter pet data.**

```python
MyCharacter.get_hunter_pet_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'hunterPets'.

See https://dev.battle.net/io-docs for details.

**2) Selected hunter character's pet names.**

```python
MyCharacter.get_hunter_pet_names()
```

``PARAMS``: None

Returns a list of ``str`` of the selected character's hunter pet names.

**3) Selected hunter character's pet's information.**

```python
MyCharacter.get_hunter_pet_info(pet_name)
```

``PARAMS``: None

Returns a dictionary containing information about the selected character's pet with the name ``pet_name``.

Keys:
- ``name``: Pet's name
- ``creature``: Pet's creature ID
- ``slot``: Pet's slot number
- ``spec``: Pet's specialization. A dictionary.
- ``calcSpec``:
- ``familyId``: Pet's family ID
- ``familyName``: Pet's family name

#### _Retrieving the character's equiped items data:_

**1) Raw API character items data.**

```python
MyCharacter.get_items_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'items'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's item level.**

```python
MyCharacter.get_ilvl()
```

``PARAMS``: None

Returns a ``tuple``. The first element is an ``int`` of the selected character's total item level, and the second element is an ``int`` of the selected character's equipped item level.

**3) Selected character's item in a specific slot.**

```python
MyCharacter.get_gear_piece(slot_name)
```

``PARAMS``:
- ``slot_name``: ``str`` name of the gear slot to search.

Accepted slot names: 'head', 'neck', 'shoulder', 'back', 'chest', 'shirt', 'tabard', 'wrist', 'hands', 'waist', 'legs', 'feet', 'finger1', 'finger2', 'trinket1', 'trinket2', 'mainHand'

Returns a dictionary containing information about the gear in ``slot_name``.

Keys in returned dictionary:
- ``id``:
- ``name``:
- ``icon``:
- ``quality``:
- ``itemLevel``:
- ``tooltipParams``:
- ``stats``:
- ``armor``:
- ``context``:
- ``bonusLists``:
- ``artifactId``:
- ``displayInfoId``:
- ``artifactAppearanceId``:
- ``artifactTraits``:
- ``relics``:
- ``appearance``:
- ``azeriteItem``:
- ``azeriteEmpoweredItem``:

#### _Retrieving the character's mounts data:_

**1) Raw API character mounts data.**

```python
MyCharacter.get_mounts_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'mounts'.

See https://dev.battle.net/io-docs for details.

**2) Search for a mount owned by the selected character.**

```python
MyCharacter.search_mount(mount_name)
```

``PARAMS``:
- ``mount_name``: ``str`` name of the mount to search. Case sensitive.

Returns a dictionary containing information about the selected mount.

Keys in returned dictionary:
- ``name``:
- ``spellId``:
- ``creatureId``:
- ``itemId``:
- ``qualityId``:
- ``icon``:
- ``isGround``:
- ``isFlying``:
- ``isAquatic``:
- ``isJumping``:

**3) Selected character's mounts' names.**

```python
MyCharacter.get_mount_names()
```

``PARAMS``: None

Returns a list of ``str`` of the character's mounts' names.

**4) Selected character's ground mounts.**

```python
MyCharacter.get_ground_mounts()
```

``PARAMS``: None

Returns a list of ``str`` of the character's ground mounts' names. Can intersect with flying mounts.

**5) Selected character's flying mounts.**

```python
MyCharacter.get_flying_mounts()
```

``PARAMS``: None

Returns a list of ``str`` of the character's flying mounts' names. Can intersect with ground mounts.


#### _Retrieving the character's non-hunter pets data:_

**1) Raw API character non-hunter pets data.**

```python
MyCharacter.get_pets_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'pets'.

See https://dev.battle.net/io-docs for details.

**2) Number of non-hunter pets the selected character owns.**

```python
MyCharacter.get_num_pets()
```

``PARAMS``: None

Returns an ``int`` of the number of non-hunter pets the selected character owns.

**3) Percentage of all pets the selected character owns.**

```python
MyCharacter.get_percent_collected()
```

``PARAMS``: None

Returns an ``int`` of the percentage (e.g. 53 for 53%) of pets owned.

**4) Selected character's non-hunter pets' names.**

```python
MyCharacter.get_pet_names()
```

``PARAMS``: None

Returns a list of ``str`` of the non-hunter pet names.

**5) Selected character's non-hunter pets' IDs.**

```python
MyCharacter.get_pet_ids()
```

``PARAMS``: None

Returns a list of ``int`` of the non-hunter pet IDs.

**6) Selected character's favorite pets.**

```python
MyCharacter.get_favorite_pets(as_names=False)
```

``PARAMS``:
- ``as_names``: ``boolean``. Return the favorite pets as a list of ``str`` of the pets' names if ``True.`` Else, return them as dictionaries containing pet information.

Returns the favorite lists as a list of ``str`` of the pets' names if ``as_names=True.`` Else, return them as dictionaries containing pet information.

Keys in returned dictionary:
- ``name``:
- ``spellId``:
- ``creatureId``:
- ``itemId``:
- ``qualityId``:
- ``icon``:
- ``stats``:
- ``battlePetGuid``:
- ``isFavorite``:
- ``isFirstAbilitySlotSelected``:
- ``isSecondAbilitySlotSelected``:
- ``isThirdAbilitySlotSelected``:
- ``creatureName``:
- ``canBattle``:

**7) Selected character's pet's quality.**

```python
MyCharacter.get_pet_quality(pet_name)
```

``PARAMS``:
- ``pet_name``: ``str`` name of the pet to be searched.

Returns an ``int`` of the pet's quality (``qualityId``).

**8) Selected character's pet's stats.**

```python
MyCharacter.get_pet_stats(pet_name)
```

``PARAMS``:
- ``pet_name``: ``str`` name of the pet to be searched.

Returns a dictionary containing information about the pet's stats.

Keys in returned dictionary:
- ``speciesId``
- ``breedId``
- ``petQualityId``
- ``level``
- ``health``
- ``power``
- ``speed``

#### _Retrieving the character's professions data:_

**1) Raw API character professions data.**

```python
MyCharacter.get_professions_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'professions'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's primary professions.**

```python
MyCharacter.get_primary_professions()
```

``PARAMS``: None

Returns a dictionary whose keys are the character's primary profession names, and values are the ranks associated with that profession.

**3) Selected character's secondary professions.**

```python
MyCharacter.get_secondary_professions()
```

``PARAMS``: None

Returns a dictionary whose keys are the character's secondary profession names, and values are the ranks associated with that profession.

#### _Retrieving the character's raid progression data:_

**1) Raw API character raid progression data.**

```python
MyCharacter.get_raid_prog_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'progression'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's raid progression for a specific raid.**

```python
MyCharacter.get_raid_prog(raid_name)
```

``PARAMS``:
- ``raid_name``: ``str`` of the name of the raid to be searched. Not case sensitive.

Returns a dictionary that contains progression information about the selected raid.

Keys in returned dictionary:
- ``name``:
- ``lfr``:
- ``normal``:
- ``heroic``:
- ``mythic``:
- ``id``:
- ``bosses``: A list containing information about each boss. Each boss is a dictionary; keys: ``id``, ``name``, ``lfrKills``, ``lfrTimestamp``, ``normalKills``, ``normalTimestamp``, ``heroicKills``, ``heroicTimestamp``, ``mythicKills``, ``mythicTimestamp``

**3) Selected character's number of boss kills in a specific raid on a specific difficulty.**

```python
MyCharacter.get_num_boss_kills(boss_name, raid_name, difficulty)
```

``PARAMS``:
- ``boss_name``: ``str`` of the name of the boss of the raid. Not case sensitive.
- ``raid_name``: ``str`` of the name of the raid to be searched. Not case sensitive.
- ``difficulty``: ``str`` of the name of the difficulty of the raid. Not case sensitive.

Returns an ``int`` of the number of boss kills in that raid on that difficulty.

**4) Selected character's first boss kill timestamp in a specific raid on a specific difficulty.**

```python
MyCharacter.get_boss_kill_time(boss_name, raid_name, difficulty)
```

``PARAMS``:
- ``boss_name``: ``str`` of the name of the boss of the raid. Not case sensitive.
- ``raid_name``: ``str`` of the name of the raid to be searched. Not case sensitive.
- ``difficulty``: ``str`` of the name of the difficulty of the raid. Not case sensitive.

Returns an ``int`` of the timetamp of the first selected boss kill in that raid on that difficulty.

#### _Retrieving the character's PVP statistics:_

**1) Raw API character PVP data.**

```python
MyCharacter.get_pvp_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'pvp'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's battlegroup.**

```python
MyCharacter.get_battlegroup()
```

``PARAMS``: None

Returns a ``str`` of the character's battlegroup.

**3) Selected character's number of honorable kills.**

```python
MyCharacter.get_totalHK()
```

``PARAMS``: None

Returns an ``int`` of the character's total number of honorable kills.

**4) Selected character's rated 2v2 arena statistics.**

```python
MyCharacter.get_2v2_stats()
```

``PARAMS``: None

Returns a dictionary containing the player's 2v2 arena statistics.

Keys in returned dictionary:
- ``slug``:
- ``rating``:
- ``weeklyPlayed``:
- ``weeklyWon``:
- ``weeklyLost``:
- ``seasonPlayed``:
- ``seasonWon``:
- ``seasonLost``:

**5) Selected character's rated 2v2 arena winrate.**

```python
MyCharacter.get_2v2_winrate()
```

``PARAMS``: None

Returns a ``float`` of the character's winrate percentage (e.g. 53.1 for 53.1%).

**6) Selected character's 3v3 and RBG info.**

Simply replace "2v2" with "3v3" or "rbg" in the methods above.

Examples:

```python
MyCharacter.get_3v3_winrate()
MyCharacter.get_rbg_stats()
```

#### _Retrieving the character's reputations data:_

**1) Raw API character reputation data.**

```python
MyCharacter.get_reputation_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'reputation'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's reputation factions.**

```python
MyCharacter.get_reputation_factions()
```

``PARAMS``: None

Returns a list of ``str`` of all faction names the selected character has reputation with.

**3) Selected character's reputation amount for a specific faction.**

```python
MyCharacter.get_reputation_amount(faction_name)
```

``PARAMS``:
- ``faction_name``: ``str`` name of the faction to be searched. Not case sensitive.

Returns an ``int`` of the character's reputation amount with the selected faction.

**4) Selected character's reputation level for a specific faction.**

```python
MyCharacter.get_reputation_amount(faction_name)
```

``PARAMS``:
- ``faction_name``: ``str`` name of the faction to be searched. Not case sensitive.

Returns a ``str`` of the character's reputation level with the selected faction.

Reputation levels: "Exalted", "Revered", "Honored", "Friendly", "Neutral", "Unfriendly", "Hostile", "Hated"

**5) Selected character's REP_LEVEL factions.**

```python
MyCharacter.get_REP_LEVEL_factions()
```

Simply replace "REP_LEVEL" with "exalted", "revered", "honored", "friendly", "neutral", "unfriendly", "hostile", or "hated".

Example:

```python
MyCharacter.get_exalted_factions()
```

``PARAMS``: None

Returns a list of ``str`` of the faction names with REP_LEVEL.

#### _Retrieving the character's quests data:_

**1) Raw API character quests data.**

```python
MyCharacter.get_quests_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'quests'.

See https://dev.battle.net/io-docs for details.

**2) Whether or not the selected character has completed a quest.**

```python
MyCharacter.has_completed_quest(quest_id)
```

``PARAMS``:
- ``quest_id``: ``int`` ID of the quest to be searched.

Returns a ``boolean``. ``True`` if the character completed that quest; ``False`` otherwise.

#### _Retrieving the character's gameplay statistics (most used X, least used Y, etc.):_

**1) Raw API character gameplay statistics data.**

```python
MyCharacter.get_statistics_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'statistics'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving the character's in-game stats data (Str, Int, Agi, etc.):_

**1) Raw API character stats data.**

```python
MyCharacter.get_stats_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'stats'.

See https://dev.battle.net/io-docs for details.

#### _Retrieving the character's talents data_:

**1) Raw API character talents data.**

```python
MyCharacter.get_talents_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'talents'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's chosen talents by spec.**

```python
MyCharacter.get_talents_by_spec(spec)
```

``PARAMS``:
- ``spec``: ``str`` name of the character's spec. The spec must be valid for the character's class.

Returns a dictionary whose keys are talent tiers (``int`` between 1-7), and values are the ``str`` name of the talent selected at that tier.

#### _Retrieving the character's titles data:_

**1) Raw API character titles data.**

```python
MyCharacter.get_titles_data()
```

``PARAMS``: None

Returns a Python dictionary. Contains unchanged raw Blizzard API data read from the json file, with endpoint 'titles'.

See https://dev.battle.net/io-docs for details.

**2) Selected character's title names.**

```python
MyCharacter.get_title_names()
```

``PARAMS``: None

Returns a list of ``str`` of title names the selected character owns.

**3) Number of titles the selected character owns.**

```python
MyCharacter.get_num_titles()
```

``PARAMS``: None

Returns an ``int`` of the number of titles the character owns.

