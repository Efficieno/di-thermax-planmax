from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxtmxTechOclMstrTbl(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxtmx_tech_ocl_mstr_tbl"
    __table_args__ = {"schema": "xxtmx", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 0, "ui_y_pos": 0, "colour": "#F2F3F5"}

    otm_header_id: Mapped[str] = mapped_column('otm_header_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_no: Mapped[str] = mapped_column('otm_tech_ocl_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_date: Mapped[str] = mapped_column('otm_tech_ocl_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_amd_no: Mapped[str] = mapped_column('otm_tech_ocl_amd_no', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_tech_ocl_amd_date: Mapped[str] = mapped_column('otm_tech_ocl_amd_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_sales_order_id: Mapped[str] = mapped_column('otm_sales_order_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_sales_order_no: Mapped[str] = mapped_column('otm_sales_order_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_model_family: Mapped[str] = mapped_column('otm_model_family', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_model_no: Mapped[str] = mapped_column('otm_model_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_item_code: Mapped[str] = mapped_column('otm_item_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_item_id: Mapped[str] = mapped_column('otm_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_status: Mapped[str] = mapped_column('otm_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_authorized_by: Mapped[str] = mapped_column('otm_authorized_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_authorized_date: Mapped[str] = mapped_column('otm_authorized_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_sales_order_line_id: Mapped[str] = mapped_column('otm_sales_order_line_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otm_sales_order_line_num: Mapped[str] = mapped_column('otm_sales_order_line_num', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})




