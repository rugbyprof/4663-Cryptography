"""
pip install reverend
pip install sets
Source Code :https://laslabs.github.io/python-reverend/_modules/reverend/thomas.html
Overview of Bayes Rule: https://towardsdatascience.com/bayes-rule-with-a-simple-and-practical-example-2bce3d0f4ad0
"""
from reverend.thomas import Bayes
g = Bayes()    # guesser
g.train('french','La souris est rentre dans son trou.')
g.train('english','my tailor is rich.')
g.train('french','Je ne sais pas si je viendrai demain.')
g.train('english','I do not plan to update my website soon and I would really like some help from the rest of you idiots.')

print(g.guess('Jumping out of cliffs it not a good idea.'))

# print(g.guess('Demain il fera trs probablement chaud.'))
