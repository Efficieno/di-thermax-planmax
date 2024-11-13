from .order_lines import OrderLines
from .order_headers import OrderHeaders
# from efficieno.components.data_objects import ObjectBase, ColumnMetadata
from sqlalchemy.orm import Mapped, mapped_column, relationship

OrderLines.OrderHeaders_header_id = relationship(
    "OrderHeaders",
    back_populates="OrderLines_header_id",
    primaryjoin="OeOrderHeadersAll.header_id==OeOrderLinesAll.header_id",
    foreign_keys="[OeOrderHeadersAll.header_id]",
    viewonly=True,
)

OrderHeaders.OrderLines_header_id = relationship("OrderLines",
                                                 back_populates="OrderHeaders_header_id",
                                                 primaryjoin="OeOrderHeadersAll.header_id==OeOrderLinesAll.header_id",
                                                 foreign_keys="[OeOrderHeadersAll.header_id]",
                                                 viewonly=True,
                                                 )
