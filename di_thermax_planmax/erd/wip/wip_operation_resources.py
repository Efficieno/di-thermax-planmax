from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..wip.wip_discrete_jobs import WipDiscreteJobs


class WipOperationResources(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "wip_operation_resources"
    __table_args__ = {"schema": "wip", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1101.9152221679688, "ui_y_pos": 1622.38232421875, "colour": "#F2F3F5"}

    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    operation_seq_num: Mapped[str] = mapped_column('operation_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    resource_seq_num: Mapped[str] = mapped_column('resource_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    resource_id: Mapped[str] = mapped_column('resource_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uom_code: Mapped[str] = mapped_column('uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    basis_type: Mapped[str] = mapped_column('basis_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    usage_rate_or_amount: Mapped[str] = mapped_column('usage_rate_or_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    activity_id: Mapped[str] = mapped_column('activity_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_flag: Mapped[str] = mapped_column('scheduled_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    assigned_units: Mapped[str] = mapped_column('assigned_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    autocharge_type: Mapped[str] = mapped_column('autocharge_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    standard_rate_flag: Mapped[str] = mapped_column('standard_rate_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    applied_resource_units: Mapped[str] = mapped_column('applied_resource_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    applied_resource_value: Mapped[str] = mapped_column('applied_resource_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_date: Mapped[str] = mapped_column('start_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    completion_date: Mapped[str] = mapped_column('completion_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    relieved_res_completion_units: Mapped[str] = mapped_column('relieved_res_completion_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_res_scrap_units: Mapped[str] = mapped_column('relieved_res_scrap_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_res_completion_value: Mapped[str] = mapped_column('relieved_res_completion_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_res_scrap_value: Mapped[str] = mapped_column('relieved_res_scrap_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_variance_value: Mapped[str] = mapped_column('relieved_variance_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    temp_relieved_value: Mapped[str] = mapped_column('temp_relieved_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_res_final_comp_units: Mapped[str] = mapped_column('relieved_res_final_comp_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    department_id: Mapped[str] = mapped_column('department_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    phantom_flag: Mapped[str] = mapped_column('phantom_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    phantom_op_seq_num: Mapped[str] = mapped_column('phantom_op_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    phantom_item_id: Mapped[str] = mapped_column('phantom_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    schedule_seq_num: Mapped[str] = mapped_column('schedule_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    substitute_group_num: Mapped[str] = mapped_column('substitute_group_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    replacement_group_num: Mapped[str] = mapped_column('replacement_group_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    principle_flag: Mapped[str] = mapped_column('principle_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    setup_id: Mapped[str] = mapped_column('setup_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    parent_resource_seq: Mapped[str] = mapped_column('parent_resource_seq', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    batch_id: Mapped[str] = mapped_column('batch_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_res_units: Mapped[str] = mapped_column('relieved_res_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    relieved_res_value: Mapped[str] = mapped_column('relieved_res_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maximum_assigned_units: Mapped[str] = mapped_column('maximum_assigned_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    firm_flag: Mapped[str] = mapped_column('firm_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_sequence_id: Mapped[str] = mapped_column('group_sequence_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_sequence_number: Mapped[str] = mapped_column('group_sequence_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    actual_start_date: Mapped[str] = mapped_column('actual_start_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    actual_completion_date: Mapped[str] = mapped_column('actual_completion_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    projected_completion_date: Mapped[str] = mapped_column('projected_completion_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    WipDiscreteJobs_wip_entity_id: Mapped["WipDiscreteJobs"] = relationship(back_populates="WipOperationResources_wip_entity_id", primaryjoin="WipDiscreteJobs.wip_entity_id==WipOperationResources.wip_entity_id", foreign_keys="[WipOperationResources.wip_entity_id]", viewonly=True)



