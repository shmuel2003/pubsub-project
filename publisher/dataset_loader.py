from sklearn.datasets import fetch_20newsgroups
import random

class DatasetLoader:
    def __init__(self):
        self.interesting_categories = [
            'alt.atheism','comp.graphics','comp.os.ms-windows.misc',
            'comp.sys.ibm.pc.hardware','comp.sys.mac.hardware',
            'comp.windows.x','misc.forsale','rec.autos',
            'rec.motorcycles','rec.sport.baseball'
        ]
        self.not_interesting_categories = [
            'rec.sport.hockey','sci.crypt','sci.electronics',
            'sci.med','sci.space','soc.religion.christian',
            'talk.politics.guns','talk.politics.mideast',
            'talk.politics.misc','talk.religion.misc'
        ]

        self.data_interesting = fetch_20newsgroups(
            subset='all', categories=self.interesting_categories
        )
        self.data_not_interesting = fetch_20newsgroups(
            subset='all', categories=self.not_interesting_categories
        )

    def get_samples(self, n=20):
        interesting_samples = random.sample(self.data_interesting.data, n)
        not_interesting_samples = random.sample(self.data_not_interesting.data, n)

        return {
            "interesting": interesting_samples,
            "not_interesting": not_interesting_samples
        }