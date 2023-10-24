import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from sklearn.decomposition import PCA

class PCAGraphs:
    @staticmethod
    def scatter_plot(pca_result, countries, loadings, variables):
        pca_df = pd.DataFrame(data=pca_result, columns=["PC1", "PC2"])
        pca_df["Country"] = countries
        plt.figure(figsize=(10, 8))
        plt.scatter(pca_df["PC1"], pca_df["PC2"])
        plt.xlabel("Principal Component 1 (PC1)")
        plt.ylabel("Principal Component 2 (PC2)")
        plt.title("PCA Analysis")
        plt.grid()

        for i, country in enumerate(pca_df["Country"]):
            plt.annotate(country, (pca_df["PC1"][i], pca_df["PC2"][i]))

        scale = 4
        for i, item in enumerate(variables):
            plt.arrow(0, 0, loadings[0][i] * scale, loadings[1][i] * scale, color='blue', width=0.006)
            plt.text(loadings[0][i] * scale, loadings[1][i] * scale, item, fontsize=12, color='blue')

        plt.show()

    @staticmethod
    def scatter_plot_with_PBI(pc1,pc2, countries, loadings, variables):
        pca_df = pd.DataFrame({"PC1": pc1, "PC2": pc2, "Country": countries})
        top_half = pca_df.iloc[:14]
        bottom_half = pca_df.iloc[14:]

        # Create a scatterplot with red for the top half and blue for the bottom half
        plt.figure(figsize=(10, 8))
        plt.scatter(top_half["PC1"], top_half["PC2"], c="red", label="Top Half")
        plt.scatter(bottom_half["PC1"], bottom_half["PC2"], c="blue", label="Bottom Half")
        plt.xlabel("Principal Component 1 (PC1)")
        plt.ylabel("Principal Component 2 (PC2)")
        plt.title("PCA Analysis")
        plt.grid()

        # Annotate points with country names
        for i, country in enumerate(pca_df["Country"]):
            plt.annotate(country, (pca_df["PC1"][i], pca_df["PC2"][i]))

        scale = 4
        for i, item in enumerate(variables):
            plt.arrow(0, 0, loadings[0][i] * scale, loadings[1][i] * scale, color='blue', width=0.006)
            plt.text(loadings[0][i] * scale, loadings[1][i] * scale, item, fontsize=12, color='blue')
        # Add a legend
        plt.legend(loc="upper right")

        plt.show()

    @staticmethod
    def blox_plot(scaled_data,header):
        pca_df = pd.DataFrame(data=scaled_data, columns=header)
        fig = px.box(pca_df, title='Box plot of the variables')
        fig.show()
    @staticmethod
    def bar_plot(pc1, countries):
        pc1uax = []
        for i in pc1:
            pc1uax.append(i[0])
        pca_df = pd.DataFrame({"PC1": pc1uax, "Country": countries})
        fig = px.bar(pca_df, x='Country', y='PC1', title='PC1 by country')
        fig.show()
    @staticmethod
    def scree_plot(pca: PCA):
        pca_values = np.arange(pca.n_components_) + 1
        plt.plot(pca_values, pca.explained_variance_ratio_, 'ro-', linewidth=2)
        plt.title('Scree Plot')
        plt.xlabel('Principal Component')
        plt.ylabel('Proportion of Variance Explained')
        plt.show()
