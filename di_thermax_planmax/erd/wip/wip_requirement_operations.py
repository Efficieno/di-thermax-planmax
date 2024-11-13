from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..wip.wip_discrete_jobs import WipDiscreteJobs


class WipRequirementOperations(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "wip_requirement_operations"
    __table_args__ = {"schema": "wip", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1425.3232421875, "ui_y_pos": 1613.55517578125, "colour": "#F2F3F5"}

    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operation_seq_num: Mapped[str] = mapped_column('operation_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    repetitive_schedule_id: Mapped[str] = mapped_column('repetitive_schedule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_sequence_id: Mapped[str] = mapped_column('component_sequence_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    department_id: Mapped[str] = mapped_column('department_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_supply_type: Mapped[str] = mapped_column('wip_supply_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_required: Mapped[str] = mapped_column('date_required', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    required_quantity: Mapped[str] = mapped_column('required_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_issued: Mapped[str] = mapped_column('quantity_issued', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_per_assembly: Mapped[str] = mapped_column('quantity_per_assembly', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    comments: Mapped[str] = mapped_column('comments', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_subinventory: Mapped[str] = mapped_column('supply_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supply_locator_id: Mapped[str] = mapped_column('supply_locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrp_net_flag: Mapped[str] = mapped_column('mrp_net_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mps_required_quantity: Mapped[str] = mapped_column('mps_required_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mps_date_required: Mapped[str] = mapped_column('mps_date_required', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment1: Mapped[str] = mapped_column('segment1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment2: Mapped[str] = mapped_column('segment2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment3: Mapped[str] = mapped_column('segment3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment4: Mapped[str] = mapped_column('segment4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment5: Mapped[str] = mapped_column('segment5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment6: Mapped[str] = mapped_column('segment6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment7: Mapped[str] = mapped_column('segment7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment8: Mapped[str] = mapped_column('segment8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment9: Mapped[str] = mapped_column('segment9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment10: Mapped[str] = mapped_column('segment10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment11: Mapped[str] = mapped_column('segment11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment12: Mapped[str] = mapped_column('segment12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment13: Mapped[str] = mapped_column('segment13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment14: Mapped[str] = mapped_column('segment14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment15: Mapped[str] = mapped_column('segment15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment16: Mapped[str] = mapped_column('segment16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment17: Mapped[str] = mapped_column('segment17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment18: Mapped[str] = mapped_column('segment18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment19: Mapped[str] = mapped_column('segment19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment20: Mapped[str] = mapped_column('segment20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    relieved_matl_completion_qty: Mapped[str] = mapped_column('relieved_matl_completion_qty', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_matl_scrap_quantity: Mapped[str] = mapped_column('relieved_matl_scrap_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_matl_final_comp_qty: Mapped[str] = mapped_column('relieved_matl_final_comp_qty', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_allocated: Mapped[str] = mapped_column('quantity_allocated', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_backordered: Mapped[str] = mapped_column('quantity_backordered', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_relieved: Mapped[str] = mapped_column('quantity_relieved', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    costed_quantity_issued: Mapped[str] = mapped_column('costed_quantity_issued', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    costed_quantity_relieved: Mapped[str] = mapped_column('costed_quantity_relieved', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_request_material: Mapped[str] = mapped_column('auto_request_material', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    released_quantity: Mapped[str] = mapped_column('released_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    suggested_vendor_name: Mapped[str] = mapped_column('suggested_vendor_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_id: Mapped[str] = mapped_column('vendor_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_price: Mapped[str] = mapped_column('unit_price', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_component_id: Mapped[str] = mapped_column('primary_component_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    basis_type: Mapped[str] = mapped_column('basis_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    component_yield_factor: Mapped[str] = mapped_column('component_yield_factor', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_site_id: Mapped[str] = mapped_column('vendor_site_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_contact_id: Mapped[str] = mapped_column('vendor_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="WipRequirementOperations_organization_id", primaryjoin="MtlSystemItemsB.organization_id==WipRequirementOperations.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="WipRequirementOperations_inventory_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==WipRequirementOperations.inventory_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)
        

    

    WipDiscreteJobs_wip_entity_id: Mapped["WipDiscreteJobs"] = relationship(back_populates="WipRequirementOperations_wip_entity_id", primaryjoin="WipDiscreteJobs.wip_entity_id==WipRequirementOperations.wip_entity_id", foreign_keys="[WipRequirementOperations.wip_entity_id]", viewonly=True)



