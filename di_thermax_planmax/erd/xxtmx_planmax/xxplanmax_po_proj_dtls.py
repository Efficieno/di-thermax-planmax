from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxPoProjDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_po_proj_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 0, "ui_y_pos": 0, "colour": "#F2F3F5"}

    org_id: Mapped[str] = mapped_column('org_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_number: Mapped[str] = mapped_column('po_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_num: Mapped[str] = mapped_column('po_line_num', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_id: Mapped[str] = mapped_column('item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_item_uom: Mapped[str] = mapped_column('po_item_uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_auth_status: Mapped[str] = mapped_column('po_auth_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_approved_date: Mapped[str] = mapped_column('po_approved_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_quantity: Mapped[str] = mapped_column('po_line_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_received: Mapped[str] = mapped_column('quantity_received', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_accepted: Mapped[str] = mapped_column('quantity_accepted', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_header_id: Mapped[str] = mapped_column('po_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_id: Mapped[str] = mapped_column('po_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_location_id: Mapped[str] = mapped_column('line_location_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_distribution_id: Mapped[str] = mapped_column('po_distribution_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requisition_header_id: Mapped[str] = mapped_column('requisition_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_preparer_id: Mapped[str] = mapped_column('req_preparer_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_number: Mapped[str] = mapped_column('req_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_auth_status: Mapped[str] = mapped_column('req_auth_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_type_lookup_code: Mapped[str] = mapped_column('req_type_lookup_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_interface_source_code: Mapped[str] = mapped_column('req_interface_source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_approved_date: Mapped[str] = mapped_column('req_approved_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requisition_line_id: Mapped[str] = mapped_column('requisition_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    category_id: Mapped[str] = mapped_column('category_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    suggested_buyer_id: Mapped[str] = mapped_column('suggested_buyer_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_distribution_id: Mapped[str] = mapped_column('req_distribution_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_line_num: Mapped[str] = mapped_column('req_line_num', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_item_id: Mapped[str] = mapped_column('req_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_item_uom: Mapped[str] = mapped_column('req_item_uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_quantity: Mapped[str] = mapped_column('req_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_source_type_code: Mapped[str] = mapped_column('req_source_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_item_revision: Mapped[str] = mapped_column('req_item_revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_need_by_date: Mapped[str] = mapped_column('req_need_by_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_destination_type_code: Mapped[str] = mapped_column('req_destination_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_unit_price: Mapped[str] = mapped_column('req_unit_price', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_quantity_cancelled: Mapped[str] = mapped_column('req_quantity_cancelled', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_cancel_date: Mapped[str] = mapped_column('req_cancel_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_cancel_reason: Mapped[str] = mapped_column('req_cancel_reason', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_closed_code: Mapped[str] = mapped_column('req_closed_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_currency_code: Mapped[str] = mapped_column('req_currency_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_currency_code: Mapped[str] = mapped_column('po_currency_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_rate_type: Mapped[str] = mapped_column('po_rate_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_rate_date: Mapped[str] = mapped_column('po_rate_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_rate: Mapped[str] = mapped_column('po_rate', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_hdr_comments: Mapped[str] = mapped_column('po_hdr_comments', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_hdr_closed_date: Mapped[str] = mapped_column('po_hdr_closed_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_hdr_closed_code: Mapped[str] = mapped_column('po_hdr_closed_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_cancel_flag: Mapped[str] = mapped_column('po_line_cancel_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_cancelled_by: Mapped[str] = mapped_column('po_line_cancelled_by', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_cancel_date: Mapped[str] = mapped_column('po_line_cancel_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_cancel_reason: Mapped[str] = mapped_column('po_line_cancel_reason', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_closed_code: Mapped[str] = mapped_column('po_line_closed_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_closed_date: Mapped[str] = mapped_column('po_line_closed_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_closed_reason: Mapped[str] = mapped_column('po_line_closed_reason', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_closed_by: Mapped[str] = mapped_column('po_line_closed_by', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    need_by_date: Mapped[str] = mapped_column('need_by_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    promised_date: Mapped[str] = mapped_column('promised_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_name: Mapped[str] = mapped_column('vendor_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_number: Mapped[str] = mapped_column('vendor_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_site_code: Mapped[str] = mapped_column('vendor_site_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_id: Mapped[str] = mapped_column('vendor_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_site_id: Mapped[str] = mapped_column('vendor_site_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_name: Mapped[str] = mapped_column('project_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_segment1: Mapped[str] = mapped_column('project_segment1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_description: Mapped[str] = mapped_column('project_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_number: Mapped[str] = mapped_column('project_task_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_name: Mapped[str] = mapped_column('project_task_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_task_description: Mapped[str] = mapped_column('project_task_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})




