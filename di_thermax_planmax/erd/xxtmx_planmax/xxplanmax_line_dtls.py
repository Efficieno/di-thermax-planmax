from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxLineDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_line_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 106.38436889648438, "ui_y_pos": 556.7813720703125, "colour": "#F2F3F5"}

    sales_order_header_id: Mapped[str] = mapped_column('sales_order_header_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    sales_order_header: Mapped[str] = mapped_column('sales_order_header', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_order_line_id: Mapped[str] = mapped_column('sales_order_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_order_line: Mapped[str] = mapped_column('sales_order_line', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line_id: Mapped[str] = mapped_column('reference_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line: Mapped[str] = mapped_column('reference_line', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_sequence_id: Mapped[str] = mapped_column('bill_sequence_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_implementation_date: Mapped[str] = mapped_column('bom_implementation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_notice: Mapped[str] = mapped_column('change_notice', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    common_bill_sequence_id: Mapped[str] = mapped_column('common_bill_sequence_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    common_organization_id: Mapped[str] = mapped_column('common_organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item_id: Mapped[str] = mapped_column('assembly_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item: Mapped[str] = mapped_column('assembly_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item_type: Mapped[str] = mapped_column('assembly_item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_level: Mapped[str] = mapped_column('plan_level', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    effectivity_date: Mapped[str] = mapped_column('effectivity_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    disable_date: Mapped[str] = mapped_column('disable_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_num: Mapped[str] = mapped_column('item_num', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operation_seq_num: Mapped[str] = mapped_column('operation_seq_num', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    implementation_date: Mapped[str] = mapped_column('implementation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_code: Mapped[str] = mapped_column('component_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item_id: Mapped[str] = mapped_column('component_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item: Mapped[str] = mapped_column('component_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item_revision_war: Mapped[str] = mapped_column('component_item_revision_war', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item_revision_en1: Mapped[str] = mapped_column('component_item_revision_en1', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item_type: Mapped[str] = mapped_column('component_item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_quantity: Mapped[str] = mapped_column('component_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engg_org_exists: Mapped[str] = mapped_column('engg_org_exists', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    warehouse_org_exists: Mapped[str] = mapped_column('warehouse_org_exists', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    extended_quantity: Mapped[str] = mapped_column('extended_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_shippable_item_flag: Mapped[str] = mapped_column('component_shippable_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_make_buy_code: Mapped[str] = mapped_column('planning_make_buy_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_unit_of_measure: Mapped[str] = mapped_column('primary_unit_of_measure', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_cost: Mapped[str] = mapped_column('item_cost', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_item_type: Mapped[str] = mapped_column('line_item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_item_sub_type: Mapped[str] = mapped_column('line_item_sub_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number: Mapped[str] = mapped_column('project_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    show_on_view: Mapped[str] = mapped_column('show_on_view', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_line_item_type: Mapped[str] = mapped_column('order_line_item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shippable_flag: Mapped[str] = mapped_column('shippable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_number: Mapped[str] = mapped_column('po_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_header_id: Mapped[str] = mapped_column('po_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_num: Mapped[str] = mapped_column('po_line_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_id: Mapped[str] = mapped_column('po_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_location_id: Mapped[str] = mapped_column('po_line_location_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_distribution_id: Mapped[str] = mapped_column('po_distribution_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_auth_status: Mapped[str] = mapped_column('po_auth_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_approved_date: Mapped[str] = mapped_column('po_approved_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_qty: Mapped[str] = mapped_column('po_line_qty', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_qty_received: Mapped[str] = mapped_column('po_qty_received', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_qty_accepted: Mapped[str] = mapped_column('po_qty_accepted', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requisition_header_id: Mapped[str] = mapped_column('requisition_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_preparer_id: Mapped[str] = mapped_column('req_preparer_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_number: Mapped[str] = mapped_column('req_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_auth_status: Mapped[str] = mapped_column('req_auth_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_approved_date: Mapped[str] = mapped_column('req_approved_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requisition_line_id: Mapped[str] = mapped_column('requisition_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    suggested_buyer_id: Mapped[str] = mapped_column('suggested_buyer_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_distribution_id: Mapped[str] = mapped_column('req_distribution_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_name: Mapped[str] = mapped_column('wip_entity_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_type: Mapped[str] = mapped_column('wip_job_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_status: Mapped[str] = mapped_column('wip_job_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_class: Mapped[str] = mapped_column('wip_job_class', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_qty: Mapped[str] = mapped_column('wip_job_qty', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_onhand_qty: Mapped[str] = mapped_column('curr_onhand_qty', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_required_quantity: Mapped[str] = mapped_column('wip_required_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_quantity_issued: Mapped[str] = mapped_column('wip_quantity_issued', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_quantity_pending: Mapped[str] = mapped_column('wip_quantity_pending', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_onhand: Mapped[str] = mapped_column('wip_onhand', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_reservation: Mapped[str] = mapped_column('wip_reservation', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_explosion_date: Mapped[str] = mapped_column('bom_explosion_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})




