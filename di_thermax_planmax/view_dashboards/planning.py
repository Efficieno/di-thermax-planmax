from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty, FilterField, FilterComponent
from sqlalchemy import Integer, Select, bindparam, String
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class Planning(Dashboard):
    __dashboard_name__ = "planning"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts__aEywZ_Sh'], 'activeView': 'charts__aEywZ_Sh', 'id': '1'}, 'size': 348}, {'type': 'leaf', 'data': {'views': ['charts_hL_B6ejVG'], 'activeView': 'charts_hL_B6ejVG', 'id': '2'}, 'size': 349.375}], 'size': 1526.578125}
    __grid_width__ = 1526.578125
    __grid_height__ = 697.375
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 2

    charts__aEywZ_Sh = PanelComponent(component_type="charts",
                          name="Demo Header",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr/ 100000).label('value')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Order Information",
                          description="Demo Description",
                          content_component="mediator",
                          relations=[],
                          metadata={'chartOptions': {'legend': {'data': ['Count', 'Value']}, 'series': [{'encode': {'x': 'order_status', 'y': 'count'}, 'name': 'Count', 'type': 'bar', 'yAxisIndex': 0}, {'encode': {'x': 'order_status', 'y': 'value'}, 'name': 'Value', 'type': 'line', 'yAxisIndex': 1}], 'title': {'text': 'Orders by Status'}, 'tooltip': {'trigger': 'axis'}, 'xAxis': {'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]}},
                          drill_downs={'0': {'name': 'Month', 'value': 'PlanmaxHeaders.month_name'}, '1': {'name': 'Group', 'value': 'PlanmaxHeaders.group_name'}, '2': {'name': 'Region', 'value': 'PlanmaxHeaders.region_of_order'}, '3': {'name': 'Product Category', 'value': 'PlanmaxHeaders.product_category'}, '4': {'name': 'MFG Organization', 'value': 'PlanmaxHeaders.mfg_organization_code'}, '5': {'name': 'Planner', 'value': 'PlanmaxHeaders.planner'}, '6': {'name': 'Regional Commercial', 'value': 'PlanmaxHeaders.regional_commercial'}},
                          actions=[],
                          inline_actions={'name': '', 'value': ''},
                          details=[])
    charts_hL_B6ejVG = PanelComponent(component_type="charts",
                          name="Demo Header",
                          query="Select(PlanmaxHeaders.prn_creation_status, func.count(PlanmaxHeaders.prn_creation_status).label('count')).filter(PlanmaxHeaders.order_status == 'OPEN').group_by(PlanmaxHeaders.prn_creation_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="PRN Status",
                          description="Demo Description",
                          content_component="mediator",
                          relations=[],
                          metadata={'chartOptions': {'title': {'text': '', 'subtext': '', 'left': 'left', 'top': 'top'}, 'tooltip': {'show': True, 'trigger': 'item', 'formatter': ''}, 'legend': {'show': True, 'orient': 'horizontal', 'left': 'center', 'data': ['P', 'C', 'NA']}, 'xAxis': {'show': False, 'type': 'category', 'name': ''}, 'yAxis': {'show': False, 'type': 'value', 'name': ''}, 'series': [{'name': '', 'type': 'pie', 'encode': {'x': '', 'y': '', 'value': 'count', 'itemName': 'prn_creation_status'}, 'datasetIndex': 0}]}},
                          drill_downs={},
                          actions=[],
                          inline_actions={'name': '', 'value': ''},
                          details=[])


    dashboard_filters = FilterComponent(filter_fields={})
