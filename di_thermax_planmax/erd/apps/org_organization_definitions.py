from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..xxtmx_planmax.xxplanmax_header_dtls import XxplanmaxHeaderDtls
    from ..apps.mtl_reservations_v import MtlReservationsV
    from ..apps.mtl_onhand_total_v import MtlOnhandTotalV
    from ..ont.oe_order_headers_all import OeOrderHeadersAll
    from ..ont.oe_order_lines_all import OeOrderLinesAll
    from ..wip.wip_discrete_jobs import WipDiscreteJobs
    from ..apps.hr_operating_units import HrOperatingUnits
    from ..inv.mtl_system_items_b import MtlSystemItemsB


class OrgOrganizationDefinitions(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "org_organization_definitions"
    __table_args__ = {"schema": "apps", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 493.15992736816406, "ui_y_pos": 737.4390029907227, "colour": "#F2F3F5"}

    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata(display_name="Organization ID")})
    business_group_id: Mapped[str] = mapped_column('business_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    user_definition_enable_date: Mapped[str] = mapped_column('user_definition_enable_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    disable_date: Mapped[str] = mapped_column('disable_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_code: Mapped[str] = mapped_column('organization_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_name: Mapped[str] = mapped_column('organization_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    set_of_books_id: Mapped[str] = mapped_column('set_of_books_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    chart_of_accounts_id: Mapped[str] = mapped_column('chart_of_accounts_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_enabled_flag: Mapped[str] = mapped_column('inventory_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operating_unit: Mapped[str] = mapped_column('operating_unit', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    legal_entity: Mapped[str] = mapped_column('legal_entity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    XxplanmaxHeaderDtls_mfg_organization_id: Mapped["XxplanmaxHeaderDtls"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="XxplanmaxHeaderDtls.mfg_organization_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    MtlReservationsV_organization_id: Mapped["MtlReservationsV"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="MtlReservationsV.organization_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    MtlOnhandTotalV_organization_id: Mapped["MtlOnhandTotalV"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="MtlOnhandTotalV.organization_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    OeOrderHeadersAll_ship_from_org_id: Mapped["OeOrderHeadersAll"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="OeOrderHeadersAll.ship_from_org_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    OeOrderLinesAll_ship_from_org_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="OeOrderLinesAll.ship_from_org_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    WipDiscreteJobs_organization_id: Mapped["WipDiscreteJobs"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="WipDiscreteJobs.organization_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[WipDiscreteJobs.organization_id]", viewonly=True)
        

    

    HrOperatingUnits_organization_id: Mapped["HrOperatingUnits"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="HrOperatingUnits.organization_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[HrOperatingUnits.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="OrgOrganizationDefinitions_organization_id", primaryjoin="MtlSystemItemsB.organization_id==OrgOrganizationDefinitions.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)



