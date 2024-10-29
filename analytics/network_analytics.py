import pandas as pd
import networkx as nx
import plotly.express as px
from database import session
from models import Contact

class NetworkAnalytics:
    def __init__(self):
        self.contacts = session.query(Contact).all()
        self.G = self.build_graph()

    def build_graph(self):
        G = nx.Graph()
        for contact in self.contacts:
            G.add_node(contact.name)
            for related_contact in contact.relationships:
                G.add_edge(contact.name, related_contact.name)
        return G

    def calculate_diversity(self):
        degrees = dict(self.G.degree())
        diversity = pd.DataFrame(list(degrees.items()), columns=['Contact', 'Degree'])
        return diversity

    def generate_diversity_chart(self):
        diversity = self.calculate_diversity()
        fig = px.bar(diversity, x='Contact', y='Degree', title='Network Diversity')
        return fig
