from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningDashboard(Dashboard):
    __dashboard_name__ = "Planning Dashboard"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_booked_order_by_curr'], 'activeView': 'charts_booked_order_by_curr', 'id': '10'},
                                                         'size': 260, 'visible': False}], 'size': 1787.949951171875}
    __grid_width__ = 1787.949951171875
    __grid_height__ = 777.7833251953125
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 7

    charts_booked_order_by_curr = PanelComponent(component_type="charts",
                                                 name="Booked Orders by Curr",
                                                 query="Select(OrderHeaders.transactional_curr_code, func.count(OrderHeaders.header_id).label('count')).group_by(OrderHeaders.transactional_curr_code)",
                                                 data_objects={'OrderHeaders': 'di_thermax_planmax.ontologies.order_headers'},
                                                 header="Booked Orders by Curr",
                                                 description="Booked Orders by Curr",
                                                 columns=[],
                                                 chart_options={
                                                     "series": [
                                                         {
                                                             "label": {
                                                                 "margin": 8,
                                                                 "show": True
                                                             },
                                                             "name": "Items",
                                                             "type": "bar"
                                                         }
                                                     ],
                                                     "title": [
                                                         {
                                                             "show": True,
                                                             "subtext": "Open orders",
                                                             "text": "Open Jobs by Currency"
                                                         }
                                                     ],
                                                     "tooltip": {
                                                         "show": True
                                                     },
                                                     "xAxis": {
                                                         "type": "category"
                                                     },
                                                     "yAxis": {
                                                     }
                                                 },
                                                 content_component="mediator",
                                                 relations=[])