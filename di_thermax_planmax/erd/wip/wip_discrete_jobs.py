from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..apps.org_organization_definitions import OrgOrganizationDefinitions
    from ..wip.wip_entities import WipEntities
    from ..wip.wip_requirement_operations import WipRequirementOperations
    from ..wip.wip_operation_resources import WipOperationResources


class WipDiscreteJobs(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "wip_discrete_jobs"
    __table_args__ = {"schema": "wip", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1182.859130859375, "ui_y_pos": 1354.39501953125, "colour": "#F2F3F5"}

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
    source_line_id: Mapped[str] = mapped_column('source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_code: Mapped[str] = mapped_column('source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status_type: Mapped[str] = mapped_column('status_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_item_id: Mapped[str] = mapped_column('primary_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    firm_planned_flag: Mapped[str] = mapped_column('firm_planned_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    job_type: Mapped[str] = mapped_column('job_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_supply_type: Mapped[str] = mapped_column('wip_supply_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    class_code: Mapped[str] = mapped_column('class_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    material_account: Mapped[str] = mapped_column('material_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    material_overhead_account: Mapped[str] = mapped_column('material_overhead_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    resource_account: Mapped[str] = mapped_column('resource_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    outside_processing_account: Mapped[str] = mapped_column('outside_processing_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    material_variance_account: Mapped[str] = mapped_column('material_variance_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    resource_variance_account: Mapped[str] = mapped_column('resource_variance_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    outside_proc_variance_account: Mapped[str] = mapped_column('outside_proc_variance_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_cost_adjustment_account: Mapped[str] = mapped_column('std_cost_adjustment_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overhead_account: Mapped[str] = mapped_column('overhead_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overhead_variance_account: Mapped[str] = mapped_column('overhead_variance_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_start_date: Mapped[str] = mapped_column('scheduled_start_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_released: Mapped[str] = mapped_column('date_released', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_completion_date: Mapped[str] = mapped_column('scheduled_completion_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_completed: Mapped[str] = mapped_column('date_completed', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_closed: Mapped[str] = mapped_column('date_closed', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_quantity: Mapped[str] = mapped_column('start_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_completed: Mapped[str] = mapped_column('quantity_completed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_scrapped: Mapped[str] = mapped_column('quantity_scrapped', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    net_quantity: Mapped[str] = mapped_column('net_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_reference_id: Mapped[str] = mapped_column('bom_reference_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    routing_reference_id: Mapped[str] = mapped_column('routing_reference_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    common_bom_sequence_id: Mapped[str] = mapped_column('common_bom_sequence_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    common_routing_sequence_id: Mapped[str] = mapped_column('common_routing_sequence_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_revision: Mapped[str] = mapped_column('bom_revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    routing_revision: Mapped[str] = mapped_column('routing_revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_revision_date: Mapped[str] = mapped_column('bom_revision_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    routing_revision_date: Mapped[str] = mapped_column('routing_revision_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_number: Mapped[str] = mapped_column('lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    alternate_bom_designator: Mapped[str] = mapped_column('alternate_bom_designator', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    alternate_routing_designator: Mapped[str] = mapped_column('alternate_routing_designator', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    completion_subinventory: Mapped[str] = mapped_column('completion_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    completion_locator_id: Mapped[str] = mapped_column('completion_locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mps_scheduled_completion_date: Mapped[str] = mapped_column('mps_scheduled_completion_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mps_net_quantity: Mapped[str] = mapped_column('mps_net_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_class: Mapped[str] = mapped_column('demand_class', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    schedule_group_id: Mapped[str] = mapped_column('schedule_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    build_sequence: Mapped[str] = mapped_column('build_sequence', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_id: Mapped[str] = mapped_column('line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    kanban_card_id: Mapped[str] = mapped_column('kanban_card_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overcompletion_tolerance_type: Mapped[str] = mapped_column('overcompletion_tolerance_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overcompletion_tolerance_value: Mapped[str] = mapped_column('overcompletion_tolerance_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_item_unit_number: Mapped[str] = mapped_column('end_item_unit_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_creation_time: Mapped[str] = mapped_column('po_creation_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    priority: Mapped[str] = mapped_column('priority', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    due_date: Mapped[str] = mapped_column('due_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    est_scrap_account: Mapped[str] = mapped_column('est_scrap_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    est_scrap_var_account: Mapped[str] = mapped_column('est_scrap_var_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    est_scrap_prior_qty: Mapped[str] = mapped_column('est_scrap_prior_qty', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    due_date_penalty: Mapped[str] = mapped_column('due_date_penalty', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    due_date_tolerance: Mapped[str] = mapped_column('due_date_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    coproducts_supply: Mapped[str] = mapped_column('coproducts_supply', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    parent_wip_entity_id: Mapped[str] = mapped_column('parent_wip_entity_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    asset_number: Mapped[str] = mapped_column('asset_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    asset_group_id: Mapped[str] = mapped_column('asset_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rebuild_item_id: Mapped[str] = mapped_column('rebuild_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rebuild_serial_number: Mapped[str] = mapped_column('rebuild_serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    manual_rebuild_flag: Mapped[str] = mapped_column('manual_rebuild_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shutdown_type: Mapped[str] = mapped_column('shutdown_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    estimation_status: Mapped[str] = mapped_column('estimation_status', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requested_start_date: Mapped[str] = mapped_column('requested_start_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    notification_required: Mapped[str] = mapped_column('notification_required', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    work_order_type: Mapped[str] = mapped_column('work_order_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    owning_department: Mapped[str] = mapped_column('owning_department', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    activity_type: Mapped[str] = mapped_column('activity_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    activity_cause: Mapped[str] = mapped_column('activity_cause', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tagout_required: Mapped[str] = mapped_column('tagout_required', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plan_maintenance: Mapped[str] = mapped_column('plan_maintenance', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pm_schedule_id: Mapped[str] = mapped_column('pm_schedule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_estimation_date: Mapped[str] = mapped_column('last_estimation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_estimation_req_id: Mapped[str] = mapped_column('last_estimation_req_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    activity_source: Mapped[str] = mapped_column('activity_source', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serialization_start_op: Mapped[str] = mapped_column('serialization_start_op', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maintenance_object_id: Mapped[str] = mapped_column('maintenance_object_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maintenance_object_type: Mapped[str] = mapped_column('maintenance_object_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maintenance_object_source: Mapped[str] = mapped_column('maintenance_object_source', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    material_issue_by_mo: Mapped[str] = mapped_column('material_issue_by_mo', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduling_request_id: Mapped[str] = mapped_column('scheduling_request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    issue_zero_cost_flag: Mapped[str] = mapped_column('issue_zero_cost_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_linear_location_id: Mapped[str] = mapped_column('eam_linear_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    actual_start_date: Mapped[str] = mapped_column('actual_start_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expected_hold_release_date: Mapped[str] = mapped_column('expected_hold_release_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expedited: Mapped[str] = mapped_column('expedited', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    job_note: Mapped[str] = mapped_column('job_note', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="WipDiscreteJobs_organization_id", primaryjoin="MtlSystemItemsB.organization_id==WipDiscreteJobs.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    MtlSystemItemsB_inventory_item_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="WipDiscreteJobs_primary_item_id", primaryjoin="MtlSystemItemsB.inventory_item_id==WipDiscreteJobs.primary_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)
        

    

    OrgOrganizationDefinitions_organization_id: Mapped["OrgOrganizationDefinitions"] = relationship(back_populates="WipDiscreteJobs_organization_id", primaryjoin="OrgOrganizationDefinitions.organization_id==WipDiscreteJobs.organization_id", foreign_keys="[WipDiscreteJobs.organization_id]", viewonly=True)
        

    

    WipEntities_wip_entity_id: Mapped["WipEntities"] = relationship(back_populates="WipDiscreteJobs_wip_entity_id", primaryjoin="WipEntities.wip_entity_id==WipDiscreteJobs.wip_entity_id", foreign_keys="[WipEntities.wip_entity_id]", viewonly=True)
        

    

    WipRequirementOperations_wip_entity_id: Mapped["WipRequirementOperations"] = relationship(back_populates="WipDiscreteJobs_wip_entity_id", primaryjoin="WipRequirementOperations.wip_entity_id==WipDiscreteJobs.wip_entity_id", foreign_keys="[WipRequirementOperations.wip_entity_id]", viewonly=True)
        

    

    WipOperationResources_wip_entity_id: Mapped["WipOperationResources"] = relationship(back_populates="WipDiscreteJobs_wip_entity_id", primaryjoin="WipOperationResources.wip_entity_id==WipDiscreteJobs.wip_entity_id", foreign_keys="[WipOperationResources.wip_entity_id]", viewonly=True)



