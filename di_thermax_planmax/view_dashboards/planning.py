from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty, FilterField, FilterComponent
from sqlalchemy import Integer, Select, bindparam, String
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.order_headers import OrderHeaders
from di_thermax_planmax.ontologies.order_headers import OrderHeaders


class Planning(Dashboard):
    __dashboard_name__ = "planning"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts__aEywZ_Sh'], 'activeView': 'charts__aEywZ_Sh', 'id': '1'}, 'size': 249}, {'type': 'leaf', 'data': {'views': ['panel__NXT8QrunU'], 'activeView': 'panel__NXT8QrunU', 'id': '2'}, 'size': 249}, {'type': 'leaf', 'data': {'views': ['panel_SrQ6YWB5ry'], 'activeView': 'panel_SrQ6YWB5ry', 'id': '3'}, 'size': 247.46875}], 'size': 1526.578125}
    __grid_width__ = 1526.578125
    __grid_height__ = 745.46875
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 1

    charts__aEywZ_Sh = PanelComponent(component_type="charts",
                          name="Demo Header",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr/ 100000).label('value')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Order Information",
                          description="Demo Description",
                          content_component="mediator",
                          relations=[],
                          metadata={'chartOptions': {'legend': {'data': [], 'left': 'center', 'orient': 'horizontal', 'show': True}, 'series': [{'datasetIndex': 0, 'encode': {'itemName': '', 'value': '', 'x': 'order_status', 'y': 'count'}, 'name': '', 'type': 'bar'}, {'datasetIndex': 1, 'encode': {'itemName': '', 'value': '', 'x': 'order_status', 'y': 'value'}, 'name': '', 'type': 'line'}], 'title': {'left': 'left', 'subtext': '', 'text': 'Order Information', 'top': 'top'}, 'tooltip': {'formatter': '', 'show': True, 'trigger': 'item'}, 'xAxis': {'name': '', 'show': True, 'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]}},
                          drill_downs={'0': {'name': 'Month', 'value': 'PlanmaxHeaders.month_name'}, '1': {'name': 'Group', 'value': 'PlanmaxHeaders.group_name'}, '2': {'name': 'Region', 'value': 'PlanmaxHeaders.region_of_order'}, '3': {'name': 'Product Category', 'value': 'PlanmaxHeaders.product_category'}, '4': {'name': 'MFG Organization', 'value': 'PlanmaxHeaders.mfg_organization_code'}, '5': {'name': 'Planner', 'value': 'PlanmaxHeaders.planner'}, '6': {'name': 'Regional Commercial', 'value': 'PlanmaxHeaders.regional_commercial'}},
                          actions=[],
                          inline_actions={'name': '', 'value': ''},
                          details=[])
    panel__NXT8QrunU = PanelComponent(component_type="metrics",
                          name="Panel 1",
                          query="Select(func.count(OrderHeaders.header_id).label('Count Orders'))",
                          data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                          header="Demo Metric Header",
                          description="Demo Metric Description",
                          content_component="default",
                          relations=[],
                          metadata={},
                          drill_downs={},
                          actions=[],
                          inline_actions=[],
                          details=[])
    panel_SrQ6YWB5ry = PanelComponent(component_type="metrics",
                          name="Panel 1",
                          query="Select(func.count(OrderHeaders.header_id).label('Count Orders'))",
                          data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                          header="Demo Metric Header",
                          description="Demo Metric Description",
                          content_component="default",
                          relations=[],
                          metadata={},
                          drill_downs={},
                          actions=[],
                          inline_actions=[],
                          details=[])


    dashboard_filters = FilterComponent(filter_fields={})
