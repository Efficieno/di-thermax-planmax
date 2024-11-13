from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class FndConcurrentProcesses(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "fnd_concurrent_processes"
    __table_args__ = {"schema": "applsys", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 0, "ui_y_pos": 0, "colour": "#F2F3F5"}

    concurrent_process_id: Mapped[str] = mapped_column('concurrent_process_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    queue_application_id: Mapped[str] = mapped_column('queue_application_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    concurrent_queue_id: Mapped[str] = mapped_column('concurrent_queue_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_status_code: Mapped[str] = mapped_column('process_status_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    session_id: Mapped[str] = mapped_column('session_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oracle_process_id: Mapped[str] = mapped_column('oracle_process_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_start_date: Mapped[str] = mapped_column('process_start_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    os_process_name: Mapped[str] = mapped_column('os_process_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    os_process_id: Mapped[str] = mapped_column('os_process_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    manager_type: Mapped[str] = mapped_column('manager_type', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    db_name: Mapped[str] = mapped_column('db_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    db_domain: Mapped[str] = mapped_column('db_domain', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sqlnet_string: Mapped[str] = mapped_column('sqlnet_string', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    logfile_name: Mapped[str] = mapped_column('logfile_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    job_id: Mapped[str] = mapped_column('job_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    db_instance: Mapped[str] = mapped_column('db_instance', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lk_handle: Mapped[str] = mapped_column('lk_handle', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plsql_log: Mapped[str] = mapped_column('plsql_log', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plsql_out: Mapped[str] = mapped_column('plsql_out', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_txn_start: Mapped[str] = mapped_column('last_txn_start', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_txn_end: Mapped[str] = mapped_column('last_txn_end', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    plsql_dir: Mapped[str] = mapped_column('plsql_dir', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    instance_number: Mapped[str] = mapped_column('instance_number', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_context: Mapped[str] = mapped_column('process_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_parameters: Mapped[str] = mapped_column('service_parameters', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gsm_internal_status: Mapped[str] = mapped_column('gsm_internal_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gsm_internal_info: Mapped[str] = mapped_column('gsm_internal_info', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    security_group_id: Mapped[str] = mapped_column('security_group_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})




