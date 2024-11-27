from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty, FilterField, FilterComponent
from sqlalchemy import Integer, Select, bindparam, String
from di_thermax_planmax.ontologies.order_headers import OrderHeaders
from di_thermax_planmax.ontologies.order_headers import OrderHeaders
from di_thermax_planmax.ontologies.order_headers import OrderHeaders


class PlanningBasic(Dashboard):
    __dashboard_name__ = "planning_basic"
    __dashboard_description__ = "planning basic dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['panel_IP1_fhJ_R'], 'activeView': 'panel_IP1_fhJ_R', 'id': '1'}, 'size': 259}, {'type': 'leaf', 'data': {'views': ['panel__NXT8QrunU'], 'activeView': 'panel__NXT8QrunU', 'id': '2'}, 'size': 259}, {'type': 'leaf', 'data': {'views': ['panel_SrQ6YWB5ry'], 'activeView': 'panel_SrQ6YWB5ry', 'id': '3'}, 'size': 258.015625}], 'size': 1787.953125}
    __grid_width__ = 1787.953125
    __grid_height__ = 776.015625
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 1

    panel_IP1_fhJ_R = PanelComponent(component_type="metrics",
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
