from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty, FilterField, FilterComponent
from sqlalchemy import Integer, Select, bindparam, String
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningBasic(Dashboard):
    __dashboard_name__ = "planning_basic"
    __dashboard_description__ = "planning basic dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_p0ZNWAd17'], 'activeView': 'metrics_p0ZNWAd17', 'id': '1'}, 'size': 508}, {'type': 'leaf', 'data': {'views': ['metrics_u6_jxLXFw'], 'activeView': 'metrics_u6_jxLXFw', 'id': '2'}, 'size': 508}, {'type': 'leaf', 'data': {'views': ['metrics_40vIQtFUN'], 'activeView': 'metrics_40vIQtFUN', 'id': '3'}, 'size': 510.578125}], 'size': 745.46875}
    __grid_width__ = 1526.578125
    __grid_height__ = 745.46875
    __grid_orientation__ = "HORIZONTAL"
    __active_group__ = 3

    metrics_p0ZNWAd17 = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="Select(func.concat(func.concat(func.count(PlanmaxHeaders.sales_order_header_id).label('count'), '/') ,func.round(func.sum(PlanmaxHeaders.total_unit_value_in_inr/ 100000), 2).label('value')))",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Total Orders",
                          description="Total orders (count/value)",
                          content_component="mediator",
                          relations=[],
                          metadata={'display': '1000', 'fontSize': '2', 'fontStyle': [], 'additionalFieldVisible': True},
                          drill_downs={},
                          actions=[],
                          inline_actions={'name': '', 'value': ''},
                          details=[])
    metrics_u6_jxLXFw = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="Select(func.concat(func.concat(func.count(PlanmaxHeaders.sales_order_header_id).label('count'), '/') ,func.round(func.sum(PlanmaxHeaders.total_unit_value_in_inr/ 100000), 2).label('value'))).filter(PlanmaxHeaders.group_name == 'HO')",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Total HO Orders",
                          description="Total HO Orders (count/value)",
                          content_component="mediator",
                          relations=[],
                          metadata={'display': '1000', 'fontSize': '2', 'fontStyle': [], 'additionalFieldVisible': True},
                          drill_downs={},
                          actions=[],
                          inline_actions={'name': '', 'value': ''},
                          details=[])
    metrics_40vIQtFUN = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="Select(func.concat(func.concat(func.count(PlanmaxHeaders.sales_order_header_id).label('count'), '/') ,func.round(func.sum(PlanmaxHeaders.total_unit_value_in_inr/ 100000), 2).label('value'))).filter(PlanmaxHeaders.order_status.in_(["OPEN", "FULFILLED", "HOLD", "HOLD_POST PRN"]))",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Total Rolling Plan",
                          description="Rolling Plan (count/value)",
                          content_component="mediator",
                          relations=[],
                          metadata={'display': '1000', 'fontSize': '2', 'fontStyle': [], 'additionalFieldVisible': True},
                          drill_downs={},
                          actions=[],
                          inline_actions={'name': '', 'value': ''},
                          details=[])


    dashboard_filters = FilterComponent(filter_fields={})
