from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxWipProjDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_wip_proj_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -737.5357666015625, "ui_y_pos": 914.0802612304688, "colour": "#F2F3F5"}

    organization_code: Mapped[str] = mapped_column('organization_code', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number: Mapped[str] = mapped_column('project_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_segment1: Mapped[str] = mapped_column('project_segment1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_number: Mapped[str] = mapped_column('task_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_name: Mapped[str] = mapped_column('wip_entity_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_item_id: Mapped[str] = mapped_column('primary_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item: Mapped[str] = mapped_column('assembly_item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_type: Mapped[str] = mapped_column('wip_job_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_status: Mapped[str] = mapped_column('wip_job_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_class: Mapped[str] = mapped_column('wip_job_class', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_job_qty: Mapped[str] = mapped_column('wip_job_qty', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    net_quantity: Mapped[str] = mapped_column('net_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_completed: Mapped[str] = mapped_column('quantity_completed', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_start_date: Mapped[str] = mapped_column('scheduled_start_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_completion_date: Mapped[str] = mapped_column('scheduled_completion_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_released: Mapped[str] = mapped_column('date_released', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_completed: Mapped[str] = mapped_column('date_completed', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_closed: Mapped[str] = mapped_column('date_closed', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assembly_item_type: Mapped[str] = mapped_column('assembly_item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})




