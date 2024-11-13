from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..po.po_requisition_lines_all import PoRequisitionLinesAll


class PoRequisitionHeadersAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "po_requisition_headers_all"
    __table_args__ = {"schema": "po", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -206.8192596435547, "ui_y_pos": 1172.4560546875, "colour": "#F2F3F5"}

    requisition_header_id: Mapped[str] = mapped_column('requisition_header_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    preparer_id: Mapped[str] = mapped_column('preparer_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment1: Mapped[str] = mapped_column('segment1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    summary_flag: Mapped[str] = mapped_column('summary_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    enabled_flag: Mapped[str] = mapped_column('enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment2: Mapped[str] = mapped_column('segment2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment3: Mapped[str] = mapped_column('segment3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment4: Mapped[str] = mapped_column('segment4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment5: Mapped[str] = mapped_column('segment5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_date_active: Mapped[str] = mapped_column('start_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_date_active: Mapped[str] = mapped_column('end_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    authorization_status: Mapped[str] = mapped_column('authorization_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    note_to_authorizer: Mapped[str] = mapped_column('note_to_authorizer', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    type_lookup_code: Mapped[str] = mapped_column('type_lookup_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transferred_to_oe_flag: Mapped[str] = mapped_column('transferred_to_oe_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute_category: Mapped[str] = mapped_column('attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute1: Mapped[str] = mapped_column('attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute2: Mapped[str] = mapped_column('attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute3: Mapped[str] = mapped_column('attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute4: Mapped[str] = mapped_column('attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute5: Mapped[str] = mapped_column('attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    on_line_flag: Mapped[str] = mapped_column('on_line_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preliminary_research_flag: Mapped[str] = mapped_column('preliminary_research_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    research_complete_flag: Mapped[str] = mapped_column('research_complete_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preparer_finished_flag: Mapped[str] = mapped_column('preparer_finished_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preparer_finished_date: Mapped[str] = mapped_column('preparer_finished_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    agent_return_flag: Mapped[str] = mapped_column('agent_return_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    agent_return_note: Mapped[str] = mapped_column('agent_return_note', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancel_flag: Mapped[str] = mapped_column('cancel_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    ussgl_transaction_code: Mapped[str] = mapped_column('ussgl_transaction_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    government_context: Mapped[str] = mapped_column('government_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    interface_source_code: Mapped[str] = mapped_column('interface_source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    interface_source_line_id: Mapped[str] = mapped_column('interface_source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    closed_code: Mapped[str] = mapped_column('closed_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wf_item_type: Mapped[str] = mapped_column('wf_item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wf_item_key: Mapped[str] = mapped_column('wf_item_key', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    emergency_po_num: Mapped[str] = mapped_column('emergency_po_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pcard_id: Mapped[str] = mapped_column('pcard_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    apps_source_code: Mapped[str] = mapped_column('apps_source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cbc_accounting_date: Mapped[str] = mapped_column('cbc_accounting_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_pending_flag: Mapped[str] = mapped_column('change_pending_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    active_shopping_cart_flag: Mapped[str] = mapped_column('active_shopping_cart_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contractor_status: Mapped[str] = mapped_column('contractor_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contractor_requisition_flag: Mapped[str] = mapped_column('contractor_requisition_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supplier_notified_flag: Mapped[str] = mapped_column('supplier_notified_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    emergency_po_org_id: Mapped[str] = mapped_column('emergency_po_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    approved_date: Mapped[str] = mapped_column('approved_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_attribute_update_code: Mapped[str] = mapped_column('tax_attribute_update_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    first_approver_id: Mapped[str] = mapped_column('first_approver_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    first_position_id: Mapped[str] = mapped_column('first_position_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    federal_flag: Mapped[str] = mapped_column('federal_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conformed_header_id: Mapped[str] = mapped_column('conformed_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision_num: Mapped[str] = mapped_column('revision_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amendment_type: Mapped[str] = mapped_column('amendment_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amendment_status: Mapped[str] = mapped_column('amendment_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amendment_reason: Mapped[str] = mapped_column('amendment_reason', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uda_template_id: Mapped[str] = mapped_column('uda_template_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uda_template_date: Mapped[str] = mapped_column('uda_template_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_issuing_office: Mapped[str] = mapped_column('clm_issuing_office', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_cotr_office: Mapped[str] = mapped_column('clm_cotr_office', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_cotr_contact: Mapped[str] = mapped_column('clm_cotr_contact', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_priority_code: Mapped[str] = mapped_column('clm_priority_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    suggested_award_no: Mapped[str] = mapped_column('suggested_award_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_assist_office: Mapped[str] = mapped_column('clm_assist_office', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_mipr_prepared_date: Mapped[str] = mapped_column('clm_mipr_prepared_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_mipr_ref_num: Mapped[str] = mapped_column('clm_mipr_ref_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_mipr_type: Mapped[str] = mapped_column('clm_mipr_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_req_office: Mapped[str] = mapped_column('clm_req_office', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    par_draft_id: Mapped[str] = mapped_column('par_draft_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    par_flag: Mapped[str] = mapped_column('par_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_mipr_acknowledged_flag: Mapped[str] = mapped_column('clm_mipr_acknowledged_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_assist_contact: Mapped[str] = mapped_column('clm_assist_contact', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_req_contact: Mapped[str] = mapped_column('clm_req_contact', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    notify_requester_flag: Mapped[str] = mapped_column('notify_requester_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    igt_document_flag: Mapped[str] = mapped_column('igt_document_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    PoRequisitionLinesAll_requisition_header_id: Mapped["PoRequisitionLinesAll"] = relationship(back_populates="PoRequisitionHeadersAll_requisition_header_id", primaryjoin="PoRequisitionLinesAll.requisition_header_id==PoRequisitionHeadersAll.requisition_header_id", foreign_keys="[PoRequisitionLinesAll.requisition_header_id]", viewonly=True)



