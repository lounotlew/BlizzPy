# SC2Profile - Documentations
> Written by Lewis Kim

### Usage

``SC2Profile`` is a wrapper for player profile data in the SC2 Community API.

To initialize an instance of ``SC2Profile``:

```python
from blizzpy.sc2 import SC2Profile

MyProfile = SC2Profile(api_key, profile_id, profile_name, region_id=1, locale="en_US", token=None):
```

Supported locales: "en_US", "eu_GB", "ko_KR".

Example:

For a player named "Hazzah" in "en_US",

```python
MyCharacter = SC2Profile(api_key="SOME_API_KEY", realm="proudmoore")
```

Or, for a player named "Hoozah" in "eu_GB",

```python
MyCharacter = SC2Profile(api_key="SOME_API_KEY", realm="Tarren-Mill", locale="eu_GB")
```

To get a profile's ``profile_id`` and ``region_id``, search the player's name and look at the URLs to find them (``region_id`` is a single digit, while ``profile_id`` is 5-6 digits).

There is currently no native way in the Blizzard API to obtain these information.

### Methods

_*Any method in the form_ ``get_X_data()`` _returns unchanged raw json data from the Blizzard API in a dictionary._

#### _Retrieving profile data:_

**1) Raw API profile data.**

```python
MyProfile.get_profile_data()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Selected profile's clan name.**

```python
MyProfile.get_clan_name()
```

``PARAMS``: None

Returns the ``str`` name of the clan the selected profile is a part of.

**3) Selected profile's clan tag.**

```python
MyProfile.get_clan_tag()
```

``PARAMS``: None

Returns the ``str`` tag of the clan the selected profile is a part of.

**4) Selected profile's clan name.**

```python
MyProfile.get_clan_name()
```

``PARAMS``: None

Returns the ``str`` name of the clan the selected profile is a part of.

**5) Selected profile's career data.**

```python
MyProfile.get_profile_career()
```

``PARAMS``: None

Returns a dictionary containing information about the selected profile's career/play statistics.

Keys in returned dictionary:
- ``primaryRace``:
- ``terranWins``:
- ``protossWins``:
- ``zergWins``:
- ``highest1v1Rank``:
- ``highestTeamRank``:
- ``seasonTotalGames``:
- ``careerTotalGames``:

**6) Selected profile's primary race.**

```python
MyProfile.get_primary_race()
```

``PARAMS``: None

Returns a ``str`` name of the selected profile's primary SC2 race.
Races: Terran, Protoss, Zerg

**7) Selected profile's # of wins by race.**

```python
MyProfile.get_race_wins()
```

``PARAMS``: None

Returns a dictionary whose keys are the SC2 races and values are the number of wins corresponding to that race.

**8) Selected profile's total # of games this season.**

```python
MyProfile.get_season_total_games()
```

``PARAMS``: None

Returns an ``int`` number of games the selected profile has had so far this season.

**9) Selected profile's total # of games.**

```python
MyProfile.get_career_total_games()
```

``PARAMS``: None

Returns an ``int`` number of games the selected profile has had so far.

**10) Selected profile's winrate this season.**

```python
MyProfile.get_season_winrate()
```

``PARAMS``: None

Returns a ``float`` winrate the selected profile has this season so far.

**11) Selected profile's highest 1v1 rank.**

```python
MyProfile.get_highest_1v1_rank()
```

``PARAMS``: None

Returns the ``int`` highest 1v1 rank the selected profile has held.

**12) Selected profile's highest team rank.**

```python
MyProfile.get_highest_team_rank()
```

``PARAMS``: None

Returns the ``int`` highest team rank the selected profile has held.

**13) Selected profile's rewards.**

```python
MyProfile.get_profile_rewards()
```

``PARAMS``: None

Returns a dictionary that contains information about the selected profile's chosen and earned rewards.

Keys in returned dictionary:
- ``selected``:
- ``earned``:

**14) Whether or not the selected profile has earned a reward.**

```python
MyProfile.has_earned_reward(reward_id)
```

``PARAMS``:
- ``reward_id``: ``int`` ID of the reward to be searched.

Returns a ``boolean``. ``True`` if the selected profile has earned the reward with ``reward_id``; ``False`` otherwise.

**15) Selected profile's achievements.**

```python
MyProfile.get_profile_achievements()
```

``PARAMS``: None

Returns a dictionary containing information about the profile's achievements.

Keys in returned dictionary:
- ``points``: A dictionary with two keys: ``totalPoints`` and ``categoryPoints``. ``totalPoints`` points to an ``int`` total achievement points, and ``categoryPoints`` points to a dictionary that breaks down ``totalPoints`` into points by category (categories: ``'4330138'``, ``'4386911'``, ``'4364473'``, ``'4325379'``, ``'4325410'``, ``'4325377'``).
- ``achievements``: A list of dictionaries about all achievements the profile has earned. Each dictionary contains 2 keys: ``achievementId`` and ``completionDate``.

**16) Whether or not the selected profile has earned an achievement.**

``python
MyProfile.has_earned_achievement(achievement_id)
``

``PARAMS``:
- ``achievement_id``: ``int`` ID of the achievement to be searched.

Returns a ``boolean``. ``True`` if the profile has earned the achievement; ``False`` otherwise.

#### _Retrieving profile ladder data:_

**1) Raw API profile ladder data.**

```python
MyProfile.get_profile_ladder_data()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Selected profile's ladder in the current season.**

``python
MyProfile.get_current_ladder()
``

``PARAMS``: None

Returns a dictionary that contains information about the profile's current ladder. Returns ``None`` if the profile has not been active in the current season.

Keys in returned dictionary:
- ``ladderName``:
- ``ladderId``:
- ``division``:
- ``rank``:
- ``league``:
- ``matchMakingQueue``:
- ``wins``:
- ``losses``:
- ``showcase``:

**3) Selected profile's current-season ladder name.**

``python
MyProfile.get_current_ladder_name()
``

``PARAMS``: None

Returns the ``str`` name of the profile's current ladder. Returns ``None`` if the profile has not been active in the current season.

**4) Selected profile's current-season league.**

``python
MyProfile.get_current_league()
``

``PARAMS``: None

Returns the ``str`` name of the profile's current league.Returns ``None`` if the profile has not been active in the current season.

#### _Retrieving match history data:_

**1) Raw API profile match history data.**

```python
MyProfile.get_match_history_data()
```

``PARAMS``: None

Returns a dictionary. Contains unchanged raw Blizzard API data read from the json file.

See https://dev.battle.net/io-docs for details.

**2) Selected profile's number of games played.**

``python
MyProfile.num_games_played()
``

``PARAMS``: None

Returns the ``int`` number of games the profile has played in the current season, both ranked and unranked.

**3) Selected profile's total winrate.**

``python
MyProfile.total_winrate()
``

``PARAMS``: None

Returns the ``float`` winrate of games the profile has played in the current season, both ranked and unranked.

**4) Selected profile's current season solo ranked winrate.**

``python
MyProfile.solo_winrate()
``

``PARAMS``: None

Returns the ``float`` winrate of solo ranked games the profile has played in the current season.

**5) Selected profile's solo ranked games.**

``python
MyProfile.get_solo_games()
``

``PARAMS``: None

Returns a list of dictionaries that contain information about all of the solo ranked games the profile has played.

Keys in returned dictionaries:
- ``map``: ``str`` name of the map the game was played on.
- ``type``: ``str`` name of the game type. They will all be ``'SOLO'``.
- ``decision``: ``str`` name of the decision; ``'WIN'`` or ``'LOSS'``.
- ``speed``: 
- ``date``: ``int`` timestamp of when the game was played.

