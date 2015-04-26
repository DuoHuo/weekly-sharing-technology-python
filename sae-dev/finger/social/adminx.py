import xadmin
from xadmin import views
from models import *
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

# class MainDashboard(object):
#     widgets = [
#         [
#             {"type": "html", "title": "main", "content": "<h3> Welcome to Xadmin! </h3><p>Join Online Group: <br/></p>"},
#             # {"type": "chart", "model": "app.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2013-01-08', 'p': 1, '_p_date__lt': '2013-01-29'}},
#             {"type": "list", "model": "social.shop", 'params': {
#                 'o':'-create_time'}},
#         ],
#         # [
#         #     {"type": "qbutton", "title": "Quick Start", "btns": [{'model': Host}, {'model':IDC}, {'title': "Google", 'url': "http://www.google.com"}]},
#         #     {"type": "addform", "model": MaintainLog},
#         # ]
#     ]
# xadmin.site.register(views.website.IndexView, MainDashboard)
