class ZScoreStandarisation:

    def ZScore(self, data):
        return (data - data.mean()) / data.std()

