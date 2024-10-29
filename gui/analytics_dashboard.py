from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from analytics.network_analytics import NetworkAnalytics

class AnalyticsDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        self.show_analytics()

    def show_analytics(self):
        analytics = NetworkAnalytics()
        fig = analytics.generate_diversity_chart()
        self.web_view.setHtml(fig.to_html(include_plotlyjs='cdn'))
