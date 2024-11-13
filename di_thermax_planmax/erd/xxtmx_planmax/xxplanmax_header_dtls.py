from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..apps.hr_operating_units import HrOperatingUnits
    from ..ont.oe_order_lines_all import OeOrderLinesAll
    from ..ont.oe_order_lines_all import OeOrderLinesAll
    from ..ont.oe_order_headers_all import OeOrderHeadersAll
    from ..xxtmx_planmax.xxplanmax_line_dtls import XxplanmaxLineDtls
    from ..xxtmx_planmax.xxplanmax_line_dtls import XxplanmaxLineDtls


class XxplanmaxHeaderDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_header_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -154.86566925048828, "ui_y_pos": 423.68280029296875, "colour": "#F2F3F5"}

    operating_unit_id: Mapped[str] = mapped_column('operating_unit_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    sales_order_header_id: Mapped[str] = mapped_column('sales_order_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_order_number: Mapped[str] = mapped_column('sales_order_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    model_line_id: Mapped[str] = mapped_column('model_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    model_line_number: Mapped[str] = mapped_column('model_line_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_type_id: Mapped[str] = mapped_column('order_type_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_name: Mapped[str] = mapped_column('group_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sub_group: Mapped[str] = mapped_column('sub_group', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_category: Mapped[str] = mapped_column('product_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_applicable: Mapped[str] = mapped_column('prn_applicable', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inspection_required: Mapped[str] = mapped_column('inspection_required', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number: Mapped[str] = mapped_column('project_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_nstd: Mapped[str] = mapped_column('std_nstd', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_item: Mapped[str] = mapped_column('sos_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_organization_id: Mapped[str] = mapped_column('mfg_organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_cust_required_date: Mapped[str] = mapped_column('orig_cust_required_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_cust_required_date: Mapped[str] = mapped_column('curr_cust_required_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_thx_commitment_date: Mapped[str] = mapped_column('orig_thx_commitment_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_thx_commitment_date: Mapped[str] = mapped_column('curr_thx_commitment_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ho_order_commited_to: Mapped[str] = mapped_column('ho_order_commited_to', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ho_order_so_header: Mapped[str] = mapped_column('ho_order_so_header', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ho_order_so_line: Mapped[str] = mapped_column('ho_order_so_line', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_no: Mapped[str] = mapped_column('oc_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_date: Mapped[str] = mapped_column('oc_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tech_clarity_date: Mapped[str] = mapped_column('tech_clarity_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engg_commt_dt: Mapped[str] = mapped_column('engg_commt_dt', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_status: Mapped[str] = mapped_column('oc_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_closure_date: Mapped[str] = mapped_column('oc_closure_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planned_invoice_dates: Mapped[str] = mapped_column('planned_invoice_dates', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planned_invoice_value: Mapped[str] = mapped_column('planned_invoice_value', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_folder_release_date: Mapped[str] = mapped_column('wip_folder_release_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commissioning_date: Mapped[str] = mapped_column('commissioning_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_release_date: Mapped[str] = mapped_column('site_release_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planner: Mapped[str] = mapped_column('planner', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tca: Mapped[str] = mapped_column('tca', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    send_email: Mapped[str] = mapped_column('send_email', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fg_month_change_remarks: Mapped[str] = mapped_column('fg_month_change_remarks', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shell_boiler_appr_auth: Mapped[str] = mapped_column('shell_boiler_appr_auth', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reason_for_otp: Mapped[str] = mapped_column('reason_for_otp', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    manual_ord_chg_status: Mapped[str] = mapped_column('manual_ord_chg_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_status: Mapped[str] = mapped_column('order_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    interface_status: Mapped[str] = mapped_column('interface_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    refresh_date: Mapped[str] = mapped_column('refresh_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_site_use_id: Mapped[str] = mapped_column('bill_site_use_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_cust_acct_site_id: Mapped[str] = mapped_column('bill_cust_acct_site_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_party_site_id: Mapped[str] = mapped_column('bill_party_site_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_party_id: Mapped[str] = mapped_column('bill_party_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_location_id: Mapped[str] = mapped_column('bill_location_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_site_use_id: Mapped[str] = mapped_column('ship_site_use_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_cust_acct_site_id: Mapped[str] = mapped_column('ship_cust_acct_site_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_party_site_id: Mapped[str] = mapped_column('ship_party_site_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_party_id: Mapped[str] = mapped_column('ship_party_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_location_id: Mapped[str] = mapped_column('ship_location_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_intake_status: Mapped[str] = mapped_column('order_intake_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_common_status: Mapped[str] = mapped_column('bom_common_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reflection_config_status: Mapped[str] = mapped_column('reflection_config_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mat_planning_status: Mapped[str] = mapped_column('mat_planning_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sourcing_status: Mapped[str] = mapped_column('sourcing_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commit_dates_status_mfg: Mapped[str] = mapped_column('commit_dates_status_mfg', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commit_dates_status_mat: Mapped[str] = mapped_column('commit_dates_status_mat', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_job_folder_status: Mapped[str] = mapped_column('mfg_job_folder_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_status: Mapped[str] = mapped_column('prn_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eol_mat_avail_status: Mapped[str] = mapped_column('eol_mat_avail_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_pur_mat_status: Mapped[str] = mapped_column('wip_pur_mat_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_segment1: Mapped[str] = mapped_column('project_segment1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_description: Mapped[str] = mapped_column('project_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_number: Mapped[str] = mapped_column('project_task_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_id: Mapped[str] = mapped_column('project_task_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_description: Mapped[str] = mapped_column('project_task_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operating_unit_name: Mapped[str] = mapped_column('operating_unit_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    region_of_order: Mapped[str] = mapped_column('region_of_order', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    type_of_order: Mapped[str] = mapped_column('type_of_order', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hdr_order_type: Mapped[str] = mapped_column('hdr_order_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hdr_booked_date: Mapped[str] = mapped_column('hdr_booked_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_no: Mapped[str] = mapped_column('otm_tech_ocl_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fuel: Mapped[str] = mapped_column('fuel', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pressure: Mapped[str] = mapped_column('pressure', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    special_instructions: Mapped[str] = mapped_column('special_instructions', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_model: Mapped[str] = mapped_column('product_model', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_date: Mapped[str] = mapped_column('ordered_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_currency: Mapped[str] = mapped_column('order_currency', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_unit_value: Mapped[str] = mapped_column('total_unit_value', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_rate: Mapped[str] = mapped_column('conversion_rate', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_unit_value_in_inr: Mapped[str] = mapped_column('total_unit_value_in_inr', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_customer_dely_date: Mapped[str] = mapped_column('prn_customer_dely_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_revised_dely_reqd_date: Mapped[str] = mapped_column('prn_revised_dely_reqd_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_number: Mapped[str] = mapped_column('prn_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_approved_date: Mapped[str] = mapped_column('prn_approved_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_pay: Mapped[str] = mapped_column('freight_pay', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inco_terms: Mapped[str] = mapped_column('inco_terms', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    abp_percent: Mapped[str] = mapped_column('abp_percent', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pgb_percent: Mapped[str] = mapped_column('pgb_percent', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bonus: Mapped[str] = mapped_column('bonus', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ld_applicable: Mapped[str] = mapped_column('ld_applicable', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    penalty: Mapped[str] = mapped_column('penalty', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    insurance_by: Mapped[str] = mapped_column('insurance_by', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_engineer: Mapped[str] = mapped_column('sales_engineer', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_header_id: Mapped[str] = mapped_column('otm_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_name: Mapped[str] = mapped_column('project_task_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    proj_specific_llbom: Mapped[str] = mapped_column('proj_specific_llbom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    llbom_release_date: Mapped[str] = mapped_column('llbom_release_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    llbom_pr: Mapped[str] = mapped_column('llbom_pr', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_number: Mapped[str] = mapped_column('di_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_date: Mapped[str] = mapped_column('di_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_value: Mapped[str] = mapped_column('di_value', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_freight: Mapped[str] = mapped_column('di_freight', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_recommended_transporter: Mapped[str] = mapped_column('di_recommended_transporter', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    di_transportation_scope: Mapped[str] = mapped_column('di_transportation_scope', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_invoice_no: Mapped[str] = mapped_column('last_invoice_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_invoice_date: Mapped[str] = mapped_column('last_invoice_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoiced_value: Mapped[str] = mapped_column('invoiced_value', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contractual_plan_otp: Mapped[str] = mapped_column('contractual_plan_otp', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    delivery_otp: Mapped[str] = mapped_column('delivery_otp', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_project_no: Mapped[str] = mapped_column('original_project_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rated_standard_man_hrs: Mapped[str] = mapped_column('rated_standard_man_hrs', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_commitment_date: Mapped[str] = mapped_column('mfg_commitment_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_eol_mech_date: Mapped[str] = mapped_column('plan_eol_mech_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_eol_ei_date: Mapped[str] = mapped_column('plan_eol_ei_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    folder_status: Mapped[str] = mapped_column('folder_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    regional_commercial: Mapped[str] = mapped_column('regional_commercial', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    actual_fg_date: Mapped[str] = mapped_column('actual_fg_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shop_subcontract: Mapped[str] = mapped_column('shop_subcontract', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oc_required: Mapped[str] = mapped_column('oc_required', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    suggested_plan_date: Mapped[str] = mapped_column('suggested_plan_date', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_attribute9: Mapped[str] = mapped_column('line_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_en1_revision: Mapped[str] = mapped_column('sos_en1_revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_mfg_revision: Mapped[str] = mapped_column('sos_mfg_revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_revision_date: Mapped[str] = mapped_column('sos_revision_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mfg_organization_code: Mapped[str] = mapped_column('mfg_organization_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_name: Mapped[str] = mapped_column('customer_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    account_number: Mapped[str] = mapped_column('account_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_creation_status: Mapped[str] = mapped_column('prn_creation_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    manual_order_status: Mapped[str] = mapped_column('manual_order_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_item: Mapped[str] = mapped_column('ordered_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_item_id: Mapped[str] = mapped_column('ordered_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sos_item_id: Mapped[str] = mapped_column('sos_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reflection_completion_date: Mapped[str] = mapped_column('reflection_completion_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    HrOperatingUnits_organization_id: Mapped["HrOperatingUnits"] = relationship(back_populates="XxplanmaxHeaderDtls_operating_unit_id", primaryjoin="HrOperatingUnits.organization_id==XxplanmaxHeaderDtls.operating_unit_id", foreign_keys="[HrOperatingUnits.organization_id]", viewonly=True)
        

    

    OeOrderLinesAll_header_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="XxplanmaxHeaderDtls_sales_order_header_id", primaryjoin="OeOrderLinesAll.header_id==XxplanmaxHeaderDtls.sales_order_header_id", foreign_keys="[OeOrderLinesAll.header_id]", viewonly=True)
        

    

    OeOrderLinesAll_line_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="XxplanmaxHeaderDtls_model_line_id", primaryjoin="OeOrderLinesAll.line_id==XxplanmaxHeaderDtls.model_line_id", foreign_keys="[OeOrderLinesAll.line_id]", viewonly=True)
        

    

    OeOrderHeadersAll_header_id: Mapped["OeOrderHeadersAll"] = relationship(back_populates="XxplanmaxHeaderDtls_sales_order_header_id", primaryjoin="OeOrderHeadersAll.header_id==XxplanmaxHeaderDtls.sales_order_header_id", foreign_keys="[OeOrderHeadersAll.header_id]", viewonly=True)
        

    

    XxplanmaxLineDtls_reference_line_id: Mapped["XxplanmaxLineDtls"] = relationship(back_populates="XxplanmaxHeaderDtls_model_line_id", primaryjoin="XxplanmaxLineDtls.reference_line_id==XxplanmaxHeaderDtls.model_line_id", foreign_keys="[XxplanmaxLineDtls.reference_line_id]", viewonly=True)
        

    

    XxplanmaxLineDtls_sales_order_header_id: Mapped["XxplanmaxLineDtls"] = relationship(back_populates="XxplanmaxHeaderDtls_sales_order_header_id", primaryjoin="XxplanmaxLineDtls.sales_order_header_id==XxplanmaxHeaderDtls.sales_order_header_id", foreign_keys="[XxplanmaxLineDtls.sales_order_header_id]", viewonly=True)



