from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class QProductionReleaseNoteStV(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "q_production_release_note_st_v"
    __table_args__ = {"schema": "apps", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -1201.8595423679058, "ui_y_pos": 407.37632009256833, "colour": "#F2F3F5"}

    plan_id: Mapped[str] = mapped_column('plan_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    plan_name: Mapped[str] = mapped_column('plan_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_name: Mapped[str] = mapped_column('organization_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    collection_id: Mapped[str] = mapped_column('collection_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    occurrence: Mapped[str] = mapped_column('occurrence', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by_id: Mapped[str] = mapped_column('last_updated_by_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by_id: Mapped[str] = mapped_column('created_by_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    so_header_id: Mapped[str] = mapped_column('so_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_order_number: Mapped[str] = mapped_column('sales_order_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_id: Mapped[str] = mapped_column('customer_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer: Mapped[str] = mapped_column('customer', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_number_so: Mapped[str] = mapped_column('project_number_so', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    region_zone: Mapped[str] = mapped_column('region_zone', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    area_country: Mapped[str] = mapped_column('area_country', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ch_product_type: Mapped[str] = mapped_column('ch_product_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_route: Mapped[str] = mapped_column('group_route', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_dely_date: Mapped[str] = mapped_column('customer_dely_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_number: Mapped[str] = mapped_column('prn_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revised_dely_reqd_date: Mapped[str] = mapped_column('revised_dely_reqd_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_status: Mapped[str] = mapped_column('prn_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_approved_date: Mapped[str] = mapped_column('prn_approved_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    remarks: Mapped[str] = mapped_column('remarks', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reporting_employee: Mapped[str] = mapped_column('reporting_employee', String, primary_key=False, info={"column_metadata": ColumnMetadata()})




