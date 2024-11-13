from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..apps.org_organization_definitions import OrgOrganizationDefinitions
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB


class MtlReservationsV(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_reservations_v"
    __table_args__ = {"schema": "apps", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 127.00927782252393, "ui_y_pos": -105.48286417256838, "colour": "#F2F3F5"}

    demand_id: Mapped[str] = mapped_column('demand_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    padded_concatenated_segments: Mapped[str] = mapped_column('padded_concatenated_segments', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requirement_date: Mapped[str] = mapped_column('requirement_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_type: Mapped[str] = mapped_column('source_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_type_id: Mapped[str] = mapped_column('source_type_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    descriptive_flex_context_code: Mapped[str] = mapped_column('descriptive_flex_context_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_id: Mapped[str] = mapped_column('source_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_line: Mapped[str] = mapped_column('demand_source_line', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_name: Mapped[str] = mapped_column('source_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uom: Mapped[str] = mapped_column('uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    puom: Mapped[str] = mapped_column('puom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rsv_quantity: Mapped[str] = mapped_column('rsv_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    puom_issued_quantity: Mapped[str] = mapped_column('puom_issued_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    puom_quantity: Mapped[str] = mapped_column('puom_quantity', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision: Mapped[str] = mapped_column('revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot: Mapped[str] = mapped_column('lot', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sub: Mapped[str] = mapped_column('sub', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator_id: Mapped[str] = mapped_column('locator_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute_category: Mapped[str] = mapped_column('attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute1: Mapped[str] = mapped_column('attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute2: Mapped[str] = mapped_column('attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute3: Mapped[str] = mapped_column('attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute4: Mapped[str] = mapped_column('attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute5: Mapped[str] = mapped_column('attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute6: Mapped[str] = mapped_column('attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute7: Mapped[str] = mapped_column('attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute8: Mapped[str] = mapped_column('attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute9: Mapped[str] = mapped_column('attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute10: Mapped[str] = mapped_column('attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    parent_demand_id: Mapped[str] = mapped_column('parent_demand_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    user_line_num: Mapped[str] = mapped_column('user_line_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    OrgOrganizationDefinitions_organization_id: Mapped["OrgOrganizationDefinitions"] = relationship(back_populates="MtlReservationsV_organization_id", primaryjoin="OrgOrganizationDefinitions.organization_id==MtlReservationsV.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlReservationsV_organization_id", primaryjoin="MtlSystemItemsB.organization_id==MtlReservationsV.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlReservationsV_inventory_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==MtlReservationsV.inventory_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)



