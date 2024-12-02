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
from di_thermax_planmax.erd.apps.q_production_release_note_st_v import QProductionReleaseNoteStV


class QPPRNDetails(ERDBase):
  
    __table__ = QProductionReleaseNoteStV.__table__
    # __table__ = join(XxplanmaxHeaderDtls, XxplanmaxCalender, XxplanmaxHeaderDtls.XxplanmaxCalender_day_id.expression)
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}  
  
    plan_id = column_property(QProductionReleaseNoteStV.plan_id)
    plan_name = column_property(QProductionReleaseNoteStV.plan_name)
    organization_id = column_property(QProductionReleaseNoteStV.organization_id)
    organization_name = column_property(QProductionReleaseNoteStV.organization_name)
    collection_id = column_property(QProductionReleaseNoteStV.collection_id)
    occurrence = column_property(QProductionReleaseNoteStV.occurrence)
    last_update_date = column_property(QProductionReleaseNoteStV.last_update_date)
    last_updated_by_id = column_property(QProductionReleaseNoteStV.last_updated_by_id)
    last_updated_by = column_property(QProductionReleaseNoteStV.last_updated_by)
    creation_date = column_property(QProductionReleaseNoteStV.creation_date)
    created_by_id = column_property(QProductionReleaseNoteStV.created_by_id)
    created_by = column_property(QProductionReleaseNoteStV.created_by)
    last_update_login = column_property(QProductionReleaseNoteStV.last_update_login)
    so_header_id = column_property(QProductionReleaseNoteStV.so_header_id)
    sales_order_number = column_property(QProductionReleaseNoteStV.sales_order_number)
    customer_id = column_property(QProductionReleaseNoteStV.customer_id)
    customer = column_property(QProductionReleaseNoteStV.customer)
    project_number_so = column_property(QProductionReleaseNoteStV.project_number_so)
    region_zone = column_property(QProductionReleaseNoteStV.region_zone)
    area_country = column_property(QProductionReleaseNoteStV.area_country)
    ch_product_type = column_property(QProductionReleaseNoteStV.ch_product_type)
    group_route = column_property(QProductionReleaseNoteStV.group_route)
    customer_dely_date = column_property(QProductionReleaseNoteStV.customer_dely_date)
    prn_number = column_property(QProductionReleaseNoteStV.prn_number)
    revised_dely_reqd_date = column_property(QProductionReleaseNoteStV.revised_dely_reqd_date)
    prn_status = column_property(QProductionReleaseNoteStV.prn_status)
    prn_approved_date = column_property(QProductionReleaseNoteStV.prn_approved_date)
    remarks = column_property(QProductionReleaseNoteStV.remarks)
    reporting_employee = column_property(QProductionReleaseNoteStV.reporting_employee)
