from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB


class MtlItemRevisionsB(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_item_revisions_b"
    __table_args__ = {"schema": "inv", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 878.2383422851562, "ui_y_pos": -321.3984146118164, "colour": "#F2F3F5"}

    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision: Mapped[str] = mapped_column('revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_notice: Mapped[str] = mapped_column('change_notice', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ecn_initiation_date: Mapped[str] = mapped_column('ecn_initiation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    implementation_date: Mapped[str] = mapped_column('implementation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    implemented_serial_number: Mapped[str] = mapped_column('implemented_serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    effectivity_date: Mapped[str] = mapped_column('effectivity_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revised_item_sequence_id: Mapped[str] = mapped_column('revised_item_sequence_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    object_version_number: Mapped[str] = mapped_column('object_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision_id: Mapped[str] = mapped_column('revision_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision_label: Mapped[str] = mapped_column('revision_label', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision_reason: Mapped[str] = mapped_column('revision_reason', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lifecycle_id: Mapped[str] = mapped_column('lifecycle_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    current_phase_id: Mapped[str] = mapped_column('current_phase_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlItemRevisionsB_organization_id", primaryjoin="MtlSystemItemsB.organization_id==MtlItemRevisionsB.organization_id", foreign_keys="[MtlItemRevisionsB.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="MtlItemRevisionsB_inventory_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==MtlItemRevisionsB.inventory_item_id", foreign_keys="[MtlItemRevisionsB.inventory_item_id]", viewonly=True)



