# 'Gambling' experiments

The purpose of this repo is to explore asymptotics of various simple games.  First we begin with five card draw.

## Five Card Draw

In the five card draw "game", I've set up a deck and a drawing without replacement scheme.  So that I can have multiple "players", play the game.  I've also constructed a point system, based on hand hierarchy and then established relative points within each hand determined by high card.  Thus the rules of the game have been fully specified within the code, at present.

### Experiment One

In this first experiment, I begin by asking the question - do certain players have an advantage based solely on turn order?  It turns out the answer is yes.  

```
For  2 players at 1000 experiments, the results were {0: 0.554, 1: 0.446}
For  2 players at 10000 experiments, the results were {0: 0.5357, 1: 0.4643}
For  2 players at 100000 experiments, the results were {0: 0.5291, 1: 0.4709}
For  3 players at 1000 experiments, the results were {0: 0.34, 1: 0.335, 2: 0.325}
For  3 players at 10000 experiments, the results were {0: 0.3532, 1: 0.3329, 2: 0.3139}
For  3 players at 100000 experiments, the results were {0: 0.35381, 1: 0.32918, 2: 0.31701}
For  4 players at 1000 experiments, the results were {0: 0.301, 1: 0.239, 2: 0.24, 3: 0.22}
For  4 players at 10000 experiments, the results were {0: 0.2692, 1: 0.2539, 2: 0.2399, 3: 0.237}
For  4 players at 100000 experiments, the results were {0: 0.26237, 1: 0.25241, 2: 0.24544, 3: 0.23978}
```

As you can see, for 2 players, player '0', the first player to draw always has a slight advantage.  As the number of games increases, this advantage decreases.  But in the real world, it's not just about what happens at infinity, it's the path taken as the system tends towards infinity.  It's important to note, that this version of the game isn't played the way normal five card draw is done.  There is no redraw period in this game.  This is because I was interested first, if any player had a natural advantage before redraw.  The next set of experiments will consider redraw.  

Even without redraw, we can draw some interesting conclusions:

1. Chances of winning are ordered by draw order.  Player 1 always has an advantage compared with all other players.  And each player who draws next has a slightly higher probability of winning then the next one.  This should make sense, it's because of the resource allocation issue.  If we treat cards as a resource, the first player has the possibilty of reaching the most possible cards.  Any players who go after this will have a lower chance of getting these better cards, because it's possibly they are taken.  So this leads to a general conclusion, under certain conditions.  We'll consider the generalization of this first conclusion in the next section.

2. The asymptotics appear to be heading towards equality for the 2 player and the 4 player case, but not the 3 player case.  For the 2 player case and the 4 player case, the probabilities of each successive player increase, as the number of games increases.  The increase at different rates, with the 4 player case showing some interesting dynamics between players 2, 3 and 4.  Specifically, we can look at the rate of change in probabilities as the number of experiments increase.  It looks as though the asymptotics are possibily not strictly increasing, which is fascinating.  

Now let's consider some generalizations of our "game":

If we treat 5 card draw not as  