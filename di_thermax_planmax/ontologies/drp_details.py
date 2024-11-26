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
