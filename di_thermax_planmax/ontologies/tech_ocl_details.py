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


class TechOCLDetails(ERDBase):
    # __table__ = (join(XxplanmaxHeaderDtls, XxplanmaxCustDtls, XxplanmaxHeaderDtls.XxplanmaxCustDtls_site_use_id.expression)
    #              .join(OrgOrganizationDefinitions, XxplanmaxHeaderDtls.OrgOrganizationDefinitions_organization_id.expression))
    # __table__ = XxplanmaxDrpDetails.__table__
    __table__ = join(XxtmxTechOclMstrTbl, XxtmxTechOclSpecsTbl, XxtmxTechOclMstrTbl.XxtmxTechOclSpecsTbl_otm_header_id.expression)
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}

    otm_header_id = column_property(XxtmxTechOclMstrTbl.otm_header_id, XxtmxTechOclSpecsTbl.otm_header_id)
    organization_id = column_property(XxtmxTechOclMstrTbl.organization_id, XxtmxTechOclSpecsTbl.organization_id)
    otm_tech_ocl_no = column_property(XxtmxTechOclMstrTbl.otm_tech_ocl_no)
    otm_tech_ocl_date = column_property(XxtmxTechOclMstrTbl.otm_tech_ocl_date)
    otm_tech_ocl_amd_no = column_property(XxtmxTechOclMstrTbl.otm_tech_ocl_amd_no)
    otm_tech_ocl_amd_date = column_property(XxtmxTechOclMstrTbl.otm_tech_ocl_amd_date)
    otm_sales_order_id = column_property(XxtmxTechOclMstrTbl.otm_sales_order_id)
    otm_sales_order_no = column_property(XxtmxTechOclMstrTbl.otm_sales_order_no)
    otm_model_family = column_property(XxtmxTechOclMstrTbl.otm_model_family)
    otm_model_no = column_property(XxtmxTechOclMstrTbl.otm_model_no)
    otm_item_code = column_property(XxtmxTechOclMstrTbl.otm_item_code)
    otm_item_id = column_property(XxtmxTechOclMstrTbl.otm_item_id)
    otm_status = column_property(XxtmxTechOclMstrTbl.otm_status)
    otm_authorized_by = column_property(XxtmxTechOclMstrTbl.otm_authorized_by)
    otm_authorized_date = column_property(XxtmxTechOclMstrTbl.otm_authorized_date)
    created_by = column_property(XxtmxTechOclMstrTbl.created_by, XxtmxTechOclSpecsTbl.created_by)
    creation_date = column_property(XxtmxTechOclMstrTbl.creation_date, XxtmxTechOclSpecsTbl.creation_date)
    last_updated_by = column_property(XxtmxTechOclMstrTbl.last_updated_by, XxtmxTechOclSpecsTbl.last_updated_by)
    last_update_date = column_property(XxtmxTechOclMstrTbl.last_update_date, XxtmxTechOclSpecsTbl.last_update_date)
    last_update_login = column_property(XxtmxTechOclMstrTbl.last_update_login, XxtmxTechOclSpecsTbl.last_update_login)
    otm_sales_order_line_id = column_property(XxtmxTechOclMstrTbl.otm_sales_order_line_id)
    otm_sales_order_line_num = column_property(XxtmxTechOclMstrTbl.otm_sales_order_line_num)

    otos_line_id = column_property(XxtmxTechOclSpecsTbl.otos_line_id)
    otos_der_model_no = column_property(XxtmxTechOclSpecsTbl.otos_der_model_no)
    otos_param_id = column_property(XxtmxTechOclSpecsTbl.otos_param_id)
    otos_section = column_property(XxtmxTechOclSpecsTbl.otos_section)
    otos_param_name = column_property(XxtmxTechOclSpecsTbl.otos_param_name)
    otos_srl_no = column_property(XxtmxTechOclSpecsTbl.otos_srl_no)
    otos_value_1 = column_property(XxtmxTechOclSpecsTbl.otos_value_1)
    otos_value_2 = column_property(XxtmxTechOclSpecsTbl.otos_value_2)
    otos_value_3 = column_property(XxtmxTechOclSpecsTbl.otos_value_3)
    otos_remark = column_property(XxtmxTechOclSpecsTbl.otos_remark)
