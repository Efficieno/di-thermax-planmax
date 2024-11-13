from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..po.po_requisition_lines_all import PoRequisitionLinesAll
    from ..po.po_distributions_all import PoDistributionsAll


class PoReqDistributionsAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "po_req_distributions_all"
    __table_args__ = {"schema": "po", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -404.6912536621094, "ui_y_pos": 1465.0336303710938, "colour": "#F2F3F5"}

    distribution_id: Mapped[str] = mapped_column('distribution_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requisition_line_id: Mapped[str] = mapped_column('requisition_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    set_of_books_id: Mapped[str] = mapped_column('set_of_books_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    code_combination_id: Mapped[str] = mapped_column('code_combination_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_line_quantity: Mapped[str] = mapped_column('req_line_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    encumbered_flag: Mapped[str] = mapped_column('encumbered_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_encumbered_date: Mapped[str] = mapped_column('gl_encumbered_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_encumbered_period_name: Mapped[str] = mapped_column('gl_encumbered_period_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_cancelled_date: Mapped[str] = mapped_column('gl_cancelled_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    failed_funds_lookup_code: Mapped[str] = mapped_column('failed_funds_lookup_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    encumbered_amount: Mapped[str] = mapped_column('encumbered_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    budget_account_id: Mapped[str] = mapped_column('budget_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accrual_account_id: Mapped[str] = mapped_column('accrual_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    variance_account_id: Mapped[str] = mapped_column('variance_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prevent_encumbrance_flag: Mapped[str] = mapped_column('prevent_encumbrance_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    ussgl_transaction_code: Mapped[str] = mapped_column('ussgl_transaction_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    government_context: Mapped[str] = mapped_column('government_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expenditure_type: Mapped[str] = mapped_column('expenditure_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_accounting_context: Mapped[str] = mapped_column('project_accounting_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expenditure_organization_id: Mapped[str] = mapped_column('expenditure_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_closed_date: Mapped[str] = mapped_column('gl_closed_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_req_distribution_id: Mapped[str] = mapped_column('source_req_distribution_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    distribution_num: Mapped[str] = mapped_column('distribution_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_related_flag: Mapped[str] = mapped_column('project_related_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expenditure_item_date: Mapped[str] = mapped_column('expenditure_item_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allocation_type: Mapped[str] = mapped_column('allocation_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allocation_value: Mapped[str] = mapped_column('allocation_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    award_id: Mapped[str] = mapped_column('award_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_item_unit_number: Mapped[str] = mapped_column('end_item_unit_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    recoverable_tax: Mapped[str] = mapped_column('recoverable_tax', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    nonrecoverable_tax: Mapped[str] = mapped_column('nonrecoverable_tax', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    recovery_rate: Mapped[str] = mapped_column('recovery_rate', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_recovery_override_flag: Mapped[str] = mapped_column('tax_recovery_override_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oke_contract_line_id: Mapped[str] = mapped_column('oke_contract_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oke_contract_deliverable_id: Mapped[str] = mapped_column('oke_contract_deliverable_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_line_amount: Mapped[str] = mapped_column('req_line_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_line_currency_amount: Mapped[str] = mapped_column('req_line_currency_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_award_id: Mapped[str] = mapped_column('req_award_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    event_id: Mapped[str] = mapped_column('event_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conformed_dist_id: Mapped[str] = mapped_column('conformed_dist_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amendment_type: Mapped[str] = mapped_column('amendment_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amendment_status: Mapped[str] = mapped_column('amendment_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uda_template_id: Mapped[str] = mapped_column('uda_template_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    info_line_id: Mapped[str] = mapped_column('info_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_funded: Mapped[str] = mapped_column('amount_funded', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    funded_value: Mapped[str] = mapped_column('funded_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    partial_funded_flag: Mapped[str] = mapped_column('partial_funded_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_funded: Mapped[str] = mapped_column('quantity_funded', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_misc_loa: Mapped[str] = mapped_column('clm_misc_loa', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_defence_funding: Mapped[str] = mapped_column('clm_defence_funding', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_fms_case_number: Mapped[str] = mapped_column('clm_fms_case_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_agency_acct_identifier: Mapped[str] = mapped_column('clm_agency_acct_identifier', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_in_funded_value: Mapped[str] = mapped_column('change_in_funded_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unencumbered_amount: Mapped[str] = mapped_column('unencumbered_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    funds_liquidated: Mapped[str] = mapped_column('funds_liquidated', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    acrn: Mapped[str] = mapped_column('acrn', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    par_distribution_id: Mapped[str] = mapped_column('par_distribution_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    par_draft_id: Mapped[str] = mapped_column('par_draft_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    PoRequisitionLinesAll_requisition_line_id: Mapped["PoRequisitionLinesAll"] = relationship(back_populates="PoReqDistributionsAll_requisition_line_id", primaryjoin="PoRequisitionLinesAll.requisition_line_id==PoReqDistributionsAll.requisition_line_id", foreign_keys="[PoReqDistributionsAll.requisition_line_id]", viewonly=True)
        

    

    PoDistributionsAll_req_distribution_id: Mapped["PoDistributionsAll"] = relationship(back_populates="PoReqDistributionsAll_distribution_id", primaryjoin="PoDistributionsAll.req_distribution_id==PoReqDistributionsAll.distribution_id", foreign_keys="[PoReqDistributionsAll.distribution_id]", viewonly=True)



