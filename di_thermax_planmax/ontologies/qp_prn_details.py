from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime, join
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from efficieno.components.erd_objects import ERDBase, ColumnMetadata

from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_header_dtls import XxplanmaxHeaderDtls
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_cust_dtls import XxplanmaxCustDtls
from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_calender import XxplanmaxCalender
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_drp_details import XxplanmaxDrpDetails
from di_thermax_planmax.erd.xxtmx.xxtmx_tech_ocl_mstr_tbl import XxtmxTechOclMstrTbl
from di_thermax_planmax.erd.xxtmx.xxtmx_tech_ocl_specs_tbl import XxtmxTechOclSpecsTbl
from di_thermax_planmax.apps.q_production_release_note_st_v import QProductionReleaseNoteStV


class QPPRNDetails(ERDBase):
  
    __table__ = QProductionReleaseNoteStV.__table__
    # __table__ = join(XxplanmaxHeaderDtls, XxplanmaxCalender, XxplanmaxHeaderDtls.XxplanmaxCalender_day_id.expression)
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}  
  
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
