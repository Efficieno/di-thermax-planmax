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
