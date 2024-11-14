from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningDashboard(Dashboard):
    __dashboard_name__ = "Planning Dashboard"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 
                             'data': [
                                 {'type': 'leaf', 'data': {'views': ['charts_orders_by_status'], 'activeView': 'charts_orders_by_status', 'id': '1'}, 'size': 1778.296875},
                                 {'type': 'leaf', 'data': {'views': ['charts_orders_by_group'], 'activeView': 'charts_orders_by_group', 'id': '1'}, 'size': 1778.296875}
                             ], 'size': 707.53125}
    __grid_width__ = 1778.296875
    __grid_height__ = 707.53125
    __grid_orientation__ = "HORIZONTAL"
    __active_group__ = 1

    charts_orders_by_status = PanelComponent(component_type="charts",
                          name="Orders by Status",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Open Orders by Status",
                          description="Open Orders by Status",
                          columns=[],
                          chart_options={
    "title": {
        "text": "Order Status: Count and Value"
    },
    "tooltip": {
        "trigger": "axis"
    },
    "legend": {
        "data": ["Count", "Value"]
    },
    "xAxis": {
        "type": "category",
        "axisLabel": {
            "rotate": 45
        }
    },
    "yAxis": [
        {
            "type": "value",
            "name": "Count",
            "position": "left"
        },
        {
            "type": "value",
            "name": "Value",
            "position": "right"
        }
    ],
    "series": [
        {
            "type": "bar",
            "encode": {
                "x": "order_status",
                "y": "count"
            },
            "yAxisIndex": 0,
            "name": "Count"
        },
        {
            "type": "bar",
            "encode": {
                "x": "order_status",
                "y": "value"
            },
            "yAxisIndex": 1,
            "name": "Value"
        }
    ]
},
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
                          chart_options={
    "title": {
        "text": "Order Status: Count and Value"
    },
    "tooltip": {
        "trigger": "axis"
    },
    "legend": {
        "data": ["Count", "Value"]
    },
    "xAxis": {
        "type": "category",
        "axisLabel": {
            "rotate": 45
        }
    },
    "yAxis": [
        {
            "type": "value",
            "name": "Count",
            "position": "left"
        },
        {
            "type": "value",
            "name": "Value",
            "position": "right"
        }
    ],
    "series": [
        {
            "type": "bar",
            "encode": {
                "x": "group_name",
                "y": "count"
            },
            "yAxisIndex": 0,
            "name": "Count"
        },
        {
            "type": "bar",
            "encode": {
                "x": "group_name",
                "y": "value"
            },
            "yAxisIndex": 1,
            "name": "Value"
        }
    ]
},
                          content_component="mediator",
                          relations=[],
                          metadata={})

