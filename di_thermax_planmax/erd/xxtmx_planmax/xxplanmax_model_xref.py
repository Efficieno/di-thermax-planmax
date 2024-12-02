from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxModelXref(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_model_xref"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -453.2254943847656, "ui_y_pos": 522.4486389160156, "colour": "#F2F3F5"}

    model_item: Mapped[str] = mapped_column('model_item', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    model_number: Mapped[str] = mapped_column('model_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_planner: Mapped[str] = mapped_column('product_planner', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_rsmh: Mapped[str] = mapped_column('std_rsmh', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prn_applicable: Mapped[str] = mapped_column('prn_applicable', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    full_lead_time: Mapped[str] = mapped_column('full_lead_time', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_category: Mapped[str] = mapped_column('product_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})




