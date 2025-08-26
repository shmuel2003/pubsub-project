[1mdiff --git a/publisher/dataset_loader.py b/publisher/dataset_loader.py[m
[1mindex e69de29..50fad98 100644[m
[1m--- a/publisher/dataset_loader.py[m
[1m+++ b/publisher/dataset_loader.py[m
[36m@@ -0,0 +1,33 @@[m
[32m+[m[32mfrom sklearn.datasets import fetch_20newsgroups[m
[32m+[m[32mimport random[m
[32m+[m
[32m+[m[32mclass DatasetLoader:[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        self.interesting_categories = [[m
[32m+[m[32m            'alt.atheism','comp.graphics','comp.os.ms-windows.misc',[m
[32m+[m[32m            'comp.sys.ibm.pc.hardware','comp.sys.mac.hardware',[m
[32m+[m[32m            'comp.windows.x','misc.forsale','rec.autos',[m
[32m+[m[32m            'rec.motorcycles','rec.sport.baseball'[m
[32m+[m[32m        ][m
[32m+[m[32m        self.not_interesting_categories = [[m
[32m+[m[32m            'rec.sport.hockey','sci.crypt','sci.electronics',[m
[32m+[m[32m            'sci.med','sci.space','soc.religion.christian',[m
[32m+[m[32m            'talk.politics.guns','talk.politics.mideast',[m
[32m+[m[32m            'talk.politics.misc','talk.religion.misc'[m
[32m+[m[32m        ][m
[32m+[m
[32m+[m[32m        self.data_interesting = fetch_20newsgroups([m
[32m+[m[32m            subset='all', categories=self.interesting_categories[m
[32m+[m[32m        )[m
[32m+[m[32m        self.data_not_interesting = fetch_20newsgroups([m
[32m+[m[32m            subset='all', categories=self.not_interesting_categories[m
[32m+[m[32m        )[m
[32m+[m
[32m+[m[32m    def get_samples(self, n=20):[m
[32m+[m[32m        interesting_samples = random.sample(self.data_interesting.data, n)[m
[32m+[m[32m        not_interesting_samples = random.sample(self.data_not_interesting.data, n)[m
[32m+[m
[32m+[m[32m        return {[m
[32m+[m[32m            "interesting": interesting_samples,[m
[32m+[m[32m            "not_interesting": not_interesting_samples[m
[32m+[m[32m        }[m
\ No newline at end of file[m
