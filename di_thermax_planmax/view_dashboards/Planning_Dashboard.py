from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
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

    __grid_root_element__ = {'type': 'branch', 'data': [
        {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_orders_by_status'], 'activeView': 'charts_orders_by_status', 'id': '1'}, 'size': 372}], 'size': 1472}, {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_JZSFQImkw'], 'activeView': 'metrics_JZSFQImkw', 'id': '4'}, 'size': 138}, {'type': 'leaf', 'data': {'views': ['metrics_MGiwGCl28'], 'activeView': 'metrics_MGiwGCl28', 'id': '5'}, 'size': 156}, {'type': 'leaf', 'data': {'views': ['metrics_w1T41TC2A'], 'activeView': 'metrics_w1T41TC2A', 'id': '6'}, 'size': 170}, {'type': 'leaf', 'data': {'views': ['charts_orders_by_group'], 'activeView': 'charts_orders_by_group', 'id': '3'}, 'size': 281.46875}], 'size': 314.09375}], 'size': 745.46875}
    __grid_width__ = 1786.09375
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
                          metadata={},
                          drill_downs={0: "PlanmaxHeaders.group_name",
                                       1: "PlanmaxHeaders.sub_group"})

    table_order_header_details = PanelComponent(component_type="tables",
                                                name="Order Header Details",
                                                query="Select(PlanMaxHeaders.sales_order_header_id,PlanMaxHeaders.model_line_id,PlanMaxHeaders.otm_header_id,PlanMaxHeaders.product_category,PlanMaxHeaders.region_of_order,PlanMaxHeaders.customer_name,PlanMaxHeaders.sales_order_number,PlanMaxHeaders.project_segment1,PlanMaxHeaders.orig_cust_required_date,PlanMaxHeaders.curr_cust_required_date,PlanMaxHeaders.curr_thx_commitment_date,PlanMaxHeaders.mfg_organization_code,PlanMaxHeaders.std_nstd,PlanMaxHeaders.sos_item,PlanMaxHeaders.product_model,PlanMaxHeaders.ld_applicable,PlanMaxHeaders.order_status,PlanMaxHeaders.wip_folder_release_date,PlanMaxHeaders.mfg_job_folder_status,PlanMaxHeaders.remarks,PlanMaxHeaders.rated_standard_man_hrs,PlanMaxHeaders.reason_for_otp,PlanMaxHeaders.prn_applicable,PlanMaxHeaders.oc_status,PlanMaxHeaders.oc_closure_date,PlanMaxHeaders.plan_eol_mech_date,PlanMaxHeaders.plan_eol_ei_date,PlanMaxHeaders.mfg_commitment_date,PlanMaxHeaders.planner,PlanMaxHeaders.model_line_number,(PlanMaxHeaders.total_unit_value / 100000).label('Total Unit value'),PlanMaxHeaders.order_intake_status,PlanMaxHeaders.prn_creation_status,PlanMaxHeaders.bom_common_status).filter(PlanMaxHeaders.order_status.not_in(['CLOSED', 'CANCELLED', 'ENTERED'])).filter(PlanMaxHeaders.group_name != 'HO')",
                                                data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                                                header="Order Header Details",
                                                description="Order Header Details",
                                                columns=[ColumnProperty(column=OrderHeaders.organization_code, display_name="Org Code"),
                                                         ColumnProperty(column=OrderHeaders.order_type_id, display_name="Order Type ID", invisible=True),
                                                         ColumnProperty(column=OrderHeaders.order_number, display_name="Order Number"),
                                                         ColumnProperty(column=OrderHeaders.version_number, display_name="Version Number")],
                                                chart_options={},
                                                content_component="mediator",
                                                relations=[],
                                                inline_actions=None,
                                                actions=[]
                                                )
    # charts_orders_by_group_bar = PanelComponent(component_type="charts",
    #                       name="Orders by Status",
    #                       query="Select(PlanmaxHeaders.group_name, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.group_name)",
    #                       data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
    #                       header="Open Orders by Status",
    #                       description="Open Orders by Status",
    #                       columns=[],
    #                       chart_options={'legend': {'data': ['Count', 'Value']}, 'series': [{'encode': {'x': 'group_name', 'y': 'count'}, 'name': 'Count', 'type': 'bar', 'yAxisIndex': 0}, {'encode': {'x': 'group_name', 'y': 'value'}, 'name': 'Value', 'type': 'line', 'yAxisIndex': 1}], 'title': {'text': 'Orders by Status'}, 'tooltip': {'trigger': 'axis'}, 'xAxis': {'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]},
    #                       content_component="mediator",
    #                       relations=[],
    #                       metadata={})
    charts_orders_by_group = PanelComponent(component_type="charts",
                          name="Orders by Group",
                          query="Select(PlanmaxHeaders.group_name, func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.group_name)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Orders by Group",
                          description="Orders by Group",
                          columns=[],
                          chart_options={'legend': {'data': ['DOM', 'HO', 'EXP'], 'left': 'left', 'orient': 'vertical'}, 'series': [{'encode': {'itemName': 'group_name', 'value': 'value'}, 'label': {'formatter': '{b}: {c} ({d}%)', 'show': True}, 'radius': '50%', 'type': 'pie'}], 'title': {'left': 'center', 'subtext': 'Value Breakdown', 'text': 'Group Name Distribution'}, 'tooltip': {'formatter': '{b}: {c} ({d}%)', 'trigger': 'item'}},
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
                          metadata={'additional_field_visible': True, 'display': '1000', 'font_size': '2', 'font_style': ['bold']})
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
                          metadata={'additional_field_visible': True, 'display': '1000', 'font_size': '2', 'font_style': ['bold']})
