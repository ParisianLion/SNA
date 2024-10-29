from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
import networkx as nx
import plotly.graph_objects as go
from database import session
from models import Contact

class NetworkVisualization(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)
        self.update_graph()

    def update_graph(self):
        contacts = session.query(Contact).all()
        G = nx.Graph()

        for contact in contacts:
            G.add_node(contact.name)
            for related_contact in contact.relationships:
                G.add_edge(contact.name, related_contact.name)

        pos = nx.spring_layout(G, dim=3)

        node_x = []
        node_y = []
        node_z = []
        node_text = []

        for node in G.nodes():
            x, y, z = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_z.append(z)
            node_text.append(node)

        edge_x = []
        edge_y = []
        edge_z = []

        for edge in G.edges():
            x0, y0, z0 = pos[edge[0]]
            x1, y1, z1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            edge_z.extend([z0, z1, None])

        edge_trace = go.Scatter3d(
            x=edge_x, y=edge_y, z=edge_z,
            mode='lines',
            line=dict(color='black', width=2),
            hoverinfo='none'
        )

        node_trace = go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers+text',
            marker=dict(size=10, color='blue'),
            text=node_text,
            textposition='top center',
            hoverinfo='text'
        )

        fig = go.Figure(data=[edge_trace, node_trace])
        fig.update_layout(showlegend=False)

        self.web_view.setHtml(fig.to_html(include_plotlyjs='cdn'))
