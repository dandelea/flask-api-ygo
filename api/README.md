## API Module

### GET /card
Query a card defined by *codepass*.
Params:
| Name | Mandatory | Description |
| --- | --- | --- |
| `codepass` | :heavy_check_mark: | Codepass unique identifier |

Response:
```json
{
    {
        "type": "spell"|"trap"|"monster",
        "illegal": true|false,
        "image": <string>,
        "name": <string>,
        "codepass": <integer>,
        "has_name_condition": true|false,
        "thumbnail": <string>,
        "text": <string>,
        "id": <integer>,

        "spell_family": "continuous"|"quick-play"|"normal"|"equip"|"field"|"ritual", // optional

        "trap_family": "continuous"|"counter"|"normal",  //optional

        "attack" : <string>,    //optional
        "defense" : <string>,   //optional
        "stars" : <integer [1-12]>, //optional
        "attribute" : "dark"|"divine"|"earth"|"fire"|"light"|"water"|"wind",    //optional
        "species" : "aqua"|"beast"|"beast-warrior"|"creator god"|"cyberse"|"dinosaur"|"divine-beast"|"dragon"|"fairy"|"fiend"|"fish"|"insect"|"machine"|"plant"|"psychic"|"pyro"|"reptile"|"rock"|"sea serpent"|"spellcaster"|"thunder"|"warrior"|"winged beast"|"wyrm"|"zombie",   //optional
    }
}
```

Example request:
```/api/card?codepass=34541863```
Example response:
```json
{
    "type": "spell",
    "illegal": false,
    "image": "https://ygohub.com/card_images/126bc4b1-fe1f-4842-bd49-f06537c7ecbe.jpg",
    "name": "\"A\" Cell Breeding Device",
    "spell_family": "continuous",
    "codepass": 34541863,
    "has_name_condition": false,
    "thumbnail": "https://ygohub.com/card_images/126bc4b1-fe1f-4842-bd49-f06537c7ecbe_thumbnail.jpg",
    "text": "During each of your Standby Phases, put 1 A-Counter on 1 face-up monster your opponent controls.",
    "id": 1
}
```

### POST /cards

Perform a search query of the cards table. Perform an AND filter with possible values in body data. Order by `order` `inverse` field.

Params:
| Name | Mandatory | Description |
| --- | --- | --- |
| `attributes` | :heavy_multiplication_x: | List of possible `attribute` value of the `Card` objects |
| `species` | :heavy_multiplication_x: | List of possible `species` value of the `Card` objects |
| `stars` | :heavy_multiplication_x: | List of possible `stars` value of the `Card` objects |
| `monster_types` | :heavy_multiplication_x: | List of possible `monster_type` value of the `Card` objects |
| `spell_families` | :heavy_multiplication_x: | List of possible `spell_family` value of the `Card` objects |
| `trap_families` | :heavy_multiplication_x: | List of possible `trap_family` value of the `Card` objects |
| `archetypes`  | :heavy_multiplication_x: | List of possible `archetype` values associated to the `Card` objects |
| `order`  | :heavy_multiplication_x: | References the field of the `Card` object to be ordered by |
| `inverse` | :heavy_multiplication_x: | Toggle inverse order of the result |

Response:
```json
[
    {
        "type": "spell"|"trap"|"monster",
        "illegal": true|false,
        "image": <string>,
        "name": <string>,
        "codepass": <integer>,
        "has_name_condition": true|false,
        "thumbnail": <string>,
        "text": <string>,
        "id": <integer>,

        "spell_family": "continuous"|"quick-play"|"normal"|"equip"|"field"|"ritual", // optional

        "trap_family": "continuous"|"counter"|"normal",  //optional

        "attack" : <string>,    //optional
        "defense" : <string>,   //optional
        "stars" : <integer [1-12]>, //optional
        "attribute" : "dark"|"divine"|"earth"|"fire"|"light"|"water"|"wind",    //optional
        "species" : "aqua"|"beast"|"beast-warrior"|"creator god"|"cyberse"|"dinosaur"|"divine-beast"|"dragon"|"fairy"|"fiend"|"fish"|"insect"|"machine"|"plant"|"psychic"|"pyro"|"reptile"|"rock"|"sea serpent"|"spellcaster"|"thunder"|"warrior"|"winged beast"|"wyrm"|"zombie",   //optional
    },
    ...
]
```

Example request:
```/api/cards```
```json
{
	"attributes": [],
	"species": ["reptile"],
	"stars": [1],
	"monster_types": [],
	"spell_families": [],
	"trap_families": [],
	"archetypes": ["Worm"],
	"order": "name",
	"inverse" : false
}
```
Example response:
```json
[
    {
        "type": "monster",
        "illegal": false,
        "image": "https://ygohub.com/card_images/6a16bf54-9a87-401c-83b4-f02ffc197999.jpg",
        "name": "Worm Apocalypse",
        "codepass": 88650530,
        "stars": 1,
        "attack": "300",
        "species": "reptile",
        "has_name_condition": false,
        "thumbnail": "https://ygohub.com/card_images/6a16bf54-9a87-401c-83b4-f02ffc197999_thumbnail.jpg",
        "text": "FLIP: Target 1 Spell/Trap Card on the field; destroy that target.",
        "id": 8661,
        "attribute": "light",
        "defense": "200"
    },
    {
        "type": "monster",
        "illegal": false,
        "image": "https://ygohub.com/card_images/fd1cdfa9-dbca-4d49-853d-7f2cf4950512.jpg",
        "name": "Worm Hope",
        "codepass": 11159464,
        "stars": 1,
        "attack": "800",
        "species": "reptile",
        "has_name_condition": false,
        "thumbnail": "https://ygohub.com/card_images/fd1cdfa9-dbca-4d49-853d-7f2cf4950512_thumbnail.jpg",
        "text": "FLIP: When this card is flipped face-up by an opponent's monster's attack, draw 1 card.When this card is sent from the field to the Graveyard, send 1 card from your hand to the Graveyard.",
        "id": 8671,
        "attribute": "light",
        "defense": "1500"
    },
    {
        "type": "monster",
        "illegal": false,
        "image": "https://ygohub.com/card_images/20b40364-67ce-4880-94c3-fecda7d7f897.jpg",
        "name": "Worm Ugly",
        "codepass": 76683171,
        "stars": 1,
        "attack": "100",
        "species": "reptile",
        "has_name_condition": false,
        "thumbnail": "https://ygohub.com/card_images/20b40364-67ce-4880-94c3-fecda7d7f897_thumbnail.jpg",
        "text": "When you Tribute Summon a Reptile-Type \"Worm\" monster by Tributing this card, you can Special Summon this card from your Graveyard to your opponent's side of the field, in face-up Attack Position.",
        "id": 8684,
        "attribute": "light",
        "defense": "100"
    }
]
```

### GET /values

Query a list of all possible values of a `field` in a `table`.

Params: 
| Name | Mandatory | Description |
| --- | --- | --- |
| `field` | :heavy_check_mark: | Column name parameter |
| `table` | :heavy_check_mark: | Table name parameter |

Response:
```json
[ <object>, ... ]
```

Example request:
```/api/values?table=cards&field=stars```
Example response:
```json
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, null]
```