from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..wsh.wsh_delivery_details import WshDeliveryDetails
    from ..wsh.wsh_new_deliveries import WshNewDeliveries


class WshDeliveryAssignments(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "wsh_delivery_assignments"
    __table_args__ = {"schema": "wsh", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 2084.218994140625, "ui_y_pos": 561.1759033203125, "colour": "#F2F3F5"}

    delivery_assignment_id: Mapped[str] = mapped_column('delivery_assignment_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    delivery_id: Mapped[str] = mapped_column('delivery_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    parent_delivery_id: Mapped[str] = mapped_column('parent_delivery_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    delivery_detail_id: Mapped[str] = mapped_column('delivery_detail_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    parent_delivery_detail_id: Mapped[str] = mapped_column('parent_delivery_detail_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    active_flag: Mapped[str] = mapped_column('active_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    type: Mapped[str] = mapped_column('type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    WshDeliveryDetails_delivery_detail_id: Mapped["WshDeliveryDetails"] = relationship(back_populates="WshDeliveryAssignments_delivery_detail_id", primaryjoin="WshDeliveryDetails.delivery_detail_id==WshDeliveryAssignments.delivery_detail_id", foreign_keys="[WshDeliveryAssignments.delivery_detail_id]", viewonly=True)
        

    

    WshNewDeliveries_delivery_id: Mapped["WshNewDeliveries"] = relationship(back_populates="WshDeliveryAssignments_delivery_id", primaryjoin="WshNewDeliveries.delivery_id==WshDeliveryAssignments.delivery_id", foreign_keys="[WshDeliveryAssignments.delivery_id]", viewonly=True)



