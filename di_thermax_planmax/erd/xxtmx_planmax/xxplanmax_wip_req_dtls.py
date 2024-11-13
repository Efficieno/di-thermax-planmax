from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxWipReqDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_wip_req_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 0, "ui_y_pos": 0, "colour": "#F2F3F5"}

    organization_code: Mapped[str] = mapped_column('organization_code', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    project_number: Mapped[str] = mapped_column('project_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_number: Mapped[str] = mapped_column('task_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_name: Mapped[str] = mapped_column('wip_entity_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item: Mapped[str] = mapped_column('assembly_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_type: Mapped[str] = mapped_column('wip_job_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_status: Mapped[str] = mapped_column('wip_job_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_class: Mapped[str] = mapped_column('wip_job_class', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_qty: Mapped[str] = mapped_column('wip_job_qty', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    department_id: Mapped[str] = mapped_column('department_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operation_seq_num: Mapped[str] = mapped_column('operation_seq_num', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_item: Mapped[str] = mapped_column('component_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_description: Mapped[str] = mapped_column('component_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_uom_code: Mapped[str] = mapped_column('primary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    required_quantity: Mapped[str] = mapped_column('required_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_issued: Mapped[str] = mapped_column('quantity_issued', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_pending: Mapped[str] = mapped_column('quantity_pending', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_oh_proj_locator: Mapped[str] = mapped_column('component_oh_proj_locator', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_reservation: Mapped[str] = mapped_column('component_reservation', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_pr: Mapped[str] = mapped_column('component_pr', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_po: Mapped[str] = mapped_column('component_po', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_type: Mapped[str] = mapped_column('item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_buyer: Mapped[str] = mapped_column('po_buyer', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer: Mapped[str] = mapped_column('customer', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_proj_plan_dt: Mapped[str] = mapped_column('curr_proj_plan_dt', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_make_buy_code: Mapped[str] = mapped_column('planning_make_buy_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})




