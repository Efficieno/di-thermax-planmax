from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.order_lines import OrderLines
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.order_lines import OrderLines
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningDashboard(Dashboard):
    __dashboard_name__ = "Planning Dashboard"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_orders_by_status'], 'activeView': 'charts_orders_by_status', 'id': '1'}, 'size': 372}, {'type': 'leaf', 'data': {'views': ['charts_orders_by_group'], 'activeView': 'charts_orders_by_group', 'id': '2'}, 'size': 373.46875}], 'size': 1258}, {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_JZSFQImkw'], 'activeView': 'metrics_JZSFQImkw', 'id': '3'}, 'size': 248}, {'type': 'leaf', 'data': {'views': ['metrics_MGiwGCl28'], 'activeView': 'metrics_MGiwGCl28', 'id': '4'}, 'size': 248}, {'type': 'leaf', 'data': {'views': ['metrics_w1T41TC2A'], 'activeView': 'metrics_w1T41TC2A', 'id': '5'}, 'size': 249.46875}], 'size': 268.578125}], 'size': 745.46875}
    __grid_width__ = 1526.578125
    __grid_height__ = 745.46875
    __grid_orientation__ = "HORIZONTAL"
    __active_group__ = 3

    charts_orders_by_status = PanelComponent(component_type="charts",
                          name="Orders by Status",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Open Orders by Status",
                          description="Open Orders by Status",
                          columns=[],
                          chart_options={'legend': {'data': ['Count', 'Value']}, 'series': [{'encode': {'x': 'order_status', 'y': 'count'}, 'name': 'Count', 'type': 'bar', 'yAxisIndex': 0}, {'encode': {'x': 'order_status', 'y': 'value'}, 'name': 'Value', 'type': 'line', 'yAxisIndex': 1}], 'title': {'text': 'Orders by Status'}, 'tooltip': {'trigger': 'axis'}, 'xAxis': {'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]},
                          content_component="mediator",
                          relations=[],
                          metadata={})
    charts_orders_by_group = PanelComponent(component_type="charts",
                          name="Orders by Group",
                          query="Select(PlanmaxHeaders.group_name, func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.group_name)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Orders by Group",
                          description="Orders by Group",
                          columns=[],
                          chart_options={
    "title": {
        "text": "Group Name Distribution",
        "subtext": "Value Breakdown",
        "left": "center"
    },
    "tooltip": {
        "trigger": "item",
    },
    "legend": {
        "orient": "vertical",
        "left": "left",
    },
    "series": [
        {
            "type": "pie",
            "radius": "50%",
            "encode": {
                "itemName": "group_name",
                "value": "value"
            },
            "label": {
                "show": True,
            }
        }
    ]
},
                          content_component="mediator",
                          relations=[],
                          metadata={})
    metrics_JZSFQImkw = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="Select(func.count(PlanmaxHeaders.order_intake_status).label('count')).filter(PlanmaxHeaders.order_intake_status== 'P')",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Orders Intake Pending",
                          description="Orders with intake config pending",
                          columns=[],
                          chart_options={},
                          content_component="mediator",
                          relations=[],
                          metadata={'additional_field_visible': True, 'display': '1000', 'font_size': '1.5', 'font_style': ['bold']})
    metrics_MGiwGCl28 = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="Select(func.count(PlanmaxHeaders.reflection_config_status).label('count')).filter(PlanmaxHeaders.reflection_config_status == 'P')",
                          data_objects={'OrderLines': 'di_thermax_planmax.ontologies.order_lines', 'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Pending Reflection",
                          description="Pending Reflection",
                          columns=[],
                          chart_options={},
                          content_component="mediator",
                          relations=[],
                          metadata={'display': '1000', 'font_size': '2', 'font_style': ['bold'], 'additional_field_visible': True})
    metrics_w1T41TC2A = PanelComponent(component_type="metrics",
                          name="Demo Header",
                          query="Select(func.count(PlanmaxHeaders.bom_common_status).label('count')).filter(PlanmaxHeaders.bom_common_status== 'P')",
                          data_objects={'OrderLines': 'di_thermax_planmax.ontologies.order_lines', 'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Pending BOM Common",
                          description="Pending BOM Common",
                          columns=[],
                          chart_options={},
                          content_component="mediator",
                          relations=[],
                          metadata={'display': '1000', 'font_size': '2', 'font_style': ['bold'], 'additional_field_visible': True})
