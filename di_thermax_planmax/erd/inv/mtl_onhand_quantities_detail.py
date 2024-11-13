from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB


class MtlOnhandQuantitiesDetail(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_onhand_quantities_detail"
    __table_args__ = {"schema": "inv", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 891.0896301269531, "ui_y_pos": -145.3840103149414, "colour": "#F2F3F5"}

    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_received: Mapped[str] = mapped_column('date_received', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_transaction_quantity: Mapped[str] = mapped_column('primary_transaction_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subinventory_code: Mapped[str] = mapped_column('subinventory_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision: Mapped[str] = mapped_column('revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator_id: Mapped[str] = mapped_column('locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    create_transaction_id: Mapped[str] = mapped_column('create_transaction_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    update_transaction_id: Mapped[str] = mapped_column('update_transaction_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_number: Mapped[str] = mapped_column('lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_date_received: Mapped[str] = mapped_column('orig_date_received', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cost_group_id: Mapped[str] = mapped_column('cost_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    containerized_flag: Mapped[str] = mapped_column('containerized_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    onhand_quantities_id: Mapped[str] = mapped_column('onhand_quantities_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_type: Mapped[str] = mapped_column('organization_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    owning_organization_id: Mapped[str] = mapped_column('owning_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    owning_tp_type: Mapped[str] = mapped_column('owning_tp_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_organization_id: Mapped[str] = mapped_column('planning_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_tp_type: Mapped[str] = mapped_column('planning_tp_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transaction_uom_code: Mapped[str] = mapped_column('transaction_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transaction_quantity: Mapped[str] = mapped_column('transaction_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_uom_code: Mapped[str] = mapped_column('secondary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_transaction_quantity: Mapped[str] = mapped_column('secondary_transaction_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    is_consigned: Mapped[str] = mapped_column('is_consigned', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lpn_id: Mapped[str] = mapped_column('lpn_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status_id: Mapped[str] = mapped_column('status_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mcc_code: Mapped[str] = mapped_column('mcc_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlOnhandQuantitiesDetail_organization_id", primaryjoin="MtlSystemItemsB.organization_id==MtlOnhandQuantitiesDetail.organization_id", foreign_keys="[MtlOnhandQuantitiesDetail.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlOnhandQuantitiesDetail_inventory_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==MtlOnhandQuantitiesDetail.inventory_item_id", foreign_keys="[MtlOnhandQuantitiesDetail.inventory_item_id]", viewonly=True)



