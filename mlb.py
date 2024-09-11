import mlbstatsapi
mlb = mlbstatsapi.Mlb()
shohei_id = mlb.get_people_id("Shohei Ohtani")
print(shohei_id)

stats = ['season', 'seasonAdvanced']
groups = ['hitting']
params={"season":2024}
sho_stats=mlb.get_player_stats(int(shohei_id[0]),stats,groups,**params)
sho_dict = sho_stats['hitting']['season']


sho_site_map= {
    'homeruns':0,
    'avg': 0,
    'stolenbases':0,
    'rbi':0
}

for split in sho_dict.splits:
    for k,v in split.stat.__dict__.items():
        # print(k,v)
        if k in sho_site_map:
            sho_site_map[k] = v

print(sho_site_map)


