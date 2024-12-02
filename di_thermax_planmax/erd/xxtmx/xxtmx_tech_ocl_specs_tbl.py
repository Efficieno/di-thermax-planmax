from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxtmxTechOclSpecsTbl(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxtmx_tech_ocl_specs_tbl"
    __table_args__ = {"schema": "xxtmx", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -822.3855590820312, "ui_y_pos": 497.44317626953125, "colour": "#F2F3F5"}

    otos_line_id: Mapped[str] = mapped_column('otos_line_id', Numeric, primary_key=True, info={"column_metadata": ColumnMetadata()})
    otm_header_id: Mapped[str] = mapped_column('otm_header_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_der_model_no: Mapped[str] = mapped_column('otos_der_model_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_param_id: Mapped[str] = mapped_column('otos_param_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_section: Mapped[str] = mapped_column('otos_section', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_param_name: Mapped[str] = mapped_column('otos_param_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_srl_no: Mapped[str] = mapped_column('otos_srl_no', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_value_1: Mapped[str] = mapped_column('otos_value_1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_value_2: Mapped[str] = mapped_column('otos_value_2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_value_3: Mapped[str] = mapped_column('otos_value_3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    otos_remark: Mapped[str] = mapped_column('otos_remark', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

    XxtmxTechOclMstrTbl_otm_header_id: Mapped["XxtmxTechOclMstrTbl"] = relationship(back_populates="XxtmxTechOclSpecsTbl_otm_header_id", primaryjoin="XxtmxTechOclMstrTbl.otm_header_id==XxtmxTechOclSpecsTbl.otm_header_id", foreign_keys="[XxtmxTechOclSpecsTbl.otm_header_id]", viewonly=True) 



