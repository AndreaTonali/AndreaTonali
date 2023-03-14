# SUMMARY

Go to the following URL, and download the dataset on sampled Last.fm usage:

- http://ocelma.net/MusicRecommendationDataset/lastfm-1K.html

**Note**: Assuming Linux/MacOS environment, plus Python & Spark.

Please dowonload `userid-timestamp-artid-artname-traid-traname.tsv` from the above `URL` and place it in the `./app_musicrecommendation/dataset/` folder.

Run `./init.sh`. Make sure the file is executable, example below:

```bash
chmod 755 init.sh
```
Assuming the below schema of the dataset with no duplicates entry registred:

```bash
root
 |-- userid: string (nullable = true)
 |-- timestamp: timestamp (nullable = true)
 |-- musicbrainz-artist-id: string (nullable = true)
 |-- artist-name: string (nullable = true)
 |-- musicbrainz-track-id: string (nullable = true)
 |-- track-name: string (nullable = true)
```

The script will print the below output in command line and also respectivelly save the results into a csv within the respctive Solution folder, one for each part (e.g. `./SolutionA`). Results are alreday available in the folders. 

## Part A

The list of user IDs, along with the number of distinct songs each user has played:

```bash
+-----------+-------------+                                                     
|     userid|DistinctSongs|
+-----------+-------------+
|user_000691|        55559|
|user_000861|        44523|
|user_000681|        39810|
|user_000800|        35847|
|user_000427|        32481|
|user_000774|        31852|
|user_000702|        26594|
|user_000345|        24283|
|user_000783|        23336|
|user_000882|        23055|
+-----------+-------------+
only showing top 10 rows
```
The approach taken in the `distinct_songs_per_user` function is to group by `user_id` and count distinct per `track-name`.

## Part B

The list of the 100 most popular songs (artist and title) in the dataset, with the number of times
each was played:

```bash
+--------------------+--------------------+-----+                               
|         artist-name|          track-name|count|
+--------------------+--------------------+-----+
|  The Postal Service|  Such Great Heights| 3992|
|        Boy Division|Love Will Tear Us...| 3663|
|           Radiohead|        Karma Police| 3534|
|                Muse|Supermassive Blac...| 3483|
| Death Cab For Cutie|     Soul Meets Body| 3479|
|           The Knife|          Heartbeats| 3156|
|                Muse|           Starlight| 3060|
|         Arcade Fire|    Rebellion (Lies)| 3048|
|      Britney Spears|          Gimme More| 3004|
|         The Killers| When You Were Young| 2998|
|            Interpol|                Evil| 2989|
|          Kanye West|       Love Lockdown| 2950|
|      Massive Attack|            Teardrop| 2948|
| Death Cab For Cutie|I Will Follow You...| 2947|
|                Muse| Time Is Running Out| 2945|
|          Bloc Party|             Banquet| 2906|
|         Arcade Fire|Neighborhood #1 (...| 2826|
|           Radiohead|          All I Need| 2696|
|  The Postal Service|      Nothing Better| 2670|
|         Snow Patrol|        Chasing Cars| 2667|
|           Radiohead|               Creep| 2651|
|           Radiohead|             15 Step| 2647|
|          Kanye West|           Heartless| 2644|
|           Radiohead|                Nude| 2639|
|      Britney Spears|           Womanizer| 2635|
|      Gnarls Barkley|               Crazy| 2603|
|           Radiohead|            Reckoner| 2588|
|                Mgmt|     Time To Pretend| 2584|
|           Radiohead|    Paranoid Android| 2568|
|            Coldplay|       The Scientist| 2563|
|      Arctic Monkeys|I Bet You Look Go...| 2557|
|               Oasis|          Wonderwall| 2519|
|           Radiohead|  Fake Plastic Trees| 2490|
|        Joy Division|  She'S Lost Control| 2447|
|         Arcade Fire|Neighborhood #3 (...| 2444|
|           Radiohead|Jigsaw Falling In...| 2420|
|            Coldplay|        Viva La Vida| 2387|
|         The Killers|All These Things ...| 2385|
|          Kanye West|Welcome To Heartb...| 2376|
|        Depeche Mode|   Enjoy The Silence| 2369|
|  The Postal Service|The District Slee...| 2365|
|     Franz Ferdinand|         Take Me Out| 2355|
|          Kanye West|Amazing (Feat. Yo...| 2354|
|            Interpol|          Slow Hands| 2344|
|       José González|          Heartbeats| 2333|
|                Mgmt|                Kids| 2333|
|         The Killers|    Somebody Told Me| 2318|
|          Pink Floyd|  Wish You Were Here| 2314|
|            Interpol|          Obstacle 1| 2313|
|     Yeah Yeah Yeahs|                Maps| 2311|
|           Radiohead|       Bodysnatchers| 2294|
|           The Shins|           New Slang| 2281|
|                Muse|  Knights Of Cydonia| 2280|
|                Muse|Map Of The Proble...| 2276|
|           Radiohead|Everything In Its...| 2275|
|                Muse|            Hysteria| 2264|
|          Kanye West|Paranoid (Feat. M...| 2261|
|           The Shins|    Caring Is Creepy| 2247|
|            Coldplay|              Clocks| 2246|
|           Radiohead|      House Of Cards| 2243|
|              M.I.A.|        Paper Planes| 2240|
|         Imogen Heap|       Hide And Seek| 2239|
|            Coldplay|         Don'T Panic| 2232|
|             Nirvana|Smells Like Teen ...| 2229|
|          Kanye West|        Say You Will| 2229|
|           Radiohead|        No Surprises| 2227|
|             Klaxons|        Golden Skans| 2226|
|          Bloc Party|          Blue Light| 2216|
|            Coldplay|             Fix You| 2215|
|        Jeff Buckley|          Hallelujah| 2210|
|     Tv On The Radio|  Staring At The Sun| 2209|
|          Kanye West|      Coldest Winter| 2201|
|         Arcade Fire|          No Cars Go| 2195|
|         The Killers|Smile Like You Me...| 2182|
|        Modest Mouse|            Float On| 2178|
|       Amy Winehouse|               Rehab| 2167|
|          Kanye West|            Bad News| 2163|
|            Coldplay|              Yellow| 2158|
|                Mgmt|       Electric Feel| 2155|
|      Regina Spektor|            Fidelity| 2119|
| Death Cab For Cutie|         Summer Skin| 2115|
|         Johnny Cash|                Hurt| 2114|
|         Arcade Fire|Une Année Sans Lu...| 2111|
|         Arcade Fire|             Wake Up| 2108|
|          Kanye West|Pinocchio Story (...| 2107|
|          Kanye West|             Robocop| 2106|
|          Kanye West|See You In My Nig...| 2092|
|Red Hot Chili Pep...|         Scar Tissue| 2091|
|           Radiohead|Weird Fishes/Arpeggi| 2089|
|  The Postal Service|         Clark Gable| 2088|
|           Radiohead|Exit Music (For A...| 2088|
|       Nelly Furtado|        Say It Right| 2080|
|  The Postal Service|    Brand New Colony| 2076|
|      Massive Attack|               Angel| 2071|
|      Britney Spears|         Piece Of Me| 2071|
|            The Fray|  How To Save A Life| 2064|
|      Dread Zeppelin|  Stairway To Heaven| 2062|
|           Radiohead|           Videotape| 2061|
|          Kanye West|       Street Lights| 2051|
|         Snow Patrol|                 Run| 2048|
+--------------------+--------------------+-----+
only showing top 100 rows
```
The appoach taken in the `top_100_songs` function is to count and groupby combining `artist-name` & `track-name`.

## Part C

Defined user’s “session” of Last.fm usage to be comprised of one or more songs played by a
user, where each song is started within 20 minutes of the previous song’s start time. Created a list of the top 10 longest sessions (by elapsed time), with the following information about each session: userid, timestamp of first and last songs in the session, and the list of songs played in the session (in order of play).

```bash
+-----------+----------+-------------------+-------------------+--------------------+--------------------+
|     userid| sessionid|      start_session|        end_session|          track_list|time_elapsed_minutes|
+-----------+----------+-------------------+-------------------+--------------------+--------------------+
|user_000949|       150|2006-02-12 17:49:31|2006-02-27 11:29:37|Chained To You; T...|             21220.0|
|user_000997|        17|2007-04-26 01:36:02|2007-05-10 18:55:03|Unentitled States...|             21199.0|
|user_000949|       558|2007-05-01 03:41:15|2007-05-14 01:05:52|White Daisy Passi...|             18565.0|
|user_000544|        74|2007-02-12 13:03:52|2007-02-23 00:51:08|Finally Woken; On...|             15107.0|
|user_000949|       138|2005-12-09 08:26:38|2005-12-18 04:40:04|Neighborhood #2 (...|             12733.0|
|user_000949|       124|2005-11-11 03:30:37|2005-11-18 22:50:07|Excuse Me Miss Ag...|             11240.0|
|user_000949|       188|2006-03-18 23:04:14|2006-03-26 19:13:45|Disco Science; He...|             11230.0|
|user_000544|        54|2007-01-06 01:07:04|2007-01-13 13:57:45|La Murga; Breathe...|             10851.0|
|user_000250|      1284|2008-02-21 15:31:45|2008-02-28 21:18:03|Lazarus Heart; Sp...|             10426.0|
|user_000949|       151|2006-02-27 17:47:28|2006-03-06 19:52:35|Y-Control; Banque...|             10205.0|
+-----------+----------+-------------------+-------------------+--------------------+--------------------+
only showing top 10 rows
```

The approach taken in the `top_10_sessions` function:

- Order by `timestamp` while partitioning by `userid`.
- Compare `timestamp` against previous timestamp to verify which are falling within the 20 minutes window.
- Create a `sessionid`. Unique idetifier of the session (e.g. same `userid` can have multiple `sessionids`).
- Groupby `userid` & `sessionid`. Idetifying max and min timestamp for each session (i.e. end and start of the session) and related preordered list of songs per each session.
- Add column with `time_elapsed` in minutes. 
- Order results by the above column. 
