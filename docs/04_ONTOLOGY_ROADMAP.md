# Ontology Roadmap

Counts are FACT, computed from the inherited entity list (`01_NER_MASTER_LIST.csv`, 992 rows). Type definitions are UNVERIFIED drafts until Ontology V0.1 sign-off (P1).

## Entity types in the inherited list

| Type | Count | Subtypes | Examples |
|---|---|---|---|
| MIL_ORG | 111 | AGENCY, ALLIANCE, COMMAND, SERVICE, THEATRE | Indian Army, Indian Navy, Indian Air Force |
| WEAPON | 109 | ARTILLERY, ATGM, BOMB_PGM, MANPADS, MISSILE_AAM, MISSILE_AGM, MISSILE_BALLISTIC, MISSILE_CRUISE, NUCLEAR_WEAPON, SAM, SMALL_ARM, TORPEDO | Agni-I, Agni-II, Agni-III |
| GOV_ORG | 78 | INTEL_AGENCY, INTL_ORG, LEGISLATURE, MINISTRY, PARAMILITARY | Ministry of Defence (India), Ministry of External Affairs (India), Ministry of Home Affairs (India) |
| DEF_INDUSTRY | 73 | MANUFACTURER, RESEARCH_LAB, SHIPYARD | Hindustan Aeronautics Limited, Bharat Electronics Limited, Bharat Dynamics Limited |
| PLATFORM_AIR | 56 | AEW, BOMBER, FIGHTER, HELO, MPA, TRANSPORT, UAV | Tejas Mk1A, Tejas Mk2, Su-30MKI |
| PLATFORM_SEA | 51 | CLASS, SUBMARINE, VESSEL | INS Vikrant, INS Vikramaditya, INS Arihant |
| MIL_UNIT | 48 | CORPS, DIVISION, FLEET, REGIMENT, SQUADRON | 14 Corps, 15 Corps, 16 Corps |
| NSAG | 48 | INSURGENT, MILITIA, PMC, TERRORIST_DESIGNATED | Lashkar-e-Taiba, The Resistance Front, Jamaat-ud-Dawa |
| TREATY_DOCTRINE | 43 | AGREEMENT, DOCTRINE, TREATY | Simla Agreement, Indus Waters Treaty, Tashkent Declaration |
| CONFLICT_EVENT | 42 | BATTLE, CLASH, CRISIS, INSURGENCY, STANDOFF, STRIKE, TERROR_ATTACK, WAR | Kargil War, Indo-Pakistani War of 1947, Indo-Pakistani War of 1965 |
| PERSON | 42 | (none) | Manoj Pande, Upendra Dwivedi, Dinesh K. Tripathi |
| RANK_ROLE | 39 | APPOINTMENT, RANK | Field Marshal, General, Lieutenant General |
| EXERCISE | 38 | (none) | Malabar, Yudh Abhyas, Garuda Shakti |
| OPERATION | 33 | (none) | Operation Vijay, Operation Sindoor, Operation Bunyan-um-Marsoos |
| CYBER_ACTOR | 33 | APT, MALWARE_FAMILY | APT36, SideWinder, Patchwork |
| MIL_FACILITY | 28 | AIRBASE, MISSILE_RANGE, NAVAL_BASE, NUCLEAR_FACILITY | Ambala Air Force Station, Hasimara Air Force Station, Pathankot Air Force Station |
| PROGRAMME | 20 | (none) | Project-75I, Project-75 Alpha, Project Kusha |
| SENSOR_C4ISR | 19 | DATALINK, EW, RADAR, SATELLITE | Swordfish LRTR, RISAT-2B, RISAT-2BR1 |
| PLATFORM_LAND | 18 | IFV, MBT | Arjun Mk1A, T-90 Bhishma, T-72 Ajeya |
| LOC | 16 | BORDER_LINE, MOUNTAIN_PASS, REGION, SEA_STRAIT | Galwan Valley, Siachen Glacier, Line of Actual Control |
| MIL_DESIGNATOR | 15 | ALPHANUM_CODE, HULL_PENNANT, NATO_REPORTING_NAME | Flanker, Fulcrum, Fishbed |
| GPE | 8 | CITY, REGION, STATE_PROVINCE | Ladakh, Jammu and Kashmir, Aksai Chin |
| LAW_POLICY | 8 | (none) | Armed Forces (Special Powers) Act, Unlawful Activities (Prevention) Act, Official Secrets Act |
| MIL_AWARD | 7 | (none) | Param Vir Chakra, Maha Vir Chakra, Vir Chakra |
| MIL_EDU | 5 | (none) | National Defence Academy, Indian Military Academy, Pakistan Military Academy |
| MIL_DOC | 4 | (none) | Military Balance, Joint Doctrine Indian Armed Forces, China's National Defense in the New Era |
| **Total** | **992** | | |

## Ambiguity and open-decision cases

63 inherited rows carry an ambiguity or open-decision note (FACT). The full list of ambiguous abbreviations is in `reports/P0-03_INHERITED_ASSETS.md`. Samples:

- Indian Army (MIL_ORG): Abbrev IA is ambiguous (Indian Airlines; Iowa)
- Indian Navy (MIL_ORG): Abbrev IN collides with country code and common word
- Indian Air Force (MIL_ORG): IAF also = Israeli Air Force (see 02 ambiguity list) - resolve by country context
- Indian Coast Guard (MIL_ORG): Could also be GOV_ORG PARAMILITARY - ontology decision needed
- Western Command (Indian Army) (MIL_ORG): Same surface form as Indian Air Force Western Air Command - disambiguate by service
- Defence Intelligence Agency (India) (MIL_ORG): Abbrev DIA collides with US Defense Intelligence Agency
- Territorial Army (India) (MIL_ORG): TA abbreviation highly ambiguous
- People's Liberation Army (MIL_ORG): PLA also = People's Liberation Army (Manipur) NSAG - disambiguate
- Central Military Commission (MIL_ORG): CMC abbreviation ambiguous (Christian Medical College etc.)
- United States Army (MIL_ORG): USA abbreviation collides with country
- United States Northern Command (MIL_ORG): See Northern Command (Indian Army) - ambiguity per 02
- Israel Defense Forces (MIL_ORG): IDF abbreviation unambiguous in defence context

### Cases to resolve in P1-05

- Same acronym, several entities ("IA": Indian Army vs Indian Airlines vs Iowa; "IAF": Indian vs Israeli Air Force): resolve with country context.
- Same name, several countries ("Northern Command", "Ministry of Defence"): keep country in the entity record.
- Metonymy ("New Delhi said", "the Navy announced"): rule needed.
- Organisation vs programme vs platform vs weapon (e.g. LCA programme vs Tejas Mk1A): rule needed.

## Boundary cases

- **Coast Guard**: the inherited note says "Could also be GOV_ORG PARAMILITARY - ontology decision needed". Current rows: Indian Coast Guard -> MIL_ORG/SERVICE; China Coast Guard -> MIL_ORG/AGENCY; United States Coast Guard -> MIL_ORG/SERVICE. RECOMMENDATION: decide once in P1 and apply to every country.
- **Operation vs exercise**: a named combat operation is OPERATION, a training exercise is EXERCISE (both exist: 33 and 38 rows). RECOMMENDATION.
- **Variants** (Su-27 vs Su-30, Arjun Mk1 vs Mk2): RECOMMENDATION: separate entity when the inventory has separate rows, else a version attribute. Decide in P1-05.
- **Person vs role**: named individuals are PERSON, titles are RANK_ROLE (both types exist).
- **Sensitive detail**: CLAUDE.md rule 9 applies: public detail is annotated.

## Freeze

RECOMMENDATION: Ontology V0.1 is frozen at P1-08 (git tag `ontology-v0.1`). After that, no new types without a new version.

## Next steps

- P1: formalise into `configs/ontology.yaml` and guidelines.
- P2: gazetteers and synthetic data.
- P6: full annotation guidelines.
