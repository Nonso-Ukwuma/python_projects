#!/usr/bin/env python
# coding: utf-8

# In[211]:


class Hockey_league:
    
    def __init__(self, stats, tnames):
        self.stats = stats
        self.tnames = tnames
        
    def summarize(self):
        game_summary = []
        for stat in self.stats:
            name1 = ''
            name2 = ''
            for names in self.tnames:
                for k, v in names.items():
                    if str(stat[1]) == v:
                        name1 = k
                        
                    if str(stat[2]) == v:
                        name2 = k
                        
            game_summary.append({'Game': stat[0], 'Home': name1, 'HG': stat[3], 'Away': name2, 'AG': stat[4]})
        
        print('Game Summaries ')
        print(f'Game\t Home\t \t\t Away\t \t')
        for i in range(0, len(game_summary)):
            print(f"{game_summary[i]['Game']}\t {game_summary[i]['Home']}\t ({game_summary[i]['HG']})\t {game_summary[i]['Away']:8}\t ({game_summary[i]['AG']})\t")
        
    def standings(self):
        from collections import OrderedDict
        
        table = []
        f_table = {}
        
        for name in self.tnames:
            for k, v in name.items():
                table.append({'num': v, 'name': k, 'Points': 0, 'Wins': 0, 'Losses': 0, 'Ties': 0})
        
        for stats in self.stats:
            for i in range(0, len(table)):
                if table[i]['num'] == str(stats[1]):
                    if stats[3] > stats[4]:
                        table[i]['Wins']+= 1
                        table[i]['Points']+= 2
                    elif stats[3] == stats[4]:
                        table[i]['Ties']+= 1
                        table[i]['Points']+= 1
                    else:
                        table[i]['Losses']+= 1
                        
                elif table[i]['num'] == str(stats[2]):
                    if stats[4] > stats[3]:
                        table[i]['Wins']+= 1
                        table[i]['Points']+= 2
                    elif stats[4] == stats[3]:
                        table[i]['Ties']+= 1
                        table[i]['Points']+= 1
                    else:
                        table[i]['Losses']+= 1
        
        #prepare and sort the final table standings in descending order of points per team
        for i in range(0, len(table)):
            f_table.update({i: table[i]})
        
        stand = OrderedDict(sorted(f_table.items(), key=lambda kv: kv[1]['Points'], reverse=True))
        
        print('Team Standings')
        print(f'Team\t\tPoints\tWins\tLosses\tTies\t')
        for k, v in stand.items():
            print(f"{v['name']:12}\t{v['Points']:6}\t  {v['Wins']}\t  {v['Losses']:4}\t  {v['Ties']:2}\t")


# In[212]:


def extract_data():
        import csv
        team = open('teams.csv')
        goals = open('team_goals.csv')

        team_names = csv.DictReader(team)
        team_goals = csv.reader(goals)
        t_names = []
        
        #Extract the team names and team numbers
        for t in team_names:
            t_names.append({t['name'] : t['num']})
        team.close()
        
        #Extract the match summary details
        t_goals = []
        for g in team_goals:
            t_goals.append(g)
        goals.close()
        
        games = []
        for i in t_goals:
            if '#' in str(i):
                continue
            else:
                games.append(i)
        
        #format the games summary into a list of dictionaries for extraction of the individual match statistics
        keys = ['Game', 'Team', 'Goal', 'Assist_1', 'Assist_2']
        game_summary = []
        for v in range(1, len(games)):
            game_summary.append(dict(zip(keys, games[v])))
            
        #Extract individual match details
        summ = [0, 0, 0, 0, 0]

        gamesummary = []
        for i in range(0, len(game_summary)):
            result = []
           
            if summ[0] == 0:
                    summ[0] = int(game_summary[i]['Game'])

            if game_summary[i]['Game'] == str(summ[0]):
                if summ[1] == 0:
                    summ[1] = int(game_summary[i]['Team'])

                if game_summary[i]['Team'] != str(summ[1]):
                    summ[2] = int(game_summary[i]['Team'])

                if game_summary[i]['Team'] == str(summ[1]):
                    for k, v in game_summary[i].items():
                        if k == 'Goal':
                            summ[3] += 1

                elif game_summary[i]['Team'] == str(summ[2]):
                    for k, v in game_summary[i].items():
                        if k == 'Goal':
                            summ[4] += 1  
            else:
                result = list(summ)
                gamesummary.append(result)
                summ[0] = int(game_summary[i]['Game'])
                summ[1] = int(game_summary[i]['Team'])
                summ[2] = 0
                summ[3] = 0
                summ[4] = 0
                if game_summary[i]['Team'] == str(summ[1]):
                    for k, v in game_summary[i].items():
                        if k == 'Goal':
                            summ[3] += 1

        result = list(summ)
        gamesummary.append(result)
        
        return gamesummary, t_names


# In[213]:


def main():
    game_stats, names = extract_data()
    hockey_stats = Hockey_league(game_stats, names)
    hockey_stats.summarize()
    print('\n \n')
    hockey_stats.standings()
    
    


# In[214]:


main()


# In[ ]:




