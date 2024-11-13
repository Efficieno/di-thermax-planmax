from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata


if TYPE_CHECKING:
    from ..apps.org_organization_definitions import OrgOrganizationDefinitions


class HrOperatingUnits(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hr_operating_units"
    __table_args__ = {"schema": "apps", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}

    business_group_id: Mapped[str] = mapped_column('business_group_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column('name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_from: Mapped[str] = mapped_column('date_from', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_to: Mapped[str] = mapped_column('date_to', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    short_code: Mapped[str] = mapped_column('short_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    set_of_books_id: Mapped[str] = mapped_column('set_of_books_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_legal_context_id: Mapped[str] = mapped_column('default_legal_context_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    usable_flag: Mapped[str] = mapped_column('usable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    OrgOrganizationDefinitions_organization_id: Mapped["OrgOrganizationDefinitions"] = relationship(back_populates="HrOperatingUnits_organization_id", primaryjoin="OrgOrganizationDefinitions.organization_id==HrOperatingUnits.organization_id", foreign_keys="[HrOperatingUnits.organization_id]", viewonly=True)



