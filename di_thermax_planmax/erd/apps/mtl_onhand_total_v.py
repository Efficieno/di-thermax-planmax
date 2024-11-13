from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..apps.org_organization_definitions import OrgOrganizationDefinitions
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB


class MtlOnhandTotalV(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_onhand_total_v"
    __table_args__ = {"schema": "apps", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1.4413228054340834, "ui_y_pos": -259.27489450704104, "colour": "#F2F3F5"}

    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_code: Mapped[str] = mapped_column('organization_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subinventory_code: Mapped[str] = mapped_column('subinventory_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator_id: Mapped[str] = mapped_column('locator_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator: Mapped[str] = mapped_column('locator', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_description: Mapped[str] = mapped_column('item_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item: Mapped[str] = mapped_column('item', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision: Mapped[str] = mapped_column('revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uom: Mapped[str] = mapped_column('uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    on_hand: Mapped[str] = mapped_column('on_hand', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unpacked: Mapped[str] = mapped_column('unpacked', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    packed: Mapped[str] = mapped_column('packed', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cost_group_id: Mapped[str] = mapped_column('cost_group_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lpn_id: Mapped[str] = mapped_column('lpn_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lpn: Mapped[str] = mapped_column('lpn', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_number: Mapped[str] = mapped_column('lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expiration_date: Mapped[str] = mapped_column('expiration_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_number: Mapped[str] = mapped_column('serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_number: Mapped[str] = mapped_column('unit_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subinventory_status_id: Mapped[str] = mapped_column('subinventory_status_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator_status_id: Mapped[str] = mapped_column('locator_status_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_status_id: Mapped[str] = mapped_column('lot_status_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_status_id: Mapped[str] = mapped_column('serial_status_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    containerized_flag: Mapped[str] = mapped_column('containerized_flag', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status_level: Mapped[str] = mapped_column('status_level', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_tp_type: Mapped[str] = mapped_column('planning_tp_type', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_organization_id: Mapped[str] = mapped_column('planning_organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    owning_tp_type: Mapped[str] = mapped_column('owning_tp_type', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    owning_organization_id: Mapped[str] = mapped_column('owning_organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_lot_control: Mapped[str] = mapped_column('item_lot_control', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_serial_control: Mapped[str] = mapped_column('item_serial_control', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_uom_code: Mapped[str] = mapped_column('secondary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_onhand: Mapped[str] = mapped_column('secondary_onhand', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    grade_code: Mapped[str] = mapped_column('grade_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_unpacked: Mapped[str] = mapped_column('secondary_unpacked', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_packed: Mapped[str] = mapped_column('secondary_packed', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    onhand_status_id: Mapped[str] = mapped_column('onhand_status_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    create_transaction_id: Mapped[str] = mapped_column('create_transaction_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    OrgOrganizationDefinitions_organization_id: Mapped["OrgOrganizationDefinitions"] = relationship(back_populates="MtlOnhandTotalV_organization_id", primaryjoin="OrgOrganizationDefinitions.organization_id==MtlOnhandTotalV.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlOnhandTotalV_organization_id", primaryjoin="MtlSystemItemsB.organization_id==MtlOnhandTotalV.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlOnhandTotalV_inventory_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==MtlOnhandTotalV.inventory_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)



