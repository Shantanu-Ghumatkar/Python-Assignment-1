import point as pt

player = {
    'Virat Kohli': pt.bating(run=112, four=10, balls=119),
    'du Plessis': pt.bating(run=120, four=11, six=2, balls=112),
    'Bhuvneshwar Kumar': pt.bowling(wicket=1, over=10, run=71),
    'Yuzvendra Chahal': pt.bowling(wicket=2, over=10, run=45),
    'Kuldeep Yadav': pt.bowling(wicket=3, over=10, run=34)
}

for name, score in player.items():
    print("name : '" + name, "', 'score': {}".format(score))
