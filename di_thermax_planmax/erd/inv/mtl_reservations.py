from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB


class MtlReservations(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_reservations"
    __table_args__ = {"schema": "inv", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 494.62567138671875, "ui_y_pos": -320.91362380981445, "colour": "#F2F3F5"}

    reservation_id: Mapped[str] = mapped_column('reservation_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    requirement_date: Mapped[str] = mapped_column('requirement_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_type_id: Mapped[str] = mapped_column('demand_source_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_name: Mapped[str] = mapped_column('demand_source_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_header_id: Mapped[str] = mapped_column('demand_source_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_line_id: Mapped[str] = mapped_column('demand_source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_delivery: Mapped[str] = mapped_column('demand_source_delivery', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_uom_code: Mapped[str] = mapped_column('primary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_uom_id: Mapped[str] = mapped_column('primary_uom_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reservation_uom_code: Mapped[str] = mapped_column('reservation_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reservation_uom_id: Mapped[str] = mapped_column('reservation_uom_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reservation_quantity: Mapped[str] = mapped_column('reservation_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_reservation_quantity: Mapped[str] = mapped_column('primary_reservation_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    autodetail_group_id: Mapped[str] = mapped_column('autodetail_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    external_source_code: Mapped[str] = mapped_column('external_source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    external_source_line_id: Mapped[str] = mapped_column('external_source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_source_type_id: Mapped[str] = mapped_column('supply_source_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_source_header_id: Mapped[str] = mapped_column('supply_source_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_source_line_id: Mapped[str] = mapped_column('supply_source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_source_line_detail: Mapped[str] = mapped_column('supply_source_line_detail', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_source_name: Mapped[str] = mapped_column('supply_source_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision: Mapped[str] = mapped_column('revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subinventory_code: Mapped[str] = mapped_column('subinventory_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subinventory_id: Mapped[str] = mapped_column('subinventory_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator_id: Mapped[str] = mapped_column('locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_number: Mapped[str] = mapped_column('lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_number_id: Mapped[str] = mapped_column('lot_number_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_number: Mapped[str] = mapped_column('serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_number_id: Mapped[str] = mapped_column('serial_number_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    partial_quantities_allowed: Mapped[str] = mapped_column('partial_quantities_allowed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_detailed: Mapped[str] = mapped_column('auto_detailed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pick_slip_number: Mapped[str] = mapped_column('pick_slip_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lpn_id: Mapped[str] = mapped_column('lpn_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    ship_ready_flag: Mapped[str] = mapped_column('ship_ready_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    n_column1: Mapped[str] = mapped_column('n_column1', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    detailed_quantity: Mapped[str] = mapped_column('detailed_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cost_group_id: Mapped[str] = mapped_column('cost_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    container_lpn_id: Mapped[str] = mapped_column('container_lpn_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    staged_flag: Mapped[str] = mapped_column('staged_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_detailed_quantity: Mapped[str] = mapped_column('secondary_detailed_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_reservation_quantity: Mapped[str] = mapped_column('secondary_reservation_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_uom_code: Mapped[str] = mapped_column('secondary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_uom_id: Mapped[str] = mapped_column('secondary_uom_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    crossdock_flag: Mapped[str] = mapped_column('crossdock_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    crossdock_criteria_id: Mapped[str] = mapped_column('crossdock_criteria_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_source_line_detail: Mapped[str] = mapped_column('demand_source_line_detail', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_reservation_quantity: Mapped[str] = mapped_column('serial_reservation_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_receipt_date: Mapped[str] = mapped_column('supply_receipt_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_ship_date: Mapped[str] = mapped_column('demand_ship_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    exception_code: Mapped[str] = mapped_column('exception_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_supply_source_type_id: Mapped[str] = mapped_column('orig_supply_source_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_supply_source_header_id: Mapped[str] = mapped_column('orig_supply_source_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_supply_source_line_id: Mapped[str] = mapped_column('orig_supply_source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_supply_source_line_detail: Mapped[str] = mapped_column('orig_supply_source_line_detail', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_demand_source_type_id: Mapped[str] = mapped_column('orig_demand_source_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_demand_source_header_id: Mapped[str] = mapped_column('orig_demand_source_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_demand_source_line_id: Mapped[str] = mapped_column('orig_demand_source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_demand_source_line_detail: Mapped[str] = mapped_column('orig_demand_source_line_detail', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mcc_code: Mapped[str] = mapped_column('mcc_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlReservations_organization_id", primaryjoin="MtlSystemItemsB.organization_id==MtlReservations.organization_id", foreign_keys="[MtlReservations.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlReservations_inventory_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==MtlReservations.inventory_item_id", foreign_keys="[MtlReservations.inventory_item_id]", viewonly=True)



