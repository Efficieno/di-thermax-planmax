from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..wip.wip_discrete_jobs import WipDiscreteJobs


class WipEntities(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "wip_entities"
    __table_args__ = {"schema": "wip", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 865.3472290039062, "ui_y_pos": 1462.0111694335938, "colour": "#F2F3F5"}

    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_entity_name: Mapped[str] = mapped_column('wip_entity_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    entity_type: Mapped[str] = mapped_column('entity_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_item_id: Mapped[str] = mapped_column('primary_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gen_object_id: Mapped[str] = mapped_column('gen_object_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    WipDiscreteJobs_wip_entity_id: Mapped["WipDiscreteJobs"] = relationship(back_populates="WipEntities_wip_entity_id", primaryjoin="WipDiscreteJobs.wip_entity_id==WipEntities.wip_entity_id", foreign_keys="[WipEntities.wip_entity_id]", viewonly=True)



