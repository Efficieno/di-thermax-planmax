from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxCalender(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_calender"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 0, "ui_y_pos": 0, "colour": "#F2F3F5"}

    day_id: Mapped[str] = mapped_column('day_id', DateTime, primary_key=True, info={"column_metadata": ColumnMetadata()})
    day_name: Mapped[str] = mapped_column('day_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    num_days_in_day: Mapped[str] = mapped_column('num_days_in_day', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_end_date: Mapped[str] = mapped_column('day_end_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_num_of_week: Mapped[str] = mapped_column('day_num_of_week', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_num_of_month: Mapped[str] = mapped_column('day_num_of_month', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_number_in_year: Mapped[str] = mapped_column('day_number_in_year', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_number_in_month: Mapped[str] = mapped_column('day_number_in_month', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    day_number_in_week: Mapped[str] = mapped_column('day_number_in_week', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_id: Mapped[str] = mapped_column('month_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_name: Mapped[str] = mapped_column('month_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_time_span: Mapped[str] = mapped_column('month_time_span', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_end_date: Mapped[str] = mapped_column('month_end_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    month_number_in_year: Mapped[str] = mapped_column('month_number_in_year', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_id: Mapped[str] = mapped_column('quarter_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_short_name: Mapped[str] = mapped_column('quarter_short_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_name: Mapped[str] = mapped_column('quarter_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_time_span: Mapped[str] = mapped_column('quarter_time_span', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_end_date: Mapped[str] = mapped_column('quarter_end_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quarter_number_in_year: Mapped[str] = mapped_column('quarter_number_in_year', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_id: Mapped[str] = mapped_column('year_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_name: Mapped[str] = mapped_column('year_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    num_days_in_year: Mapped[str] = mapped_column('num_days_in_year', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_end_date: Mapped[str] = mapped_column('year_end_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})




