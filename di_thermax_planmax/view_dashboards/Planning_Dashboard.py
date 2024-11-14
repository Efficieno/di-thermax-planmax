from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningDashboard(Dashboard):
    __dashboard_name__ = "Planning Dashboard"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_booked_order_by_curr'], 'activeView': 'charts_booked_order_by_curr', 'id': '1'}, 'size': 1778.296875}], 'size': 707.53125}
    __grid_width__ = 1778.296875
    __grid_height__ = 707.53125
    __grid_orientation__ = "HORIZONTAL"
    __active_group__ = 1

    charts_booked_order_by_curr = PanelComponent(component_type="charts",
                          name="Booked Orders by Curr",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Open Orders by Status",
                          description="Open Orders by Status",
                          columns=[],
                          chart_options={'series': [{'label': {'margin': 8, 'show': True}, 'name': 'Items', 'type': 'bar'}], 'title': [{'show': True, 'subtext': 'Open orders', 'text': 'Open Orders By Status'}], 'tooltip': {'show': True}, 'xAxis': {'type': 'category'}, 'yAxis': {}},
                          content_component="mediator",
                          relations=[],
                          metadata={})
