from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime, join
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from efficieno.components.erd_objects import ERDBase, ColumnMetadata

from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_header_dtls import XxplanmaxHeaderDtls
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_cust_dtls import XxplanmaxCustDtls
from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_calender import XxplanmaxCalender
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_drp_details import XxplanmaxDrpDetails


class PlanmaxDRPDetails(ERDBase):
    # __table__ = (join(XxplanmaxHeaderDtls, XxplanmaxCustDtls, XxplanmaxHeaderDtls.XxplanmaxCustDtls_site_use_id.expression)
    #              .join(OrgOrganizationDefinitions, XxplanmaxHeaderDtls.OrgOrganizationDefinitions_organization_id.expression))
    __table__ = XxplanmaxDrpDetails.__table__
    # __table__ = join(XxplanmaxHeaderDtls, XxplanmaxCalender, XxplanmaxHeaderDtls.XxplanmaxCalender_day_id.expression)
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}

    org_code = column_property(XxplanmaxDrpDetails.org_code)
    organization_id = column_property(XxplanmaxDrpDetails.organization_id)
    project_id = column_property(XxplanmaxDrpDetails.project_id)
    project_name = column_property(XxplanmaxDrpDetails.project_name)
    item_code = column_property(XxplanmaxDrpDetails.item_code)
    item_description = column_property(XxplanmaxDrpDetails.item_description)
    quantity = column_property(XxplanmaxDrpDetails.quantity)
    item_type = column_property(XxplanmaxDrpDetails.item_type)
    order_type = column_property(XxplanmaxDrpDetails.order_type)
    job_name = column_property(XxplanmaxDrpDetails.job_name)
    pr_num = column_property(XxplanmaxDrpDetails.pr_num)
    action = column_property(XxplanmaxDrpDetails.action)
