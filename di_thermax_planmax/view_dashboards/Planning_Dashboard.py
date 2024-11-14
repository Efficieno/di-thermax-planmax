from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningDashboard(Dashboard):
    __dashboard_name__ = "Planning Dashboard"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_orders_by_status'], 'activeView': 'charts_orders_by_status', 'id': '1'}, 'size': 763}, {'type': 'leaf', 'data': {'views': ['charts_orders_by_group'], 'activeView': 'charts_orders_by_group', 'id': '2'}, 'size': 763.578125}], 'size': 244}, {'type': 'leaf', 'data': {'views': ['metrics_JZSFQImkw'], 'activeView': 'metrics_JZSFQImkw', 'id': '3'}, 'size': 244.3125}], 'size': 1526.578125}
    __grid_width__ = 1526.578125
    __grid_height__ = 488.3125
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 3

    charts_orders_by_status = PanelComponent(component_type="charts",
                          name="Orders by Status",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Open Orders by Status",
                          description="Open Orders by Status",
                          columns=[],
                          chart_options={'legend': {'data': ['Count', 'Value']}, 'series': [{'encode': {'x': 'order_status', 'y': 'count'}, 'name': 'Count', 'type': 'bar', 'yAxisIndex': 0}, {'encode': {'x': 'order_status', 'y': 'value'}, 'name': 'Value', 'type': 'bar', 'yAxisIndex': 1}], 'title': {'text': 'Order Status: Count and Value'}, 'tooltip': {'trigger': 'axis'}, 'xAxis': {'axisLabel': {'rotate': 45}, 'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]},
                          content_component="mediator",
                          relations=[],
                          metadata={})
    charts_orders_by_group = PanelComponent(component_type="charts",
                          name="Orders by Group",
                          query="Select(PlanmaxHeaders.group_name, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.group_name)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Orders by Group",
                          description="Orders by Group",
                          columns=[],
                          chart_options={'legend': {'data': ['Count', 'Value']}, 'series': [{'encode': {'x': 'group_name', 'y': 'count'}, 'name': 'Count', 'type': 'bar', 'yAxisIndex': 0}, {'encode': {'x': 'group_name', 'y': 'value'}, 'name': 'Value', 'type': 'bar', 'yAxisIndex': 1}], 'title': {'text': 'Order Status: Count and Value'}, 'tooltip': {'trigger': 'axis'}, 'xAxis': {'axisLabel': {'rotate': 45}, 'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]},
                          content_component="mediator",
                          relations=[],
                          metadata={})
    metrics_JZSFQImkw = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Demo Header",
                          description="Demo Description",
                          columns=[],
                          chart_options={},
                          content_component="mediator",
                          relations=[],
                          metadata={'display': '1000', 'font_size': '2', 'font_style': ['bold'], 'additional_field_visible': True})
