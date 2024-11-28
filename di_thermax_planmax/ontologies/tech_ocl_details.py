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
    __table__ = XxplanmaxDrpDetails.__table__
    # __table__ = join(XxplanmaxHeaderDtls, XxplanmaxCalender, XxplanmaxHeaderDtls.XxplanmaxCalender_day_id.expression)
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}

