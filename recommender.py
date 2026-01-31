from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, df):
        self.df = df
        self.user_item = df.pivot_table(
            index='Customer ID',
            columns='StockCode',
            values='Total',
            fill_value=0
        )

        self.similarity = cosine_similarity(self.user_item)

    def recommend(self, user_id, top_n=5):
        if user_id not in self.user_item.index:
            return self.trending(top_n)

        users = list(self.user_item.index)
        idx = users.index(user_id)

        scores = list(enumerate(self.similarity[idx]))
        scores.sort(key=lambda x: x[1], reverse=True)

        similar_users = [users[i] for i,_ in scores[1:6]]

        products = self.df[self.df["Customer ID"].isin(similar_users)]["StockCode"]

        return products.value_counts().head(top_n).index.tolist()

    def trending(self, top_n=5):
        return self.df["StockCode"].value_counts().head(top_n).index.tolist()
