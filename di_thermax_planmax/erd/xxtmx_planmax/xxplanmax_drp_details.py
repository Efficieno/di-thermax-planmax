from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxDrpDetails(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_drp_details"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 0, "ui_y_pos": 0, "colour": "#F2F3F5"}

    org_code: Mapped[str] = mapped_column('org_code', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_name: Mapped[str] = mapped_column('project_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_code: Mapped[str] = mapped_column('item_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_description: Mapped[str] = mapped_column('item_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity: Mapped[str] = mapped_column('quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_type: Mapped[str] = mapped_column('item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_type: Mapped[str] = mapped_column('order_type', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    job_name: Mapped[str] = mapped_column('job_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pr_num: Mapped[str] = mapped_column('pr_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    action: Mapped[str] = mapped_column('action', String, primary_key=False, info={"column_metadata": ColumnMetadata()})




