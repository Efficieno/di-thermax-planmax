from efficieno.components.dashboard_objects import PanelComponent, Dashboard, ColumnProperty
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.order_lines import OrderLines
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.order_lines import OrderLines
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders
from di_thermax_planmax.ontologies.planmax_headers import PlanmaxHeaders


class PlanningDashboard(Dashboard):
    __dashboard_name__ = "Planning Dashboard"
    __dashboard_description__ = "Planning Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_JZSFQImkw'], 'activeView': 'metrics_JZSFQImkw', 'id': '7'}, 'size': 595}, {'type': 'leaf', 'data': {'views': ['metrics_MGiwGCl28'], 'activeView': 'metrics_MGiwGCl28', 'id': '5'}, 'size': 595}, {'type': 'leaf', 'data': {'views': ['metrics_w1T41TC2A'], 'activeView': 'metrics_w1T41TC2A', 'id': '6'}, 'size': 596.09375}], 'size': 155}, {'type': 'branch', 'data': [{'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_orders_by_status'], 'activeView': 'charts_orders_by_status', 'id': '1'}, 'size': 590.46875}], 'size': 1209}, {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['charts_orders_by_group'], 'activeView': 'charts_orders_by_group', 'id': '3'}, 'size': 590.46875}, {'type': 'leaf', 'data': {'views': ['table_order_header_details'], 'activeView': 'table_order_header_details', 'id': '10'}, 'size': 372, 'visible': False}], 'size': 577.09375}], 'size': 590.46875}], 'size': 1786.09375}
    __grid_width__ = 1786.09375
    __grid_height__ = 745.46875
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 6

    charts_orders_by_status = PanelComponent(component_type="charts",
                          name="Orders by Status",
                          query="Select(PlanmaxHeaders.order_status, func.count(PlanmaxHeaders.sales_order_header_id).label('count'), func.sum(PlanmaxHeaders.total_unit_value_in_inr).label('value')).group_by(PlanmaxHeaders.order_status)",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Open Orders by Status",
                          description="Open Orders by Status",
                          columns=[],
                          chart_options={'legend': {'data': ['Count', 'Value']}, 'series': [{'encode': {'x': 'order_status', 'y': 'count'}, 'name': 'Count', 'type': 'bar', 'yAxisIndex': 0}, {'encode': {'x': 'order_status', 'y': 'value'}, 'name': 'Value', 'type': 'line', 'yAxisIndex': 1}], 'title': {'text': 'Orders by Status'}, 'tooltip': {'trigger': 'axis'}, 'xAxis': {'type': 'category'}, 'yAxis': [{'name': 'Count', 'position': 'left', 'type': 'value'}, {'name': 'Value', 'position': 'right', 'type': 'value'}]},
                          content_component="mediator",
                          relations=[{'component_name': 'table_order_header_details', 'relation_name': 'Order Header Details', 'relations': [{'destination_class_name': 'PlanmaxHeaders', 'destination_column_name': 'order_status', 'source_class_name': 'PlanmaxHeaders', 'source_column_name': 'order_status'}]}],
                          metadata={})
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
    table_order_header_details = PanelComponent(component_type="tables",
                          name="Order Header Details",
                          query="Select(PlanmaxHeaders.sales_order_header_id,PlanmaxHeaders.model_line_id,PlanmaxHeaders.otm_header_id,PlanmaxHeaders.product_category,PlanmaxHeaders.region_of_order,PlanmaxHeaders.group_name, PlanmaxHeaders.sub_group, PlanmaxHeaders.customer_name,PlanmaxHeaders.sales_order_number,PlanmaxHeaders.project_segment1,PlanmaxHeaders.orig_cust_required_date,PlanmaxHeaders.curr_cust_required_date,PlanmaxHeaders.curr_thx_commitment_date,PlanmaxHeaders.mfg_organization_code,PlanmaxHeaders.std_nstd,PlanmaxHeaders.sos_item,PlanmaxHeaders.product_model,PlanmaxHeaders.ld_applicable,PlanmaxHeaders.order_status,PlanmaxHeaders.wip_folder_release_date,PlanmaxHeaders.mfg_job_folder_status,PlanmaxHeaders.rated_standard_man_hrs,PlanmaxHeaders.reason_for_otp,PlanmaxHeaders.prn_applicable,PlanmaxHeaders.oc_status,PlanmaxHeaders.oc_closure_date,PlanmaxHeaders.plan_eol_mech_date,PlanmaxHeaders.plan_eol_ei_date,PlanmaxHeaders.mfg_commitment_date,PlanmaxHeaders.planner,PlanmaxHeaders.model_line_number,PlanmaxHeaders.total_unit_value,PlanmaxHeaders.order_intake_status,PlanmaxHeaders.prn_creation_status,PlanmaxHeaders.bom_common_status).filter(PlanmaxHeaders.order_status.not_in(['CLOSED', 'CANCELLED', 'ENTERED'])).filter(PlanmaxHeaders.group_name != 'HO')",
                          data_objects={'PlanmaxHeaders': 'di_thermax_planmax.ontologies.planmax_headers'},
                          header="Order Header Details",
                          description="Order Header Details",
                          columns=[
                            ColumnProperty(column=PlanmaxHeaders.sales_order_header_id, display_name="Header ID"),
                            ColumnProperty(column=PlanmaxHeaders.model_line_id, display_name="Line ID"),
                            ColumnProperty(column=PlanmaxHeaders.otm_header_id, display_name="otm_header_id"),
                            ColumnProperty(column=PlanmaxHeaders.product_category, display_name="Product Category"),
                            ColumnProperty(column=PlanmaxHeaders.region_of_order, display_name="region_of_order"),
                            ColumnProperty(column=PlanmaxHeaders.group_name, display_name="group_name"),
                            ColumnProperty(column=PlanmaxHeaders.sub_group, display_name="sub_group"),
                            ColumnProperty(column=PlanmaxHeaders.customer_name, display_name="customer_name"),
                            ColumnProperty(column=PlanmaxHeaders.sales_order_number, display_name="sales_order_number"),
                            ColumnProperty(column=PlanmaxHeaders.project_segment1, display_name="project_segment1"),
                            ColumnProperty(column=PlanmaxHeaders.orig_cust_required_date, display_name="orig_cust_required_date"),
                            ColumnProperty(column=PlanmaxHeaders.curr_cust_required_date, display_name="curr_cust_required_date"),
                            ColumnProperty(column=PlanmaxHeaders.curr_thx_commitment_date, display_name="curr_thx_commitment_date"),
                            ColumnProperty(column=PlanmaxHeaders.mfg_organization_code, display_name="mfg_organization_code"),
                            ColumnProperty(column=PlanmaxHeaders.std_nstd, display_name="std_nstd"),
                            ColumnProperty(column=PlanmaxHeaders.sos_item, display_name="sos_item"),
                            ColumnProperty(column=PlanmaxHeaders.product_model, display_name="product_model"),
                            ColumnProperty(column=PlanmaxHeaders.ld_applicable, display_name="ld_applicable"),
                            ColumnProperty(column=PlanmaxHeaders.order_status, display_name="order_status"),
                            ColumnProperty(column=PlanmaxHeaders.wip_folder_release_date, display_name="wip_folder_release_date"),
                            ColumnProperty(column=PlanmaxHeaders.mfg_job_folder_status, display_name="mfg_job_folder_status"),
                            ColumnProperty(column=PlanmaxHeaders.rated_standard_man_hrs, display_name="rated_standard_man_hrs"),
                            ColumnProperty(column=PlanmaxHeaders.reason_for_otp, display_name="reason_for_otp"),
                            ColumnProperty(column=PlanmaxHeaders.prn_applicable, display_name="prn_applicable"),
                            ColumnProperty(column=PlanmaxHeaders.oc_status, display_name="oc_status"),
                            ColumnProperty(column=PlanmaxHeaders.oc_closure_date, display_name="oc_closure_date"),
                            ColumnProperty(column=PlanmaxHeaders.plan_eol_mech_date, display_name="plan_eol_mech_date"),
                            ColumnProperty(column=PlanmaxHeaders.plan_eol_ei_date, display_name="plan_eol_ei_date"),
                            ColumnProperty(column=PlanmaxHeaders.mfg_commitment_date, display_name="mfg_commitment_date"),
                            ColumnProperty(column=PlanmaxHeaders.planner, display_name="planner"),
                            ColumnProperty(column=PlanmaxHeaders.model_line_number, display_name="model_line_number"),
                            ColumnProperty(column=PlanmaxHeaders.total_unit_value, display_name="total_unit_value"),
                            ColumnProperty(column=PlanmaxHeaders.order_intake_status, display_name="order_intake_status"),
                            ColumnProperty(column=PlanmaxHeaders.prn_creation_status, display_name="prn_creation_status"),
                            ColumnProperty(column=PlanmaxHeaders.bom_common_status, display_name="bom_common_status"),
                          ],
                          chart_options={},
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
